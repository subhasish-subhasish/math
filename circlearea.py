import numpy as np
r= float(input("Enter Circle radious : "))
def area(r):
    return np.pi*(r**2)
def perimeter(r):
    return 2*np.pi*r
area=area(r)
perimeter=perimeter(r)
print('area of the circle : ',area)
print('perimeter of circcle : ',perimeter)