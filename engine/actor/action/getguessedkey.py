import pygame
from pygame.locals import *

class Get_Key:
    def __init__(self, word):
        self.types = "event"
        self.entity_state = None
        self.word = word
        self.verbose = False
        self.name = "get key class action"
        self.guessed_letters = []
        self.correct_letters = []
        self.wrong_letters = []


    def is_my_letter_active(self, name, activity):
        for a in self.entity_state.actions:
            if a.name == "Display Screen Action":
                for e in a.children:
                    if e.entity_state.name == name:
                        e.entity_state.active = activity

    def guess_check(self, letter):
        letter = str.lower(letter)
        for char in self.word:
            if char == letter:
                if letter not in self.guessed_letters:
                    self.guessed_letters.append(letter)
            if letter not in self.correct_letters and letter in self.word:
                self.correct_letters.append(letter)
        if letter not in self.word:
            if letter not in self.wrong_letters:
                self.wrong_letters.append(letter)
        
    def condition_to_act(self, event):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        elif event.type != KEYDOWN:
            return False
        return True


    def act(self, event):
        if self.condition_to_act(event):
            self.Key_Input(event)
            for currentLetter in self.word:
                if currentLetter in self.correct_letters:
                    self.is_my_letter_active(currentLetter, True)
                    self.is_my_letter_active("rectangle_"+currentLetter, False)

                correct_word_counter = 0
                for n in self.correct_letters:
                    for x in self.word:
                        if n == x:
                            correct_word_counter = correct_word_counter + 1

                if correct_word_counter == len(self.word):
                    print("YOU WON!")
                    self.entity_state.terminate()


                for i in range(0, len(self.wrong_letters)):
                    self.is_my_letter_active("Hangman" + str(i), True)
                    #print("Hangman"+str(i))
                for l in self.wrong_letters:
                    print(self.wrong_letters)
                    self.is_my_letter_active("letter"+str(l), True)

                if len(self.wrong_letters) >= 7:
                    print("YOU LOSE!")
                    self.entity_state.terminate()

    def Key_Input(self, event):
        self.verbose = True
        if event.type == KEYDOWN:
            if event.key == K_q:
                if self.verbose:
                    print("q was detected")
                self.guess_check("Q")
            if event.key == K_w:
                if self.verbose:
                    print("w was detected")
                self.guess_check("W")
            elif event.key == K_e:
                if self.verbose:
                   print("e was detected")
                self.guess_check("E")
            elif event.key == K_r:
                if self.verbose:
                    print("r was detected")
                self.guess_check("R")
            elif event.key == K_t:
                if self.verbose:
                    print("t was detected")
                self.guess_check("T")
            elif event.key == K_y:
               if self.verbose:
                print("y was detected")
                self.guess_check("Y")
            elif event.key == K_u:
                if self.verbose:
                    print("u was detected")
                self.guess_check("U")
            elif event.key == K_i:
                if self.verbose:
                    print("i was detected")
                self.guess_check("I")
            elif event.key == K_o:
                if self.verbose:
                    print("o was detected")
                self.guess_check("O")
            elif event.key == K_p:
                if self.verbose:
                    print("p was detected")
                self.guess_check("P")
            elif event.key == K_a:
                if self.verbose:
                    print("a was detected")
                self.guess_check("A")
            elif event.key == K_s:
                if self.verbose:
                    print("s was detected")
                self.guess_check("S")
            elif event.key == K_d:
                if self.verbose:
                    print("d was detected")
                self.guess_check("D")
            elif event.key == K_f:
                if self.verbose:
                    print("f was detected")
                self.guess_check("F")
            elif event.key == K_g:
                if self.verbose:
                    print("g was detected")
                self.guess_check("G")
            elif event.key == K_h:
                if self.verbose:
                    print("h was detected")
                self.guess_check("H")
            elif event.key == K_j:
                if self.verbose:
                    print("j was detected")
                self.guess_check("J")
            elif event.key == K_k:
                if self.verbose:
                    print("k was detected")
                self.guess_check("K")
            elif event.key == K_l:
                if self.verbose:
                    print("l was detected")
                self.guess_check("L")
            elif event.key == K_z:
                if self.verbose:
                    print("z was detected")
                self.guess_check("Z")
            elif event.key == K_x:
                if self.verbose:
                    print("x was detected")
                self.guess_check("X")
            elif event.key == K_c:
                if self.verbose:
                    print("c was detected")
                self.guess_check("C")
            elif event.key == K_v:
                if self.verbose:
                    print("v was detected")
                self.guess_check("V")
            elif event.key == K_b:
                if self.verbose:
                    print("b was detected")
                self.guess_check("B")
            elif event.key == K_n:
                if self.verbose:
                    print("n was detected")
                self.guess_check("N")
            elif event.key == K_m:
                if self.verbose:
                    print("m was detected")
                self.guess_check("M")

            
        