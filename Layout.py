screen_helper = """
ScreenManager:
    LoginScreen:
    RegisterScreen:
    MainScreen:
    Change:
    ShowObj:
    account:
<LoginScreen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'mountains.jpg'
    name: 'Login'
    MDLabel:
        text:"Login"
        halign:'center'
        theme_text_color:'Custom'
        text_color:(1, 1, 1, 1)
        font_style:'H4'
        pos_hint:{"center_x": .5, "center_y": 0.825}
    MDTextField:
        id: username
        hint_text:"username"
        pos_hint:{"center_x": .5, "center_y": 0.625}
        size_hint_x:None
        width:300
        current_hint_text_color: (1,1,1,1)
        icon_right:'account'
        icon_right_color: (1,1,1,1)
    MDTextField:
        id: password
        hint_text:"password"
        password: True
        pos_hint:{"center_x": .5, "center_y": 0.525}
        size_hint_x:None
        width:300
        current_hint_text_color: (1,1,1,1) 
        icon_right: 'eye-off'
        color_active: 1, 1, 1, 1
        icon_right_color: (1,1,1,1)
    MDRoundFlatButton:
        text: 'Register'
        pos_hint: {'center_x':0.42,'center_y':0.375}
        text_color:(1, 1, 1, 1)
        on_press: root.manager.current = 'Register'
    MDRoundFlatButton:
        text: 'login'
        pos_hint: {'center_x':0.58,'center_y':0.375}
        text_color:(1, 1, 1, 1)
        on_release: app.verify(username.text, password.text)
        
        
        
        
        

<RegisterScreen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'mountains.jpg'
    name: 'Register'
    MDLabel:
        text:"Sign in"
        halign:'center'
        theme_text_color:'Custom'
        text_color:(1, 1, 1, 1)
        font_style:'H4'
        pos_hint:{"center_x": .5, "center_y": 0.825}
    MDTextField:
        id: RegUsername
        hint_text:"username"
        pos_hint:{"center_x": .5, "center_y": 0.675}
        size_hint_x:None
        current_hint_text_color: (1,1,1,1)
        width:300
        icon_right:'account'
        icon_right_color: (1,1,1,1)
    MDTextField:
        id: RegPassword
        hint_text:"password"
        password: True
        pos_hint:{"center_x": .5, "center_y": 0.575}
        size_hint_x:None
        width:300
        current_hint_text_color: (1,1,1,1)
        icon_right: 'eye-off'
        icon_right_color: (1,1,1,1)
    MDTextField:
        id: RegRepeatPassword
        hint_text:"repeat password"
        password: True
        pos_hint:{"center_x": .5, "center_y": 0.475}
        size_hint_x:None
        width:300
        current_hint_text_color: (1,1,1,1)
        icon_right: 'eye-off'
        icon_right_color: (1,1,1,1)
    MDRoundFlatButton:
        text: 'Register'
        pos_hint: {'center_x':0.42,'center_y':0.375}
        text_color:(1, 1, 1, 1)
        on_release: app.register(RegUsername.text, RegPassword.text, RegRepeatPassword.text)
    MDRoundFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.58,'center_y':0.375}
        text_color:(1, 1, 1, 1)
        on_press: root.manager.current = 'Login'



<MainScreen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'mountains.jpg'
    name: 'main'
    NavigationLayout:
        ScreenManager:
            Screen:    
                orientation: 'vertical'
                MDToolbar:
                    title: app.username
                    left_action_items:[["menu",lambda x: nav_drawer.toggle_nav_drawer()]]
                    elevation :12
                    pos_hint:{"center_x": .5, "center_y": .95}
                MDRoundFlatButton:
                    text: 'Start Object identify here'
                    text_color:(1, 1, 1, 1)
                    size: 110, 110
                    on_release: app.Yolo()
                    pos_hint:{"center_x": .5, "center_y": 0.5}

                MDLabel:
                    text:"Press esc to stop."
                    halign:'center'
                    theme_text_color:'Custom'
                    text_color:(1, 1, 1, 1)
                    font_style:'Subtitle1'
                    pos_hint:{"center_x": .5, "center_y": 0.35}
                MDIconButton:
                    icon: "account"
                    pos_hint:{"center_x": .95, "center_y": .95}
                    user_font_size: "35sp"
                    on_press: root.manager.current = 'account'
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    
                    
                    
                    
                
                    
                    
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout: 
                orientation: 'vertical'
                ScrollView:
                    MDList:
                        OneLineListItem:
                            text:'detected objects'
                            on_press: root.manager.current = 'Show'
                        OneLineListItem:
                            on_press: root.manager.current = 'Login'
                            text:'Logout'
                            
            
            
            
                            
                            
<Change>:
    name: 'change'
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'mountains.jpg' 
    NavigationLayout:
        ScreenManager:
            Screen:    
                orientation: 'vertical'
                MDToolbar:
                    title: app.username
                    left_action_items:[["menu",lambda x: nav_drawer.toggle_nav_drawer()]]
                    elevation :12
                    pos_hint:{"center_x": .5, "center_y": .95}
                MDLabel:
                    text:"change password"
                    halign:'center'
                    theme_text_color:'Custom'
                    text_color:(1, 1, 1, 1)
                    font_style:'H4'
                    pos_hint:{"center_x": .5, "center_y": 0.825}
                MDTextField:
                    id: ChangePas
                    hint_text:"new password"
                    pos_hint:{"center_x": .5, "center_y": 0.625}
                    size_hint_x:None
                    width:300
                    current_hint_text_color: (1,1,1,1)
                    icon_right:'account'
                    icon_right_color: (1,1,1,1)
                MDTextField:
                    id: ChangePasRep
                    hint_text:"repeat new password"
                    password: True
                    pos_hint:{"center_x": .5, "center_y": 0.525}
                    size_hint_x:None
                    width:300
                    current_hint_text_color: (1,1,1,1) 
                    icon_right: 'eye-off'
                    color_active: 1, 1, 1, 1
                    icon_right_color: (1,1,1,1)
                MDRoundFlatButton:
                    text: 'Change password'
                    pos_hint: {'center_x':0.5,'center_y':0.375}
                    text_color:(1, 1, 1, 1)
                    on_release: app.Change(ChangePas.text, ChangePasRep.text)
                MDRoundFlatButton:
                    text: 'Back'
                    pos_hint: {'center_x':0.5,'center_y':0.275}
                    text_color:(1, 1, 1, 1)
                    on_press: root.manager.current = 'account'
                    
                MDIconButton:
                    icon: "account"
                    pos_hint:{"center_x": .95, "center_y": .95}
                    user_font_size: "35sp"
                    on_press: root.manager.current = 'account'
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    
                    
                                  
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout: 
                orientation: 'vertical'
                ScrollView:
                    MDList:
                    
                        OneLineListItem:
                            on_press: root.manager.current = 'main'
                            text:'start detecting objects'
                            
                        OneLineListItem:
                            text:'detected objects'
                            on_press: root.manager.current = 'Show'

                        OneLineListItem:
                            on_press: root.manager.current = 'Login'
                            text:'Logout'
                            
                            
                            
                            
<ShowObj>:
    name: 'Show'
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'mountains.jpg' 
    NavigationLayout:
        ScreenManager:
            Screen:    
                orientation: 'vertical'
                MDToolbar:
                    title: app.username
                    left_action_items:[["menu",lambda x: nav_drawer.toggle_nav_drawer()]]
                    elevation :12
                    pos_hint:{"center_x": .5, "center_y": .95}
                MDRoundFlatButton:
                    text: 'Show detected objects'
                    pos_hint: {'center_x':0.5,'center_y':0.5}
                    text_color:(1, 1, 1, 1)
                    size: 110, 110
                    on_release: app.open_table()
                MDIconButton:
                    icon: "account"
                    pos_hint:{"center_x": .95, "center_y": .95}
                    user_font_size: "35sp"
                    on_press: root.manager.current = 'account'
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    
                
                    
                    
                                  
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout: 
                orientation: 'vertical'
                ScrollView:
                    MDList:
                        OneLineListItem:
                            on_press: root.manager.current = 'main'
                            text:'start detecting objects'
          
                        OneLineListItem:
                            on_press: root.manager.current = 'Login'
                            text:'Logout'                            
                            
                            
                            
                            
<account>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'mountains.jpg'
    name: 'account'
    NavigationLayout:
        ScreenManager:
            Screen:    
                orientation: 'vertical'
                MDToolbar:
                    title: app.username
                    left_action_items:[["menu",lambda x: nav_drawer.toggle_nav_drawer()]]
                    elevation :12
                    pos_hint:{"center_x": .5, "center_y": .95}
                MDLabel:
                    text:"your account"
                    halign:'center'
                    theme_text_color:'Custom'
                    text_color:(1, 1, 1, 1)
                    font_style:'H4'
                    pos_hint:{"center_x": .5, "center_y": 0.8}
                
                MDLabel:
                    text:"User ID :"
                    halign:'left'
                    theme_text_color:'Custom'
                    text_color:(1, 1, 1, 1)
                    pos_hint:{"center_x": 0.9, "center_y": 0.5} 
                    
                MDLabel:
                    text: app.strID
                    halign:'left'
                    theme_text_color:'Custom'
                    text_color:(1, 1, 1, 1)
                    pos_hint:{"center_x": 1.005, "center_y": 0.5}
                   
                MDLabel:
                    text:"Username :"
                    halign:'right'
                    theme_text_color:'Custom'
                    text_color:(1, 1, 1, 1)
                    pos_hint:{"center_x": 0.0, "center_y": 0.7}
                    
                MDLabel:
                    text: app.username
                    halign:'left'
                    theme_text_color:'Custom'
                    text_color:(1, 1, 1, 1)
                    pos_hint:{"center_x": 1.005, "center_y": 0.7}
                    
                MDLabel:
                    text:"Time of registration : "
                    halign:'right'
                    theme_text_color:'Custom'
                    text_color:(1, 1, 1, 1)
                    pos_hint:{"center_x": .0, "center_y": 0.4}
                    
                MDLabel:
                    text: app.TimeOfReg
                    halign:'left'
                    theme_text_color:'Custom'
                    text_color:(1, 1, 1, 1)
                    pos_hint:{"center_x": 1.005, "center_y": 0.4}
                    
                MDLabel:
                    text:"password :"
                    halign:'right'
                    theme_text_color:'Custom'
                    text_color:(1, 1, 1, 1)
                    pos_hint:{"center_x": .0, "center_y": 0.6}
                    
                MDLabel:
                    text: app.password
                    halign:'left'
                    theme_text_color:'Custom'
                    text_color:(1, 1, 1, 1)
                    pos_hint:{"center_x": 1.005, "center_y": 0.6}

                
                MDRoundFlatButton:
                    text: 'change password'
                    pos_hint: {'center_x':0.5,'center_y':0.3}
                    text_color:(1, 1, 1, 1)
                    on_press: root.manager.current = 'change'
                    
                MDIconButton:
                    icon: "account"
                    pos_hint:{"center_x": .95, "center_y": .95}
                    user_font_size: "35sp"
                    on_press: root.manager.current = 'account'
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    
                    
                    
                
                    
                    
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout: 
                orientation: 'vertical'
                ScrollView:
                    MDList:
                        OneLineListItem:
                            text:'start detecting objects'
                            on_press: root.manager.current = 'main'
                        OneLineListItem:
                            text:'detected objects'
                            on_press: root.manager.current = 'Show'
                        OneLineListItem:
                            on_press: root.manager.current = 'Login'
                            text:'Logout'                          
    
                  
"""



