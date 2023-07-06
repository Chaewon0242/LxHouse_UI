import { Fragment, useEffect, useRef, useState } from "react"
import { useRouter } from "next/router"
import { connect, E, getRefValue, isTrue, preventDefault, processEvent, refs, set_val, uploadFiles } from "/utils/state"
import "focus-visible/dist/focus-visible"
import { Box, Button, ButtonGroup, Center, Divider, Flex, Grid, GridItem, Image, Input, Spacer, Text, useColorMode, VStack } from "@chakra-ui/react"
import NextHead from "next/head"


export default function Component() {
  const [state, setState] = useState({"is_hydrated": false, "events": [{"name": "state.hydrate"}], "files": []})
  const [result, setResult] = useState({"state": null, "events": [], "final": true, "processing": false})
  const [notConnected, setNotConnected] = useState(false)
  const router = useRouter()
  const socket = useRef(null)
  const { isReady } = router
  const { colorMode, toggleColorMode } = useColorMode()
  const focusRef = useRef();
  
  // Function to add new events to the event queue.
  const Event = (events, _e) => {
      preventDefault(_e);
      setState(state => ({
        ...state,
        events: [...state.events, ...events],
      }))
  }

  // Function to add new files to be uploaded.
  const File = files => setState(state => ({
    ...state,
    files,
  }))

  // Main event loop.
  useEffect(()=> {
    // Skip if the router is not ready.
    if (!isReady) {
      return;
    }

    // Initialize the websocket connection.
    if (!socket.current) {
      connect(socket, state, setState, result, setResult, router, ['websocket', 'polling'], setNotConnected)
    }

    // If we are not processing an event, process the next event.
    if (!result.processing) {
      processEvent(state, setState, result, setResult, router, socket.current)
    }

    // If there is a new result, update the state.
    if (result.state != null) {
      // Apply the new result to the state and the new events to the queue.
      setState(state => ({
        ...result.state,
        events: [...state.events, ...result.events],
      }))

      // Reset the result.
      setResult(result => ({
        state: null,
        events: [],
        final: true,
        processing: !result.final,
      }))

      // Process the next event.
      processEvent(state, setState, result, setResult, router, socket.current)
    }
  })

  // Set focus to the specified element.
  useEffect(() => {
    if (focusRef.current) {
      focusRef.current.focus();
    }
  })

  // Route after the initial page hydration.
  useEffect(() => {
    const change_complete = () => Event([E('state.hydrate', {})])
    router.events.on('routeChangeComplete', change_complete)
    return () => {
      router.events.off('routeChangeComplete', change_complete)
    }
  }, [router])


  return (
  <Fragment><Fragment>
  <VStack sx={{"marginLeft": "20px", "marginRight": "20px", "gap": "0"}}>
  <Flex sx={{"width": "100%", "marginTop": "16px", "marginBottom": "10px"}}>
  <ButtonGroup>
  <Button sx={{"bg": "#141723", "_hover": {"bg": "#141723"}}}>
  <Image src="iprism_logo_st1.png"/>
</Button>
</ButtonGroup>
  <Spacer/>
  <ButtonGroup isAttached={true}>
  <Button sx={{"color": "#fff", "bg": "#12C365", "borderRadius": "4px", "width": "160px", "height": "36px", "_hover": {"bg": "#079d4e"}}}>
  {`START`}
</Button>
  <Button sx={{"color": "#fff", "bg": "#02071a", "borderRadius": "4px", "width": "160px", "height": "36px", "_hover": {"bg": "#000"}}}>
  {`STOP`}
</Button>
</ButtonGroup>
  <Spacer/>
  <ButtonGroup>
  <Button sx={{"bg": "#141723", "paddingLeft": "0px", "paddingRight": "0px", "height": "32px", "_hover": {"bg": "#141723"}}}>
  <Image src="btn_setting_32.png"/>
</Button>
  <Button sx={{"bg": "#141723", "paddingLeft": "0px", "paddingRight": "0px", "height": "32px", "_hover": {"bg": "#141723"}}}>
  <Image src="btn_exit_32.png"/>
</Button>
</ButtonGroup>
</Flex>
  <Grid sx={{"width": "100%", "gap": 0}} templateColumns="repeat(15, 1fr)">
  <GridItem colSpan={9}>
  <Box>
  <Box sx={{"height": "470px"}}>
  <Center sx={{"width": "100%", "height": "100%", "bg": "#3D4056"}}>
  <Image src="inspection_ready_st1.png"/>
</Center>
</Box>
</Box>
</GridItem>
  <GridItem colSpan={6}>
  <VStack sx={{"marginLeft": "10px"}}>
  <Flex sx={{"bg": "#1E202F", "borderRadius": "4px", "paddingTop": "4px", "paddingBottom": "4px", "paddingLeft": "16px", "paddingRight": "16px", "width": "100%"}}>
  <Center>
  <Text>
  {`Trigger Interval`}
</Text>
</Center>
  <Spacer/>
  <Center>
  <Input errorBorderColor="#FE2C55" focusBorderColor="#0276F9" isRequired={true} placeholder="0" sx={{"borderColor": "#E3E3E3", "width": "120px", "height": "36px", "bg": "#3D4056", "textAlign": "right"}} type="number"/>
  <Text sx={{"marginLeft": "8px", "fontSize": "13px"}}>
  {`초`}
</Text>
</Center>
</Flex>
  <VStack sx={{"width": "100%", "marginTop": "5px"}}>
  <Box sx={{"width": "100%"}}>
  <Text sx={{"width": "100%", "textAlign": "left", "marginTop": "5px"}}>
  {`검사영역 ROI`}
</Text>
</Box>
  <Flex sx={{"width": "100%"}}>
  <Center sx={{"width": "50%"}}>
  <Text sx={{"fontSize": "13px"}}>
  {`X`}
</Text>
  <Input errorBorderColor="#FE2C55" focusBorderColor="#0276F9" isRequired={true} placeholder="0" sx={{"borderColor": "#E3E3E3", "width": "120px", "bg": "#3D4056", "textAlign": "right", "marginLeft": "10px", "height": "36px"}} type="number"/>
</Center>
  <Center sx={{"width": "50%"}}>
  <Text sx={{"fontSize": "13px"}}>
  {`W`}
</Text>
  <Input errorBorderColor="#FE2C55" focusBorderColor="#0276F9" isRequired={true} placeholder="0" sx={{"borderColor": "#E3E3E3", "width": "120px", "bg": "#3D4056", "textAlign": "right", "marginLeft": "10px", "height": "36px"}} type="number"/>
</Center>
</Flex>
  <Flex sx={{"width": "100%"}}>
  <Center sx={{"width": "50%"}}>
  <Text sx={{"fontSize": "13px"}}>
  {`Y`}
</Text>
  <Input errorBorderColor="#FE2C55" focusBorderColor="#0276F9" isRequired={true} placeholder="0" sx={{"borderColor": "#E3E3E3", "width": "120px", "bg": "#3D4056", "textAlign": "right", "marginLeft": "10px", "height": "36px"}} type="number"/>
</Center>
  <Center sx={{"width": "50%"}}>
  <Text sx={{"fontSize": "13px"}}>
  {`D`}
</Text>
  <Input errorBorderColor="#FE2C55" focusBorderColor="#0276F9" isRequired={true} placeholder="0" sx={{"borderColor": "#E3E3E3", "width": "120px", "bg": "#3D4056", "textAlign": "right", "marginLeft": "10px", "height": "36px"}} type="number"/>
</Center>
</Flex>
  <Center>
  <Button sx={{"color": "#fff", "bg": "#F00BBE", "borderRadius": "20px", "marginTop": "10px", "paddingLeft": "50px", "paddingRight": "50px", "height": "32px", "_hover": {"bg": "#C00898"}}}>
  {`적용`}
</Button>
</Center>
</VStack>
  <Divider sx={{"borderColor": "#707289", "boxShadow": "0px 2px 1px #000", "marginTop": "5px", "marginBottom": "5px"}}/>
  <Flex sx={{"width": "100%", "marginTop": "5px"}}>
  <Box sx={{"width": "33%", "paddingLeft": "5px", "paddingRight": "5px", "paddingBottom": "5px"}}>
  <VStack>
  <Text>
  {`이미지 CIELab`}
</Text>
  <Center>
  <Text sx={{"fontSize": "13px"}}>
  {`L`}
</Text>
  <Input errorBorderColor="#FE2C55" focusBorderColor="#0276F9" placeholder="0" sx={{"borderColor": "#2E3040", "bg": "#121424", "textAlign": "right", "marginLeft": "5px", "marginRight": "5px", "height": "36px"}} type="number"/>
</Center>
  <Center>
  <Text sx={{"fontSize": "13px"}}>
  {`a`}
</Text>
  <Input errorBorderColor="#FE2C55" focusBorderColor="#0276F9" placeholder="0" sx={{"borderColor": "#2E3040", "bg": "#121424", "textAlign": "right", "marginLeft": "5px", "marginRight": "5px", "height": "36px"}} type="number"/>
</Center>
  <Center>
  <Text sx={{"fontSize": "13px"}}>
  {`b`}
</Text>
  <Input errorBorderColor="#FE2C55" focusBorderColor="#0276F9" placeholder="0" sx={{"borderColor": "#2E3040", "bg": "#121424", "textAlign": "right", "marginLeft": "5px", "marginRight": "5px", "height": "36px"}} type="number"/>
</Center>
</VStack>
</Box>
  <Box sx={{"width": "32%", "paddingRight": "5px", "paddingBottom": "5px"}}>
  <VStack>
  <Text>
  {`After Calibration`}
</Text>
  <Center>
  <Input errorBorderColor="#FE2C55" focusBorderColor="#0276F9" placeholder="0" sx={{"borderColor": "#2E3040", "bg": "#121424", "textAlign": "right", "marginLeft": "5px", "marginRight": "5px", "height": "36px"}} type="number"/>
</Center>
  <Center>
  <Input errorBorderColor="#FE2C55" focusBorderColor="#0276F9" placeholder="0" sx={{"borderColor": "#2E3040", "bg": "#121424", "textAlign": "right", "marginLeft": "5px", "marginRight": "5px", "height": "36px"}} type="number"/>
</Center>
  <Center>
  <Input errorBorderColor="#FE2C55" focusBorderColor="#0276F9" placeholder="0" sx={{"borderColor": "#2E3040", "bg": "#121424", "textAlign": "right", "marginLeft": "5px", "marginRight": "5px", "height": "36px"}} type="number"/>
</Center>
</VStack>
</Box>
  <Box sx={{"width": "35%", "bg": "#DEDEDE", "borderRadius": "4px", "color": "#000", "paddingRight": "5px", "paddingBottom": "5px"}}>
  <VStack>
  <Text>
  {`Delta LabE`}
</Text>
  <Center>
  <Input errorBorderColor="#FE2C55" focusBorderColor="#0276F9" placeholder="0" sx={{"borderColor": "#2E3040", "bg": "#121424", "textAlign": "right", "marginLeft": "5px", "marginRight": "5px", "height": "36px"}} type="number"/>
  <Text sx={{"fontSize": "13px", "fontWeight": "600"}}>
  {`ΔL`}
</Text>
</Center>
  <Center>
  <Input errorBorderColor="#FE2C55" focusBorderColor="#0276F9" placeholder="0" sx={{"borderColor": "#2E3040", "bg": "#121424", "textAlign": "right", "marginLeft": "5px", "marginRight": "5px", "height": "36px"}} type="number"/>
  <Text sx={{"fontSize": "13px", "fontWeight": "600"}}>
  {`Δa`}
</Text>
</Center>
  <Center>
  <Input errorBorderColor="#FE2C55" focusBorderColor="#0276F9" placeholder="0" sx={{"borderColor": "#2E3040", "bg": "#121424", "textAlign": "right", "marginLeft": "5px", "marginRight": "5px", "height": "36px"}} type="number"/>
  <Text sx={{"fontSize": "13px", "fontWeight": "600"}}>
  {`Δb`}
</Text>
</Center>
  <Center>
  <Input errorBorderColor="#FE2C55" focusBorderColor="#0276F9" placeholder="0" sx={{"borderColor": "#2E3040", "bg": "#121424", "textAlign": "right", "marginLeft": "5px", "marginRight": "5px", "height": "36px"}} type="number"/>
  <Text sx={{"fontSize": "13px", "fontWeight": "600"}}>
  {`ΔE`}
</Text>
</Center>
</VStack>
</Box>
</Flex>
</VStack>
</GridItem>
</Grid>
  <Flex sx={{"width": "100%", "gap": "0", "marginTop": "10px"}}>
  <Box sx={{"width": "45%", "height": "120px"}}>
  <VStack>
  <Flex sx={{"width": "100%", "marginBottom": "10px"}}>
  <Center sx={{"bg": "#121424", "paddingLeft": "12px", "width": "75%", "border": "1px", "borderRadius": "4px", "borderColor": "#5a5b5f"}}>
  <Text>
  {`저장된 이미지 파일 경로...`}
</Text>
  <Spacer/>
</Center>
  <Spacer/>
  <Center>
  <Button sx={{"bg": "#0276F9", "color": "#ffffff", "paddingLeft": "16px", "paddingRight": "16px", "height": "36px", "_hover": [{"bg": "#014593"}]}} type="submit">
  {`경로 열기`}
</Button>
</Center>
</Flex>
  <Grid sx={{"h": "150px", "width": "100%", "bg": "#1E202F", "paddingTop": "12px", "paddingBottom": "12px", "paddingLeft": "10px", "paddingRight": "10px", "borderRadius": "4px", "gap": "4"}} templateColumns="repeat(3, 1fr)">
  <GridItem colSpan={1} rowSpan={1} sx={{"bg": "#00e500"}}>
  <Center sx={{"h": "126px"}}>
  <VStack>
  <Image src="ico_camera_on_64.png"/>
  <Text as="strong">
  {`CAMERA`}
</Text>
</VStack>
</Center>
</GridItem>
  <GridItem colSpan={1} rowSpan={1} sx={{"bg": "#00e500"}}>
  <Center sx={{"h": "126px"}}>
  <VStack>
  <Image src="ico_plc_on_64.png"/>
  <Text as="strong">
  {`PLC`}
</Text>
</VStack>
</Center>
</GridItem>
</Grid>
</VStack>
</Box>
  <Box sx={{"bg": "#1E202F", "width": "55%", "height": "auto", "marginLeft": "10px", "borderRadius": "4px"}}>
  <VStack sx={{"gap": "0", "paddingBottom": "10px"}}>
  <Flex sx={{"width": "100%", "marginTop": "4px", "paddingLeft": "12px", "paddingRight": "12px"}}>
  <Center>
  <Text>
  {`2023.06.22  00:00:00  L(xx), a(xx), b(xx), ΔE(xx), ΔL(xx), Δa(xx), Δb(xx)`}
</Text>
</Center>
  <Spacer/>
  <Center>
  <Text sx={{"color": "#00ff00"}}>
  {`양호`}
</Text>
</Center>
</Flex>
  <Flex sx={{"width": "100%", "marginTop": "4px", "paddingLeft": "12px", "paddingRight": "12px"}}>
  <Center>
  <Text>
  {`2023.06.22  00:00:00  L(xx), a(xx), b(xx), ΔE(xx), ΔL(xx), Δa(xx), Δb(xx)`}
</Text>
</Center>
  <Spacer/>
  <Center>
  <Text sx={{"color": "#ffee00"}}>
  {`경고`}
</Text>
</Center>
</Flex>
  <Flex sx={{"width": "100%", "marginTop": "4px", "paddingLeft": "12px", "paddingRight": "12px"}}>
  <Center>
  <Text>
  {`2023.06.22  00:00:00  L(xx), a(xx), b(xx), ΔE(xx), ΔL(xx), Δa(xx), Δb(xx)`}
</Text>
</Center>
  <Spacer/>
  <Center>
  <Text sx={{"color": "#ff3e3e"}}>
  {`불량`}
</Text>
</Center>
</Flex>
  <Flex sx={{"width": "100%", "marginTop": "4px", "paddingLeft": "12px", "paddingRight": "12px"}}>
  <Center>
  <Text>
  {`2023.06.22  00:00:00  L(xx), a(xx), b(xx), ΔE(xx), ΔL(xx), Δa(xx), Δb(xx)`}
</Text>
</Center>
  <Spacer/>
  <Center>
  <Text sx={{"color": "#00ff00"}}>
  {`양호`}
</Text>
</Center>
</Flex>
  <Flex sx={{"width": "100%", "marginTop": "4px", "paddingLeft": "12px", "paddingRight": "12px"}}>
  <Center>
  <Text>
  {`2023.06.22  00:00:00  L(xx), a(xx), b(xx), ΔE(xx), ΔL(xx), Δa(xx), Δb(xx)`}
</Text>
</Center>
  <Spacer/>
  <Center>
  <Text sx={{"color": "#ffee00"}}>
  {`경고`}
</Text>
</Center>
</Flex>
  <Flex sx={{"width": "100%", "marginTop": "4px", "paddingLeft": "12px", "paddingRight": "12px"}}>
  <Center>
  <Text>
  {`2023.06.22  00:00:00  L(xx), a(xx), b(xx), ΔE(xx), ΔL(xx), Δa(xx), Δb(xx)`}
</Text>
</Center>
  <Spacer/>
  <Center>
  <Text sx={{"color": "#ff3e3e"}}>
  {`불량`}
</Text>
</Center>
</Flex>
  <Flex sx={{"width": "100%", "marginTop": "4px", "paddingLeft": "12px", "paddingRight": "12px"}}>
  <Center>
  <Text>
  {`2023.06.22  00:00:00  L(xx), a(xx), b(xx), ΔE(xx), ΔL(xx), Δa(xx), Δb(xx)`}
</Text>
</Center>
  <Spacer/>
  <Center>
  <Text sx={{"color": "#00ff00"}}>
  {`양호`}
</Text>
</Center>
</Flex>
</VStack>
</Box>
</Flex>
</VStack>
  <NextHead>
  <title>
  {`Pynecone App`}
</title>
  <meta content="A Pynecone app." name="description"/>
  <meta content="favicon.ico" property="og:image"/>
</NextHead>
</Fragment>
    </Fragment>
  )
}
