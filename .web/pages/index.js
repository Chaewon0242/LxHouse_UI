import { Fragment, useEffect, useRef, useState } from "react"
import { useRouter } from "next/router"
import { connect, E, getRefValue, isTrue, preventDefault, processEvent, refs, set_val, uploadFiles } from "/utils/state"
import "focus-visible/dist/focus-visible"
import { Box, Button, ButtonGroup, Center, Divider, Flex, Grid, GridItem, Image, Input, Modal, ModalBody, ModalContent, ModalFooter, ModalHeader, ModalOverlay, Spacer, Text, useColorMode, VStack } from "@chakra-ui/react"
import NextHead from "next/head"


export default function Component() {
  const [state, setState] = useState({"btn_start_bg": "#12C365", "btn_start_disabled": false, "btn_start_hover_bg": "#079d4e", "btn_start_off_bg": "#02071a", "btn_start_off_hover_bg": "#000", "btn_start_on_bg": "#12C365", "btn_start_on_hover_bg": "#079d4e", "btn_stop_bg": "#02071a", "btn_stop_disabled": false, "btn_stop_hover_bg": "#000", "btn_stop_off_bg": "#02071a", "btn_stop_off_hover_bg": "#000", "btn_stop_on_bg": "#fe2c55", "btn_stop_on_hover_bg": "#c91236", "is_hydrated": false, "is_start": false, "setting_show": false, "events": [{"name": "state.hydrate"}], "files": []})
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

  const ref_w = useRef(null); refs['ref_w'] = ref_w;
  const ref_default_E = useRef(null); refs['ref_default_E'] = ref_default_E;
  const ref_d = useRef(null); refs['ref_d'] = ref_d;
  const ref_trigger_interval = useRef(null); refs['ref_trigger_interval'] = ref_trigger_interval;
  const ref_calibration_E = useRef(null); refs['ref_calibration_E'] = ref_calibration_E;
  const ref_delta_warning_E = useRef(null); refs['ref_delta_warning_E'] = ref_delta_warning_E;
  const ref_delta_bad_a = useRef(null); refs['ref_delta_bad_a'] = ref_delta_bad_a;
  const ref_delta_warning_b = useRef(null); refs['ref_delta_warning_b'] = ref_delta_warning_b;
  const ref_delta_bad_L = useRef(null); refs['ref_delta_bad_L'] = ref_delta_bad_L;
  const ref_delta_warning_a = useRef(null); refs['ref_delta_warning_a'] = ref_delta_warning_a;
  const ref_default_b = useRef(null); refs['ref_default_b'] = ref_default_b;
  const ref_calibration_b = useRef(null); refs['ref_calibration_b'] = ref_calibration_b;
  const ref_delta_bad_E = useRef(null); refs['ref_delta_bad_E'] = ref_delta_bad_E;
  const ref_x = useRef(null); refs['ref_x'] = ref_x;
  const ref_calibration_a = useRef(null); refs['ref_calibration_a'] = ref_calibration_a;
  const ref_delta_bad_b = useRef(null); refs['ref_delta_bad_b'] = ref_delta_bad_b;
  const ref_y = useRef(null); refs['ref_y'] = ref_y;
  const ref_default_a = useRef(null); refs['ref_default_a'] = ref_default_a;
  const ref_default_L = useRef(null); refs['ref_default_L'] = ref_default_L;
  const ref_calibration_L = useRef(null); refs['ref_calibration_L'] = ref_calibration_L;
  const ref_delta_warning_L = useRef(null); refs['ref_delta_warning_L'] = ref_delta_warning_L;

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
  <Button onClick={_e => Event([E("state.Click_Start", {})], _e)} sx={{"color": "#fff", "borderRadius": "4px", "width": "160px", "height": "36px", "bg": state.btn_start_bg, "_hover": {"bg": state.btn_start_hover_bg}}}>
  {`START`}
</Button>
  <Button onClick={_e => Event([E("state.Click_Stop", {})], _e)} sx={{"color": "#fff", "borderRadius": "4px", "width": "160px", "height": "36px", "bg": state.btn_stop_bg, "_hover": {"bg": state.btn_stop_hover_bg}}}>
  {`STOP`}
</Button>
</ButtonGroup>
  <Spacer/>
  <ButtonGroup>
  <Button onClick={_e => Event([E("state.Click_Setting", {})], _e)} sx={{"bg": "#141723", "paddingLeft": "0px", "paddingRight": "0px", "height": "32px", "_hover": {"bg": "#141723"}}}>
  <Image src="btn_setting_32.png"/>
</Button>
  <Modal isOpen={state.setting_show} size="xl">
  <ModalOverlay>
  <Box as="form" onSubmit={_e => Event([E("state.Click_SettingApply", {form_data:{"delta_bad_b": getRefValue(ref_delta_bad_b), "delta_warning_b": getRefValue(ref_delta_warning_b), "calibration_E": getRefValue(ref_calibration_E), "calibration_L": getRefValue(ref_calibration_L), "default_L": getRefValue(ref_default_L), "delta_warning_E": getRefValue(ref_delta_warning_E), "delta_bad_L": getRefValue(ref_delta_bad_L), "delta_bad_E": getRefValue(ref_delta_bad_E), "delta_warning_L": getRefValue(ref_delta_warning_L), "delta_warning_a": getRefValue(ref_delta_warning_a), "default_a": getRefValue(ref_default_a), "delta_bad_a": getRefValue(ref_delta_bad_a), "calibration_a": getRefValue(ref_calibration_a), "default_E": getRefValue(ref_default_E), "default_b": getRefValue(ref_default_b), "calibration_b": getRefValue(ref_calibration_b)}})], _e)}>
  <ModalContent>
  <ModalHeader sx={{"color": "#000"}}>
  {`설정`}
</ModalHeader>
  <ModalBody sx={{"color": "#000", "width": "100%"}}>
  <VStack sx={{"width": "100%", "border": "1px", "borderRadius": "4px", "borderColor": "#9EAFC5", "paddingBottom": "10px", "gap": 0}}>
  <Flex sx={{"width": "100%", "bg": "#F9FAFB", "borderTopLeftRadius": "4px", "borderTopRightRadius": "4px", "fontWeight": "600", "color": "#3D4056", "marginBottom": "10px", "borderBottom": "1px solid #9EAFC5"}}>
  <Center sx={{"height": "50px", "width": "16%"}}>
  {``}
</Center>
  <Center sx={{"height": "50px", "width": "21%"}}>
  {`Default`}
</Center>
  <Center sx={{"height": "50px", "width": "21%"}}>
  {`Calibration`}
</Center>
  <Center sx={{"height": "50px", "width": "21%"}}>
  {`Δ경고`}
</Center>
  <Center sx={{"height": "50px", "width": "21%"}}>
  {`Δ불량`}
</Center>
</Flex>
  <Flex sx={{"paddingLeft": "10px", "paddingRight": "10px", "width": "100%"}}>
  <Center sx={{"height": "50px", "width": "16%"}}>
  <Text sx={{"width": "100%", "textAlign": "left", "fontWeight": "600", "paddingLeft": "30px"}}>
  {`L`}
</Text>
</Center>
  <Center sx={{"height": "50px", "width": "21%"}}>
  <Input id="default_L" isRequired={true} placeholder="0" ref={ref_default_L} sx={{"height": "36px", "textAlign": "right", "color": "#0276F9", "borderColor": "#0276F9", "width": "90px", "_hover": {"borderColor": "#0276F9"}}} type="number"/>
</Center>
  <Center sx={{"height": "50px", "width": "21%"}}>
  <Input id="calibration_L" isRequired={true} placeholder="0" ref={ref_calibration_L} sx={{"height": "36px", "textAlign": "right", "color": "#0276F9", "borderColor": "#0276F9", "width": "90px", "_hover": {"borderColor": "#0276F9"}}} type="number"/>
</Center>
  <Center sx={{"height": "50px", "width": "21%"}}>
  <Input id="delta_warning_L" isRequired={true} placeholder="0" ref={ref_delta_warning_L} sx={{"height": "36px", "textAlign": "right", "color": "#0276F9", "borderColor": "#0276F9", "width": "90px", "_hover": {"borderColor": "#0276F9"}}} type="number"/>
</Center>
  <Center sx={{"height": "50px", "width": "21%"}}>
  <Input id="delta_bad_L" isRequired={true} placeholder="0" ref={ref_delta_bad_L} sx={{"height": "36px", "textAlign": "right", "color": "#0276F9", "borderColor": "#0276F9", "width": "90px", "_hover": {"borderColor": "#0276F9"}}} type="number"/>
</Center>
</Flex>
  <Flex sx={{"paddingLeft": "10px", "paddingRight": "10px", "width": "100%"}}>
  <Center sx={{"height": "50px", "width": "16%"}}>
  <Text sx={{"width": "100%", "textAlign": "left", "fontWeight": "600", "paddingLeft": "30px"}}>
  {`a`}
</Text>
</Center>
  <Center sx={{"height": "50px", "width": "21%"}}>
  <Input id="default_a" isRequired={true} placeholder="0" ref={ref_default_a} sx={{"height": "36px", "textAlign": "right", "color": "#0276F9", "borderColor": "#0276F9", "width": "90px", "_hover": {"borderColor": "#0276F9"}}} type="number"/>
</Center>
  <Center sx={{"height": "50px", "width": "21%"}}>
  <Input id="calibration_a" isRequired={true} placeholder="0" ref={ref_calibration_a} sx={{"height": "36px", "textAlign": "right", "color": "#0276F9", "borderColor": "#0276F9", "width": "90px", "_hover": {"borderColor": "#0276F9"}}} type="number"/>
</Center>
  <Center sx={{"height": "50px", "width": "21%"}}>
  <Input id="delta_warning_a" isRequired={true} placeholder="0" ref={ref_delta_warning_a} sx={{"height": "36px", "textAlign": "right", "color": "#0276F9", "borderColor": "#0276F9", "width": "90px", "_hover": {"borderColor": "#0276F9"}}} type="number"/>
</Center>
  <Center sx={{"height": "50px", "width": "21%"}}>
  <Input id="delta_bad_a" isRequired={true} placeholder="0" ref={ref_delta_bad_a} sx={{"height": "36px", "textAlign": "right", "color": "#0276F9", "borderColor": "#0276F9", "width": "90px", "_hover": {"borderColor": "#0276F9"}}} type="number"/>
</Center>
</Flex>
  <Flex sx={{"paddingLeft": "10px", "paddingRight": "10px", "width": "100%"}}>
  <Center sx={{"height": "50px", "width": "16%"}}>
  <Text sx={{"width": "100%", "textAlign": "left", "fontWeight": "600", "paddingLeft": "30px"}}>
  {`b`}
</Text>
</Center>
  <Center sx={{"height": "50px", "width": "21%"}}>
  <Input id="default_b" isRequired={true} placeholder="0" ref={ref_default_b} sx={{"height": "36px", "textAlign": "right", "color": "#0276F9", "borderColor": "#0276F9", "width": "90px", "_hover": {"borderColor": "#0276F9"}}} type="number"/>
</Center>
  <Center sx={{"height": "50px", "width": "21%"}}>
  <Input id="calibration_b" isRequired={true} placeholder="0" ref={ref_calibration_b} sx={{"height": "36px", "textAlign": "right", "color": "#0276F9", "borderColor": "#0276F9", "width": "90px", "_hover": {"borderColor": "#0276F9"}}} type="number"/>
</Center>
  <Center sx={{"height": "50px", "width": "21%"}}>
  <Input id="delta_warning_b" isRequired={true} placeholder="0" ref={ref_delta_warning_b} sx={{"height": "36px", "textAlign": "right", "color": "#0276F9", "borderColor": "#0276F9", "width": "90px", "_hover": {"borderColor": "#0276F9"}}} type="number"/>
</Center>
  <Center sx={{"height": "50px", "width": "21%"}}>
  <Input id="delta_bad_b" isRequired={true} placeholder="0" ref={ref_delta_bad_b} sx={{"height": "36px", "textAlign": "right", "color": "#0276F9", "borderColor": "#0276F9", "width": "90px", "_hover": {"borderColor": "#0276F9"}}} type="number"/>
</Center>
</Flex>
  <Flex sx={{"paddingLeft": "10px", "paddingRight": "10px", "width": "100%"}}>
  <Center sx={{"height": "50px", "width": "16%"}}>
  <Text sx={{"width": "100%", "textAlign": "left", "fontWeight": "600", "paddingLeft": "30px"}}>
  {`E`}
</Text>
</Center>
  <Center sx={{"height": "50px", "width": "21%"}}>
  <Input id="default_E" isRequired={true} placeholder="0" ref={ref_default_E} sx={{"height": "36px", "textAlign": "right", "color": "#0276F9", "borderColor": "#0276F9", "width": "90px", "_hover": {"borderColor": "#0276F9"}}} type="number"/>
</Center>
  <Center sx={{"height": "50px", "width": "21%"}}>
  <Input id="calibration_E" isRequired={true} placeholder="0" ref={ref_calibration_E} sx={{"height": "36px", "textAlign": "right", "color": "#0276F9", "borderColor": "#0276F9", "width": "90px", "_hover": {"borderColor": "#0276F9"}}} type="number"/>
</Center>
  <Center sx={{"height": "50px", "width": "21%"}}>
  <Input id="delta_warning_E" isRequired={true} placeholder="0" ref={ref_delta_warning_E} sx={{"height": "36px", "textAlign": "right", "color": "#0276F9", "borderColor": "#0276F9", "width": "90px", "_hover": {"borderColor": "#0276F9"}}} type="number"/>
</Center>
  <Center sx={{"height": "50px", "width": "21%"}}>
  <Input id="delta_bad_E" isRequired={true} placeholder="0" ref={ref_delta_bad_E} sx={{"height": "36px", "textAlign": "right", "color": "#0276F9", "borderColor": "#0276F9", "width": "90px", "_hover": {"borderColor": "#0276F9"}}} type="number"/>
</Center>
</Flex>
</VStack>
</ModalBody>
  <ModalFooter>
  <Flex sx={{"width": "100%"}}>
  <Box>
  <Button sx={{"bg": "#f00bbe", "color": "#fff", "fontSize": "15px", "paddingLeft": "30px", "paddingRight": "30px", "_hover": {"bg": "#C00898"}}} type="submit">
  {`적용`}
</Button>
</Box>
  <Spacer/>
  <Box>
  <Button onClick={_e => Event([E("state.Click_SettingCancel", {})], _e)} sx={{"bg": "#EDF2F7", "color": "#3D4056", "fontSize": "15px", "paddingLeft": "30px", "paddingRight": "30px", "_hover": {"bg": "#cad1db"}}}>
  {`취소`}
</Button>
</Box>
</Flex>
</ModalFooter>
</ModalContent>
</Box>
</ModalOverlay>
</Modal>
  <Button onClick={_e => Event([E("state.Click_Exit", {})], _e)} sx={{"bg": "#141723", "paddingLeft": "0px", "paddingRight": "0px", "height": "32px", "_hover": {"bg": "#141723"}}}>
  <Image src="btn_exit_32.png"/>
</Button>
</ButtonGroup>
</Flex>
  <Grid sx={{"width": "100%", "marginBottom": "10px", "gap": 0}} templateColumns="repeat(15, 1fr)">
  <GridItem colSpan={9}>
  <Box>
  <Box sx={{"height": "470px"}}>
  <Center sx={{"width": "100%", "height": "100%", "bg": "#3D4056"}}>
  <Image src="img_sample_900x720.png" sx={{"width": "auto", "height": "100%"}}/>
</Center>
</Box>
</Box>
</GridItem>
  <GridItem colSpan={6}>
  <VStack sx={{"marginLeft": "10px"}}>
  <Box as="form" onSubmit={_e => Event([E("state.Click_UserInputApply", {form_data:{"d": getRefValue(ref_d), "w": getRefValue(ref_w), "y": getRefValue(ref_y), "trigger_interval": getRefValue(ref_trigger_interval), "x": getRefValue(ref_x)}})], _e)} sx={{"width": "100%"}}>
  <Flex sx={{"bg": "#1E202F", "borderRadius": "4px", "paddingTop": "4px", "paddingBottom": "4px", "paddingLeft": "16px", "paddingRight": "16px", "width": "100%"}}>
  <Center>
  <Text>
  {`Trigger Interval`}
</Text>
</Center>
  <Spacer/>
  <Center>
  <Input errorBorderColor="#FE2C55" focusBorderColor="#0276F9" id="trigger_interval" isRequired={true} placeholder="0" ref={ref_trigger_interval} sx={{"borderColor": "#E3E3E3", "width": "120px", "height": "36px", "bg": "#3D4056", "textAlign": "right"}} type="number"/>
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
  <Text sx={{"fontSize": "13px", "marginRight": "10px"}}>
  {`X`}
</Text>
  <Input errorBorderColor="#FE2C55" focusBorderColor="#0276F9" id="x" isRequired={true} placeholder="0" ref={ref_x} sx={{"borderColor": "#E3E3E3", "width": "120px", "height": "36px", "bg": "#3D4056", "textAlign": "right"}} type="number"/>
</Center>
  <Center sx={{"width": "50%"}}>
  <Text sx={{"fontSize": "13px", "marginRight": "10px"}}>
  {`W`}
</Text>
  <Input errorBorderColor="#FE2C55" focusBorderColor="#0276F9" id="w" isRequired={true} placeholder="0" ref={ref_w} sx={{"borderColor": "#E3E3E3", "width": "120px", "height": "36px", "bg": "#3D4056", "textAlign": "right"}} type="number"/>
</Center>
</Flex>
  <Flex sx={{"width": "100%"}}>
  <Center sx={{"width": "50%"}}>
  <Text sx={{"fontSize": "13px", "marginRight": "10px"}}>
  {`Y`}
</Text>
  <Input errorBorderColor="#FE2C55" focusBorderColor="#0276F9" id="y" isRequired={true} placeholder="0" ref={ref_y} sx={{"borderColor": "#E3E3E3", "width": "120px", "height": "36px", "bg": "#3D4056", "textAlign": "right"}} type="number"/>
</Center>
  <Center sx={{"width": "50%"}}>
  <Text sx={{"fontSize": "13px", "marginRight": "10px"}}>
  {`D`}
</Text>
  <Input errorBorderColor="#FE2C55" focusBorderColor="#0276F9" id="d" isRequired={true} placeholder="0" ref={ref_d} sx={{"borderColor": "#E3E3E3", "width": "120px", "height": "36px", "bg": "#3D4056", "textAlign": "right"}} type="number"/>
</Center>
</Flex>
  <Center>
  <Button sx={{"color": "#fff", "bg": "#F00BBE", "borderRadius": "20px", "marginTop": "10px", "paddingLeft": "50px", "paddingRight": "50px", "height": "32px", "_hover": {"bg": "#C00898"}}} type="submit">
  {`적용`}
</Button>
</Center>
</VStack>
</Box>
  <Divider sx={{"borderColor": "#707289", "boxShadow": "0px 2px 1px #000", "marginTop": "5px", "marginBottom": "5px"}}/>
  <Flex sx={{"tyle": {"width": "100%", "marginTop": "5px"}}}>
  <Box sx={{"width": "33%", "paddingLeft": "5px", "paddingRight": "5px", "paddingBottom": "5px"}}>
  <VStack>
  <Text>
  {`이미지 CIELab`}
</Text>
  <Center>
  <Text sx={{"fontSize": "13px"}}>
  {`L`}
</Text>
  <Input errorBorderColor="#FE2C55" focusBorderColor="#2E3040" isReadOnly={true} placeholder="0" sx={{"borderColor": "#2E3040", "bg": "#121424", "height": "36px", "textAlign": "right", "_hover": {"borderColor": "#2E3040"}, "marginLeft": "5px", "marginRight": "5px"}} type="number"/>
</Center>
  <Center>
  <Text sx={{"fontSize": "13px"}}>
  {`a`}
</Text>
  <Input errorBorderColor="#FE2C55" focusBorderColor="#2E3040" isReadOnly={true} placeholder="0" sx={{"borderColor": "#2E3040", "bg": "#121424", "height": "36px", "textAlign": "right", "_hover": {"borderColor": "#2E3040"}, "marginLeft": "5px", "marginRight": "5px"}} type="number"/>
</Center>
  <Center>
  <Text sx={{"fontSize": "13px"}}>
  {`b`}
</Text>
  <Input errorBorderColor="#FE2C55" focusBorderColor="#2E3040" isReadOnly={true} placeholder="0" sx={{"borderColor": "#2E3040", "bg": "#121424", "height": "36px", "textAlign": "right", "_hover": {"borderColor": "#2E3040"}, "marginLeft": "5px", "marginRight": "5px"}} type="number"/>
</Center>
</VStack>
</Box>
  <Box sx={{"width": "32%", "paddingRight": "5px", "paddingBottom": "5px"}}>
  <VStack>
  <Text>
  {`After Calibration`}
</Text>
  <Center>
  <Input errorBorderColor="#FE2C55" focusBorderColor="#2E3040" isReadOnly={true} placeholder="0" sx={{"borderColor": "#2E3040", "bg": "#121424", "height": "36px", "textAlign": "right", "_hover": {"borderColor": "#2E3040"}, "marginLeft": "5px", "marginRight": "5px"}} type="number"/>
</Center>
  <Center>
  <Input errorBorderColor="#FE2C55" focusBorderColor="#2E3040" isReadOnly={true} placeholder="0" sx={{"borderColor": "#2E3040", "bg": "#121424", "height": "36px", "textAlign": "right", "_hover": {"borderColor": "#2E3040"}, "marginLeft": "5px", "marginRight": "5px"}} type="number"/>
</Center>
  <Center>
  <Input errorBorderColor="#FE2C55" focusBorderColor="#2E3040" isReadOnly={true} placeholder="0" sx={{"borderColor": "#2E3040", "bg": "#121424", "height": "36px", "textAlign": "right", "_hover": {"borderColor": "#2E3040"}, "marginLeft": "5px", "marginRight": "5px"}} type="number"/>
</Center>
</VStack>
</Box>
  <Box sx={{"bg": "#DEDEDE", "borderRadius": "4px", "color": "#000", "paddingRight": "5px", "paddingBottom": "5px", "width": "35%"}}>
  <VStack>
  <Text>
  {`Delta LabE`}
</Text>
  <Center>
  <Input errorBorderColor="#FE2C55" focusBorderColor="#2E3040" isReadOnly={true} placeholder="0" sx={{"borderColor": "#2E3040", "bg": "#121424", "height": "36px", "textAlign": "right", "_hover": {"borderColor": "#2E3040"}, "marginLeft": "5px", "marginRight": "5px"}} type="number"/>
  <Text sx={{"fontSize": "13px"}}>
  {`ΔL`}
</Text>
</Center>
  <Center>
  <Input errorBorderColor="#FE2C55" focusBorderColor="#2E3040" isReadOnly={true} placeholder="0" sx={{"borderColor": "#2E3040", "bg": "#121424", "height": "36px", "textAlign": "right", "_hover": {"borderColor": "#2E3040"}, "marginLeft": "5px", "marginRight": "5px"}} type="number"/>
  <Text sx={{"fontSize": "13px"}}>
  {`Δa`}
</Text>
</Center>
  <Center>
  <Input errorBorderColor="#FE2C55" focusBorderColor="#2E3040" isReadOnly={true} placeholder="0" sx={{"borderColor": "#2E3040", "bg": "#121424", "height": "36px", "textAlign": "right", "_hover": {"borderColor": "#2E3040"}, "marginLeft": "5px", "marginRight": "5px"}} type="number"/>
  <Text sx={{"fontSize": "13px"}}>
  {`Δb`}
</Text>
</Center>
  <Center>
  <Input errorBorderColor="#FE2C55" focusBorderColor="#2E3040" isReadOnly={true} placeholder="0" sx={{"borderColor": "#2E3040", "bg": "#121424", "height": "36px", "textAlign": "right", "_hover": {"borderColor": "#2E3040"}, "marginLeft": "5px", "marginRight": "5px"}} type="number"/>
  <Text sx={{"fontSize": "13px"}}>
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
  <Button onClick={_e => Event([E("state.Click_CurFileOpen", {})], _e)} sx={{"bg": "#0276F9", "color": "#ffffff", "paddingLeft": "16px", "paddingRight": "16px", "height": "36px", "_hover": [{"bg": "#014593"}]}} type="submit">
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
