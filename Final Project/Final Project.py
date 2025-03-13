# Date: 2021-12-06
# Name: Jodie Chen
# Description: ICS3C1 Final Project

#startup
import pygame, sys
from pygame import *

pygame.init()

#fps
clock = pygame.time.Clock()

#window
WIDTH = 600
HEIGHT = 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cookie Battle Academy")

#colours
WHITE = (255, 255, 255)
GREY = (200, 200, 200)
BLACK = (0, 0, 0)
COOKIE = (217, 170, 85)
RED = (255, 0, 0)

#variables
name = ""
screen = 0
musicVol = 0.0

subject = 0
health = 0
qtnPage = 0
retries = 0
score = 0

#images
#BG
cookies = pygame.image.load("cookieBG.jpeg")
cookieBG = pygame.transform.scale(cookies, (cookies.get_width()/1.25, cookies.get_height()/1.25))

dark = pygame.image.load("darkBG.png")
darkBG = pygame.transform.scale(dark, (dark.get_width()/1.5, dark.get_height()/1.5))

#items
OGFlower = pygame.image.load("flower.png")
flower = pygame.transform.scale(OGFlower, (OGFlower.get_width()/1.5, OGFlower.get_height()/1.5))

OGAxe = pygame.image.load("axe.png")
axe = pygame.transform.scale(OGAxe, (OGAxe.get_width()/3, OGAxe.get_height()/3))

#enemies
jellyWorm = pygame.image.load("jellyworm.png")
enemyOne = pygame.transform.scale(jellyWorm, (jellyWorm.get_width()/2, jellyWorm.get_height()/2))

cakeHound = pygame.image.load("cakehound.png")
enemyTwo = pygame.transform.scale(cakeHound, (cakeHound.get_width()/2, cakeHound.get_height()/2))

#cookies
custard = pygame.image.load("butterfly.png")
custard = pygame.transform.scale(custard, (custard.get_width()/10, custard.get_height()/10))

#music
muscON = pygame.image.load("muscON.png")
muscON = pygame.transform.scale(muscON, (muscON.get_width()/30, muscON.get_height()/30))

muscOFF = pygame.image.load("muscOFF.png")
muscOFF = pygame.transform.scale(muscOFF, (muscOFF.get_width()/8, muscOFF.get_height()/8))

#functions
def musicType():
    global musicVol

    if musicVol == 0.5:
        pygame.mixer.music.unpause()
        return muscON

    elif musicVol == 0.0:
        pygame.mixer.music.pause()
        return muscOFF

def enterNameScreen():
    global screen
    global name
    global musicVol
    
    #screen background
    WINDOW.blit(cookieBG, (-110, 0))

    #CBA (Cookie Battle Academy)
    font = pygame.font.SysFont(None, 75)
    pygame.draw.rect(WINDOW, COOKIE, (115, 110, 375, 120))
    textCBattle = font.render("Cookie Battle", True, BLACK)
    WINDOW.blit(textCBattle, (130, 120))
    textAcademy = font.render("Academy", True, BLACK)
    WINDOW.blit(textAcademy, (190, 170))

    #start button
    buttonFont = pygame.font.SysFont(None, 50)
    btnStart = pygame.draw.rect(WINDOW, COOKIE, (250, 300, 110, 55))
    textStart = buttonFont.render("Start", True, BLACK)
    WINDOW.blit(textStart, (265, 310))

    #instructions button
    btnInstruc = pygame.draw.rect(WINDOW, COOKIE, (200, 365, 225, 55))
    textInstruc = buttonFont.render("Instructions", True, BLACK)
    WINDOW.blit(textInstruc, (210, 375))

    #exit button
    btnExit = pygame.draw.rect(WINDOW, COOKIE, (250, 430, 110, 55))
    textExit = buttonFont.render("Exit", True, BLACK)
    WINDOW.blit(textExit, (270, 440))

    #music button
    btnMusic = pygame.draw.rect(WINDOW, COOKIE, (515, 10, 75, 75))
    WINDOW.blit(musicType(), (520, 15))

    #enter name box
    pygame.draw.rect(WINDOW, BLACK, (600/2-200, 500/2-140, 400, 220), 5)
    pygame.draw.rect(WINDOW, WHITE, (600/2-200, 500/2-140, 400, 220))
    
    enterNText = font.render("Enter Name: ", True, BLACK)
    WINDOW.blit(enterNText, (600/2-175, 500/2-110))

    pygame.draw.rect(WINDOW, GREY, (600/2-175, 500/2-45, 350, 100))
    printName = font.render(name, True, BLACK)
    WINDOW.blit(printName, (600/2-175, 500/2-30))

    
    for event in pygame.event.get():

        #type name        
        if event.type == pygame.KEYDOWN:
            if pygame.key.name(event.key) == "enter" or pygame.key.name(event.key) == "return":
                screen = 1

            elif pygame.key.name(event.key) == "backspace":
                name = name[:-1]
                
            else:
                name += event.unicode

        if event.type == pygame.MOUSEBUTTONDOWN:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]

            #music
            if musicVol == 0.5 and btnMusic.collidepoint([x, y]):
                musicVol = 0.0

            elif musicVol == 0.0 and btnMusic.collidepoint([x, y]):
                musicVol = 0.5

def homeScreen():
    global screen
    global musicVol
    global beforeTrans
    global transition
    beforeTrans = 0
    transition = 600

    #screen background
    WINDOW.blit(cookieBG, (-110, 0))

    #music button
    btnMusic = pygame.draw.rect(WINDOW, COOKIE, (515, 10, 75, 75))
    WINDOW.blit(musicType(), (520, 15))

    #welcome
    font = pygame.font.SysFont(None, 75)
    printName = font.render("Welcome " + name + "!", True, BLACK)
    WINDOW.blit(printName, (100, 50))

    #CBA (Cookie Battle Academy)
    pygame.draw.rect(WINDOW, COOKIE, (115, 110, 375, 120))
    textCBattle = font.render("Cookie Battle", True, BLACK)
    WINDOW.blit(textCBattle, (130, 120))
    textAcademy = font.render("Academy", True, BLACK)
    WINDOW.blit(textAcademy, (190, 170))

    #start button
    buttonFont = pygame.font.SysFont(None, 50)
    btnStart = pygame.draw.rect(WINDOW, COOKIE, (250, 300, 110, 55))
    textStart = buttonFont.render("Start", True, BLACK)
    WINDOW.blit(textStart, (265, 310))

    #instructions button
    btnInstruc = pygame.draw.rect(WINDOW, COOKIE, (200, 365, 225, 55))
    textInstruc = buttonFont.render("Instructions", True, BLACK)
    WINDOW.blit(textInstruc, (210, 375))

    #exit button
    btnExit = pygame.draw.rect(WINDOW, COOKIE, (250, 430, 110, 55))
    textExit = buttonFont.render("Exit", True, BLACK)
    WINDOW.blit(textExit, (270, 440))

    #custard cookie
    WINDOW.blit(custard, (420 + custardX, 250 + custardY))

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]

            #buttons
            if btnStart.collidepoint([x, y]):
                screen = 2

            elif btnInstruc.collidepoint([x, y]):
                screen = 1.1

            elif btnExit.collidepoint([x, y]):
                pygame.quit()
                sys.exit()

            #music
            elif musicVol == 0.5 and btnMusic.collidepoint([x, y]):
                musicVol = 0.0

            elif musicVol == 0.0 and btnMusic.collidepoint([x, y]):
                musicVol = 0.5

def instructions():
    global screen
    global musicVol
    
    #screen background
    WINDOW.blit(cookieBG, (-110, 0))

    #before transition
    #welcome
    font = pygame.font.SysFont(None, 75)
    printName = font.render("Welcome " + name + "!", True, BLACK)
    WINDOW.blit(printName, (100 + beforeTrans, 50))

    #CBA (Cookie Battle Academy)
    pygame.draw.rect(WINDOW, COOKIE, (115 + beforeTrans, 110, 375, 120))
    textCBattle = font.render("Cookie Battle", True, BLACK)
    WINDOW.blit(textCBattle, (130 + beforeTrans, 120))
    textAcademy = font.render("Academy", True, BLACK)
    WINDOW.blit(textAcademy, (190 + beforeTrans, 170))

    #start button
    buttonFont = pygame.font.SysFont(None, 50)
    btnStart = pygame.draw.rect(WINDOW, COOKIE, (250 + beforeTrans, 300, 110, 55))
    textStart = buttonFont.render("Start", True, BLACK)
    WINDOW.blit(textStart, (265 + beforeTrans, 310))

    #instructions button
    btnInstruc = pygame.draw.rect(WINDOW, COOKIE, (200 + beforeTrans, 365, 225, 55))
    textInstruc = buttonFont.render("Instructions", True, BLACK)
    WINDOW.blit(textInstruc, (210 + beforeTrans, 375))

    #exit button
    btnExit = pygame.draw.rect(WINDOW, COOKIE, (250 + beforeTrans, 430, 110, 55))
    textExit = buttonFont.render("Exit", True, BLACK)
    WINDOW.blit(textExit, (270 + beforeTrans, 440))

    #custard cookie
    WINDOW.blit(custard, (420 + custardX + beforeTrans, 250 + custardY))

    #after transition
    #music button
    btnMusic = pygame.draw.rect(WINDOW, COOKIE, (515, 10, 75, 75))
    WINDOW.blit(musicType(), (520, 15))

    #back button
    buttonFont = pygame.font.SysFont(None, 50)
    arrowBack = pygame.draw.polygon(WINDOW, COOKIE, ((10 + transition, 40), (50 + transition, 10), (50 + transition, 70)))
    btnBack = pygame.draw.rect(WINDOW, COOKIE, (50 + transition, 18, 110, 45))
    textBack = buttonFont.render("Back", True, BLACK)
    WINDOW.blit(textBack, (60 + transition, 24))

    #rules
    pygame.draw.rect(WINDOW, WHITE, (40 + transition, 90, 500, 300))
    
    rulesFont = pygame.font.SysFont(None, 25)
    rules = rulesFont.render("Cookie Battle Academy will make students fight against", True, BLACK)
    WINDOW.blit(rules, (50 + transition, 100))
    rules = rulesFont.render("enemies to save the cookie kingdom. Students will use", True, BLACK)
    WINDOW.blit(rules, (50 + transition, 125))
    rules = rulesFont.render("their math and english skills to defeat opponents. Simply", True, BLACK)
    WINDOW.blit(rules, (50 + transition, 150))
    rules = rulesFont.render("choose which enemy to fight, which unit you are confident", True, BLACK)
    WINDOW.blit(rules, (50 + transition, 175))
    rules = rulesFont.render("in, and answer the questions correctly to deal damage to", True, BLACK)
    WINDOW.blit(rules, (50 + transition, 200))
    rules = rulesFont.render("the enemy. The game ends when the enemy is defeated.", True, BLACK)
    WINDOW.blit(rules, (50 + transition, 225))
    rules = rulesFont.render("Ready to Play?", True, BLACK)
    WINDOW.blit(rules, (225 + transition, 275))

    #start button
    buttonFont = pygame.font.SysFont(None, 50)
    btnStart = pygame.draw.rect(WINDOW, COOKIE, (230 + transition, 300, 110, 55))
    textStart = buttonFont.render("Start", True, BLACK)
    WINDOW.blit(textStart, (245 + transition, 310))

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]

            #buttons
            if btnStart.collidepoint([x, y]):
                screen = 2
                
            elif btnBack.collidepoint([x, y]):
                screen = 1

            #music
            elif musicVol == 0.5 and btnMusic.collidepoint([x, y]):
                musicVol = 0.0

            elif musicVol == 0.0 and btnMusic.collidepoint([x, y]):
                musicVol = 0.5
    
def subjectScreen():
    global screen
    global subject
    global musicVol
    
    #screen background
    WINDOW.blit(darkBG, (-80, 0))

    #music button
    btnMusic = pygame.draw.rect(WINDOW, COOKIE, (515, 10, 75, 75))
    WINDOW.blit(musicType(), (520, 15))

    #back button
    buttonFont = pygame.font.SysFont(None, 50)
    arrowBack = pygame.draw.polygon(WINDOW, GREY, ((10, 40), (50, 10), (50, 70)))
    btnBack = pygame.draw.rect(WINDOW, GREY, (50, 18, 110, 45))
    textBack = buttonFont.render("Back", True, BLACK)
    WINDOW.blit(textBack, (60, 24))

    #title text
    pygame.draw.rect(WINDOW, GREY, (65, 30+40, 500, 150))
    font = pygame.font.SysFont(None, 75)
    printText1 = font.render("Which Enemy Will", True, BLACK)
    WINDOW.blit(printText1, (90, 50+40))
    printText2 = font.render("You Be Fighting?", True, BLACK)
    WINDOW.blit(printText2, (100, 110+40))

    #math button
    buttonFont = pygame.font.SysFont(None, 50)
    btnMath = pygame.draw.rect(WINDOW, GREY, (150, 253, 110, 55))
    textMath = buttonFont.render("Math", True, BLACK)
    WINDOW.blit(textMath, (165, 265))

    #math enemy
    WINDOW.blit(enemyOne, (150, 325))

    #english button
    btnEnglish = pygame.draw.rect(WINDOW, GREY, (325, 253, 155, 55))
    textEnglish = buttonFont.render("English", True, BLACK)
    WINDOW.blit(textEnglish, (340, 265))

    #english enemy
    WINDOW.blit(enemyTwo, (340, 325))

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]

            #buttons
            if btnMath.collidepoint([x, y]):
                screen = 3
                subject = 1

            elif btnEnglish.collidepoint([x, y]):
                screen = 5
                subject = 2

            elif btnBack.collidepoint([x, y]):
                screen = 1

            #music
            elif musicVol == 0.5 and btnMusic.collidepoint([x, y]):
                musicVol = 0.0

            elif musicVol == 0.0 and btnMusic.collidepoint([x, y]):
                musicVol = 0.5

