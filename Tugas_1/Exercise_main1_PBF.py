# M. Zaky Mahdavikia Zein Program main1_120450034.py
# Author : M. Zaky Mahdavikia Zein
# NIM : 120450034
# Kelas : RB
# Affiliation : Sains Data ITERA
# Date : 14 march 2022
# Perbaikan kuis 1 PBF RA
# Program Description : Program to solve simple encryption password problem 

from spetools_120450034 import encrypt

while True:
    jawab=input("Apakah kamu ingin melakukan enkripsi (y/n)? ")
    if jawab  == "y":
        text = input("Masukkan text pasword anda : ")
        print ("Text : " + text)
        print ("Cipher : " + encrypt(text))
    else:
        print("Terimakasih")
        break
        
