# M. Zaky Mahdavikia Zein Program main1_120450034.py
# Author : M. Zaky Mahdavikia Zein
# NIM : 120450034
# Kelas : RB
# Affiliation : Sains Data ITERA
# Date : 14 march 2022
# Perbaikan kuis 1 PBF RA
# Program Description : Program to solve simple encryption password problem 

from spetools_120450034 import decrypt

text1 = 'Sc+T_+Sc+T[+TS-Sg+TS-Sg+Se+TW+TP-T\+Sc+TV+Sf+Sc+TX+TT+T]+T[+TU+TQ-TV+T]+T[+'
print('encrypted password :', text1)
print('decrypted password :', decrypt(text1))

text2 = 'TU+TQ-TV+TQ-TU+Sc+TT+Sh+T]+TV+Si+T[+TQ-TV+Ta+Sc+Sc+Sf+Sc+RQ-'
print('encrypted password :', text2)
print('decrypted password :', decrypt(text2))

text3 = 'Sd+Sg+TT+T]+TU+TX+Sg+TZ+TQ-TW+Sf+Sg+T[+T]+Sd+TU+TQ-T\+T\+T]+Si+Sc+T[+T[+T]+TV+TV+Sc+TP-'
print('encrypted password :', text3)
print('decrypted password :', decrypt(text3))

text4 = 'Sc+TV+Sc+TS-T[+Sc+TQ-TV+T[+Sf+Sc+T\+Sc+Qh+Qf+Qh+Qf+TS-Sg+Se+Sg+'
print('encrypted password :', text4)
print('decrypted password :', decrypt(text4))