#which enemy
def enemy(subject):
    if subject == 1:
        return enemyOne

    if subject == 2:
        return enemyTwo

def math():
    global screen
    global musicVol
    
    #screen background
    WINDOW.blit(darkBG, (-80, 0))

    #music button
    btnMusic = pygame.draw.rect(WINDOW, COOKIE, (515, 10, 75, 75))
    WINDOW.blit(musicType(), (520, 15))

    #back button
    buttonFont = pygame.font.SysFont(None, 50)
    arrowBack = pygame.draw.polygon(WINDOW, GREY, ((10, 40), (50, 10), (50, 70)))
    btnBack = pygame.draw.rect(WINDOW, GREY, (50, 18, 110, 45))
    textBack = buttonFont.render("Back", True, BLACK)
    WINDOW.blit(textBack, (60, 24))

    #title text
    pygame.draw.rect(WINDOW, GREY, (95, 30+40, 405, 150))
    font = pygame.font.SysFont(None, 75)
    printText1 = font.render("Which Unit Do", True, BLACK)
    WINDOW.blit(printText1, (120, 50+40))
    printText2 = font.render("You Choose?", True, BLACK)
    WINDOW.blit(printText2, (130, 110+40))

    #addition button
    buttonFont = pygame.font.SysFont(None, 50)
    btnAdd = pygame.draw.rect(WINDOW, GREY, (90, 278, 175, 55))
    textAdd = buttonFont.render("Addition", True, BLACK)
    WINDOW.blit(textAdd, (105, 290))

    #subtraction button
    btnSubtract = pygame.draw.rect(WINDOW, GREY, (285, 278, 225, 55))
    textSubtract = buttonFont.render("Subtraction", True, BLACK)
    WINDOW.blit(textSubtract, (300, 290))

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]

            #buttons
            if btnAdd.collidepoint([x, y]):
                screen = 3.1

            elif btnSubtract.collidepoint([x, y]):
                screen = 4.1

            elif btnBack.collidepoint([x, y]):
                screen = 2

            #music
            elif musicVol == 0.5 and btnMusic.collidepoint([x, y]):
                musicVol = 0.0

            elif musicVol == 0.0 and btnMusic.collidepoint([x, y]):
                musicVol = 0.5

def add1():
    global screen
    global health
    global retries
    global score
    global qtnPage
    global musicVol
    health = 0
    retries = 0
    score = 0
    qtnPage = 3.1
    
    #screen background
    WINDOW.blit(darkBG, (-80, 0))

    #music button
    btnMusic = pygame.draw.rect(WINDOW, COOKIE, (515, 10, 75, 75))
    WINDOW.blit(musicType(), (520, 15))

    #question text
    pygame.draw.rect(WINDOW, GREY, (50, 50, 350, 230))

    qFont = pygame.font.SysFont(None, 75)
    q1 = qFont.render("1 + 2 = ?", True, BLACK)
    WINDOW.blit(q1, (110, 75))

    #question image
    WINDOW.blit(flower, (80, 150))
    imgQ1 = qFont.render("+         = ?", True, BLACK)
    WINDOW.blit(imgQ1, (150, 150))
    WINDOW.blit(flower, (175, 150))
    WINDOW.blit(flower, (240, 150))

    #retries
    smolFont = pygame.font.SysFont(None, 25)
    tRetries = smolFont.render("retries: " + str(retries), True, BLACK)
    WINDOW.blit(tRetries, (75, 210+40))

    #score
    tScore = smolFont.render("score: " + str(score), True, BLACK)
    WINDOW.blit(tScore, (300, 210+40))

    #answer options
    opt1 = pygame.draw.rect(WINDOW, GREY, (50, 300, 165, 75))
    opt1Text = qFont.render("4", True, BLACK)
    WINDOW.blit(opt1Text, (115, 315))

    opt2 = pygame.draw.rect(WINDOW, GREY, (235, 300, 165, 75))
    opt2Text = qFont.render("3", True, BLACK)
    WINDOW.blit(opt2Text, (300, 315))

    opt3 = pygame.draw.rect(WINDOW, GREY, (50, 390, 165, 75))
    opt3Text = qFont.render("2", True, BLACK)
    WINDOW.blit(opt3Text, (115, 405))

    opt4 = pygame.draw.rect(WINDOW, GREY, (235, 390, 165, 75))
    opt4Text = qFont.render("5", True, BLACK)
    WINDOW.blit(opt4Text, (300, 405))

    #enemy
    WINDOW.blit(enemyOne, (415, 150))

    #health bar
    pygame.draw.rect(WINDOW, WHITE, (425, 120, 150, 20))
    pygame.draw.rect(WINDOW, RED, (425, 120, 150-health, 20))
    pygame.draw.rect(WINDOW, BLACK, (425, 120, 150, 20), 2)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN: 
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]

            #buttons
            if opt2.collidepoint([x, y]):
                screen = 7.1
                health += 30
                score += 1

            elif opt1.collidepoint([x, y]):
                screen = 7.2

            elif opt3.collidepoint([x, y]):
                screen = 7.2

            elif opt4.collidepoint([x, y]):
                screen = 7.2

            #music
            elif musicVol == 0.5 and btnMusic.collidepoint([x, y]):
                musicVol = 0.0

            elif musicVol == 0.0 and btnMusic.collidepoint([x, y]):
                musicVol = 0.5

def add2():
    global screen
    global health
    global retries
    global score
    global qtnPage
    global musicVol
    qtnPage = 3.2
    
    #screen background
    WINDOW.blit(darkBG, (-80, 0))

    #music button
    btnMusic = pygame.draw.rect(WINDOW, COOKIE, (515, 10, 75, 75))
    WINDOW.blit(musicType(), (520, 15))

    #question text
    pygame.draw.rect(WINDOW, GREY, (50, 50, 350, 230))

    qFont = pygame.font.SysFont(None, 75)
    q2 = qFont.render("2 + 3 = ?", True, BLACK)
    WINDOW.blit(q2, (110, 75))

    #question image
    WINDOW.blit(axe, (100, 150))
    WINDOW.blit(axe, (50, 150))
    imgQ2 = qFont.render("+          = ?", True, BLACK)
    WINDOW.blit(imgQ2, (150, 150))
    WINDOW.blit(axe, (175, 150))
    WINDOW.blit(axe, (223, 150))
    WINDOW.blit(axe, (270, 150))

    #retries
    smolFont = pygame.font.SysFont(None, 25)
    tRetries = smolFont.render("retries: " + str(retries), True, BLACK)
    WINDOW.blit(tRetries, (75, 210+40))

    #score
    tScore = smolFont.render("score: " + str(score), True, BLACK)
    WINDOW.blit(tScore, (300, 210+40))
    
    #answer options
    opt1 = pygame.draw.rect(WINDOW, GREY, (50, 300, 165, 75))
    opt1Text = qFont.render("5", True, BLACK)
    WINDOW.blit(opt1Text, (115, 315))

    opt2 = pygame.draw.rect(WINDOW, GREY, (235, 300, 165, 75))
    opt2Text = qFont.render("7", True, BLACK)
    WINDOW.blit(opt2Text, (300, 315))

    opt3 = pygame.draw.rect(WINDOW, GREY, (50, 390, 165, 75))
    opt3Text = qFont.render("6", True, BLACK)
    WINDOW.blit(opt3Text, (115, 405))

    opt4 = pygame.draw.rect(WINDOW, GREY, (235, 390, 165, 75))
    opt4Text = qFont.render("4", True, BLACK)
    WINDOW.blit(opt4Text, (300, 405))

    #enemy
    WINDOW.blit(enemyOne, (415, 150))

    #health bar
    pygame.draw.rect(WINDOW, WHITE, (425, 120, 150, 20))
    pygame.draw.rect(WINDOW, RED, (425, 120, 150-health, 20))
    pygame.draw.rect(WINDOW, BLACK, (425, 120, 150, 20), 2)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN: 
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]

            #buttons
            if opt1.collidepoint([x, y]):
                screen = 7.1
                health += 30
                score += 1

            elif opt2.collidepoint([x, y]):
                screen = 7.2

            elif opt3.collidepoint([x, y]):
                screen = 7.2

            elif opt4.collidepoint([x, y]):
                screen = 7.2

            #music
            elif musicVol == 0.5 and btnMusic.collidepoint([x, y]):
                musicVol = 0.0

            elif musicVol == 0.0 and btnMusic.collidepoint([x, y]):
                musicVol = 0.5

def add3():
    global screen
    global health
    global retries
    global score
    global qtnPage
    global musicVol
    qtnPage = 3.3
    
    #screen background
    WINDOW.blit(darkBG, (-80, 0))

    #music button
    btnMusic = pygame.draw.rect(WINDOW, COOKIE, (515, 10, 75, 75))
    WINDOW.blit(musicType(), (520, 15))

    #question text
    pygame.draw.rect(WINDOW, GREY, (50, 50, 350, 230))

    qFont = pygame.font.SysFont(None, 75)
    q3 = qFont.render("3 + 4 = ?", True, BLACK)
    WINDOW.blit(q3, (110, 75))

    #question image
    WINDOW.blit(axe, (100, 120))
    WINDOW.blit(axe, (200, 120))
    WINDOW.blit(axe, (150, 120))
    
    imgQ3 = qFont.render("+", True, BLACK)
    WINDOW.blit(imgQ3, (167, 150))
    
    WINDOW.blit(axe, (80, 190))
    WINDOW.blit(axe, (180, 190))
    WINDOW.blit(axe, (130, 190))
    WINDOW.blit(axe, (230, 190))
    
    imgQ3 = qFont.render("= ?", True, BLACK)
    WINDOW.blit(imgQ3, (275, 150))

    #retries
    smolFont = pygame.font.SysFont(None, 25)
    tRetries = smolFont.render("retries: " + str(retries), True, BLACK)
    WINDOW.blit(tRetries, (75, 210+40))

    #score
    tScore = smolFont.render("score: " + str(score), True, BLACK)
    WINDOW.blit(tScore, (300, 210+40))
    
    #answer options
    opt1 = pygame.draw.rect(WINDOW, GREY, (50, 300, 165, 75))
    opt1Text = qFont.render("5", True, BLACK)
    WINDOW.blit(opt1Text, (115, 315))

    opt2 = pygame.draw.rect(WINDOW, GREY, (235, 300, 165, 75))
    opt2Text = qFont.render("8", True, BLACK)
    WINDOW.blit(opt2Text, (300, 315))

    opt3 = pygame.draw.rect(WINDOW, GREY, (50, 390, 165, 75))
    opt3Text = qFont.render("6", True, BLACK)
    WINDOW.blit(opt3Text, (115, 405))

    opt4 = pygame.draw.rect(WINDOW, GREY, (235, 390, 165, 75))
    opt4Text = qFont.render("7", True, BLACK)
    WINDOW.blit(opt4Text, (300, 405))

    #enemy
    WINDOW.blit(enemyOne, (415, 150))

    #health bar
    pygame.draw.rect(WINDOW, WHITE, (425, 120, 150, 20))
    pygame.draw.rect(WINDOW, RED, (425, 120, 150-health, 20))
    pygame.draw.rect(WINDOW, BLACK, (425, 120, 150, 20), 2)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN: 
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]

            #buttons
            if opt4.collidepoint([x, y]):
                screen = 7.1
                health += 30
                score += 1

            elif opt1.collidepoint([x, y]):
                screen = 7.2

            elif opt2.collidepoint([x, y]):
                screen = 7.2

            elif opt3.collidepoint([x, y]):
                screen = 7.2

            #music
            elif musicVol == 0.5 and btnMusic.collidepoint([x, y]):
                musicVol = 0.0

            elif musicVol == 0.0 and btnMusic.collidepoint([x, y]):
                musicVol = 0.5

