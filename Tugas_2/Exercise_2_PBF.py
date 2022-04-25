import numpy as np
a = open("text1.txt", 'w')
a.write("9502561694858652150281747994108545943651521215096841995237040384498740803993469376602031341619585763")
a.close()
aa = open("text1.txt", 'r')
f1=np.array(aa.read().split("\n")).astype(float)
ff1 = int(f1)


b = open("text2.txt", 'w')
b.write("2116068642696162934965789080530992805391900568978958496201555855833896833372295507803936243187061092")
b.close()
bb = open("text2.txt", 'r')
f2=np.array(bb.read().split("\n")).astype(float)
ff2 = int(f2)

f3 = ff1 + ff2
print(f3)
