
screen_manager = """
            
ScreenManager:
    LoginScreen:
    RegScreen:

<LoginScreen>:
    name: 'login'
    MDTextField:
        id: user
        helper_text: 'username'
        helper_text_mode: 'persistent'
        icon_left: 'shield-account'
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint_x: None
        width: 300
    MDTextField:
        id: pw
        helper_text: 'password'
        helper_text_mode: 'persistent'
        icon_left: 'shield-lock'
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        size_hint_x: None
        width: 300
    MDRectangleFlatIconButton:
        id: login_button
        text: 'Log In'
        icon: 'login-variant'
        pos_hint: {'center_x':0.5, 'center_y':0.3}
        on_press: root.get_data()
    MDRectangleFlatIconButton:
        id: reg_button
        text: 'Registration'
        icon: 'account-box' 
        pos_hint: {'center_x':0.5, 'center_y':0.22}
        on_press: root.manager.current = 'reg'
    Image:
        source: 'logowe.png'
        pos_hint: {'center_x': 0.5, 'center_y': 0.75}
    MDLabel:
        text: '2022 Anaconda 1337. All rights reserved.'
        pos_hint: {'center_x': 0.86, 'center_y': 0.05}
        font_style: 'Caption'
<RegScreen>:
    name: 'reg'
    MDRectangleFlatIconButton:
        id: confirm_button
        text: 'Submit'
        icon: 'folder-upload' 
        pos_hint: {'center_x':0.5, 'center_y':0.22}
        on_press: root.get_data_reg()
    MDIconButton:
        id: back_button
        icon: 'step-backward'
        icon_color: app.theme_cls.primary_color 
        pos_hint: {'center_x':0.33, 'center_y':0.22}
        on_press: root.manager.current = 'login'
    MDIconButton:
        id: forward_button
        icon: 'step-forward'
        icon_color: app.theme_cls.primary_color 
        pos_hint: {'center_x':0.66, 'center_y':0.22}
        on_press: root.manager.current = 'login'
    MDLabel:
        text: 'Registration'
        halign: 'center'
        pos_hint: {'center_x': 0.5, 'center_y': 0.85}
        font_style: 'Button'
    MDTextField:
        id: user_reg
        helper_text: 'username'
        helper_text_mode: 'persistent'
        icon_left: 'shield-account'
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}
        size_hint_x: None
        width: 300
    MDTextField:
        id: email_reg
        helper_text: 'email address'
        helper_text_mode: 'persistent'
        icon_left: 'email'
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        size_hint_x: None
        width: 300    
    MDTextField:
        id: pw_reg
        helper_text: 'password'
        helper_text_mode: 'persistent'
        icon_left: 'lock'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint_x: None
        width: 300
    MDTextField:
        id: pw_reg_2
        helper_text: 'password confirmation'
        helper_text_mode: 'persistent'
        icon_left: 'lock-check'
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        size_hint_x: None
        width: 300
<LoadingScreen>:
    name: 'loading'
    Image:
        source: 'logowe.png'
        pos_hint: {'center_x': 0.5, 'center_y': 0.75}

"""