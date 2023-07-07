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
#img_inspection_ready_url    = "inspection_ready_st1.png"
img_inspection_ready_url    = "img_sample_900x720.png"
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
txt_trigger_interval    = "Trigger Interval"
txt_sec                 = "초"
txt_roi                 = "검사영역 ROI"
txt_x                   = "X"
txt_y                   = "Y"
txt_w                   = "W"
txt_d                   = "D"
txt_L                   = "L"
txt_a                   = "a"
txt_b                   = "b"
txt_E                   = "E"
txt_delta_L             = "ΔL"
txt_delta_a             = "Δa"
txt_delta_b             = "Δb"
txt_delta_E             = "ΔE"
txt_btn_apply           = "적용"
txt_cielab              = "이미지 CIELab"
txt_after_calibration   = "After Calibration"
txt_delta_labe          = "Delta LabE"
txt_setting             = "설정"
txt_cancel              = "취소"
txt_apply               = "적용"
txt_empty               = ""
txt_default             = "Default"
txt_calibration         = "Calibration"
txt_delta_warning       = "Δ경고"
txt_delta_bad           = "Δ불량"


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
## Divider(구분선)
st_divider = {
    "border_color" : "#707289",
    "box_shadow" : "0px 2px 1px #000",
    "margin_top" : "5px",
    "margin_bottom" : "5px",
}
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
st_inspection_img = {
    "width":"auto",
    "height":"100%",
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
st_btn_start = {
    "color" : "#fff",
    "border_radius" : "4px",
    "width" : "160px",
    "height" : "36px",
}
st_btn_stop = {
    "color" : "#fff",
    "border_radius" : "4px",
    "width" : "160px",
    "height" : "36px",
}
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

## Top Logo Button
st_btn_logo = {
    "bg" : "#141723",
}
st_btn_logo_hover = {
    "bg" : "#141723",
}
st_btn_setting = {
    "bg" : "#141723",
    "padding_left" : "0px",
    "padding_right" : "0px",
    "height" : "32px",
}
st_btn_setting_hover = {
    "bg" : "#141723",
}
st_btn_exit = {
    "bg" : "#141723",
    "padding_left" : "0px",
    "padding_right" : "0px",
    "height" : "32px",
}
st_btn_exit_hover = {
    "bg" : "#141723",
}

## Menu 
## Menu Style
st_menu_container = {
    "margin_left" : "10px"
}
st_menu_box = {
    "width" :"100%",
    "margin_top" :"5px",
}

#st_input_enable
### Trigger Interval Container > Trigger Interval Box
st_input_enable_bg                  = "#3D4056"
st_input_enable_border_color        = "#E3E3E3"
st_input_enable_error_border_color  = "#FE2C55"
st_input_enable_focus_border_color  = "#0276F9"
st_input_disable_bg                  = "#121424"
st_input_disable_border_color        = "#2E3040"
st_input_disable_error_border_color  = "#FE2C55"
st_input_disable_focus_border_color  = "#2E3040"
st_input_num_width          = "120px"
st_input_num_height         = "36px"
st_input_num_align          = "right"
st_input_num_placeholder    = "0"
st_input_num_color_blue     = "#0276F9"
st_setting_input_num_width  = "90px"

st_trigger_interval_container = {
    "bg" : "#1E202F",
    "border_radius" : "4px",
    "padding_top" : "4px",
    "padding_bottom" : "4px",
    "padding_left" : "16px",
    "padding_right" : "16px",
    "width" : "100%",
}
st_trigger_interval_sec = {
    "margin_left" : "8px",
    "font_size": "13px",
}
st_roi_title_box = {
    "width" : "100%",
}
st_roi_title_txt = {
    "width":"100%",
    "text_align":"left",
    "margin_top":"5px",
}
st_roi_unit = {
    "font_size" : "13px",
    "margin_right" : "10px",
}
st_roi_container = {
    "width": "100%", 
}
st_btn_apply = {
    "color" : "#fff",
    "bg" : "#F00BBE",
    "border_radius" : "20px",
    "margin_top" : "10px",
    "padding_left" : "50px",
    "padding_right" : "50px",
    "height" : "32px",
}
st_btn_apply_hover =  {
    "bg" : "#C00898",
}
st_lab_unit = {
    "font_size" : "13px",
}
st_delta_labe_box = {
    "bg" : "#DEDEDE",
    "border_radius" : "4px",
    "color" : "#000",
    "padding_right" : "5px",
    "padding_bottom" : "5px",
}

# Setting User Input Table
st_setting_user_input_table_container = {
    "color" : "#000",
    "width" : "100%",
}
st_setting_user_input_table = {
    "width" : "100%",
    "border" : "1px",
    "border_radius" : "4px",
    "border_color" : "#9EAFC5",
    "padding_bottom" : "10px",
}
st_setting_btn_apply = {
    "bg" : "#f00bbe",
    "color" : "#fff",
    "font_size" : "15px",
    "padding_left" : "30px",
    "padding_right" : "30px",
}
st_setting_btn_apply_hover = {
    "bg" : "#C00898",
}
st_setting_btn_cancel = {
    "bg" : "#EDF2F7",
    "color" : "#3D4056",
    "font_size" : "15px",
    "padding_left" : "30px",
    "padding_right": "30px",
}
st_setting_btn_cancel_hover = {
    "bg" : "#cad1db",
}
st_setting_user_input_table_thead ={
    "width" : "100%",
    "bg":  "#F9FAFB",
    "border_top_left_radius" : "4px",
    "border_top_right_radius" : "4px",
    "font_weight" : "600",
    "color" : "#3D4056",
    "margin_bottom" : "10px",
    "border_bottom" : "1px solid #9EAFC5",
}
st_setting_user_input_table_th = {
    "height" : "50px",
    "width" : "16%",
}
st_setting_user_input_table_tr = {
    "padding_left" : "10px",
    "padding_right" : "10px",
    "width" : "100%",
}
st_setting_user_input_table_td = {
    "height" : "50px",
    "width" : "21%",

}



# Class
class State(pc.State):
    """The app state."""
    setting_show: bool  = False
    is_start: bool      = False
    
    btn_start_disabled     = False
    btn_stop_disabled      = False
     
    btn_start_on_bg         = "#12C365"
    btn_start_on_hover_bg   = "#079d4e"
    btn_stop_on_bg          = "#fe2c55"
    btn_stop_on_hover_bg    = "#c91236"
    btn_start_off_bg         = "#02071a"
    btn_start_off_hover_bg   = "#000"
    btn_stop_off_bg          = "#02071a"
    btn_stop_off_hover_bg    = "#000"

    btn_start_bg: str       = btn_start_on_bg
    btn_start_hover_bg: str = btn_start_on_hover_bg
    btn_stop_bg: str        = btn_stop_off_bg
    btn_stop_hover_bg: str  = btn_stop_off_hover_bg
    
    # def __init__(self):
    #     self._trigger_interval = ""
    #     self._x = ""
    #     self._y = ""
    #     self._w = ""
    #     self._h = ""
        
        
    # [경로열기] 버튼 클릭 이벤트 
    def Click_CurFileOpen(self):
        print ("Current File Open Click")
    
    # Exit 버튼 클릭 이벤트(프로그램 종료 버튼 이벤트)
    def Click_Exit(self):
        print ("Exit Click")
    
    # 상단의 [Start] 버튼 클릭 이벤트
    def Click_Start(self):
        print ("Start Click")
        if self.is_start is False :
            print ("->Start Flag is False")
            self.btn_start_bg        = self.btn_start_off_bg
            self.btn_start_hover_bg  = self.btn_start_off_hover_bg
            self.btn_stop_bg         = self.btn_stop_on_bg
            self.btn_stop_hover_bg   = self.btn_stop_on_hover_bg
            
            self.is_start = True
        else :
            print ("->Start Flag is True")
        
    # 상단의 [Stop] 버튼 클릭 이벤트
    def Click_Stop(self):
        print ("Stop Click")
        if self.is_start is True :
            print ("->Start Flag is True")
            self.btn_start_bg        = self.btn_start_on_bg
            self.btn_start_hover_bg  = self.btn_start_on_hover_bg
            self.btn_stop_bg         = self.btn_stop_off_bg
            self.btn_stop_hover_bg   = self.btn_stop_off_hover_bg
            
            self.is_start = False
        else :
            print ("->Start Flag is False")
    
    # Setting 버튼 클릭 이벤트
    def Click_Setting(self):
        print ("Setting Modal Open")
        self.setting_show = not (self.setting_show)
    
    # Setting 모달창 취소 버튼 클릭 이벤트
    def Click_SettingCancel(self):
        print ("Setting Modal Close")
        self.setting_show = not (self.setting_show)

    # Setting 모달창 적용 버튼 클릭 이벤트
    def Click_SettingApply(self, form_data: dict):
        print ("Setting - Apply Button Click")
        print (form_data)
        #print (form_data['trigger_interval'])
        self.form_data = form_data
        
    # def Click_SettingApply(self, form_data: dict):
    #     print ("Setting Apply")
    #     self.user_input_form_data = form_data
    
    # 적용 버튼 이벤트 (User Input Form data)
    def Click_UserInputApply(self, form_data: dict):
        print ("Apply Button Click")
        print (form_data)
        print (form_data['trigger_interval'])
        self.form_data = form_data
        
#index Start ->
def index() -> pc.Component:
     return pc.vstack(
            # Top Layout 
            pc.flex(
                #Top Left Layout (Logo)
                pc.button_group(
                    #아이프리즘 Logo Image button
                    pc.button( 
                        pc.image(src=img_logo_file_url),
                        style= st_btn_logo,
                        _hover = st_btn_logo_hover,            
                    ),
                ),
                #Top Spacer
                pc.spacer(),
                #Top Center ( START/STOP Button Group )
                pc.button_group(
                    #[Start] 버튼
                    pc.button( 
                        txt_btn_start,
                        style=st_btn_start,
                        bg=State.btn_start_bg,
                        _hover={
                            "bg" : State.btn_start_hover_bg,
                        },
                        on_click=State.Click_Start,
                        # Start 버튼 비활성화 표시 스타일
                        #style=st_btn_start_off,
                        #_hover=st_btn_sart_off_hover,
                        
                        # Start 버튼 활성화 표시 스타일
                        #style=st_btn_start_on,
                        #_hover=st_btn_start_on_hover,
                    ),
                    #[Stop] 버튼
                    pc.button( 
                        txt_btn_stop,
                        style=st_btn_stop,
                        bg=State.btn_stop_bg,
                        _hover={
                            "bg" : State.btn_stop_hover_bg,
                        },
                        on_click=State.Click_Stop,
                        #_hover=st_btn_stop_hover,
                        
                        # Stop 버튼 비활성화 표시 스타일
                        #style=st_btn_stop_off,
                        #_hover=st_btn_stop_off_hover,
                        
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
                    # [Setting] 버튼
                    pc.button( 
                        pc.image(src=img_btn_setting_url),
                        on_click = State.Click_Setting,  #클릭 이벤트 처리
                        style=st_btn_setting,
                        _hover=st_btn_setting_hover,
                    ),
                    # [Setting] 버튼 클릭 시 모달창 Open
                    pc.modal(
                       pc.modal_overlay(
                           pc.form(
                            # Modal Content Start -->
                            pc.modal_content(
                                #모달창 헤더 (타이틀)
                                pc.modal_header(
                                    txt_setting,
                                    color="#000",
                                ),
                                #모달창 바디 (내용)
                                pc.modal_body(
                                    # User Input Table Container
                                    # # User Input Form Start ->
                                    # pc.form(
                                        pc.vstack(
                                            # User Input Row (Thead)
                                            pc.flex(
                                                # User Input Cols
                                                pc.center(
                                                    txt_empty,
                                                    style=st_setting_user_input_table_th,
                                                ),
                                                pc.center(
                                                    txt_default,
                                                    style=st_setting_user_input_table_td,
                                                ),
                                                pc.center(
                                                    txt_calibration,
                                                    style=st_setting_user_input_table_td,
                                                ),
                                                pc.center(
                                                    txt_delta_warning,
                                                    style=st_setting_user_input_table_td,
                                                ),
                                                pc.center(
                                                    txt_delta_bad,
                                                    style=st_setting_user_input_table_td,
                                                ),
                                                style=st_setting_user_input_table_thead,
                                            ),
                                            #User Input Row-1
                                            pc.flex(
                                                #User Input Cols
                                                pc.center(
                                                    pc.text(
                                                        txt_L,
                                                        width="100%",
                                                        text_align="left",
                                                        font_weight="600",
                                                        padding_left="30px",
                                                    ),
                                                    style=st_setting_user_input_table_th, 
                                                ),
                                                pc.center(
                                                    pc.input(
                                                        id="default_L",
                                                        type_="number",
                                                        is_required=True,    #필수입력인경우 True
                                                        placeholder=st_input_num_placeholder,
                                                        height=st_input_num_height,
                                                        text_align=st_input_num_align,
                                                        color=st_input_num_color_blue,
                                                        border_color=st_input_num_color_blue,
                                                        width=st_setting_input_num_width,
                                                        _hover= {
                                                            "border_color" : st_input_num_color_blue,
                                                        }
                                                    ),
                                                    style=st_setting_user_input_table_td,
                                                ),
                                                pc.center(
                                                    pc.input(
                                                        id="calibration_L",
                                                        type_="number",
                                                        is_required=True,   #필수입력인경우 True
                                                        placeholder=st_input_num_placeholder,
                                                        height=st_input_num_height,
                                                        text_align=st_input_num_align,
                                                        color=st_input_num_color_blue,
                                                        border_color=st_input_num_color_blue,
                                                        width=st_setting_input_num_width,
                                                        _hover= {
                                                            "border_color" : st_input_num_color_blue,
                                                        }
                                                    ),
                                                    style=st_setting_user_input_table_td,
                                                ),
                                                pc.center(
                                                    pc.input(
                                                        id="delta_warning_L",
                                                        type_="number",
                                                        is_required=True,    #필수입력인경우 True
                                                        placeholder=st_input_num_placeholder,
                                                        height=st_input_num_height,
                                                        text_align=st_input_num_align,
                                                        color=st_input_num_color_blue,
                                                        border_color=st_input_num_color_blue,
                                                        width=st_setting_input_num_width,
                                                        _hover= {
                                                            "border_color" : st_input_num_color_blue,
                                                        }
                                                    ),
                                                    style=st_setting_user_input_table_td,
                                                ),
                                                pc.center(
                                                    pc.input(
                                                        id="delta_bad_L",
                                                        type_="number",
                                                        is_required=True,    #필수입력인경우 True
                                                        placeholder=st_input_num_placeholder,
                                                        height=st_input_num_height,
                                                        text_align=st_input_num_align,
                                                        color=st_input_num_color_blue,
                                                        border_color=st_input_num_color_blue,
                                                        width=st_setting_input_num_width,
                                                        _hover= {
                                                            "border_color" : st_input_num_color_blue,
                                                        }
                                                    ),
                                                    style=st_setting_user_input_table_td,
                                                ),
                                                style=st_setting_user_input_table_tr,
                                            ),
                                            pc.flex(
                                                #User Input Cols
                                                pc.center(
                                                    pc.text(
                                                        txt_a,
                                                        width="100%",
                                                        text_align="left",
                                                        font_weight="600",
                                                        padding_left="30px",
                                                    ),
                                                    style=st_setting_user_input_table_th,
                                                ),
                                                pc.center(
                                                    pc.input(
                                                        id="default_a",
                                                        type_="number",
                                                        is_required=True,    #필수입력인경우 True
                                                        placeholder=st_input_num_placeholder,
                                                        height=st_input_num_height,
                                                        text_align=st_input_num_align,
                                                        color=st_input_num_color_blue,
                                                        border_color=st_input_num_color_blue,
                                                        width=st_setting_input_num_width,
                                                        _hover= {
                                                            "border_color" : st_input_num_color_blue,
                                                        }
                                                    ),
                                                    style=st_setting_user_input_table_td,
                                                ),
                                                pc.center(
                                                    pc.input(
                                                        id="calibration_a",
                                                        type_="number",
                                                        is_required=True,    #필수입력인경우 True
                                                        placeholder=st_input_num_placeholder,
                                                        height=st_input_num_height,
                                                        text_align=st_input_num_align,
                                                        color=st_input_num_color_blue,
                                                        border_color=st_input_num_color_blue,
                                                        width=st_setting_input_num_width,
                                                        _hover= {
                                                            "border_color" : st_input_num_color_blue,
                                                        }
                                                    ),
                                                    style=st_setting_user_input_table_td,
                                                ),
                                                pc.center(
                                                    pc.input(
                                                        id="delta_warning_a",
                                                        type_="number",
                                                        is_required=True,    #필수입력인경우 True
                                                        placeholder=st_input_num_placeholder,
                                                        height=st_input_num_height,
                                                        text_align=st_input_num_align,
                                                        color=st_input_num_color_blue,
                                                        border_color=st_input_num_color_blue,
                                                        width=st_setting_input_num_width,
                                                        _hover= {
                                                            "border_color" : st_input_num_color_blue,
                                                        }
                                                    ),
                                                    style=st_setting_user_input_table_td,
                                                ),
                                                pc.center(
                                                    pc.input(
                                                        id="delta_bad_a",
                                                        type_="number",
                                                        is_required=True,    #필수입력인경우 True
                                                        placeholder=st_input_num_placeholder,
                                                        height=st_input_num_height,
                                                        text_align=st_input_num_align,
                                                        color=st_input_num_color_blue,
                                                        border_color=st_input_num_color_blue,
                                                        width=st_setting_input_num_width,
                                                        _hover= {
                                                            "border_color" : st_input_num_color_blue,
                                                        }
                                                    ),
                                                    style=st_setting_user_input_table_td,
                                                ),
                                                style=st_setting_user_input_table_tr,
                                            ),
                                            pc.flex(
                                                #User Input Cols
                                                pc.center(
                                                    pc.text(
                                                        txt_b,
                                                        width="100%",
                                                        text_align="left",
                                                        font_weight="600",
                                                        padding_left="30px",
                                                    ),
                                                    style=st_setting_user_input_table_th, 
                                                ),
                                                pc.center(
                                                    pc.input(
                                                        id="default_b",
                                                        type_="number",
                                                        is_required=True,    #필수입력인경우 True
                                                        placeholder=st_input_num_placeholder,
                                                        height=st_input_num_height,
                                                        text_align=st_input_num_align,
                                                        color=st_input_num_color_blue,
                                                        border_color=st_input_num_color_blue,
                                                        width=st_setting_input_num_width,
                                                        _hover= {
                                                            "border_color" : st_input_num_color_blue,
                                                        }
                                                    ),
                                                    style=st_setting_user_input_table_td,
                                                ),
                                                pc.center(
                                                    pc.input(
                                                        id="calibration_b",
                                                        type_="number",
                                                        is_required=True,    #필수입력인경우 True
                                                        placeholder=st_input_num_placeholder,
                                                        height=st_input_num_height,
                                                        text_align=st_input_num_align,
                                                        color=st_input_num_color_blue,
                                                        border_color=st_input_num_color_blue,
                                                        width=st_setting_input_num_width,
                                                        _hover= {
                                                            "border_color" : st_input_num_color_blue,
                                                        }
                                                    ),
                                                    style=st_setting_user_input_table_td, 
                                                ),
                                                pc.center(
                                                    pc.input(
                                                        id="delta_warning_b",
                                                        type_="number",
                                                        is_required=True,    #필수입력인경우 True
                                                        placeholder=st_input_num_placeholder,
                                                        height=st_input_num_height,
                                                        text_align=st_input_num_align,
                                                        color=st_input_num_color_blue,
                                                        border_color=st_input_num_color_blue,
                                                        width=st_setting_input_num_width,
                                                        _hover= {
                                                            "border_color" : st_input_num_color_blue,
                                                        }
                                                    ),
                                                    style=st_setting_user_input_table_td,
                                                ),
                                                pc.center(
                                                    pc.input(
                                                        id="delta_bad_b",
                                                        type_="number",
                                                        is_required=True,    #필수입력인경우 True
                                                        placeholder=st_input_num_placeholder,
                                                        height=st_input_num_height,
                                                        text_align=st_input_num_align,
                                                        color=st_input_num_color_blue,
                                                        border_color=st_input_num_color_blue,
                                                        width=st_setting_input_num_width,
                                                        _hover= {
                                                            "border_color" : st_input_num_color_blue,
                                                        }
                                                    ),
                                                    style=st_setting_user_input_table_td,
                                                ),
                                                style=st_setting_user_input_table_tr,
                                            ),
                                            pc.flex(
                                                #User Input Cols
                                                pc.center(
                                                    pc.text(
                                                        txt_E,
                                                        width="100%",
                                                        text_align="left",
                                                        font_weight="600",
                                                        padding_left="30px",
                                                    ),
                                                    style=st_setting_user_input_table_th, 
                                                ),
                                                pc.center(
                                                    pc.input(
                                                        id="default_E",
                                                        type_="number",
                                                        is_required=True,    #필수입력인경우 True
                                                        placeholder=st_input_num_placeholder,
                                                        height=st_input_num_height,
                                                        text_align=st_input_num_align,
                                                        color=st_input_num_color_blue,
                                                        border_color=st_input_num_color_blue,
                                                        width=st_setting_input_num_width,
                                                        _hover= {
                                                            "border_color" : st_input_num_color_blue,
                                                        }
                                                    ),
                                                    style=st_setting_user_input_table_td, 
                                                ),
                                                pc.center(
                                                    pc.input(
                                                        id="calibration_E",
                                                        type_="number",
                                                        is_required=True,    #필수입력인경우 True
                                                        placeholder=st_input_num_placeholder,
                                                        height=st_input_num_height,
                                                        text_align=st_input_num_align,
                                                        color=st_input_num_color_blue,
                                                        border_color=st_input_num_color_blue,
                                                        width=st_setting_input_num_width,
                                                        _hover= {
                                                            "border_color" : st_input_num_color_blue,
                                                        }
                                                    ),
                                                    style=st_setting_user_input_table_td,
                                                ),
                                                pc.center(
                                                    pc.input(
                                                        id="delta_warning_E",
                                                        type_="number",
                                                        is_required=True,    #필수입력인경우 True
                                                        placeholder=st_input_num_placeholder,
                                                        height=st_input_num_height,
                                                        text_align=st_input_num_align,
                                                        color=st_input_num_color_blue,
                                                        border_color=st_input_num_color_blue,
                                                        width=st_setting_input_num_width,
                                                        _hover= {
                                                            "border_color" : st_input_num_color_blue,
                                                        }
                                                    ),
                                                    style=st_setting_user_input_table_td,
                                                ),
                                                pc.center(
                                                    pc.input(
                                                        id="delta_bad_E",
                                                        type_="number",
                                                        is_required=True,    #필수입력인경우 True
                                                        placeholder=st_input_num_placeholder,
                                                        height=st_input_num_height,
                                                        text_align=st_input_num_align,
                                                        color=st_input_num_color_blue,
                                                        border_color=st_input_num_color_blue,
                                                        width=st_setting_input_num_width,
                                                        _hover= {
                                                            "border_color" : st_input_num_color_blue,
                                                        }
                                                    ),
                                                    style=st_setting_user_input_table_td,
                                                ),
                                                style=st_setting_user_input_table_tr,
                                            ),
                                            style=st_setting_user_input_table,
                                            gap=0,
                                        ),
                                        style=st_setting_user_input_table_container,
                                    # ),
                                    # # User Input Form End <-
                                ),
                                #모달창 푸터 (버튼영역)
                                pc.modal_footer(
                                    pc.flex(
                                        # [적용] 버튼
                                        pc.box(
                                            pc.button(
                                                txt_apply,
                                                type_="submit",
                                                #on_click=State.Click_SettingApply,
                                                style=st_setting_btn_apply,
                                                _hover=st_setting_btn_apply_hover,
                                            ),
                                        ),
                                        pc.spacer(),
                                        # [취소] 버튼
                                        pc.box(
                                            pc.button(
                                                txt_cancel, 
                                                on_click=State.Click_SettingCancel,
                                                style=st_setting_btn_cancel,
                                                _hover=st_setting_btn_cancel_hover,
                                            ),
                                        ),
                                        width="100%",
                                    ),
                                ),                                
                            ),
                            # Modal Content End <--
                            on_submit=State.Click_SettingApply,
                           ),
                        ),
                       is_open=State.setting_show,
                       size="xl",
                    ),
                    #[종료] 버튼 
                        ## 프로그램 종료가 빈도는 적겠지만 필요하다고 느낌.
                        ## 프로그램 종료할일이 없다면 주석처리 해도 됩니다.
                    pc.button( 
                        pc.image(src=img_btn_exit_url),
                        on_click = State.Click_Exit,
                        style=st_btn_exit,
                        _hover=st_btn_exit_hover,
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
                                pc.image(
                                    src=img_inspection_ready_url,
                                    style=st_inspection_img,
                                ),
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
                        pc.form(
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
                                        id="trigger_interval",
                                        type_="number",
                                        is_required=True,
                                        placeholder=st_input_num_placeholder,
                                        border_color = st_input_enable_border_color ,        #Defalut border color
                                        error_border_color=st_input_enable_error_border_color ,   #입력이 유효하지 않을때 border color
                                        focus_border_color=st_input_enable_focus_border_color ,   #포커스가 있을 때 border color
                                        width=st_input_num_width,
                                        height=st_input_num_height,
                                        bg=st_input_enable_bg, 
                                        text_align=st_input_num_align,
                                    ),
                                    pc.text(
                                        txt_sec,
                                        style=st_trigger_interval_sec,
                                    ),
                                ),
                                style=st_trigger_interval_container,
                            ),
                            # 검사영역(ROI)
                            pc.vstack(
                                pc.box(
                                    pc.text(
                                        txt_roi,
                                        style=st_roi_title_txt,
                                    ),
                                    style=st_roi_title_box,
                                ),
                                pc.flex(
                                    pc.center(
                                        pc.text(
                                            txt_x,
                                            style=st_roi_unit,
                                        ),
                                        pc.input(
                                            id="x",
                                            type_="number",
                                            is_required=True,
                                            placeholder=st_input_num_placeholder,
                                            border_color = st_input_enable_border_color ,        #Defalut border color
                                            error_border_color=st_input_enable_error_border_color ,   #입력이 유효하지 않을때 border color
                                            focus_border_color=st_input_enable_focus_border_color ,   #포커스가 있을 때 border color
                                            width=st_input_num_width,
                                            height=st_input_num_height,
                                            bg=st_input_enable_bg, 
                                            text_align=st_input_num_align,
                                        ),
                                        width="50%",
                                    ),
                                    pc.center(
                                        pc.text(
                                            txt_w,
                                            style=st_roi_unit,
                                        ),
                                        pc.input(
                                            id="w",
                                            type_="number",
                                            is_required=True,
                                            placeholder=st_input_num_placeholder,
                                            border_color = st_input_enable_border_color ,        #Defalut border color
                                            error_border_color=st_input_enable_error_border_color ,   #입력이 유효하지 않을때 border color
                                            focus_border_color=st_input_enable_focus_border_color ,   #포커스가 있을 때 border color
                                            width=st_input_num_width,
                                            height=st_input_num_height,
                                            bg=st_input_enable_bg, 
                                            text_align=st_input_num_align,
                                        ),
                                        width="50%",
                                    ),
                                    width="100%",
                                ),
                                pc.flex(
                                    pc.center(
                                        pc.text(
                                            txt_y,
                                            style=st_roi_unit,
                                        ),
                                        pc.input(
                                            id="y",
                                            type_="number",
                                            is_required=True,
                                            placeholder=st_input_num_placeholder,
                                            border_color = st_input_enable_border_color ,        #Defalut border color
                                            error_border_color=st_input_enable_error_border_color ,   #입력이 유효하지 않을때 border color
                                            focus_border_color=st_input_enable_focus_border_color ,   #포커스가 있을 때 border color
                                            width=st_input_num_width,
                                            height=st_input_num_height,
                                            bg=st_input_enable_bg, 
                                            text_align=st_input_num_align,
                                        ),
                                        width="50%",
                                    ),
                                    pc.center(
                                        pc.text(
                                            txt_d,
                                            style=st_roi_unit,
                                        ),
                                        pc.input(
                                            id="d",
                                            type_="number",
                                            is_required=True,
                                            placeholder=st_input_num_placeholder,
                                            border_color = st_input_enable_border_color ,        #Defalut border color
                                            error_border_color=st_input_enable_error_border_color ,   #입력이 유효하지 않을때 border color
                                            focus_border_color=st_input_enable_focus_border_color ,   #포커스가 있을 때 border color
                                            width=st_input_num_width,
                                            height=st_input_num_height,
                                            bg=st_input_enable_bg, 
                                            text_align=st_input_num_align,
                                        ),
                                        width="50%",
                                    ),
                                    style=st_roi_container,
                                ),
                                pc.center(
                                    pc.button(
                                        txt_btn_apply,
                                        type_="submit",
                                        style=st_btn_apply,
                                        _hover=st_btn_apply_hover,
                                    ),
                                ),
                                style=st_menu_box,
                            ),
                            width="100%",
                            on_submit = State.Click_UserInputApply,
                        ),  #pc.form end
                        
                        # 구분선
                        pc.divider( 
                            style=st_divider,
                        ),
                        
                        # CIELab 영역
                        pc.flex(
                            pc.box(
                                pc.vstack(
                                    pc.text(
                                        txt_cielab,
                                    ),
                                    pc.center(
                                        pc.text(
                                            txt_L,
                                            style=st_lab_unit,
                                        ),
                                        pc.input(
                                            type_="number",
                                            is_read_only=True,
                                            placeholder=st_input_num_placeholder,
                                            border_color =st_input_disable_border_color,        #Defalut border color
                                            error_border_color=st_input_disable_error_border_color,   #입력이 유효하지 않을때 border color
                                            focus_border_color=st_input_disable_focus_border_color,   #포커스가 있을 때 border color
                                            bg=st_input_disable_bg, 
                                            height=st_input_num_height,
                                            text_align=st_input_num_align,
                                            _hover = {
                                                "border_color" : st_input_disable_border_color,
                                            },
                                            margin_left="5px",
                                            margin_right="5px",
                                        ),
                                    ),
                                    pc.center(
                                        pc.text(
                                            txt_a,
                                            style=st_lab_unit,
                                        ),
                                        pc.input(
                                            type_="number",
                                            is_read_only=True,
                                            placeholder=st_input_num_placeholder,
                                            border_color =st_input_disable_border_color,        #Defalut border color
                                            error_border_color=st_input_disable_error_border_color,   #입력이 유효하지 않을때 border color
                                            focus_border_color=st_input_disable_focus_border_color,   #포커스가 있을 때 border color
                                            bg=st_input_disable_bg, 
                                            height=st_input_num_height,
                                            text_align=st_input_num_align,
                                            _hover = {
                                                "border_color" : st_input_disable_border_color,
                                            },
                                            margin_left="5px",
                                            margin_right="5px",
                                        ),
                                    ),
                                    pc.center(
                                        pc.text(
                                           txt_b,
                                           style=st_lab_unit,
                                        ),
                                        pc.input(
                                            type_="number",
                                            is_read_only=True,
                                            placeholder=st_input_num_placeholder,
                                            border_color =st_input_disable_border_color,        #Defalut border color
                                            error_border_color=st_input_disable_error_border_color,   #입력이 유효하지 않을때 border color
                                            focus_border_color=st_input_disable_focus_border_color,   #포커스가 있을 때 border color
                                            bg=st_input_disable_bg, 
                                            height=st_input_num_height,
                                            text_align=st_input_num_align,
                                            _hover = {
                                                "border_color" : st_input_disable_border_color,
                                            },
                                            margin_left="5px",
                                            margin_right="5px",
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
                                        txt_after_calibration,
                                    ),
                                    pc.center(
                                        pc.input(
                                            type_="number",
                                            is_read_only=True,
                                            placeholder=st_input_num_placeholder,
                                            border_color =st_input_disable_border_color,        #Defalut border color
                                            error_border_color=st_input_disable_error_border_color,   #입력이 유효하지 않을때 border color
                                            focus_border_color=st_input_disable_focus_border_color,   #포커스가 있을 때 border color
                                            bg=st_input_disable_bg, 
                                            height=st_input_num_height,
                                            text_align=st_input_num_align,
                                            _hover = {
                                                "border_color" : st_input_disable_border_color,
                                            },
                                            margin_left="5px",
                                            margin_right="5px",
                                        ),
                                    ),
                                    pc.center(
                                        pc.input(
                                            type_="number",
                                            is_read_only=True,
                                            placeholder=st_input_num_placeholder,
                                            border_color =st_input_disable_border_color,        #Defalut border color
                                            error_border_color=st_input_disable_error_border_color,   #입력이 유효하지 않을때 border color
                                            focus_border_color=st_input_disable_focus_border_color,   #포커스가 있을 때 border color
                                            bg=st_input_disable_bg, 
                                            height=st_input_num_height,
                                            text_align=st_input_num_align,
                                            _hover = {
                                                "border_color" : st_input_disable_border_color,
                                            },
                                            margin_left="5px",
                                            margin_right="5px",
                                        ),
                                    ),
                                    pc.center(
                                        pc.input(
                                            type_="number",
                                            is_read_only=True,
                                            placeholder=st_input_num_placeholder,
                                            border_color =st_input_disable_border_color,        #Defalut border color
                                            error_border_color=st_input_disable_error_border_color,   #입력이 유효하지 않을때 border color
                                            focus_border_color=st_input_disable_focus_border_color,   #포커스가 있을 때 border color
                                            bg=st_input_disable_bg, 
                                            height=st_input_num_height,
                                            text_align=st_input_num_align,
                                            _hover = {
                                                "border_color" : st_input_disable_border_color,
                                            },
                                            margin_left="5px",
                                            margin_right="5px",
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
                                        txt_delta_labe,
                                    ),
                                    pc.center(
                                        pc.input(
                                            type_="number",
                                            is_read_only=True,
                                            placeholder=st_input_num_placeholder,
                                            border_color =st_input_disable_border_color,        #Defalut border color
                                            error_border_color=st_input_disable_error_border_color,   #입력이 유효하지 않을때 border color
                                            focus_border_color=st_input_disable_focus_border_color,   #포커스가 있을 때 border color
                                            bg=st_input_disable_bg, 
                                            height=st_input_num_height,
                                            text_align=st_input_num_align,
                                            _hover = {
                                                "border_color" : st_input_disable_border_color,
                                            },
                                            margin_left="5px",
                                            margin_right="5px",
                                        ),
                                        pc.text(
                                            txt_delta_L,
                                            style=st_lab_unit,
                                        ),
                                    ),
                                    pc.center(
                                        pc.input(
                                            type_="number",
                                            is_read_only=True,
                                            placeholder=st_input_num_placeholder,
                                            border_color =st_input_disable_border_color,        #Defalut border color
                                            error_border_color=st_input_disable_error_border_color,   #입력이 유효하지 않을때 border color
                                            focus_border_color=st_input_disable_focus_border_color,   #포커스가 있을 때 border color
                                            bg=st_input_disable_bg, 
                                            height=st_input_num_height,
                                            text_align=st_input_num_align,
                                            _hover = {
                                                "border_color" : st_input_disable_border_color,
                                            },
                                            margin_left="5px",
                                            margin_right="5px",
                                        ),
                                        pc.text(
                                            txt_delta_a,
                                            style=st_lab_unit,
                                        ),
                                    ),
                                    pc.center(
                                        pc.input(
                                            type_="number",
                                            is_read_only=True,
                                            placeholder=st_input_num_placeholder,
                                            border_color =st_input_disable_border_color,        #Defalut border color
                                            error_border_color=st_input_disable_error_border_color,   #입력이 유효하지 않을때 border color
                                            focus_border_color=st_input_disable_focus_border_color,   #포커스가 있을 때 border color
                                            bg=st_input_disable_bg, 
                                            height=st_input_num_height,
                                            text_align=st_input_num_align,
                                            _hover = {
                                                "border_color" : st_input_disable_border_color,
                                            },
                                            margin_left="5px",
                                            margin_right="5px",
                                        ),
                                        pc.text(
                                            txt_delta_b,
                                            style=st_lab_unit,
                                        ),
                                    ),
                                    pc.center(
                                        pc.input(
                                            type_="number",
                                            is_read_only=True,
                                            placeholder=st_input_num_placeholder,
                                            border_color =st_input_disable_border_color,        #Defalut border color
                                            error_border_color=st_input_disable_error_border_color,   #입력이 유효하지 않을때 border color
                                            focus_border_color=st_input_disable_focus_border_color,   #포커스가 있을 때 border color
                                            bg=st_input_disable_bg, 
                                            height=st_input_num_height,
                                            text_align=st_input_num_align,
                                            _hover = {
                                                "border_color" : st_input_disable_border_color,
                                            },
                                            margin_left="5px",
                                            margin_right="5px",
                                        ),
                                        pc.text(
                                            txt_delta_E,
                                            style=st_lab_unit,
                                        ),
                                    ),
                                ),
                                width="35%",
                                style=st_delta_labe_box,
                            ),                            
                            tyle=st_menu_box,
                        ),
                        style=st_menu_container,
                    ),
                    col_span=6,     #오른쪽 메뉴영역 6/15
                ),
                template_columns="repeat(15, 1fr)",     #Grid: Width를 15단계로 나눔
                gap=0,
                style=st_contents,
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
                                # [경로 열기] 버튼
                                pc.button(
                                    txt_btn_cur_file,
                                    type_="submit",
                                    on_click= State.Click_CurFileOpen,
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
