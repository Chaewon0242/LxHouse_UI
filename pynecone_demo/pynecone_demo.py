"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc

"""
docs_url = "https://www.naver.com"
filename = f"{config.app_name}/{config.app_name}.py"
"""
filename = f"{config.app_name}/{config.app_name}.py"

# Image File URL
img_logo_file_url           = "iprism_logo_st1.png"
img_btn_exit_url            = "btn_exit_32.png"
img_btn_setting_url         = "btn_setting_32.png"
img_inspection_ready_url    = "inspection_ready_st1.png"
img_indi_camera_on          = "ico_camera_on_64.png"
img_indi_camera_off         = "ico_camera_off_64.png"
img_indi_plc_on             = "ico_plc_on_64.png"
img_indi_plc_off            = "ico_plc_off_64.png"

# Text
txt_msg_log     = "2023.06.22  00:00:00  L(xx), a(xx), b(xx), ΔE(xx), ΔL(xx), Δa(xx), Δb(xx)"
txt_msg_good    = "양호"
txt_msg_bad     = "불량"
txt_msg_warning = "경고"
txt_cur_file    = "저장된 이미지 파일 경로..."
txt_btn_cur_file    = "경로 열기"
txt_indi_camera     = "CAMERA"
txt_indi_plc        = "PLC"
txt_btn_start       = "START"
txt_btn_stop        = "STOP"
txt_trigger_interval = "Trigger Interval"

# Main Style
## initialization
style = {
    "bg": "#141723",
    "color": "#ffffff",
}
## Main Style
st_main = {
    "margin_left" : "20px",
    "margin_right" : "20px",
    "gap" : "0",
}
## Top Style
st_top = {
    "width" : "100%",
    "margin_top" : "16px",
    "margin_bottom" : "10px",
}
## Content Style
st_contents = {
    #"bg" : "yellow",
    "width" : "100%",
    "margin_bottom" :"10px",
}
## Bottom Style
st_bottom = {
    "width" : "100%",
    "gap" : "0",
    "margin_top" : "10px",
}
### Bottom Left Box Style
st_bottom_left_box = {
    "width" : "45%",
    "height" :"120px",
}
### Bottom Right Box Style
st_bottom_right_box = {
    "bg" : "#1E202F",
    "width" : "55%",
    "height" : "auto",
    "margin_left" : "10px",
    "border_radius" : "4px",
}

# Sub Style
## Log Msg [양호]
st_log_msg_good = {
    "color" : "#00ff00",
}
## Log Msg [불량] 
st_log_msg_bad  = {
    "color" : "#ff3e3e",
}
## Log Msg [경고]
st_log_msg_warning = {
    "color" : "#ffee00",
}
## Log Msg Line Style
st_log_item = {
    "width" : "100%",
    "margin_top" : "4px",
    "padding_left" : "12px",
    "padding_right" : "12px",
}
## Log Msg Box Style 
st_log_box = {
    "gap" : "0",
    "padding_bottom" : "10px",
}

## Current File Container > Current File Box > Current File Button 
st_cur_file_container = {
    "width" : "100%",
    "margin_bottom" : "10px",
}
st_cur_file_box = {
    "bg" : "#121424",
    "padding_left" : "12px",
    "width" : "75%",
    "border" : "1px",
    "border_radius" : "4px",
    "border_color" : "#5a5b5f",
}
st_btn_cur_file = {
    "bg" : "#0276F9",
    "color" : "#ffffff",
    "padding_left" : "16px",
    "padding_right" : "16px",
    "height" : "36px",
}
st_btn_cur_file_hover = {
    "bg" :"#014593",
},

## Image Container > Image box
st_img_container = {
    #"width" : "900px",
    "height" : "470px",
}
st_img_box = {
    "width" : "100%",
    "height" : "100%",
    "bg" : "#3D4056",
}

## Indicator Container > Indicator box > Indicator Item
st_indi_container = {
    "h" : "150px",
    "width" : "100%",
    "bg" : "#1E202F",
    "padding_top" : "12px",
    "padding_bottom" : "12px",
    "padding_left" :  "10px",
    "padding_right" : "10px",
    "border_radius" : "4px",
    "gap" : "4",                            
}
st_indi_box = {
    "h" : "126px",
}
st_indi_item_on = { 
    "bg" : "#00e500", 
}
st_indi_item_off = {
    "bg" : "#ff0000", 
}

