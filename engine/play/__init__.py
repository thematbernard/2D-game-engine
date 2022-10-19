def make_frame_viewer(x, y):
    import engine.play.entity.frameview as fV
    return fV.FrameViewer(x, y)
   

def make_terminate_action():
    import engine.play.action.quit as q
    return q.CloseFrameViewer()

def make_display_screen():
    import engine.play.action.displayaction as da
    window = da.DisplayAction()
    window.entity_state = "display"
    return window

def make_game_loop(content):
    import engine.play.entity.gameloop as gL
    loop = gL.GameLoop()
    for e in content:
        loop.insertEntity(e)
    return loop

def make_game_loop_action():
    import engine.play.action.loopaction as lA
    return lA.LoopAction()
    
def make_reize_action():
    import engine.play.action.resize as R
    return R.WindowResizeAction()
    