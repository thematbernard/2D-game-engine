import pygame
import time as T

class Timer:
    def __init__(self, allotted_time, start_time, current_time, e_time, name = "basic_timer_entity"):
        self.actions = []
        myClock = pygame.time.Clock()
        self.clock = myClock
        self.allotted_time = allotted_time
        self.name = name
        self.start_time = start_time
        self.current_time = current_time
        self.e_time = e_time
        self.verbose = False
        self.active = True
        return

    def insert_action(self, a):
        a.entity_state = self
        self.actions.append(a)
        return

    def tick(self):
        self.current_time = self.current_time + self.clock.tick(60)
        #print("current time = " + str(self.current_time))
        return self.current_time

    def start_timer(self):
        #this gives us a start time of 0
        myTime = pygame.time.get_ticks()
        myStartTime = myTime
        self.start_time = myTime - myStartTime
        #print("start time = " + str(self.start_time))
        return self.start_time

    def elapsed_time(self):
        elapsed_time = abs(self.current_time - self.start_time)
        self.e_time = elapsed_time
        #print("elapsed time = " + str(self.e_time))
        return self.e_time


    def change_allotted_time(self):
        if self.allotted_time >= 900:
            self.allotted_time = self.allotted_time - 250
            return self.allotted_time
    

    
    