def add4():
    global screen
    global health
    global retries
    global score
    global qtnPage
    global musicVol
    qtnPage = 3.4
    
    #screen background
    WINDOW.blit(darkBG, (-80, 0))

    #music button
    btnMusic = pygame.draw.rect(WINDOW, COOKIE, (515, 10, 75, 75))
    WINDOW.blit(musicType(), (520, 15))

    #question text
    pygame.draw.rect(WINDOW, GREY, (50, 50, 350, 230))

    qFont = pygame.font.SysFont(None, 75)
    q4 = qFont.render("2 + 2 = ?", True, BLACK)
    WINDOW.blit(q4, (110, 75))

    #question image
    WINDOW.blit(axe, (100, 150))
    WINDOW.blit(axe, (50, 150))
    imgQ4 = qFont.render("+       = ?", True, BLACK)
    WINDOW.blit(imgQ4, (150, 150))
    WINDOW.blit(axe, (175, 150))
    WINDOW.blit(axe, (223, 150))

    #retries
    smolFont = pygame.font.SysFont(None, 25)
    tRetries = smolFont.render("retries: " + str(retries), True, BLACK)
    WINDOW.blit(tRetries, (75, 210+40))

    #score
    tScore = smolFont.render("score: " + str(score), True, BLACK)
    WINDOW.blit(tScore, (300, 210+40))
    
    #answer options
    opt1 = pygame.draw.rect(WINDOW, GREY, (50, 300, 165, 75))
    opt1Text = qFont.render("6", True, BLACK)
    WINDOW.blit(opt1Text, (115, 315))

    opt2 = pygame.draw.rect(WINDOW, GREY, (235, 300, 165, 75))
    opt2Text = qFont.render("7", True, BLACK)
    WINDOW.blit(opt2Text, (300, 315))

    opt3 = pygame.draw.rect(WINDOW, GREY, (50, 390, 165, 75))
    opt3Text = qFont.render("4", True, BLACK)
    WINDOW.blit(opt3Text, (115, 405))

    opt4 = pygame.draw.rect(WINDOW, GREY, (235, 390, 165, 75))
    opt4Text = qFont.render("5", True, BLACK)
    WINDOW.blit(opt4Text, (300, 405))

    #enemy
    WINDOW.blit(enemyOne, (415, 150))

    #health bar
    pygame.draw.rect(WINDOW, WHITE, (425, 120, 150, 20))
    pygame.draw.rect(WINDOW, RED, (425, 120, 150-health, 20))
    pygame.draw.rect(WINDOW, BLACK, (425, 120, 150, 20), 2)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN: 
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]

            #buttons
            if opt3.collidepoint([x, y]):
                screen = 7.1
                health += 30
                score += 1

            elif opt1.collidepoint([x, y]):
                screen = 7.2

            elif opt2.collidepoint([x, y]):
                screen = 7.2

            elif opt4.collidepoint([x, y]):
                screen = 7.2

            #music
            elif musicVol == 0.5 and btnMusic.collidepoint([x, y]):
                musicVol = 0.0

            elif musicVol == 0.0 and btnMusic.collidepoint([x, y]):
                musicVol = 0.5

def add5():
    global screen
    global health
    global retries
    global score
    global qtnPage
    global musicVol
    qtnPage = 3.5
    
    #screen background
    WINDOW.blit(darkBG, (-80, 0))

    #music button
    btnMusic = pygame.draw.rect(WINDOW, COOKIE, (515, 10, 75, 75))
    WINDOW.blit(musicType(), (520, 15))

    #question text
    pygame.draw.rect(WINDOW, GREY, (50, 50, 350, 230))

    qFont = pygame.font.SysFont(None, 75)
    q5 = qFont.render("3 + 3 = ?", True, BLACK)
    WINDOW.blit(q5, (110, 75))

    #question image
    WINDOW.blit(axe, (100, 120))
    WINDOW.blit(axe, (200, 120))
    WINDOW.blit(axe, (150, 120))
    
    imgQ3 = qFont.render("+", True, BLACK)
    WINDOW.blit(imgQ3, (167, 150))
    
    WINDOW.blit(axe, (100, 190))
    WINDOW.blit(axe, (200, 190))
    WINDOW.blit(axe, (150, 190))

    imgQ3 = qFont.render("= ?", True, BLACK)
    WINDOW.blit(imgQ3, (275, 150))

    #retries
    smolFont = pygame.font.SysFont(None, 25)
    tRetries = smolFont.render("retries: " + str(retries), True, BLACK)
    WINDOW.blit(tRetries, (75, 210+40))

    #score
    tScore = smolFont.render("score: " + str(score), True, BLACK)
    WINDOW.blit(tScore, (300, 210+40))
    
    #answer options
    opt1 = pygame.draw.rect(WINDOW, GREY, (50, 300, 165, 75))
    opt1Text = qFont.render("5", True, BLACK)
    WINDOW.blit(opt1Text, (115, 315))

    opt2 = pygame.draw.rect(WINDOW, GREY, (235, 300, 165, 75))
    opt2Text = qFont.render("7", True, BLACK)
    WINDOW.blit(opt2Text, (300, 315))

    opt3 = pygame.draw.rect(WINDOW, GREY, (50, 390, 165, 75))
    opt3Text = qFont.render("6", True, BLACK)
    WINDOW.blit(opt3Text, (115, 405))

    opt4 = pygame.draw.rect(WINDOW, GREY, (235, 390, 165, 75))
    opt4Text = qFont.render("4", True, BLACK)
    WINDOW.blit(opt4Text, (300, 405))

    #enemy
    WINDOW.blit(enemyOne, (415, 150))

    #health bar
    pygame.draw.rect(WINDOW, WHITE, (425, 120, 150, 20))
    pygame.draw.rect(WINDOW, RED, (425, 120, 150-health, 20))
    pygame.draw.rect(WINDOW, BLACK, (425, 120, 150, 20), 2)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN: 
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]

            #buttons
            if opt3.collidepoint([x, y]):
                screen = 7.1
                health += 30
                score += 1

            elif opt1.collidepoint([x, y]):
                screen = 7.1

            elif opt2.collidepoint([x, y]):
                screen = 7.2

            elif opt4.collidepoint([x, y]):
                screen = 7.2

            #music
            elif musicVol == 0.5 and btnMusic.collidepoint([x, y]):
                musicVol = 0.0

            elif musicVol == 0.0 and btnMusic.collidepoint([x, y]):
                musicVol = 0.5
                
def sub1():
    global screen
    global health
    global retries
    global score
    global qtnPage
    global musicVol
    health = 0
    retries = 0
    score = 0
    qtnPage = 4.1
    
    #screen background
    WINDOW.blit(darkBG, (-80, 0))

    #music button
    btnMusic = pygame.draw.rect(WINDOW, COOKIE, (515, 10, 75, 75))
    WINDOW.blit(musicType(), (520, 15))

    #question text
    pygame.draw.rect(WINDOW, GREY, (50, 50, 350, 230))

    qFont = pygame.font.SysFont(None, 75)
    q1 = qFont.render("2 - 1 = ?", True, BLACK)
    WINDOW.blit(q1, (110, 75))

    #question image
    WINDOW.blit(flower, (70, 150))
    WINDOW.blit(flower, (130, 150))
    imgQ1 = qFont.render("-     = ?", True, BLACK)
    WINDOW.blit(imgQ1, (200, 150))
    WINDOW.blit(flower, (220, 150))

    #retries
    smolFont = pygame.font.SysFont(None, 25)
    tRetries = smolFont.render("retries: " + str(retries), True, BLACK)
    WINDOW.blit(tRetries, (75, 210+40))

    #score
    tScore = smolFont.render("score: " + str(score), True, BLACK)
    WINDOW.blit(tScore, (300, 210+40))

    #answer options
    opt1 = pygame.draw.rect(WINDOW, GREY, (50, 300, 165, 75))
    opt1Text = qFont.render("0", True, BLACK)
    WINDOW.blit(opt1Text, (115, 315))

    opt2 = pygame.draw.rect(WINDOW, GREY, (235, 300, 165, 75))
    opt2Text = qFont.render("1", True, BLACK)
    WINDOW.blit(opt2Text, (300, 315))

    opt3 = pygame.draw.rect(WINDOW, GREY, (50, 390, 165, 75))
    opt3Text = qFont.render("2", True, BLACK)
    WINDOW.blit(opt3Text, (115, 405))

    opt4 = pygame.draw.rect(WINDOW, GREY, (235, 390, 165, 75))
    opt4Text = qFont.render("3", True, BLACK)
    WINDOW.blit(opt4Text, (300, 405))

    #enemy
    WINDOW.blit(enemyOne, (415, 150))

    #health bar
    pygame.draw.rect(WINDOW, WHITE, (425, 120, 150, 20))
    pygame.draw.rect(WINDOW, RED, (425, 120, 150-health, 20))
    pygame.draw.rect(WINDOW, BLACK, (425, 120, 150, 20), 2)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN: 
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]

            #buttons
            if opt2.collidepoint([x, y]):
                screen = 7.1
                health += 30
                score += 1

            elif opt1.collidepoint([x, y]):
                screen = 7.2

            elif opt3.collidepoint([x, y]):
                screen = 7.2

            elif opt4.collidepoint([x, y]):
                screen = 7.2

            #music
            elif musicVol == 0.5 and btnMusic.collidepoint([x, y]):
                musicVol = 0.0

            elif musicVol == 0.0 and btnMusic.collidepoint([x, y]):
                musicVol = 0.5

def sub2():
    global screen
    global health
    global retries
    global score
    global qtnPage
    global musicVol
    qtnPage = 4.2
    
    #screen background
    WINDOW.blit(darkBG, (-80, 0))

    #music button
    btnMusic = pygame.draw.rect(WINDOW, COOKIE, (515, 10, 75, 75))
    WINDOW.blit(musicType(), (520, 15))

    #question text
    pygame.draw.rect(WINDOW, GREY, (50, 50, 350, 230))

    qFont = pygame.font.SysFont(None, 75)
    q2 = qFont.render("3 - 2 = ?", True, BLACK)
    WINDOW.blit(q2, (110, 75))

    #question image
    WINDOW.blit(axe, (100, 150))
    WINDOW.blit(axe, (50, 150))
    WINDOW.blit(axe, (150, 150))
    imgQ2 = qFont.render("-        = ?", True, BLACK)
    WINDOW.blit(imgQ2, (200, 150))
    WINDOW.blit(axe, (223, 150))
    WINDOW.blit(axe, (270, 150))

    #retries
    smolFont = pygame.font.SysFont(None, 25)
    tRetries = smolFont.render("retries: " + str(retries), True, BLACK)
    WINDOW.blit(tRetries, (75, 210+40))

    #score
    tScore = smolFont.render("score: " + str(score), True, BLACK)
    WINDOW.blit(tScore, (300, 210+40))
    
    #answer options
    opt1 = pygame.draw.rect(WINDOW, GREY, (50, 300, 165, 75))
    opt1Text = qFont.render("1", True, BLACK)
    WINDOW.blit(opt1Text, (115, 315))

    opt2 = pygame.draw.rect(WINDOW, GREY, (235, 300, 165, 75))
    opt2Text = qFont.render("0", True, BLACK)
    WINDOW.blit(opt2Text, (300, 315))

    opt3 = pygame.draw.rect(WINDOW, GREY, (50, 390, 165, 75))
    opt3Text = qFont.render("-2", True, BLACK)
    WINDOW.blit(opt3Text, (115, 405))

    opt4 = pygame.draw.rect(WINDOW, GREY, (235, 390, 165, 75))
    opt4Text = qFont.render("5", True, BLACK)
    WINDOW.blit(opt4Text, (300, 405))

    #enemy
    WINDOW.blit(enemyOne, (415, 150))

    #health bar
    pygame.draw.rect(WINDOW, WHITE, (425, 120, 150, 20))
    pygame.draw.rect(WINDOW, RED, (425, 120, 150-health, 20))
    pygame.draw.rect(WINDOW, BLACK, (425, 120, 150, 20), 2)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]

            #buttons
            if opt1.collidepoint([x, y]):
                screen = 7.1
                health += 30
                score += 1

            elif opt2.collidepoint([x, y]):
                screen = 7.2

            elif opt3.collidepoint([x, y]):
                screen = 7.2

            elif opt4.collidepoint([x, y]):
                screen = 7.2

            #music
            elif musicVol == 0.5 and btnMusic.collidepoint([x, y]):
                musicVol = 0.0

            elif musicVol == 0.0 and btnMusic.collidepoint([x, y]):
                musicVol = 0.5