## START / STOP Button Style
st_btn_start_on = {
    "color" : "#fff",
    "bg" : "#12C365",
    "border_radius" : "4px",
    "width" : "160px",
    "height" : "36px",
}
st_btn_start_on_hover = {
    "bg" :"#079d4e",
}
st_btn_start_off = {
    "color" : "#fff",
    "bg" : "#02071a",
    "border_radius" : "4px",
    "width" : "160px",
    "height" : "36px",
}
st_btn_start_off_hover = {
    "bg" :"#000",
}
st_btn_stop_on = {
    "color" : "#fff",
    "bg" : "#fe2c55",
    "border_radius" : "4px",
    "width" : "160px",
    "height" : "36px",
}
st_btn_stop_on_hover = {
    "bg" :"#c91236",
}
st_btn_stop_off = {
    "color" : "#fff",
    "bg" : "#02071a",
    "border_radius" : "4px",
    "width" : "160px",
    "height" : "36px",
}
st_btn_stop_off_hover = {
    "bg" :"#000",
}

## Menu 
### Trigger Interval Container > Trigger Interval Box 
st_trigger_interval_container = {
    "bg" : "#1E202F",
    "border_radius" : "4px",
    "padding_top" : "4px",
    "padding_bottom" : "4px",
    "padding_left" : "16px",
    "padding_right" : "16px",
    "width" : "100%",
}

# Class
class State(pc.State):
    """The app state."""
    def change(self):
        self.show = not (self.show)


