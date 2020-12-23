f = open("nov09.txt", "r")
f.readline()
f.readline()

b = []
while True:
    try:
        line = f.readline()
        for a in line.split(" "):
            b.append(float(a))
    except (EOFError, ValueError):
        break
print("COEFFICIENTS:")
print(b)
print("--------------------------")

c = []
while True:
    try:
        line = f.readline()
        for a in line.split(" "):
            c.append(float(a))
    except (EOFError, ValueError):
        break
print("RIGHT-HAND SIDE VALUES:")        
print(c)
print("--------------------------")


import numpy as np 
x = np.array([b[0:4], b[4:8], b[8:12], b[12:16]])
y = np.array(c)

z = np.linalg.solve(x,y)
print("SOLUTION:")
print(z)