def sub3():
    global screen
    global health
    global retries
    global score
    global qtnPage
    global musicVol
    qtnPage = 4.3
    
    #screen background
    WINDOW.blit(darkBG, (-80, 0))

    #music button
    btnMusic = pygame.draw.rect(WINDOW, COOKIE, (515, 10, 75, 75))
    WINDOW.blit(musicType(), (520, 15))

    #question text
    pygame.draw.rect(WINDOW, GREY, (50, 50, 350, 230))

    qFont = pygame.font.SysFont(None, 75)
    q3 = qFont.render("4 - 1 = ?", True, BLACK)
    WINDOW.blit(q3, (110, 75))

    #question image
    WINDOW.blit(axe, (80, 120))
    WINDOW.blit(axe, (180, 120))
    WINDOW.blit(axe, (130, 120))
    WINDOW.blit(axe, (230, 120))
    
    imgQ3 = qFont.render("-", True, BLACK)
    WINDOW.blit(imgQ3, (167, 160))
    
    WINDOW.blit(axe, (150, 190))
    
    imgQ3 = qFont.render("= ?", True, BLACK)
    WINDOW.blit(imgQ3, (300, 150))

    #retries
    smolFont = pygame.font.SysFont(None, 25)
    tRetries = smolFont.render("retries: " + str(retries), True, BLACK)
    WINDOW.blit(tRetries, (75, 210+40))

    #score
    tScore = smolFont.render("score: " + str(score), True, BLACK)
    WINDOW.blit(tScore, (300, 210+40))
    
    #answer options
    opt1 = pygame.draw.rect(WINDOW, GREY, (50, 300, 165, 75))
    opt1Text = qFont.render("5", True, BLACK)
    WINDOW.blit(opt1Text, (115, 315))

    opt2 = pygame.draw.rect(WINDOW, GREY, (235, 300, 165, 75))
    opt2Text = qFont.render("2", True, BLACK)
    WINDOW.blit(opt2Text, (300, 315))

    opt3 = pygame.draw.rect(WINDOW, GREY, (50, 390, 165, 75))
    opt3Text = qFont.render("4", True, BLACK)
    WINDOW.blit(opt3Text, (115, 405))

    opt4 = pygame.draw.rect(WINDOW, GREY, (235, 390, 165, 75))
    opt4Text = qFont.render("3", True, BLACK)
    WINDOW.blit(opt4Text, (300, 405))

    #enemy
    WINDOW.blit(enemyOne, (415, 150))

    #health bar
    pygame.draw.rect(WINDOW, WHITE, (425, 120, 150, 20))
    pygame.draw.rect(WINDOW, RED, (425, 120, 150-health, 20))
    pygame.draw.rect(WINDOW, BLACK, (425, 120, 150, 20), 2)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN: 
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]

            #buttons
            if opt4.collidepoint([x, y]):
                screen = 7.1
                health += 30
                score += 1

            elif opt1.collidepoint([x, y]):
                screen = 7.2

            elif opt2.collidepoint([x, y]):
                screen = 7.2

            elif opt3.collidepoint([x, y]):
                screen = 7.2

            #music
            elif musicVol == 0.5 and btnMusic.collidepoint([x, y]):
                musicVol = 0.0

            elif musicVol == 0.0 and btnMusic.collidepoint([x, y]):
                musicVol = 0.5

def sub4():
    global screen
    global health
    global retries
    global score
    global qtnPage
    global musicVol
    qtnPage = 4.4
    
    #screen background
    WINDOW.blit(darkBG, (-80, 0))

    #music button
    btnMusic = pygame.draw.rect(WINDOW, COOKIE, (515, 10, 75, 75))
    WINDOW.blit(musicType(), (520, 15))

    #question text
    pygame.draw.rect(WINDOW, GREY, (50, 50, 350, 230))

    qFont = pygame.font.SysFont(None, 75)
    q4 = qFont.render("2 - 2 = ?", True, BLACK)
    WINDOW.blit(q4, (110, 75))

    #question image
    WINDOW.blit(axe, (100, 150))
    WINDOW.blit(axe, (50, 150))
    imgQ4 = qFont.render("-       = ?", True, BLACK)
    WINDOW.blit(imgQ4, (150, 150))
    WINDOW.blit(axe, (175, 150))
    WINDOW.blit(axe, (223, 150))

    #retries
    smolFont = pygame.font.SysFont(None, 25)
    tRetries = smolFont.render("retries: " + str(retries), True, BLACK)
    WINDOW.blit(tRetries, (75, 210+40))

    #score
    tScore = smolFont.render("score: " + str(score), True, BLACK)
    WINDOW.blit(tScore, (300, 210+40))
    
    #answer options
    opt1 = pygame.draw.rect(WINDOW, GREY, (50, 300, 165, 75))
    opt1Text = qFont.render("4", True, BLACK)
    WINDOW.blit(opt1Text, (115, 315))

    opt2 = pygame.draw.rect(WINDOW, GREY, (235, 300, 165, 75))
    opt2Text = qFont.render("1", True, BLACK)
    WINDOW.blit(opt2Text, (300, 315))

    opt3 = pygame.draw.rect(WINDOW, GREY, (50, 390, 165, 75))
    opt3Text = qFont.render("0", True, BLACK)
    WINDOW.blit(opt3Text, (115, 405))

    opt4 = pygame.draw.rect(WINDOW, GREY, (235, 390, 165, 75))
    opt4Text = qFont.render("3", True, BLACK)
    WINDOW.blit(opt4Text, (300, 405))

    #enemy
    WINDOW.blit(enemyOne, (415, 150))

    #health bar
    pygame.draw.rect(WINDOW, WHITE, (425, 120, 150, 20))
    pygame.draw.rect(WINDOW, RED, (425, 120, 150-health, 20))
    pygame.draw.rect(WINDOW, BLACK, (425, 120, 150, 20), 2)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN: 
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]

            #buttons
            if opt3.collidepoint([x, y]):
                screen = 7.1
                health += 30
                score += 1

            elif opt1.collidepoint([x, y]):
                screen = 7.2

            elif opt2.collidepoint([x, y]):
                screen = 7.2

            elif opt4.collidepoint([x, y]):
                screen = 7.2

            #music
            elif musicVol == 0.5 and btnMusic.collidepoint([x, y]):
                musicVol = 0.0

            elif musicVol == 0.0 and btnMusic.collidepoint([x, y]):
                musicVol = 0.5

def sub5():
    global screen
    global health
    global retries
    global score
    global qtnPage
    global musicVol
    qtnPage = 4.5
    
    #screen background
    WINDOW.blit(darkBG, (-80, 0))

    #music button
    btnMusic = pygame.draw.rect(WINDOW, COOKIE, (515, 10, 75, 75))
    WINDOW.blit(musicType(), (520, 15))

    #question text
    pygame.draw.rect(WINDOW, GREY, (50, 50, 350, 230))

    qFont = pygame.font.SysFont(None, 75)
    q5 = qFont.render("3 - 3 = ?", True, BLACK)
    WINDOW.blit(q5, (110, 75))

    #question image
    WINDOW.blit(axe, (100, 120))
    WINDOW.blit(axe, (200, 120))
    WINDOW.blit(axe, (150, 120))
    
    imgQ3 = qFont.render("-", True, BLACK)
    WINDOW.blit(imgQ3, (167, 150))
    
    WINDOW.blit(axe, (100, 190))
    WINDOW.blit(axe, (200, 190))
    WINDOW.blit(axe, (150, 190))

    imgQ3 = qFont.render("= ?", True, BLACK)
    WINDOW.blit(imgQ3, (300, 150))

    #retries
    smolFont = pygame.font.SysFont(None, 25)
    tRetries = smolFont.render("retries: " + str(retries), True, BLACK)
    WINDOW.blit(tRetries, (75, 210+40))

    #score
    tScore = smolFont.render("score: " + str(score), True, BLACK)
    WINDOW.blit(tScore, (300, 210+40))
    
    #answer options
    opt1 = pygame.draw.rect(WINDOW, GREY, (50, 300, 165, 75))
    opt1Text = qFont.render("5", True, BLACK)
    WINDOW.blit(opt1Text, (115, 315))

    opt2 = pygame.draw.rect(WINDOW, GREY, (235, 300, 165, 75))
    opt2Text = qFont.render("2", True, BLACK)
    WINDOW.blit(opt2Text, (300, 315))

    opt3 = pygame.draw.rect(WINDOW, GREY, (50, 390, 165, 75))
    opt3Text = qFont.render("0", True, BLACK)
    WINDOW.blit(opt3Text, (115, 405))

    opt4 = pygame.draw.rect(WINDOW, GREY, (235, 390, 165, 75))
    opt4Text = qFont.render("6", True, BLACK)
    WINDOW.blit(opt4Text, (300, 405))

    #enemy
    WINDOW.blit(enemyOne, (415, 150))

    #health bar
    pygame.draw.rect(WINDOW, WHITE, (425, 120, 150, 20))
    pygame.draw.rect(WINDOW, RED, (425, 120, 150-health, 20))
    pygame.draw.rect(WINDOW, BLACK, (425, 120, 150, 20), 2)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN: 
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]

            #buttons
            if opt3.collidepoint([x, y]):
                screen = 7.1
                health += 30
                score += 1

            elif opt1.collidepoint([x, y]):
                screen = 7.1

            elif opt2.collidepoint([x, y]):
                screen = 7.2

            elif opt4.collidepoint([x, y]):
                screen = 7.2

            #music
            elif musicVol == 0.5 and btnMusic.collidepoint([x, y]):
                musicVol = 0.0

            elif musicVol == 0.0 and btnMusic.collidepoint([x, y]):
                musicVol = 0.5
                
def english():
    global screen
    global musicVol
    
    #screen background
    WINDOW.blit(darkBG, (-80, 0))

    #music button
    btnMusic = pygame.draw.rect(WINDOW, COOKIE, (515, 10, 75, 75))
    WINDOW.blit(musicType(), (520, 15))

    #back button
    buttonFont = pygame.font.SysFont(None, 50)
    arrowBack = pygame.draw.polygon(WINDOW, GREY, ((10, 40), (50, 10), (50, 70)))
    btnBack = pygame.draw.rect(WINDOW, GREY, (50, 18, 110, 45))
    textBack = buttonFont.render("Back", True, BLACK)
    WINDOW.blit(textBack, (60, 24))

    #title text
    pygame.draw.rect(WINDOW, GREY, (95, 30+40, 405, 150))
    font = pygame.font.SysFont(None, 75)
    printText1 = font.render("Which Unit Do", True, BLACK)
    WINDOW.blit(printText1, (120, 50+40))
    printText2 = font.render("You Choose?", True, BLACK)
    WINDOW.blit(printText2, (130, 110+40))

    #spelling button
    buttonFont = pygame.font.SysFont(None, 50)
    btnSpell = pygame.draw.rect(WINDOW, GREY, (110, 278, 170, 55))
    textSpell = buttonFont.render("Spelling", True, BLACK)
    WINDOW.blit(textSpell, (125, 290))

    #grammar button
    btnGrammar = pygame.draw.rect(WINDOW, GREY, (305, 278, 185, 55))
    textGrammar = buttonFont.render("Grammar", True, BLACK)
    WINDOW.blit(textGrammar, (320, 290))

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]

            #buttons
            if btnSpell.collidepoint([x, y]):
                screen = 5.1

            elif btnGrammar.collidepoint([x, y]):
                screen = 6.1

            elif btnBack.collidepoint([x, y]):
                screen = 2

            #music
            elif musicVol == 0.5 and btnMusic.collidepoint([x, y]):
                musicVol = 0.0

            elif musicVol == 0.0 and btnMusic.collidepoint([x, y]):
                musicVol = 0.5

def spell1():
    global screen
    global health
    global retries
    global score
    global qtnPage
    global musicVol
    health = 0
    retries = 0
    score = 0
    qtnPage = 5.1
    
    #screen background
    WINDOW.blit(darkBG, (-80, 0))

    #music button
    btnMusic = pygame.draw.rect(WINDOW, COOKIE, (515, 10, 75, 75))
    WINDOW.blit(musicType(), (520, 15))

    #question text
    pygame.draw.rect(WINDOW, GREY, (50, 50, 350, 230))
    qFont = pygame.font.SysFont(None, 75)
    q1 = qFont.render("Which is", True, BLACK)
    WINDOW.blit(q1, (110, 100))
    q1 = qFont.render("Correct?", True, BLACK)
    WINDOW.blit(q1, (115, 160))
    
    #retries
    smolFont = pygame.font.SysFont(None, 25)
    tRetries = smolFont.render("retries: " + str(retries), True, BLACK)
    WINDOW.blit(tRetries, (75, 210+40))

    #score
    tScore = smolFont.render("score: " + str(score), True, BLACK)
    WINDOW.blit(tScore, (300, 210+40))

    #answer options
    opt1 = pygame.draw.rect(WINDOW, GREY, (50, 300, 165, 75))
    opt1Text = qFont.render("Untill", True, BLACK)
    WINDOW.blit(opt1Text, (65, 315))

    opt2 = pygame.draw.rect(WINDOW, GREY, (235, 300, 165, 75))
    opt2Text = qFont.render("Until", True, BLACK)
    WINDOW.blit(opt2Text, (250, 315))

    opt3 = pygame.draw.rect(WINDOW, GREY, (50, 390, 165, 75))
    opt3Text = qFont.render("Unntil", True, BLACK)
    WINDOW.blit(opt3Text, (65, 405))

    opt4 = pygame.draw.rect(WINDOW, GREY, (235, 390, 165, 75))
    opt4Text = qFont.render("Untel", True, BLACK)
    WINDOW.blit(opt4Text, (250, 405))

    #enemy
    WINDOW.blit(enemyTwo, (415, 150))

    #health bar
    pygame.draw.rect(WINDOW, WHITE, (425, 120, 150, 20))
    pygame.draw.rect(WINDOW, RED, (425, 120, 150-health, 20))
    pygame.draw.rect(WINDOW, BLACK, (425, 120, 150, 20), 2)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN: 
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]

            #buttons
            if opt2.collidepoint([x, y]):
                screen = 8.1
                health += 30
                score += 1

            elif opt1.collidepoint([x, y]):
                screen = 8.2

            elif opt3.collidepoint([x, y]):
                screen = 8.2

            elif opt4.collidepoint([x, y]):
                screen = 8.2

            #music
            elif musicVol == 0.5 and btnMusic.collidepoint([x, y]):
                musicVol = 0.0

            elif musicVol == 0.0 and btnMusic.collidepoint([x, y]):
                musicVol = 0.5

