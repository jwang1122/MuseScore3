import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager
from math import pi

# A sin(kx -wt + phi)
# A=110/20
# D=146.8
# E=164.8
k=10
fA = 110
fD=146.8
fE=164.8
fC=130.8
fG=196.0
w1 = np.arange(0, fA/10, 0.02)
yA = np.sin(2*pi*w1)
y2 = 0.5*np.sin(4*pi*(w1+0.37))
y3 = yA+y2
yD = np.sin(2*pi*w1*fD/fA)
yE = np.sin(2*pi*w1*fE/fA+0.35)
yAE= yA+ yE
plt.xlabel('frequency')
plt.ylabel('sin(θ)')
plt.plot(w1, yA, label='A note')
# plt.plot(w1, y2, label='harmonics')
# plt.plot(w1, y3, label='Overlay')
plt.plot(w1, yE, label='E note')
plt.plot(w1, yAE, label='A E overlay')
plt.title('Sine Wave(A=110Hz, E=164.8Hz)')
plt.legend(loc='upper right')
plt.show()

plt.plot(w1, y3, label="A + harmonics")
plt.plot(w1, yA, label='A note')
plt.legend(loc='upper right')
plt.show()

y4 = yE + y3
plt.plot(w1, y4, label="E + A harmonics")
plt.plot(w1, yE, label='E note')
plt.legend(loc='upper right')
plt.show()

yC = np.sin(2*pi*w1*fC/fA)
yE = np.sin(2*pi*w1*fE/fA)
yG = np.sin(2*pi*w1*fG/fA)
I = yC+yE+yG
plt.plot(w1, yC, label="C note")
plt.plot(w1, yE, label='E note')
plt.plot(w1, yG, label='G note')
plt.plot(w1, I, label='Chord I')

plt.title('Sine Wave(C major chord)')
plt.legend(loc='upper right')
plt.show()

plt.plot(w1, I, label='Chord I')
plt.title('Sine Wave(C major chord)')
plt.legend(loc='upper right')
plt.show()

