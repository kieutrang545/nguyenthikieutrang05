# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 20:10:14 2024

@author: nguyenthikieutrang
"""
a = int(input("nhap nam sinh cua ban:"))
if 0<a<=2023:
    tuoi= 2023 - a
    print("tuoi cua ban la",tuoi )
else:
     print("so tuoi khong hop le")