#index Start ->
def index() -> pc.Component:
     return pc.vstack(
            # Top Layout 
            pc.flex(
                #Top Left Layout (Logo)
                pc.button_group(
                    #Logo Image button 
                    pc.button( 
                        pc.image(src=img_logo_file_url),
                        bg="#141723",
                        _hover = {
                            "bg" : "#141723",
                        }                     
                    ),
                ),
                #Top Spacer
                pc.spacer(),
                #Top Center ( START/STOP Button Group )
                pc.button_group(
                    pc.button( 
                        "START",
                        # Start 버튼 비활성화 표시 스타일
                        #style=st_btn_start_off,
                        #_hover=st_btn_sart_off_hover,
                        
                        # Start 버튼 활성화 표시 스타일
                        style=st_btn_start_on,
                        _hover=st_btn_start_on_hover,
                    ),
                    pc.button( 
                        "STOP",
                        # Stop 버튼 비활성화 표시 스타일
                        style=st_btn_stop_off,
                        _hover=st_btn_stop_off_hover,
                        
                        # Stop 버튼 활성화 표시 스타일
                        #style=st_btn_stop_on,
                        #_hover=st_btn_stop_on_hover,
                    ),
                    is_attached=True,
                ),
                #Top Spacer
                pc.spacer(),
                #Top Right (Button)
                pc.button_group(
                   pc.button( 
                        pc.image(src=img_btn_setting_url),
                        bg="#141723",
                        padding_left="0px",
                        padding_right="0px",
                        height="32px",
                        _hover = {
                            "bg" : "#141723",
                        }    
                    ),
                   pc.button( 
                        pc.image(src=img_btn_exit_url),
                        bg="#141723",
                        padding_left="0px",
                        padding_right="0px",
                        height="32px",
                        _hover = {
                            "bg" : "#141723",
                        }    
                    ),
                ),
                style=st_top,
            ),
            # Contents Layout Style-1 
            # 왼쪽 이미지 사이즈를 900x720으로 고정, 레이아웃 1280x1024 해상도 기준
            # pc.flex(
            #     #Contents Left Layout
            #     pc.box(
            #         #Image Box Layout
            #         pc.box(
            #             #Image Box
            #             pc.center(
            #                 #Image
            #                 pc.image(src=img_inspection_ready_url),
            #                 style=st_img_box,
            #             ),
            #             style=st_img_container,
            #         ),
            #     ),
            #     #Contents Right Layout
            #     pc.box(
            #         #Menu Layout
            #         pc.vstack(
            #             #Menu List
            #             pc.center( 
            #                 pc.text("OK"),
            #                 bg="green",
            #             ),
            #             width="100%",
            #         ),     
            #         width="auto",
            #     ),
            #     style=st_contents,
            # ),
            
            # Contents Layout Style-2
            # 왼쪽 이미지 사이즈가 브라우저 사이즈에 맞게 자동 Scale 되게, 1280x1024기준 영역 사이즈가 901.81x710 
            pc.grid(
                pc.grid_item(
                    pc.box(
                        #Image Box Layout
                        pc.box(
                            #Image Box
                            pc.center(
                                #Image
                                pc.image(src=img_inspection_ready_url),
                                style=st_img_box,
                            ),
                            style=st_img_container,
                        ),
                    ),
                    col_span=9,     #왼쪽 이미지 영역 9/15 (590.)
                ),
                pc.grid_item(
                    pc.vstack(
                        # # OK / NG 표시 영역
                        # pc.center(
                        #     pc.text("OK", 
                        #             as_="strong",
                        #             font_size="5em", 
                        #             margin_top="-12px",
                        #             margin_bottom="-4px",
                        #     ),
                        #     bg="#00e500",
                        #     width="100%",
                        #     border_radius = "4px",
                        # ),
                        # # 구분선
                        # pc.divider( 
                        #     border_color="#707289",
                        #     box_shadow="0px 2px 1px #000",
                        # ),
                        
                        # Trigger Interval 영역
                        pc.flex(
                            pc.center(
                                pc.text(
                                    txt_trigger_interval,
                                ),
                            ),
                            pc.spacer(),
                            pc.center(
                                pc.input(
                                    type_="number",
                                    is_required=True,
                                    placeholder="0",
                                    border_color ="#E3E3E3",        #Defalut border color
                                    error_border_color="#FE2C55",   #입력이 유효하지 않을때 border color
                                    focus_border_color="#0276F9",   #포커스가 있을 때 border color
                                    width="120px",
                                    height="36px",
                                    bg = "#3D4056", 
                                    text_align="right",
                                ),
                                pc.text(
                                    "초",
                                    margin_left="8px",
                                    font_size="13px",
                                ),
                            ),
                            style=st_trigger_interval_container,
                        ),
                        
                        # 검사영역(ROI)
                        pc.vstack(
                            pc.box(
                                pc.text(
                                    "검사영역 ROI",
                                    width="100%",
                                    text_align="left",
                                    margin_top="5px",
                                ),
                                width="100%",
                            ),
                            pc.flex(
                                pc.center(
                                    pc.text(
                                        "X",
                                        font_size="13px",
                                    ),
                                    pc.input(
                                        type_="number",
                                        is_required=True,
                                        placeholder="0",
                                        border_color ="#E3E3E3",        #Defalut border color
                                        error_border_color="#FE2C55",   #입력이 유효하지 않을때 border color
                                        focus_border_color="#0276F9",   #포커스가 있을 때 border color
                                        width="120px",
                                        bg = "#3D4056", 
                                        text_align="right",
                                        margin_left="10px",
                                        height="36px",
                                    ),
                                    width="50%",
                                ),
                                pc.center(
                                    pc.text(
                                        "W",
                                        font_size="13px",
                                    ),
                                    pc.input(
                                        type_="number",
                                        is_required=True,
                                        placeholder="0",
                                        border_color ="#E3E3E3",        #Defalut border color
                                        error_border_color="#FE2C55",   #입력이 유효하지 않을때 border color
                                        focus_border_color="#0276F9",   #포커스가 있을 때 border color
                                        width="120px",
                                        bg = "#3D4056", 
                                        text_align="right",
                                        margin_left="10px",
                                        height="36px",
                                    ),
                                    width="50%",
                                ),
                                width="100%",
                            ),
                            pc.flex(
                                pc.center(
                                    pc.text(
                                        "Y",
                                        font_size="13px",
                                    ),
                                    pc.input(
                                        type_="number",
                                        is_required=True,
                                        placeholder="0",
                                        border_color ="#E3E3E3",        #Defalut border color
                                        error_border_color="#FE2C55",   #입력이 유효하지 않을때 border color
                                        focus_border_color="#0276F9",   #포커스가 있을 때 border color
                                        width="120px",
                                        bg = "#3D4056", 
                                        text_align="right",
                                        margin_left="10px",
                                        height="36px",
                                    ),
                                    width="50%",
                                ),
                                pc.center(
                                    pc.text(
                                        "D",
                                        font_size="13px",
                                    ),
                                    pc.input(
                                        type_="number",
                                        is_required=True,
                                        placeholder="0",
                                        border_color ="#E3E3E3",        #Defalut border color
                                        error_border_color="#FE2C55",   #입력이 유효하지 않을때 border color
                                        focus_border_color="#0276F9",   #포커스가 있을 때 border color
                                        width="120px",
                                        bg = "#3D4056", 
                                        text_align="right",
                                        margin_left="10px",
                                        height="36px",
                                    ),
                                    width="50%",
                                ),
                                width="100%",
                            ),
                            pc.center(
                                pc.button(
                                    "적용",
                                    color="#fff",
                                    bg="#F00BBE",
                                    border_radius="20px",
                                    margin_top="10px",
                                    padding_left="50px",
                                    padding_right="50px",
                                    height="32px",
                                    _hover= {
                                        "bg" : "#C00898",
                                    }
                                ),
                            ),
                            width="100%",
                            margin_top="5px",
                        ),
                        
                        # 구분선
                        pc.divider( 
                            border_color="#707289",
                            box_shadow="0px 2px 1px #000",
                            margin_top="5px",
                            margin_bottom="5px",
                        ),
                        
                        # CIELab 영역
                        pc.flex(
                            pc.box(
                                pc.vstack(
                                    pc.text(
                                        "이미지 CIELab",
                                    ),
                                    pc.center(
                                        pc.text(
                                            "L",
                                            font_size="13px",
                                        ),
                                        pc.input(
                                            type_="number",
                                            placeholder="0",
                                            border_color ="#2E3040",        #Defalut border color
                                            error_border_color="#FE2C55",   #입력이 유효하지 않을때 border color
                                            focus_border_color="#0276F9",   #포커스가 있을 때 border color
                                            bg = "#121424", 
                                            text_align="right",
                                            margin_left="5px",
                                            margin_right="5px",
                                            height="36px",
                                        ),
                                    ),
                                    pc.center(
                                        pc.text(
                                            "a",
                                            font_size="13px",
                                        ),
                                        pc.input(
                                            type_="number",
                                            placeholder="0",
                                            border_color ="#2E3040",        #Defalut border color
                                            error_border_color="#FE2C55",   #입력이 유효하지 않을때 border color
                                            focus_border_color="#0276F9",   #포커스가 있을 때 border color
                                            bg = "#121424", 
                                            text_align="right",
                                            margin_left="5px",
                                            margin_right="5px",
                                            height="36px",
                                        ),
                                    ),
                                    pc.center(
                                        pc.text(
                                            "b",
                                            font_size="13px",
                                        ),
                                        pc.input(
                                            type_="number",
                                            placeholder="0",
                                            border_color ="#2E3040",        #Defalut border color
                                            error_border_color="#FE2C55",   #입력이 유효하지 않을때 border color
                                            focus_border_color="#0276F9",   #포커스가 있을 때 border color
                                            bg = "#121424", 
                                            text_align="right",
                                            margin_left="5px",
                                            margin_right="5px",
                                            height="36px",
                                        ),
                                    ),
                                ),
                                width="33%",
                                padding_left="5px",
                                padding_right="5px",
                                padding_bottom="5px",
                            ),
                            pc.box(
                                pc.vstack(
                                    pc.text(
                                        "After Calibration",
                                    ),
                                    pc.center(
                                        pc.input(
                                            type_="number",
                                            placeholder="0",
                                            border_color ="#2E3040",        #Defalut border color
                                            error_border_color="#FE2C55",   #입력이 유효하지 않을때 border color
                                            focus_border_color="#0276F9",   #포커스가 있을 때 border color
                                            bg = "#121424", 
                                            text_align="right",
                                            margin_left="5px",
                                            margin_right="5px",
                                            height="36px",
                                        ),
                                    ),
                                    pc.center(
                                        pc.input(
                                            type_="number",
                                            placeholder="0",
                                            border_color ="#2E3040",        #Defalut border color
                                            error_border_color="#FE2C55",   #입력이 유효하지 않을때 border color
                                            focus_border_color="#0276F9",   #포커스가 있을 때 border color
                                            bg = "#121424", 
                                            text_align="right",
                                            margin_left="5px",
                                            margin_right="5px",
                                            height="36px",
                                        ),
                                    ),
                                    pc.center(
                                        pc.input(
                                            type_="number",
                                            placeholder="0",
                                            border_color ="#2E3040",        #Defalut border color
                                            error_border_color="#FE2C55",   #입력이 유효하지 않을때 border color
                                            focus_border_color="#0276F9",   #포커스가 있을 때 border color
                                            bg = "#121424", 
                                            text_align="right",
                                            margin_left="5px",
                                            margin_right="5px",
                                            height="36px",
                                        ),
                                    ),
                                ),
                                width="32%",
                                padding_right="5px",
                                padding_bottom="5px",
                            ),
                            pc.box(
                                pc.vstack(
                                    pc.text(
                                        "Delta LabE",
                                    ),
                                    pc.center(
                                        pc.input(
                                            type_="number",
                                            placeholder="0",
                                            border_color ="#2E3040",        #Defalut border color
                                            error_border_color="#FE2C55",   #입력이 유효하지 않을때 border color
                                            focus_border_color="#0276F9",   #포커스가 있을 때 border color
                                            bg = "#121424", 
                                            text_align="right",
                                            margin_left="5px",
                                            margin_right="5px",
                                            height="36px",
                                        ),
                                        pc.text(
                                            "ΔL",
                                            font_size="13px",
                                            font_weight="600",
                                        ),
                                    ),
                                    pc.center(
                                        pc.input(
                                            type_="number",
                                            placeholder="0",
                                            border_color ="#2E3040",        #Defalut border color
                                            error_border_color="#FE2C55",   #입력이 유효하지 않을때 border color
                                            focus_border_color="#0276F9",   #포커스가 있을 때 border color
                                            bg = "#121424", 
                                            text_align="right",
                                            margin_left="5px",
                                            margin_right="5px",
                                            height="36px",
                                        ),
                                        pc.text(
                                            "Δa",
                                            font_size="13px",
                                            font_weight="600",
                                        ),
                                    ),
                                    pc.center(
                                        pc.input(
                                            type_="number",
                                            placeholder="0",
                                            border_color ="#2E3040",        #Defalut border color
                                            error_border_color="#FE2C55",   #입력이 유효하지 않을때 border color
                                            focus_border_color="#0276F9",   #포커스가 있을 때 border color
                                            bg = "#121424", 
                                            text_align="right",
                                            margin_left="5px",
                                            margin_right="5px",
                                            height="36px",
                                        ),
                                        pc.text(
                                            "Δb",
                                            font_size="13px",
                                            font_weight="600",
                                        ),
                                    ),
                                    pc.center(
                                        pc.input(
                                            type_="number",
                                            placeholder="0",
                                            border_color ="#2E3040",        #Defalut border color
                                            error_border_color="#FE2C55",   #입력이 유효하지 않을때 border color
                                            focus_border_color="#0276F9",   #포커스가 있을 때 border color
                                            bg = "#121424", 
                                            text_align="right",
                                            margin_left="5px",
                                            margin_right="5px",
                                            height="36px",
                                        ),
                                        pc.text(
                                            "ΔE",
                                            font_size="13px",
                                            font_weight="600",
                                        ),
                                    ),
                                ),
                                width="35%",
                                bg="#DEDEDE",
                                border_radius="4px",
                                color="#000",
                                padding_right="5px",
                                padding_bottom="5px",
                            ),                            
                            width="100%",
                            margin_top="5px",
                        ),
                        margin_left="10px",
                    ),
                    col_span=6,     #오른쪽 메뉴영역 6/15
                ),
                template_columns="repeat(15, 1fr)",     #Grid: Width를 15단계로 나눔
                width="100%",
                gap=0,
            ),            
            # Bottom Layout
            pc.flex(
                #Bottom Left Layout
                pc.box(               
                    pc.vstack(
                        #Current File Layout
                        pc.flex (
                            #Current File Box
                            pc.center(
                                #Current File Name Text
                                pc.text(txt_cur_file),
                                pc.spacer(),
                                style=st_cur_file_box,
                            ),
                            pc.spacer(),
                            pc.center(
                                pc.button(
                                    txt_btn_cur_file,
                                    type_="submit",
                                    style=st_btn_cur_file,
                                    _hover =  st_btn_cur_file_hover,
                                ),
                            ),
                            style=st_cur_file_container,
                        ),         
                        #Indicator Layout
                        pc.grid(
                            #Indicator-1 (Camera ON)
                            pc.grid_item( 
                                            pc.center(
                                                pc.vstack(
                                                    # 카메라 연결된 상태 이미지
                                                    pc.image(src=img_indi_camera_on),
                                                    # 카메라 연결이 끊긴 상태 이미지
                                                    # pc.image(src=img_indi_camera_off),
                                                    pc.text(txt_indi_camera, as_="strong"),
                                                ),
                                                style=st_indi_box,
                                            ),
                                            row_span = 1,
                                            col_span= 1,
                                            # 카메라 연결된 상태 배경 스타일(초록)
                                            style=st_indi_item_on,
                                            # 카메라 연결이 끊긴 배경 스타일(빨강)
                                            #style=st_indi_item_off,
                            ),
                            #Indicator-3 (PLC ON)
                            pc.grid_item( 
                                            pc.center(
                                                pc.vstack(
                                                    # PLC 연결된 상태 이미지
                                                    pc.image(src=img_indi_plc_on),
                                                    # PLC 연결이 끊긴 상태 이미지
                                                    # pc.image(src=img_indi_plc_off),
                                                    pc.text(txt_indi_plc, as_="strong"),
                                                ),
                                                style=st_indi_box,
                                            ), 
                                            row_span = 1,
                                            col_span= 1,
                                            # PLC 연결된 상태 배경 스타일(초록)
                                            style=st_indi_item_on,
                                            # PLC 연결이 끊긴 상태 배경 스타일(빨강)
                                            #style=st_indi_item_off,
                            ),
                            template_columns = "repeat(3, 1fr)",
                            style=st_indi_container
                        ),
                    ),
                    style=st_bottom_left_box,
                ),
                #Bottom Right Layout
                pc.box(
                    #Log Layout
                    pc.vstack(
                        #Log Item-1
                        pc.flex(
                            pc.center(
                                pc.text(txt_msg_log),
                            ),
                            pc.spacer(),
                            pc.center(
                                pc.text(txt_msg_good, style=st_log_msg_good),
                            ),
                            style= st_log_item,
                        ),
                        #Log Item-2
                        pc.flex(
                            pc.center(
                                pc.text(txt_msg_log),
                            ),
                            pc.spacer(),
                            pc.center(
                                pc.text(txt_msg_warning , style=st_log_msg_warning),
                            ),
                            style= st_log_item,
                        ),
                        #Log Item-3
                        pc.flex(
                            pc.center(
                                pc.text(txt_msg_log),
                            ),
                            pc.spacer(),
                            pc.center(
                                pc.text(txt_msg_bad , style=st_log_msg_bad),
                            ),
                            style= st_log_item,
                        ),
                        #Log Item-4
                        pc.flex(
                            pc.center(
                                pc.text(txt_msg_log),
                            ),
                            pc.spacer(),
                            pc.center(
                                pc.text(txt_msg_good , style=st_log_msg_good),
                            ),
                            style= st_log_item,
                        ),
                        #Log Item-5
                        pc.flex(
                            pc.center(
                                pc.text(txt_msg_log),
                            ),
                            pc.spacer(),
                            pc.center(
                                pc.text(txt_msg_warning , style=st_log_msg_warning),
                            ),
                            style= st_log_item,
                        ),
                        #Log Item-6
                        pc.flex(
                            pc.center(
                                pc.text(txt_msg_log),
                            ),
                            pc.spacer(),
                            pc.center(
                                pc.text(txt_msg_bad, style=st_log_msg_bad),
                            ),
                            style= st_log_item,
                        ),
                        #Log Item-7
                        pc.flex(
                            pc.center(
                                pc.text(txt_msg_log),
                            ),
                            pc.spacer(),
                            pc.center(
                                pc.text(txt_msg_good, style=st_log_msg_good),
                            ),
                            style= st_log_item,
                        ),
                       style=st_log_box,
                    ),
                    style=st_bottom_right_box,
                ),
                style=st_bottom,
            ), 
            style=st_main,
        )       
#index End <-

# Add state and page to the app.
app = pc.App(state=State, style=style)
app.add_page(index)
app.compile()