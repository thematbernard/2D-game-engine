from pygame import mixer
from assets import sounds as sounds
from pygame.locals import *
import sys

class EmitSound():
    def __init__(self):
        self.types = ["event"]
        self.entity_state = None
        self.name = "make_sound"
        self.children = []
        self.verbose = True
    

    def act(self, data): 
            print(data)
            if data == "button_press_action":
                self.noiseOnClick()
            if data == "alarm_action":
                self.noiseOnTimer()
            return 

    def noiseOnClick(self):
        path = '/Users/mathewbernard/Desktop/Game_Engine/assets/sounds/punch-2-37333.wav'
        myNoise = mixer.Sound(path)
        myNoise.play()
        return

    def noiseOnTimer(self):
        path = '/Users/mathewbernard/Desktop/Game_Engine/assets/sounds/microwave-timer-117077.wav'
        myNoise = mixer.Sound(path)
        myNoise.play()
        return