def spell2():
    global screen
    global health
    global retries
    global score
    global qtnPage
    global musicVol
    qtnPage = 5.2
    
    #screen background
    WINDOW.blit(darkBG, (-80, 0))

    #music button
    btnMusic = pygame.draw.rect(WINDOW, COOKIE, (515, 10, 75, 75))
    WINDOW.blit(musicType(), (520, 15))

    #question text
    pygame.draw.rect(WINDOW, GREY, (50, 50, 350, 230))
    qFont = pygame.font.SysFont(None, 75)
    q1 = qFont.render("Which is", True, BLACK)
    WINDOW.blit(q1, (110, 100))
    q1 = qFont.render("Correct?", True, BLACK)
    WINDOW.blit(q1, (115, 160))

    #retries
    smolFont = pygame.font.SysFont(None, 25)
    tRetries = smolFont.render("retries: " + str(retries), True, BLACK)
    WINDOW.blit(tRetries, (75, 210+40))

    #score
    tScore = smolFont.render("score: " + str(score), True, BLACK)
    WINDOW.blit(tScore, (300, 210+40))
    
    #answer options
    opt1 = pygame.draw.rect(WINDOW, GREY, (50, 300, 165, 75))
    opt1Text = qFont.render("don't", True, BLACK)
    WINDOW.blit(opt1Text, (75, 315))

    opt2 = pygame.draw.rect(WINDOW, GREY, (235, 300, 165, 75))
    opt2Text = qFont.render("do'nt", True, BLACK)
    WINDOW.blit(opt2Text, (250, 315))

    opt3 = pygame.draw.rect(WINDOW, GREY, (50, 390, 165, 75))
    opt3Text = qFont.render("dont", True, BLACK)
    WINDOW.blit(opt3Text, (75, 405))

    opt4 = pygame.draw.rect(WINDOW, GREY, (235, 390, 165, 75))
    opt4Text = qFont.render("donte", True, BLACK)
    WINDOW.blit(opt4Text, (250, 405))

    #enemy
    WINDOW.blit(enemyTwo, (415, 150))

    #health bar
    pygame.draw.rect(WINDOW, WHITE, (425, 120, 150, 20))
    pygame.draw.rect(WINDOW, RED, (425, 120, 150-health, 20))
    pygame.draw.rect(WINDOW, BLACK, (425, 120, 150, 20), 2)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]

            #buttons
            if opt1.collidepoint([x, y]):
                screen = 8.1
                health += 30
                score += 1

            elif opt2.collidepoint([x, y]):
                screen = 8.2

            elif opt3.collidepoint([x, y]):
                screen = 8.2

            elif opt4.collidepoint([x, y]):
                screen = 8.2

            #music
            elif musicVol == 0.5 and btnMusic.collidepoint([x, y]):
                musicVol = 0.0

            elif musicVol == 0.0 and btnMusic.collidepoint([x, y]):
                musicVol = 0.5

def spell3():
    global screen
    global health
    global retries
    global score
    global qtnPage
    global musicVol
    qtnPage = 5.3
    
    #screen background
    WINDOW.blit(darkBG, (-80, 0))

    #music button
    btnMusic = pygame.draw.rect(WINDOW, COOKIE, (515, 10, 75, 75))
    WINDOW.blit(musicType(), (520, 15))

    #question text
    pygame.draw.rect(WINDOW, GREY, (50, 50, 350, 230))
    qFont = pygame.font.SysFont(None, 75)
    q1 = qFont.render("Which is", True, BLACK)
    WINDOW.blit(q1, (110, 100))
    q1 = qFont.render("Correct?", True, BLACK)
    WINDOW.blit(q1, (115, 160))

    #retries
    smolFont = pygame.font.SysFont(None, 25)
    tRetries = smolFont.render("retries: " + str(retries), True, BLACK)
    WINDOW.blit(tRetries, (75, 210+40))

    #score
    tScore = smolFont.render("score: " + str(score), True, BLACK)
    WINDOW.blit(tScore, (300, 210+40))
    
    #answer options
    opt1 = pygame.draw.rect(WINDOW, GREY, (50, 300, 165, 75))
    opt1Text = qFont.render("hav", True, BLACK)
    WINDOW.blit(opt1Text, (85, 315))

    opt2 = pygame.draw.rect(WINDOW, GREY, (235, 300, 165, 75))
    opt2Text = qFont.render("hade", True, BLACK)
    WINDOW.blit(opt2Text, (250, 315))

    opt3 = pygame.draw.rect(WINDOW, GREY, (50, 390, 165, 75))
    opt3Text = qFont.render("haev", True, BLACK)
    WINDOW.blit(opt3Text, (75, 405))

    opt4 = pygame.draw.rect(WINDOW, GREY, (235, 390, 165, 75))
    opt4Text = qFont.render("have", True, BLACK)
    WINDOW.blit(opt4Text, (250, 405))

    #enemy
    WINDOW.blit(enemyTwo, (415, 150))

    #health bar
    pygame.draw.rect(WINDOW, WHITE, (425, 120, 150, 20))
    pygame.draw.rect(WINDOW, RED, (425, 120, 150-health, 20))
    pygame.draw.rect(WINDOW, BLACK, (425, 120, 150, 20), 2)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN: 
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]

            #buttons
            if opt4.collidepoint([x, y]):
                screen = 8.1
                health += 30
                score += 1

            elif opt1.collidepoint([x, y]):
                screen = 8.2

            elif opt2.collidepoint([x, y]):
                screen = 8.2

            elif opt3.collidepoint([x, y]):
                screen = 8.2

            #music
            elif musicVol == 0.5 and btnMusic.collidepoint([x, y]):
                musicVol = 0.0

            elif musicVol == 0.0 and btnMusic.collidepoint([x, y]):
                musicVol = 0.5

def spell4():
    global screen
    global health
    global retries
    global score
    global qtnPage
    global musicVol
    qtnPage = 5.4
    
    #screen background
    WINDOW.blit(darkBG, (-80, 0))

    #music button
    btnMusic = pygame.draw.rect(WINDOW, COOKIE, (515, 10, 75, 75))
    WINDOW.blit(musicType(), (520, 15))

    #question text
    pygame.draw.rect(WINDOW, GREY, (50, 50, 350, 230))
    qFont = pygame.font.SysFont(None, 75)
    q1 = qFont.render("Which is", True, BLACK)
    WINDOW.blit(q1, (110, 100))
    q1 = qFont.render("Correct?", True, BLACK)
    WINDOW.blit(q1, (115, 160))

    #retries
    smolFont = pygame.font.SysFont(None, 25)
    tRetries = smolFont.render("retries: " + str(retries), True, BLACK)
    WINDOW.blit(tRetries, (75, 210+40))

    #score
    tScore = smolFont.render("score: " + str(score), True, BLACK)
    WINDOW.blit(tScore, (300, 210+40))
    
    #answer options
    qFont = pygame.font.SysFont(None, 60)
    opt1 = pygame.draw.rect(WINDOW, GREY, (50, 300, 165, 75))
    opt1Text = qFont.render("thout", True, BLACK)
    WINDOW.blit(opt1Text, (75, 315))

    opt2 = pygame.draw.rect(WINDOW, GREY, (235, 300, 165, 75))
    opt2Text = qFont.render("toaut", True, BLACK)
    WINDOW.blit(opt2Text, (270, 315))

    opt3 = pygame.draw.rect(WINDOW, GREY, (50, 390, 165, 75))
    opt3Text = qFont.render("thought", True, BLACK)
    WINDOW.blit(opt3Text, (60, 405))

    opt4 = pygame.draw.rect(WINDOW, GREY, (235, 390, 165, 75))
    opt4Text = qFont.render("tought", True, BLACK)
    WINDOW.blit(opt4Text, (250, 405))

    #enemy
    WINDOW.blit(enemyTwo, (415, 150))

    #health bar
    pygame.draw.rect(WINDOW, WHITE, (425, 120, 150, 20))
    pygame.draw.rect(WINDOW, RED, (425, 120, 150-health, 20))
    pygame.draw.rect(WINDOW, BLACK, (425, 120, 150, 20), 2)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN: 
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]

            #buttons
            if opt3.collidepoint([x, y]):
                screen = 8.1
                health += 30
                score += 1

            elif opt1.collidepoint([x, y]):
                screen = 8.2

            elif opt2.collidepoint([x, y]):
                screen = 8.2

            elif opt4.collidepoint([x, y]):
                screen = 8.2

            #music
            elif musicVol == 0.5 and btnMusic.collidepoint([x, y]):
                musicVol = 0.0

            elif musicVol == 0.0 and btnMusic.collidepoint([x, y]):
                musicVol = 0.5

def spell5():
    global screen
    global health
    global retries
    global score
    global qtnPage
    global musicVol
    qtnPage = 5.5
    
    #screen background
    WINDOW.blit(darkBG, (-80, 0))

    #music button
    btnMusic = pygame.draw.rect(WINDOW, COOKIE, (515, 10, 75, 75))
    WINDOW.blit(musicType(), (520, 15))

    #question text
    pygame.draw.rect(WINDOW, GREY, (50, 50, 350, 230))
    qFont = pygame.font.SysFont(None, 75)
    q1 = qFont.render("Which is", True, BLACK)
    WINDOW.blit(q1, (110, 100))
    q1 = qFont.render("Correct?", True, BLACK)
    WINDOW.blit(q1, (115, 160))

    #retries
    smolFont = pygame.font.SysFont(None, 25)
    tRetries = smolFont.render("retries: " + str(retries), True, BLACK)
    WINDOW.blit(tRetries, (75, 210+40))

    #score
    tScore = smolFont.render("score: " + str(score), True, BLACK)
    WINDOW.blit(tScore, (300, 210+40))
    
    #answer options
    qFont = pygame.font.SysFont(None, 60)
    opt1 = pygame.draw.rect(WINDOW, GREY, (50, 300, 165, 75))
    opt1Text = qFont.render("becus", True, BLACK)
    WINDOW.blit(opt1Text, (75, 315))

    opt2 = pygame.draw.rect(WINDOW, GREY, (235, 300, 165, 75))
    opt2Text = qFont.render("because", True, BLACK)
    WINDOW.blit(opt2Text, (235, 315))

    opt3 = pygame.draw.rect(WINDOW, GREY, (50, 390, 165, 75))
    opt3Text = qFont.render("becaus", True, BLACK)
    WINDOW.blit(opt3Text, (65, 405))

    opt4 = pygame.draw.rect(WINDOW, GREY, (235, 390, 165, 75))
    opt4Text = qFont.render("bicause", True, BLACK)
    WINDOW.blit(opt4Text, (240, 405))

    #enemy
    WINDOW.blit(enemyTwo, (415, 150))

    #health bar
    pygame.draw.rect(WINDOW, WHITE, (425, 120, 150, 20))
    pygame.draw.rect(WINDOW, RED, (425, 120, 150-health, 20))
    pygame.draw.rect(WINDOW, BLACK, (425, 120, 150, 20), 2)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN: 
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]

            #buttons
            if opt2.collidepoint([x, y]):
                screen = 8.1
                health += 30
                score += 1

            elif opt1.collidepoint([x, y]):
                screen = 8.1

            elif opt3.collidepoint([x, y]):
                screen = 8.2

            elif opt4.collidepoint([x, y]):
                screen = 8.2

            #music
            elif musicVol == 0.5 and btnMusic.collidepoint([x, y]):
                musicVol = 0.0

            elif musicVol == 0.0 and btnMusic.collidepoint([x, y]):
                musicVol = 0.5

