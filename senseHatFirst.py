from sense_hat import SenseHat
from datetime import datetime
from random import randint
from multiprocessing import Process, BoundedSemaphore
import time


def getMatrix():
    while True:
        x = randint(1,255)
        y = randint(1,255)
        z = randint(1,255)
        c = [x,y,z]
        return c

def getColor():
    
    while True:
        semaphore.acquire()
        b = [0,0,0]
        c = getMatrix()
        smiley = [b,b,c,c,c,c,b,b,
          b,c,b,b,b,b,c,b,
          c,b,c,b,b,c,b,c,
          c,b,b,b,b,b,b,c,
          c,b,c,b,b,c,b,c,
          c,b,b,c,c,b,b,c,
          b,c,b,b,b,b,c,b,
          b,b,c,c,c,c,b,b]
        sense.set_pixels(smiley)
        semaphore.release()
        time.sleep(3)
        
    

def myMainLogic():  
    num = 0
    isRunning = True
    while isRunning:       
        for event in sense.stick.get_events():
            if(num == 0):
                semaphore.acquire()
            if(event.direction[:1] == "r" and num == 0):
                temp =  "T: "+str(sense.get_temperature())[:5]
                sense.show_message(temp, scroll_speed = 0.1,text_colour=[240,130,60])
                num = 1
            elif(event.direction[:1] == "u" and num == 0):
                time_now = datetime.now().strftime('%H:%M')
                sense.show_message(time_now, scroll_speed = 0.1,text_colour=[100,150,150])
                num = 1
            elif(event.direction[:1] == "l" and num == 0):
                pressure = 'P: ' + str(sense.get_pressure())[:6]
                sense.show_message(pressure, scroll_speed = 0.1,text_colour=[100,150,150])
                num = 1
            elif(event.direction[:1] == "d" and num == 0):
                humidity = 'H: ' + str(sense.get_humidity())[:5]
                sense.show_message(humidity, scroll_speed = 0.1,text_colour=[100,150,150])
                num = 1
            elif(event.direction[:1] == "m" and num == 0):
                sense.show_message("Bye", scroll_speed = 0.1,text_colour=[100,150,150])
                num = 1
                isRunning = False
                t1.terminate()
                semaphore.release()
                
            elif(num == 1):
                num = 0
                semaphore.release()
                time.sleep(1)
                                          
    sense.clear()

c = getMatrix()
sense = SenseHat()
sense.clear()
sense.set_rotation(180)
sense.low_light = True
semaphore = BoundedSemaphore(value=1)
t1 = Process(name="getColor",target=getColor)
t2 = Process(name="main",target=myMainLogic)
#t1.daemon = True
#t2.daemon = True
t1.start()
t2.start()
        
        
