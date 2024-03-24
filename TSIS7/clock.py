import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("circle")
r = 25
x, y = 500, 500
cond = False
clock = pygame.time.Clock()
while not cond:
    clock.tick(60)
    for cycle in pygame.event.get():
        if cycle.type == pygame.QUIT:
            cond = True

    butts = pygame.key.get_pressed()
    if butts[pygame.K_UP] and y-r > 0:
        y += -20
    elif butts[pygame.K_DOWN] and y+r < 600:
        y += 20
    elif butts[pygame.K_RIGHT] and x+r < 800:
        x += 20
    elif butts[pygame.K_LEFT] and x-r > 0:
        x += -20
        
    screen.fill("#FFFFFF")
    pygame.draw.circle(screen, "#FF0000", (x, y), r)
    
    pygame.display.flip()
pygame.quit()
sys.quit()


#Create a simple clock application (only with minutes and seconds) which is synchronized with system clock.
#Use Mickey's right hand as minutes arrow and left - as seconds.
import datetime
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((830, 900))
sec = pygame.image.load("minute.png")
min = pygame.image.load("second.png")
back = pygame.image.load("mickeyclock.jpeg")
pygame.display.set_caption("hickey clock")
sec2 = pygame.transform.scale(sec, (200, 200))
min2 = pygame.transform.scale(min, (200, 200))
clock = pygame.time.Clock()

def transformed(surface, image, topleft, angle):
    rotated = pygame.transform.rotate(image, angle)
    rectg = rotated.get_rect(center = image.get_rect(topleft = topleft).center)
    surface.blit(rotated, rectg)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(back, (0, 0))
    time = datetime.datetime.now()
    minute = time.minute
    second = time.second   
    transformed(screen, sec2, (370, 248), second* -6)
    transformed(screen, min2, (370, 248), minute* -6)
    pygame.display.flip()
    clock.tick(60)



#Create music player with keyboard controller. You have to be able to press keyboard:
#play, stop, next and previous as some keys. Player has to react to the given command appropriately.
import pygame
import sys


pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("nice pleasing music")

playlist = ['tenebro.mp3', 'cataclysm.mp3']

pygame.mixer.init()
pygame.mixer.music.load(playlist[0])
#keyboardd
play_key = pygame.K_RETURN
stop_key = pygame.K_SPACE
next_key = pygame.K_RIGHT
prev_key = pygame.K_LEFT

current_track = 0

def play():
    pygame.mixer.music.play()
def pause():
    pygame.mixer.music.pause()
def stop():
    pygame.mixer.music.stop()
def next():
    global current_track
    if current_track < len(playlist) - 1:
        current_track += 1
        pygame.mixer.music.load(playlist[current_track])
        pygame.mixer.music.play()
def previous():
    global current_track
    if current_track > 0:
        current_track -= 1
        pygame.mixer.music.load(playlist[current_track])
        pygame.mixer.music.play()

background = pygame.image.load("coole.png")
while True:
    screen.blit(background, (0, 0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == play_key:
                play()
            elif event.key == stop_key:
                stop()
            elif event.key == next_key:
                next()
            elif event.key == prev_key:
                previous()
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()