def grammar1():
    global screen
    global health
    global retries
    global score
    global qtnPage
    global musicVol
    health = 0
    retries = 0
    score = 0
    qtnPage = 6.1
    
    #screen background
    WINDOW.blit(darkBG, (-80, 0))

    #music button
    btnMusic = pygame.draw.rect(WINDOW, COOKIE, (515, 10, 75, 75))
    WINDOW.blit(musicType(), (520, 15))

    #question text
    pygame.draw.rect(WINDOW, GREY, (50, 50, 350, 230))
    qFont = pygame.font.SysFont(None, 60)
    q1 = qFont.render("What should be", True, BLACK)
    WINDOW.blit(q1, (75, 70))
    q1 = qFont.render("Capitalized?", True, BLACK)
    WINDOW.blit(q1, (75, 110))

    qFont = pygame.font.SysFont(None, 50)
    q1 = qFont.render("i went to the store.", True, BLACK)
    WINDOW.blit(q1, (75, 175))
    
    #retries
    smolFont = pygame.font.SysFont(None, 25)
    tRetries = smolFont.render("retries: " + str(retries), True, BLACK)
    WINDOW.blit(tRetries, (75, 210+40))

    #score
    tScore = smolFont.render("score: " + str(score), True, BLACK)
    WINDOW.blit(tScore, (300, 210+40))

    #answer options
    qFont = pygame.font.SysFont(None, 75)
    opt1 = pygame.draw.rect(WINDOW, GREY, (50, 300, 165, 75))
    opt1Text = qFont.render("Went", True, BLACK)
    WINDOW.blit(opt1Text, (65, 315))

    opt2 = pygame.draw.rect(WINDOW, GREY, (235, 300, 165, 75))
    opt2Text = qFont.render("I", True, BLACK)
    WINDOW.blit(opt2Text, (300, 315))

    opt3 = pygame.draw.rect(WINDOW, GREY, (50, 390, 165, 75))
    opt3Text = qFont.render("Store", True, BLACK)
    WINDOW.blit(opt3Text, (65, 405))

    opt4 = pygame.draw.rect(WINDOW, GREY, (235, 390, 165, 75))
    opt4Text = qFont.render("The", True, BLACK)
    WINDOW.blit(opt4Text, (265, 405))

    #enemy
    WINDOW.blit(enemyTwo, (415, 150))

    #health bar
    pygame.draw.rect(WINDOW, WHITE, (425, 120, 150, 20))
    pygame.draw.rect(WINDOW, RED, (425, 120, 150-health, 20))
    pygame.draw.rect(WINDOW, BLACK, (425, 120, 150, 20), 2)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN: 
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]

            #buttons
            if opt2.collidepoint([x, y]):
                screen = 8.1
                health += 30
                score += 1

            elif opt1.collidepoint([x, y]):
                screen = 8.2

            elif opt3.collidepoint([x, y]):
                screen = 8.2

            elif opt4.collidepoint([x, y]):
                screen = 8.2

            #music
            elif musicVol == 0.5 and btnMusic.collidepoint([x, y]):
                musicVol = 0.0

            elif musicVol == 0.0 and btnMusic.collidepoint([x, y]):
                musicVol = 0.5

def grammar2():
    global screen
    global health
    global retries
    global score
    global qtnPage
    global musicVol
    qtnPage = 6.2
    
    #screen background
    WINDOW.blit(darkBG, (-80, 0))

    #music button
    btnMusic = pygame.draw.rect(WINDOW, COOKIE, (515, 10, 75, 75))
    WINDOW.blit(musicType(), (520, 15))

    #question text
    pygame.draw.rect(WINDOW, GREY, (50, 50, 350, 230))
    qFont = pygame.font.SysFont(None, 60)
    q1 = qFont.render("What should be", True, BLACK)
    WINDOW.blit(q1, (75, 70))
    q1 = qFont.render("Capitalized?", True, BLACK)
    WINDOW.blit(q1, (75, 110))

    qFont = pygame.font.SysFont(None, 50)
    q1 = qFont.render("My friend's name", True, BLACK)
    WINDOW.blit(q1, (75, 175))

    q1 = qFont.render("is amy.", True, BLACK)
    WINDOW.blit(q1, (75, 210))
    
    #retries
    smolFont = pygame.font.SysFont(None, 25)
    tRetries = smolFont.render("retries: " + str(retries), True, BLACK)
    WINDOW.blit(tRetries, (75, 210+40))

    #score
    tScore = smolFont.render("score: " + str(score), True, BLACK)
    WINDOW.blit(tScore, (300, 210+40))
    
    #answer options
    qFont = pygame.font.SysFont(None, 75)
    opt1 = pygame.draw.rect(WINDOW, GREY, (50, 300, 165, 75))
    opt1Text = qFont.render("Amy", True, BLACK)
    WINDOW.blit(opt1Text, (75, 315))

    opt2 = pygame.draw.rect(WINDOW, GREY, (235, 300, 165, 75))
    opt2Text = qFont.render("Friend", True, BLACK)
    WINDOW.blit(opt2Text, (235, 315))

    opt3 = pygame.draw.rect(WINDOW, GREY, (50, 390, 165, 75))
    opt3Text = qFont.render("Name", True, BLACK)
    WINDOW.blit(opt3Text, (65, 405))

    opt4 = pygame.draw.rect(WINDOW, GREY, (235, 390, 165, 75))
    opt4Text = qFont.render("none", True, BLACK)
    WINDOW.blit(opt4Text, (250, 405))

    #enemy
    WINDOW.blit(enemyTwo, (415, 150))

    #health bar
    pygame.draw.rect(WINDOW, WHITE, (425, 120, 150, 20))
    pygame.draw.rect(WINDOW, RED, (425, 120, 150-health, 20))
    pygame.draw.rect(WINDOW, BLACK, (425, 120, 150, 20), 2)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]

            #buttons
            if opt1.collidepoint([x, y]):
                screen = 8.1
                health += 30
                score += 1

            elif opt2.collidepoint([x, y]):
                screen = 8.2

            elif opt3.collidepoint([x, y]):
                screen = 8.2

            elif opt4.collidepoint([x, y]):
                screen = 8.2

            #music
            elif musicVol == 0.5 and btnMusic.collidepoint([x, y]):
                musicVol = 0.0

            elif musicVol == 0.0 and btnMusic.collidepoint([x, y]):
                musicVol = 0.5

def grammar3():
    global screen
    global health
    global retries
    global score
    global qtnPage
    global musicVol
    qtnPage = 6.3
    
    #screen background
    WINDOW.blit(darkBG, (-80, 0))

    #music button
    btnMusic = pygame.draw.rect(WINDOW, COOKIE, (515, 10, 75, 75))
    WINDOW.blit(musicType(), (520, 15))

    #question text
    pygame.draw.rect(WINDOW, GREY, (50, 50, 350, 230))
    qFont = pygame.font.SysFont(None, 60)
    q1 = qFont.render("What should be", True, BLACK)
    WINDOW.blit(q1, (75, 70))
    q1 = qFont.render("Capitalized?", True, BLACK)
    WINDOW.blit(q1, (75, 110))

    qFont = pygame.font.SysFont(None, 50)
    q1 = qFont.render("I'm going to shop", True, BLACK)
    WINDOW.blit(q1, (75, 175))

    q1 = qFont.render("at the mall.", True, BLACK)
    WINDOW.blit(q1, (75, 210))

    #retries
    smolFont = pygame.font.SysFont(None, 25)
    tRetries = smolFont.render("retries: " + str(retries), True, BLACK)
    WINDOW.blit(tRetries, (75, 210+40))

    #score
    tScore = smolFont.render("score: " + str(score), True, BLACK)
    WINDOW.blit(tScore, (300, 210+40))
    
    #answer options
    qFont = pygame.font.SysFont(None, 75)
    opt1 = pygame.draw.rect(WINDOW, GREY, (50, 300, 165, 75))
    opt1Text = qFont.render("I'm", True, BLACK)
    WINDOW.blit(opt1Text, (95, 315))

    opt2 = pygame.draw.rect(WINDOW, GREY, (235, 300, 165, 75))
    opt2Text = qFont.render("Going", True, BLACK)
    WINDOW.blit(opt2Text, (240, 315))

    opt3 = pygame.draw.rect(WINDOW, GREY, (50, 390, 165, 75))
    opt3Text = qFont.render("Shop", True, BLACK)
    WINDOW.blit(opt3Text, (75, 405))

    opt4 = pygame.draw.rect(WINDOW, GREY, (235, 390, 165, 75))
    opt4Text = qFont.render("none", True, BLACK)
    WINDOW.blit(opt4Text, (255, 405))

    #enemy
    WINDOW.blit(enemyTwo, (415, 150))

    #health bar
    pygame.draw.rect(WINDOW, WHITE, (425, 120, 150, 20))
    pygame.draw.rect(WINDOW, RED, (425, 120, 150-health, 20))
    pygame.draw.rect(WINDOW, BLACK, (425, 120, 150, 20), 2)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN: 
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]

            #buttons
            if opt4.collidepoint([x, y]):
                screen = 8.1
                health += 30
                score += 1

            elif opt1.collidepoint([x, y]):
                screen = 8.2

            elif opt2.collidepoint([x, y]):
                screen = 8.2

            elif opt3.collidepoint([x, y]):
                screen = 8.2

            #music
            elif musicVol == 0.5 and btnMusic.collidepoint([x, y]):
                musicVol = 0.0

            elif musicVol == 0.0 and btnMusic.collidepoint([x, y]):
                musicVol = 0.5

def grammar4():
    global screen
    global health
    global retries
    global score
    global qtnPage
    global musicVol
    qtnPage = 6.4
    
    #screen background
    WINDOW.blit(darkBG, (-80, 0))

    #music button
    btnMusic = pygame.draw.rect(WINDOW, COOKIE, (515, 10, 75, 75))
    WINDOW.blit(musicType(), (520, 15))

    #question text
    pygame.draw.rect(WINDOW, GREY, (50, 50, 350, 230))
    qFont = pygame.font.SysFont(None, 60)
    q1 = qFont.render("What should be", True, BLACK)
    WINDOW.blit(q1, (75, 70))
    q1 = qFont.render("Capitalized?", True, BLACK)
    WINDOW.blit(q1, (75, 110))

    qFont = pygame.font.SysFont(None, 50)
    q1 = qFont.render("kelvin gave me a", True, BLACK)
    WINDOW.blit(q1, (75, 175))

    q1 = qFont.render("Christmas present.", True, BLACK)
    WINDOW.blit(q1, (75, 210))

    #retries
    smolFont = pygame.font.SysFont(None, 25)
    tRetries = smolFont.render("retries: " + str(retries), True, BLACK)
    WINDOW.blit(tRetries, (75, 210+40))

    #score
    tScore = smolFont.render("score: " + str(score), True, BLACK)
    WINDOW.blit(tScore, (300, 210+40))
    
    #answer options
    qFont = pygame.font.SysFont(None, 75)
    qFont = pygame.font.SysFont(None, 60)
    opt1 = pygame.draw.rect(WINDOW, GREY, (50, 300, 165, 75))
    opt1Text = qFont.render("Present", True, BLACK)
    WINDOW.blit(opt1Text, (55, 315))

    opt2 = pygame.draw.rect(WINDOW, GREY, (235, 300, 165, 75))
    opt2Text = qFont.render("Gave", True, BLACK)
    WINDOW.blit(opt2Text, (260, 315))

    opt3 = pygame.draw.rect(WINDOW, GREY, (50, 390, 165, 75))
    opt3Text = qFont.render("Kelvin", True, BLACK)
    WINDOW.blit(opt3Text, (75, 405))

    opt4 = pygame.draw.rect(WINDOW, GREY, (235, 390, 165, 75))
    opt4Text = qFont.render("none", True, BLACK)
    WINDOW.blit(opt4Text, (265, 405))

    #enemy
    WINDOW.blit(enemyTwo, (415, 150))

    #health bar
    pygame.draw.rect(WINDOW, WHITE, (425, 120, 150, 20))
    pygame.draw.rect(WINDOW, RED, (425, 120, 150-health, 20))
    pygame.draw.rect(WINDOW, BLACK, (425, 120, 150, 20), 2)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN: 
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]

            #buttons
            if opt3.collidepoint([x, y]):
                screen = 8.1
                health += 30
                score += 1

            elif opt1.collidepoint([x, y]):
                screen = 8.2

            elif opt2.collidepoint([x, y]):
                screen = 8.2

            elif opt4.collidepoint([x, y]):
                screen = 8.2

            #music
            elif musicVol == 0.5 and btnMusic.collidepoint([x, y]):
                musicVol = 0.0

            elif musicVol == 0.0 and btnMusic.collidepoint([x, y]):
                musicVol = 0.5

