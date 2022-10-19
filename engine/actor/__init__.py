import pygame

def makeRectangle(x, y, width, height):
    import engine.actor.entity.rectangle as r
    result = r.rectangle(x, y, width, height)
    return result

def draw_rectangle_action():
    import engine.actor.action.drawrectangle as drawrectangle
    return drawrectangle.Draw_Rectangle()

def makeCircle(x, y, width, radius):
    import engine.actor.entity.circle as c
    result = c.circle(x, y, width, radius)
    return result

def draw_circle_action():
    import engine.actor.action.drawcircle as drawcircle
    return drawcircle.Draw_Circle()

def makeLetter(x, y, letter):
    import engine.actor.entity.letter as l
    result = l.letter(x, y, letter)
    return result

def draw_letter_action():
    import engine.actor.action.drawletter as drawletter
    return drawletter.Draw_Letter()

def get_guessed_key_action(word):
    import engine.actor.action.getguessedkey as key
    return key.Get_Key(word)

