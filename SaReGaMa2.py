import sounddevice as sd
import numpy as np 
from math import pi
from time import sleep
import keyboard 

# Sampling Frequency
Fs = 20000
# Time axis
t = np.arange(0,1,1/Fs)
# Defining the notes 
sa1 = np.sin(2*pi*240*t)
re = np.sin(2*pi*270*t)
ga = np.sin(2*pi*300*t)
ma = np.sin(2*pi*320*t)
pa = np.sin(2*pi*360*t)
dha = np.sin(2*pi*400*t)
ni = np.sin(2*pi*450*t)
sa2 = np.sin(2*pi*490*t)

while True:
    try:
        
        if keyboard.is_pressed('a'):
            sd.play(sa1,Fs)
        elif keyboard.is_pressed('s'):
            sd.play(re,Fs)
        elif keyboard.is_pressed('d'):
            sd.play(ga,Fs)
        elif keyboard.is_pressed('f'):
            sd.play(ma,Fs)
        elif keyboard.is_pressed('g'):
            sd.play(pa,Fs)
        elif keyboard.is_pressed('h'):
            sd.play(dha,Fs)
        elif keyboard.is_pressed('j'):
            sd.play(ni,Fs)
        elif keyboard.is_pressed('k'):
            sd.play(sa2,Fs)
        elif keyboard.is_pressed('x'):
            break
        else:
            pass

    except:
        break
