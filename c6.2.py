# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 19:20:25 2024

@author: nguyenthikieutrang
"""
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
tong = a + b
hieu = a - b
tich = a * b
thuong = round(a / b, 3)
chialaydu = a % b
chialaynguyen = a // b
print("Tổng: ",tong)
print("Hiệu:", hieu)
print("Tích: ",tich)
print("Thương (làm tròn 3 chữ số): ",thuong)
print("Chia lấy dư:",chialaydu)
print("Chia lấy nguyên:", chialaynguyen)