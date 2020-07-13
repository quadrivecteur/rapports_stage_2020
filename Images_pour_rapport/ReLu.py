#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 11:36:28 2020

@author: Silver
"""

import numpy as np
import matplotlib.pyplot as plt

linx = np.linspace(0,5,500)
x = np.linspace(-5,0,500)
y1 = np.zeros (500)


fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_xlabel('x')
ax1.set_ylabel('f(x)')
ax1.set_title('Fonction ReLu')

plt.plot (x,y1, 'k')
plt.plot (linx,linx, 'k')
plt.savefig('ReLu.pdf')
plt.show()
