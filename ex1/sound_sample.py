import os
import sys
import time
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))
pg.mixer.init()  

def main():
    
    effect = pg.mixer.Sound("sound/boom.wav")  
    
    effect.play()  

    pg.mixer.music.load("sound/house_lo.wav")
    
    pg.mixer.music.play()  
    time.sleep(10)  
    pg.mixer.music.stop()  


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()