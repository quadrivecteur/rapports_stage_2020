#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 11:36:28 2020

@author: Silver
"""

import numpy as np
import matplotlib.pyplot as plt

linx = np.linspace(-5,5,1001)
y1 = np.zeros (500)
y2 = np.ones (501)


fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_xlabel('x')
ax1.set_ylabel('H(x)')
ax1.set_title('Fonction de Heaviside centrée en 0')

plt.plot (linx,np.concatenate ((y1,y2)), 'k')
plt.savefig('Heaviside.pdf')
plt.show()