def grammar5():
    global screen
    global health
    global retries
    global score
    global qtnPage
    global musicVol
    qtnPage = 6.5
    
    #screen background
    WINDOW.blit(darkBG, (-80, 0))

    #music button
    btnMusic = pygame.draw.rect(WINDOW, COOKIE, (515, 10, 75, 75))
    WINDOW.blit(musicType(), (520, 15))

    #question text
    pygame.draw.rect(WINDOW, GREY, (50, 50, 350, 230))
    qFont = pygame.font.SysFont(None, 60)
    q1 = qFont.render("What should be", True, BLACK)
    WINDOW.blit(q1, (75, 70))
    q1 = qFont.render("Capitalized?", True, BLACK)
    WINDOW.blit(q1, (75, 110))

    qFont = pygame.font.SysFont(None, 50)
    q1 = qFont.render("She had a pet", True, BLACK)
    WINDOW.blit(q1, (75, 175))

    q1 = qFont.render("rabbit.", True, BLACK)
    WINDOW.blit(q1, (75, 210))

    #retries
    smolFont = pygame.font.SysFont(None, 25)
    tRetries = smolFont.render("retries: " + str(retries), True, BLACK)
    WINDOW.blit(tRetries, (75, 210+40))

    #score
    tScore = smolFont.render("score: " + str(score), True, BLACK)
    WINDOW.blit(tScore, (300, 210+40))
    
    #answer options
    qFont = pygame.font.SysFont(None, 75)
    qFont = pygame.font.SysFont(None, 60)
    opt1 = pygame.draw.rect(WINDOW, GREY, (50, 300, 165, 75))
    opt1Text = qFont.render("She", True, BLACK)
    WINDOW.blit(opt1Text, (95, 315))

    opt2 = pygame.draw.rect(WINDOW, GREY, (235, 300, 165, 75))
    opt2Text = qFont.render("Rabbit", True, BLACK)
    WINDOW.blit(opt2Text, (250, 315))

    opt3 = pygame.draw.rect(WINDOW, GREY, (50, 390, 165, 75))
    opt3Text = qFont.render("Pet", True, BLACK)
    WINDOW.blit(opt3Text, (95, 405))

    opt4 = pygame.draw.rect(WINDOW, GREY, (235, 390, 165, 75))
    opt4Text = qFont.render("none", True, BLACK)
    WINDOW.blit(opt4Text, (270, 405))

    #enemy
    WINDOW.blit(enemyTwo, (415, 150))

    #health bar
    pygame.draw.rect(WINDOW, WHITE, (425, 120, 150, 20))
    pygame.draw.rect(WINDOW, RED, (425, 120, 150-health, 20))
    pygame.draw.rect(WINDOW, BLACK, (425, 120, 150, 20), 2)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN: 
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]

            #buttons
            if opt4.collidepoint([x, y]):
                screen = 8.1
                health += 30
                score += 1

            elif opt1.collidepoint([x, y]):
                screen = 8.1

            elif opt2.collidepoint([x, y]):
                screen = 8.2

            elif opt2.collidepoint([x, y]):
                screen = 8.2

            #music
            elif musicVol == 0.5 and btnMusic.collidepoint([x, y]):
                musicVol = 0.0

            elif musicVol == 0.0 and btnMusic.collidepoint([x, y]):
                musicVol = 0.5

def correctMath():
    global screen
    global health
    global score
    global qtnPage
    global musicVol

    #screen background
    WINDOW.blit(darkBG, (-80, 0))

    #music button
    btnMusic = pygame.draw.rect(WINDOW, COOKIE, (515, 10, 75, 75))
    WINDOW.blit(musicType(), (520, 15))

    #text box
    pygame.draw.rect(WINDOW, GREY, (50, 50, 350, 230))
    font = pygame.font.SysFont(None, 100)
    tCorrect = font.render("Correct!", True, BLACK)
    WINDOW.blit(tCorrect, (90, 130))

    #retries
    smolFont = pygame.font.SysFont(None, 25)
    tRetries = smolFont.render("retries: " + str(retries), True, BLACK)
    WINDOW.blit(tRetries, (75, 210+40))

    #score
    tScore = smolFont.render("score: " + str(score), True, BLACK)
    WINDOW.blit(tScore, (300, 210+40))
    
    #enemy
    WINDOW.blit(enemyOne, (415, 150))

    #health bar
    pygame.draw.rect(WINDOW, WHITE, (425, 120, 150, 20))
    pygame.draw.rect(WINDOW, RED, (425, 120, 150-health, 20))
    pygame.draw.rect(WINDOW, BLACK, (425, 120, 150, 20), 2)

    #continue button
    btnFont = pygame.font.SysFont(None, 50)
    btncContinue = pygame.draw.rect(WINDOW, GREY, (120, 300, 200, 75))
    tContinue = btnFont.render("Continue", True, BLACK)
    WINDOW.blit(tContinue, (145, 320))

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN: 
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]

            #buttons
            #continue add
            if qtnPage == 3.1 and btncContinue.collidepoint([x, y]):
                screen = 3.2

            elif qtnPage == 3.2 and btncContinue.collidepoint([x, y]):
                screen = 3.3

            elif qtnPage == 3.3 and btncContinue.collidepoint([x, y]):
                screen = 3.4

            elif qtnPage == 3.4 and btncContinue.collidepoint([x, y]):
                screen = 3.5

            elif health == 150 and qtnPage == 3.5 and btncContinue.collidepoint([x, y]):
                screen = 9.1

            elif health != 150 and qtnPage == 3.5 and btncContinue.collidepoint([x, y]):
                screen = 9.2

            #continue subtract
            elif qtnPage == 4.1 and btncContinue.collidepoint([x, y]):
                screen = 4.2

            elif qtnPage == 4.2 and btncContinue.collidepoint([x, y]):
                screen = 4.3

            elif qtnPage == 4.3 and btncContinue.collidepoint([x, y]):
                screen = 4.4

            elif qtnPage == 4.4 and btncContinue.collidepoint([x, y]):
                screen = 4.5

            elif health == 150 and qtnPage == 4.5 and btncContinue.collidepoint([x, y]):
                screen = 9.1

            elif health != 150 and qtnPage == 4.5 and btncContinue.collidepoint([x, y]):
                screen = 9.2

            #music
            elif musicVol == 0.5 and btnMusic.collidepoint([x, y]):
                musicVol = 0.0

            elif musicVol == 0.0 and btnMusic.collidepoint([x, y]):
                musicVol = 0.5

def wrongMath():
    global screen
    global health
    global retries
    global score
    global qtnPage
    global musicVol

    #screen background
    WINDOW.blit(darkBG, (-80, 0))

    #music button
    btnMusic = pygame.draw.rect(WINDOW, COOKIE, (515, 10, 75, 75))
    WINDOW.blit(musicType(), (520, 15))

    #text box
    pygame.draw.rect(WINDOW, GREY, (50, 50, 350, 230))
    font = pygame.font.SysFont(None, 100)
    tCorrect = font.render("Wrong!", True, BLACK)
    WINDOW.blit(tCorrect, (90, 130))

    #retries
    smolFont = pygame.font.SysFont(None, 25)
    tRetries = smolFont.render("retries: " + str(retries), True, BLACK)
    WINDOW.blit(tRetries, (75, 210+40))

    #score
    tScore = smolFont.render("score: " + str(score), True, BLACK)
    WINDOW.blit(tScore, (300, 210+40))
    
    #enemy
    WINDOW.blit(enemyOne, (415, 150))

    #health bar
    pygame.draw.rect(WINDOW, WHITE, (425, 120, 150, 20))
    pygame.draw.rect(WINDOW, RED, (425, 120, 150-health, 20))
    pygame.draw.rect(WINDOW, BLACK, (425, 120, 150, 20), 2)

    #retry button
    btnFont = pygame.font.SysFont(None, 50)
    btnRetry = pygame.draw.rect(WINDOW, GREY, (50, 300, 165, 75))
    tRetry = btnFont.render("Retry", True, BLACK)
    WINDOW.blit(tRetry, (90, 320))

    #continue button
    btncContinue = pygame.draw.rect(WINDOW, GREY, (235, 300, 165, 75))
    tContinue = btnFont.render("Continue", True, BLACK)
    WINDOW.blit(tContinue, (240, 320))

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN: 
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]

            #buttons
            #retry add
            if qtnPage == 3.1 and btnRetry.collidepoint([x, y]):
                screen = 3.1
                retries += 1

            elif qtnPage == 3.2 and btnRetry.collidepoint([x, y]):
                screen = 3.2
                retries += 1

            elif qtnPage == 3.3 and btnRetry.collidepoint([x, y]):
                screen = 3.3
                retries += 1

            elif qtnPage == 3.4 and btnRetry.collidepoint([x, y]):
                screen = 3.4
                retries += 1

            elif qtnPage == 3.5 and btnRetry.collidepoint([x, y]):
                screen = 3.5
                retries += 1

            #retry subtract
            if qtnPage == 4.1 and btnRetry.collidepoint([x, y]):
                screen = 4.1
                retries += 1

            elif qtnPage == 4.2 and btnRetry.collidepoint([x, y]):
                screen = 4.2
                retries += 1

            elif qtnPage == 4.3 and btnRetry.collidepoint([x, y]):
                screen = 4.3
                retries += 1

            elif qtnPage == 4.4 and btnRetry.collidepoint([x, y]):
                screen = 4.4
                retries += 1

            elif qtnPage == 4.5 and btnRetry.collidepoint([x, y]):
                screen = 4.5
                retries += 1

            #continue add
            elif qtnPage == 3.1 and btncContinue.collidepoint([x, y]):
                screen = 3.2

            elif qtnPage == 3.2 and btncContinue.collidepoint([x, y]):
                screen = 3.3

            elif qtnPage == 3.3 and btncContinue.collidepoint([x, y]):
                screen = 3.4

            elif qtnPage == 3.4 and btncContinue.collidepoint([x, y]):
                screen = 3.5

            elif health == 150 and qtnPage == 3.5 and btncContinue.collidepoint([x, y]):
                screen = 9.1

            elif health != 150 and qtnPage == 3.5 and btncContinue.collidepoint([x, y]):
                screen = 9.2

            #continue subtract
            elif qtnPage == 4.1 and btncContinue.collidepoint([x, y]):
                screen = 4.2

            elif qtnPage == 4.2 and btncContinue.collidepoint([x, y]):
                screen = 4.3

            elif qtnPage == 4.3 and btncContinue.collidepoint([x, y]):
                screen = 4.4

            elif qtnPage == 4.4 and btncContinue.collidepoint([x, y]):
                screen = 4.5

            elif health == 150 and qtnPage == 4.5 and btncContinue.collidepoint([x, y]):
                screen = 9.1

            elif health != 150 and qtnPage == 4.5 and btncContinue.collidepoint([x, y]):
                screen = 9.2

            #music
            elif musicVol == 0.5 and btnMusic.collidepoint([x, y]):
                musicVol = 0.0

            elif musicVol == 0.0 and btnMusic.collidepoint([x, y]):
                musicVol = 0.5

def correctEnglish():
    global screen
    global health
    global score
    global qtnPage
    global musicVol

    #screen background
    WINDOW.blit(darkBG, (-80, 0))

    #music button
    btnMusic = pygame.draw.rect(WINDOW, COOKIE, (515, 10, 75, 75))
    WINDOW.blit(musicType(), (520, 15))

    #text box
    pygame.draw.rect(WINDOW, GREY, (50, 50, 350, 230))
    font = pygame.font.SysFont(None, 100)
    tCorrect = font.render("Correct!", True, BLACK)
    WINDOW.blit(tCorrect, (90, 130))

    #retries
    smolFont = pygame.font.SysFont(None, 25)
    tRetries = smolFont.render("retries: " + str(retries), True, BLACK)
    WINDOW.blit(tRetries, (75, 210+40))

    #score
    tScore = smolFont.render("score: " + str(score), True, BLACK)
    WINDOW.blit(tScore, (300, 210+40))
    
    #enemy
    WINDOW.blit(enemyTwo, (415, 150))

    #health bar
    pygame.draw.rect(WINDOW, WHITE, (425, 120, 150, 20))
    pygame.draw.rect(WINDOW, RED, (425, 120, 150-health, 20))
    pygame.draw.rect(WINDOW, BLACK, (425, 120, 150, 20), 2)

    #continue button
    btnFont = pygame.font.SysFont(None, 50)
    btncContinue = pygame.draw.rect(WINDOW, GREY, (120, 300, 200, 75))
    tContinue = btnFont.render("Continue", True, BLACK)
    WINDOW.blit(tContinue, (145, 320))

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN: 
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]

            #buttons
            #continue spelling
            if qtnPage == 5.1 and btncContinue.collidepoint([x, y]):
                screen = 5.2

            elif qtnPage == 5.2 and btncContinue.collidepoint([x, y]):
                screen = 5.3

            elif qtnPage == 5.3 and btncContinue.collidepoint([x, y]):
                screen = 5.4

            elif qtnPage == 5.4 and btncContinue.collidepoint([x, y]):
                screen = 5.5

            elif health == 150 and qtnPage == 5.5 and btncContinue.collidepoint([x, y]):
                screen = 9.1

            elif health != 150 and qtnPage == 5.5 and btncContinue.collidepoint([x, y]):
                screen = 9.2

            #continue grammar
            elif qtnPage == 6.1 and btncContinue.collidepoint([x, y]):
                screen = 6.2

            elif qtnPage == 6.2 and btncContinue.collidepoint([x, y]):
                screen = 6.3

            elif qtnPage == 6.3 and btncContinue.collidepoint([x, y]):
                screen = 6.4

            elif qtnPage == 6.4 and btncContinue.collidepoint([x, y]):
                screen = 6.5

            elif health == 150 and qtnPage == 6.5 and btncContinue.collidepoint([x, y]):
                screen = 9.1

            elif health != 150 and qtnPage == 6.5 and btncContinue.collidepoint([x, y]):
                screen = 9.2

            #music
            elif musicVol == 0.5 and btnMusic.collidepoint([x, y]):
                musicVol = 0.0

            elif musicVol == 0.0 and btnMusic.collidepoint([x, y]):
                musicVol = 0.5

