# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 18:21:27 2024

@author: Admin
"""

tong_chan=0
tong_le=0
for i in range(101):
    if i % 2==0:
        tong_chan +=i
    else:
        tong_le +=i
print("Tổng chẵn từ 0 đến 100 là:", tong_chan)
print("Tổng lẻ từ 0 đến 100 là:", tong_le)
    
        