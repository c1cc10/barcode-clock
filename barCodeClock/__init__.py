# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import time
import datetime
import re
import code128_test

lastTickTime = 0
last = 0
now = 0
lastTickTime = time.localtime()

def getDataOra():
    return re.sub(r"\..*$","", str(datetime.datetime.now()))

data_e_ora = getDataOra()
timeCode = code128_test.code128_image(data_e_ora)
timeImage = timeCode.convert('RGBA')
player = pygame.image.frombuffer(timeImage.tobytes(), timeImage.size, timeImage.mode)
width, height = timeImage.size


pygame.init()

screen=pygame.display.set_mode((width, height))

while 1:
    screen.fill(0)
    time.sleep(.300)
    screen.blit(player, (0,0))
    pygame.display.flip()
    last = lastTickTime
    now = time.localtime()
    lastTickTime = now
    if now[:6] == last[:6]:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit() 
                exit(0)
    else:
        try:
            timeCode = code128_test.code128_image(getDataOra())
            timeImage = timeCode.convert('RGBA')
            player = pygame.image.frombuffer(timeImage.tobytes(), timeImage.size, timeImage.mode)
        except Exception, e:
            print("everySecond() error: %s" % e)

