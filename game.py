import pgzrun
from random import randint, choice
import string
import os
import random
from words import words
os.environ["SDL_VIDEO_CENTERED"] = "1"
WIDTH = 1600
HEIGHT = 900
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# LETTER = {"letter": "", "x": 0, "y": 0}
ON_SCREEN_LETTERS = []


VELOCITY = 1
VELOCITY2 = 2
VELOCITY3 = 4
SCORE = {"RIGHT": 0, "WRONG": 0}
intafad = 0
stop1 = 0
e = 0
m = 0
h = 0
st = 0
fuck = [0]

black1 = Actor('back1')
black1.pos = (150,100)
apple = Actor('apple')
apple.pos = (600,40)
stop = Actor('stop')
stop.pos = (200,100)
playcon = Actor('playcon')
playcon.pos = (800,230)
endgame = Actor('endgame')
endgame.pos = (800,630)
regame = Actor('regame')
regame.pos = (800,430)
back1 = Actor('back')
back1.pos = (800,450)
easy = Actor('easy')
easy.pos = (800,230)
hard = Actor('hard')
hard.pos = (800,630)
mid = Actor('mid')
mid.pos = (800,430)


def draw():  # Pygame Zero draw function
    global fuck
    screen.clear()
    screen.fill(BLACK)
    apple.draw()
    screen.draw.text("PLAY", (600, 40), fontsize=200, color=WHITE)
    screen.draw.text("SCROE", (540, 240), fontsize=200, color=WHITE)
    screen.draw.text("OPTION", (500, 440), fontsize=200, color=WHITE)
    screen.draw.text("QUIT", (600, 640), fontsize=200, color=WHITE)
    if intafad == 1:
        screen.clear()
        back1.draw()
        black1.draw()
        easy.draw()
        mid.draw()
        hard.draw()
        
        if e == 1 or m == 1 or h == 1:

            screen.clear()
            stop.draw()
            for LETTER in ON_SCREEN_LETTERS:
                if LETTER["x"] != fuck:
                    screen.draw.text( LETTER["letter"] , (LETTER["x"]  , LETTER["y"]), fontsize=40, color=WHITE)
                    fuck.append(LETTER["x"])
            screen.draw.text("RIGHT: " + str(SCORE["RIGHT"]), (WIDTH - 130, 10), fontsize=30, color=WHITE)
            screen.draw.text("WRONG: " + str(SCORE["WRONG"]), (WIDTH - 130, 40), fontsize=30, color=WHITE)
    if stop1 == 1:
        back1.draw()
        playcon.draw()
        regame.draw()
        endgame.draw()
    
       
    if SCORE["WRONG"] == 3:
        screen.clear()
        screen.draw.text("end: ", (WIDTH - 130, 10), fontsize=30, color=WHITE)
def update():
    global SCORE
    global stop1
    if stop1 != 1 and intafad == 1 and e == 1:
        for i, LETTER in enumerate(ON_SCREEN_LETTERS):
            LETTER["y"] += VELOCITY
            if LETTER["y"] == HEIGHT - 400:
                SCORE["WRONG"] += 1
                delete_letter(i)
        while len(ON_SCREEN_LETTERS) < 6:
            add_letter()


    if stop1 != 1 and intafad == 1 and m == 1:
        for i, LETTER in enumerate(ON_SCREEN_LETTERS):
            LETTER["y"] += VELOCITY2
            if LETTER["y"] == HEIGHT - 400:
                SCORE["WRONG"] += 1
                delete_letter(i)
        while len(ON_SCREEN_LETTERS) < 6:
            add_letter()
    if stop1 != 1 and intafad == 1 and h == 1:
        for i, LETTER in enumerate(ON_SCREEN_LETTERS):
            LETTER["y"] += VELOCITY3
            if LETTER["y"] == HEIGHT - 400:
                SCORE["WRONG"] += 1
                delete_letter(i)
        while len(ON_SCREEN_LETTERS) < 6:
            add_letter()

    


def on_key_down(key, mod, unicode):
    global SCORE
    if stop1 != 1 and intafad == 1:
        if unicode:
            for i, LETTER in enumerate(ON_SCREEN_LETTERS):
                if LETTER["letter"] == unicode:
                    SCORE["RIGHT"] += 1
                    delete_letter(i)
                    return
            else:
                SCORE["WRONG"] += 1
def on_mouse_down(pos):
    global intafad
    global stop1
    global SCORE
    global ON_SCREEN_LETTERS
    global e
    global m
    global h
    global st
    if apple.collidepoint(pos):
        intafad += 1
    if e == 1 or m == 1 or h == 1:
        if stop.collidepoint(pos):
            if stop1 >= 0 and stop1 <=1:
                stop1 += 1
    
    if stop1 == 1:
        if playcon.collidepoint(pos):
            stop1 -= 1
    
    if stop1 == 1:   
        if regame.collidepoint(pos):
            SCORE["RIGHT"] = 0
            SCORE["WRONG"] = 0
            stop1 -= 1
            ON_SCREEN_LETTERS = []
    if stop1 == 1:    
        if endgame.collidepoint(pos):
            SCORE["RIGHT"] = 0
            SCORE["WRONG"] = 0
            intafad -= 1
            stop1 -= 1
            if e == 1:
                e -= 1
                st -= 1
            if m == 1:
                m -= 1
                st -= 1
            if h == 1:
                h -= 1
                st -= 1
            ON_SCREEN_LETTERS = []
    if intafad == 1 and st == 0:
        if easy.collidepoint(pos):
            e += 1
            st += 1
    if intafad == 1 and st == 0:
        if mid.collidepoint(pos):
            m += 1
            st += 1
    if intafad == 1 and st == 0:
        if hard.collidepoint(pos):
            h += 1
            st += 1
    if intafad == 1 and st == 0:
        if black1.collidepoint(pos):
            intafad -= 1

        
def add_letter():
    if stop1 != 1 and intafad == 1 and e == 1:
        letter = random.choice(string.ascii_letters).lower()
        x = randint(400,1200)
        y = 1
        ON_SCREEN_LETTERS.append({"letter": letter, "x": x , "y": y})
    if stop1 != 1 and intafad == 1 and m == 1:
        letter = random.choice(string.ascii_letters).lower()
        x = randint(400, 1200)
        y = 2
        ON_SCREEN_LETTERS.append({"letter": letter, "x": x , "y": y})
    if stop1 != 1 and intafad == 1 and h == 1:
        letter = random.choice(string.ascii_letters).lower()
        x = randint(400, 1200)
        y = 4
        ON_SCREEN_LETTERS.append({"letter": letter, "x": x , "y": y})
        
def delete_letter(i):
    if stop1 != 1 and intafad == 1:
        del ON_SCREEN_LETTERS[i]
        add_letter()
pgzrun.go()