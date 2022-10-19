def make_button_press_action(): 
    import engine.ui.action.buttonaction as bp 
    return bp.ButtonPressAction() 
 
def make_draw_button_action(): 
    import engine.ui.action.drawbuttonaction as bp 
    return bp.DrawRectButtonAction() 

def make_basic_button(bounds, color):
    import engine.ui.entity.button as bu
    button = bu.Button(bounds, color)
    return button

def make_hud_entity(x, y, string):
    import engine.ui.entity.hud as hud
    HUD = hud.HeadsUpDisplay(x, y, string)
    return HUD

def make_hud_action():
    import engine.ui.action.draw_hud as hud
    return hud.Draw_HUD()