def wrongEnglish():
    global screen
    global health
    global retries
    global score
    global qtnPage
    global musicVol

    #screen background
    WINDOW.blit(darkBG, (-80, 0))

    #music button
    btnMusic = pygame.draw.rect(WINDOW, COOKIE, (515, 10, 75, 75))
    WINDOW.blit(musicType(), (520, 15))

    #text box
    pygame.draw.rect(WINDOW, GREY, (50, 50, 350, 230))
    font = pygame.font.SysFont(None, 100)
    tCorrect = font.render("Wrong!", True, BLACK)
    WINDOW.blit(tCorrect, (90, 130))

    #retries
    smolFont = pygame.font.SysFont(None, 25)
    tRetries = smolFont.render("retries: " + str(retries), True, BLACK)
    WINDOW.blit(tRetries, (75, 210+40))

    #score
    tScore = smolFont.render("score: " + str(score), True, BLACK)
    WINDOW.blit(tScore, (300, 210+40))
    
    #enemy
    WINDOW.blit(enemyTwo, (415, 150))

    #health bar
    pygame.draw.rect(WINDOW, WHITE, (425, 120, 150, 20))
    pygame.draw.rect(WINDOW, RED, (425, 120, 150-health, 20))
    pygame.draw.rect(WINDOW, BLACK, (425, 120, 150, 20), 2)

    #retry button
    btnFont = pygame.font.SysFont(None, 50)
    btnRetry = pygame.draw.rect(WINDOW, GREY, (50, 300, 165, 75))
    tRetry = btnFont.render("Retry", True, BLACK)
    WINDOW.blit(tRetry, (90, 320))

    #continue button
    btncContinue = pygame.draw.rect(WINDOW, GREY, (235, 300, 165, 75))
    tContinue = btnFont.render("Continue", True, BLACK)
    WINDOW.blit(tContinue, (240, 320))

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN: 
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]

            #buttons
            #retry spelling
            if qtnPage == 5.1 and btnRetry.collidepoint([x, y]):
                screen = 5.1
                retries += 1

            elif qtnPage == 5.2 and btnRetry.collidepoint([x, y]):
                screen = 5.2
                retries += 1

            elif qtnPage == 5.3 and btnRetry.collidepoint([x, y]):
                screen = 5.3
                retries += 1

            elif qtnPage == 5.4 and btnRetry.collidepoint([x, y]):
                screen = 5.4
                retries += 1

            elif qtnPage == 5.5 and btnRetry.collidepoint([x, y]):
                screen = 5.5
                retries += 1

            #retry grammar
            if qtnPage == 6.1 and btnRetry.collidepoint([x, y]):
                screen = 6.1
                retries += 1

            elif qtnPage == 6.2 and btnRetry.collidepoint([x, y]):
                screen = 6.2
                retries += 1

            elif qtnPage == 6.3 and btnRetry.collidepoint([x, y]):
                screen = 6.3
                retries += 1

            elif qtnPage == 6.4 and btnRetry.collidepoint([x, y]):
                screen = 6.4
                retries += 1

            elif qtnPage == 6.5 and btnRetry.collidepoint([x, y]):
                screen = 6.5
                retries += 1

            #continue add
            elif qtnPage == 5.1 and btncContinue.collidepoint([x, y]):
                screen = 5.2

            elif qtnPage == 5.2 and btncContinue.collidepoint([x, y]):
                screen = 5.3

            elif qtnPage == 5.3 and btncContinue.collidepoint([x, y]):
                screen = 5.4

            elif qtnPage == 5.4 and btncContinue.collidepoint([x, y]):
                screen = 5.5

            elif health == 150 and qtnPage == 5.5 and btncContinue.collidepoint([x, y]):
                screen = 9.1

            elif health != 150 and qtnPage == 5.5 and btncContinue.collidepoint([x, y]):
                screen = 9.2

            #continue subtract
            elif qtnPage == 6.1 and btncContinue.collidepoint([x, y]):
                screen = 6.2

            elif qtnPage == 6.2 and btncContinue.collidepoint([x, y]):
                screen = 6.3

            elif qtnPage == 6.3 and btncContinue.collidepoint([x, y]):
                screen = 6.4

            elif qtnPage == 6.4 and btncContinue.collidepoint([x, y]):
                screen = 6.5

            elif health == 150 and qtnPage == 6.5 and btncContinue.collidepoint([x, y]):
                screen = 9.1

            elif health != 150 and qtnPage == 6.5 and btncContinue.collidepoint([x, y]):
                screen = 9.2

            #music
            elif musicVol == 0.5 and btnMusic.collidepoint([x, y]):
                musicVol = 0.0

            elif musicVol == 0.0 and btnMusic.collidepoint([x, y]):
                musicVol = 0.5

def endWin():
    global screen
    global health
    global retries
    global score
    global musicVol

    #screen background
    WINDOW.blit(darkBG, (-80, 0))
    
    #music button
    btnMusic = pygame.draw.rect(WINDOW, COOKIE, (515, 10, 75, 75))
    WINDOW.blit(musicType(), (520, 15))

    #text box
    pygame.draw.rect(WINDOW, GREY, (50, 50, 350, 230))
    font = pygame.font.SysFont(None, 100)
    t1 = font.render("Enemy", True, BLACK)
    WINDOW.blit(t1, (110, 100))
    t2 = font.render("Defeated!", True, BLACK)
    WINDOW.blit(t2, (70, 160))

    #retries
    smolFont = pygame.font.SysFont(None, 25)
    tRetries = smolFont.render("retries: " + str(retries), True, BLACK)
    WINDOW.blit(tRetries, (75, 210+40))

    #score
    tScore = smolFont.render("score: " + str(score), True, BLACK)
    WINDOW.blit(tScore, (300, 210+40))
    
    #enemy
    WINDOW.blit(enemy(subject), (415, 150))

    #health bar
    pygame.draw.rect(WINDOW, WHITE, (425, 120, 150, 20))
    pygame.draw.rect(WINDOW, RED, (425, 120, 150-health, 20))
    pygame.draw.rect(WINDOW, BLACK, (425, 120, 150, 20), 2)

    #try again button
    btnFont = pygame.font.SysFont(None, 50)
    btnTryAgain = pygame.draw.rect(WINDOW, GREY, (50, 300, 165, 80))
    
    tTry = btnFont.render("Try", True, BLACK)
    WINDOW.blit(tTry, (100, 310))
    
    tAgain = btnFont.render("Again", True, BLACK)
    WINDOW.blit(tAgain, (85, 340))

    #home screen button
    btnHome = pygame.draw.rect(WINDOW, GREY, (235, 300, 165, 80))
    
    tHome = btnFont.render("Home", True, BLACK)
    WINDOW.blit(tHome, (270, 310))
    
    tScreen = btnFont.render("Screen", True, BLACK)
    WINDOW.blit(tScreen, (260, 340))

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN: 
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]

            #buttons
            if btnTryAgain.collidepoint([x, y]):
                screen = 2

            elif btnHome.collidepoint([x, y]):
                screen = 1

            #music
            elif musicVol == 0.5 and btnMusic.collidepoint([x, y]):
                musicVol = 0.0

            elif musicVol == 0.0 and btnMusic.collidepoint([x, y]):
                musicVol = 0.5

def endLose():
    global screen
    global health
    global retries
    global score
    global musicVol

    #screen background
    WINDOW.blit(darkBG, (-80, 0))
    #music button
    btnMusic = pygame.draw.rect(WINDOW, COOKIE, (515, 10, 75, 75))
    WINDOW.blit(musicType(), (520, 15))

    #text box
    pygame.draw.rect(WINDOW, GREY, (50, 50, 350, 230))
    font = pygame.font.SysFont(None, 100)
    t1 = font.render("You Lose", True, BLACK)
    WINDOW.blit(t1, (70, 130))

    #retries
    smolFont = pygame.font.SysFont(None, 25)
    tRetries = smolFont.render("retries: " + str(retries), True, BLACK)
    WINDOW.blit(tRetries, (75, 210+40))

    #score
    tScore = smolFont.render("score: " + str(score), True, BLACK)
    WINDOW.blit(tScore, (300, 210+40))
    
    #enemy
    WINDOW.blit(enemy(subject), (415, 150))

    #health bar
    pygame.draw.rect(WINDOW, WHITE, (425, 120, 150, 20))
    pygame.draw.rect(WINDOW, RED, (425, 120, 150-health, 20))
    pygame.draw.rect(WINDOW, BLACK, (425, 120, 150, 20), 2)

    #try again button
    btnFont = pygame.font.SysFont(None, 50)
    btnTryAgain = pygame.draw.rect(WINDOW, GREY, (50, 300, 165, 80))
    
    tTry = btnFont.render("Try", True, BLACK)
    WINDOW.blit(tTry, (100, 310))
    
    tAgain = btnFont.render("Again", True, BLACK)
    WINDOW.blit(tAgain, (85, 340))

    #home screen button
    btnHome = pygame.draw.rect(WINDOW, GREY, (235, 300, 165, 80))
    
    tHome = btnFont.render("Home", True, BLACK)
    WINDOW.blit(tHome, (270, 310))
    
    tScreen = btnFont.render("Screen", True, BLACK)
    WINDOW.blit(tScreen, (260, 340))

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN: 
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]

            #buttons
            if btnTryAgain.collidepoint([x, y]):
                screen = 2

            elif btnHome.collidepoint([x, y]):
                screen = 1

            #music
            elif musicVol == 0.5 and btnMusic.collidepoint([x, y]):
                musicVol = 0.0

            elif musicVol == 0.0 and btnMusic.collidepoint([x, y]):
                musicVol = 0.5

#music
pygame.mixer.music.load("cookieMusic.ogg")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(loops = -1)

#animation variables
custardCheck = 0
custardX = 0
custardY = 0

beforeTrans = 0
transition = 600

#main code
while True:
    if screen == 0:
        enterNameScreen()
    
    elif screen == 1:
        homeScreen()

    elif screen == 1.1:
        instructions()
        
    elif screen == 2:
        subjectScreen()

    #math unit
    elif screen == 3:
        math()

    #addition
    elif screen == 3.1:
        add1()

    elif screen == 3.2:
        add2()

    elif screen == 3.3:
        add3()

    elif screen == 3.4:
        add4()

    elif screen == 3.5:
        add5()

    #subtraction
    elif screen == 4.1:
        sub1()

    elif screen == 4.2:
        sub2()

    elif screen == 4.3:
        sub3()

    elif screen == 4.4:
        sub4()

    elif screen == 4.5:
        sub5()

    #english unit
    elif screen == 5:
        english()

    #spelling
    elif screen == 5.1:
        spell1()

    elif screen == 5.2:
        spell2()

    elif screen == 5.3:
        spell3()

    elif screen == 5.4:
        spell4()

    elif screen == 5.5:
        spell5()

    #grammar
    elif screen == 6.1:
        grammar1()

    elif screen == 6.2:
        grammar2()

    elif screen == 6.3:
        grammar3()

    elif screen == 6.4:
        grammar4()

    elif screen == 6.5:
        grammar5()

    #correct/wrong pages
    elif screen == 7.1:
        correctMath()

    elif screen == 7.2:
        wrongMath()

    elif screen == 8.1:
        correctEnglish()

    elif screen == 8.2:
        wrongEnglish()

    #ending screen
    elif screen == 9.1:
        endWin()

    elif screen == 9.2:
        endLose()

    #animation1
    if custardX == 20:
        custardCheck = 1

    if custardX == 0:
        custardCheck = 0
    
    if custardX >= 0 and custardCheck == 0:
        custardX += 1
        custardY -= 1

    if custardX <= 20 and custardCheck == 1:
        custardX -= 1
        custardY += 1

    #animation2
    if transition > 0:
        beforeTrans -= 5
        transition -= 5
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()
    clock.tick(30)
