import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
# Функция, генерирующая исходные данные для интерполяции
def bigData():
    n = 10  # контрольное значение для генерации данных
    i = np.arange(0, 2 * n + 1)
    VY = [-1.0, -2.1, -3.2, -4.1, -4.7, -4.9, -4.8, -4.4, -3.7, -2.7,
          -1.6, -0.4, 0.7, 1.7, 2.4, 2.9, 3.0, 2.7, 2.1, 1.2, 0.2]  # Y-значения исходной функции
    VX = 2 * math.pi * i / (2 * n + 1)  # X-значения исходной функции
    XJ = []
    scale = 100  # общий масштаб точек
    J = 0
    while J < scale:
        XJ.append(min(VX) + J * (max(VX) - min(VX)) / scale)
        J = J + 1
    return VY, VX, XJ
# Функция, вызываемая для генерации интерполяционных данных
def scale():
    VY,VX,X=bigData()
    XJ1=[]
    scale1=15  # масштаб для первого набора данных
    j=0
    while j<scale1:
        XJ1.append(min(VX)+j*(max(VX)-min(VX))/scale1)
        j=j+1
    XJ2=[]
    scale2=50  # масштаб для второго набора данных
    j=0
    while j<scale2:
        XJ2.append(min(VX)+j*(max(VX)-min(VX))/scale2)
        j=j+1
    XJ3=[]
    scale3=100  # масштаб для третьего набора данных
    j=0
    while j<scale3:
        XJ3.append(min(VX)+j*(max(VX)-min(VX))/scale3)
        j=j+1
    C = interpolate.splrep(VX, VY)  # сплайновая интерполяция для каждого набора данных
    spl1 = interpolate.splev(XJ1, C)
    spl2 = interpolate.splev(XJ2, C)
    spl3 = interpolate.splev(XJ3, C)
    return XJ1,XJ2,XJ3,spl1,spl2,spl3
# Функция для отрисовки графиков с различным масштабом точек
def chart1():
    VY, VX, XJ = bigData()
    X1, X2, X3, spl1, spl2, spl3 = scale()
    fig, lin = plt.subplots()
    lin.plot(VX, VY, 'r*')  # график исходных данных
    lin.plot(X1, spl1, linestyle='-', color='lime')  # график первого набора данных
    lin.plot(X2, spl2, linestyle='-', color='violet')  # график второго набора данных
    lin.plot(X3, spl3, linestyle=':', color='black')  # график третьего набора данных
    lin.legend(['Исходные точки', 'scale = 15', 'scale = 50', 'scale = 100'])
    lin.set_title('Линейная при scale')
    plt.grid()
    plt.show()
def chart2():
    VY, VX, XJ = bigData()
    X1, X2, X3, spl1, spl2, spl3 = scale()
    x = np.arange(0, 5.9, 0.01)
    fig, lin = plt.subplots()
    lin.plot(VX, VY, 'r*')
    lin.plot(X1, spl1, linestyle='-', color='orange')
    lin.plot(X2, spl2, linestyle='-', color='blue')
    lin.plot(X3, spl3, linestyle=':', color='black')
    lin.legend(['Исходные точки', 'scale = 15', 'scale = 50', 'scale = 100'])
    lin.set_title('Кубическая при scale')
    plt.grid()
    plt.show()
def chart3():
    VY, VX, XJ = bigData()
    X1, X2, X3, spl1, spl2, spl3 = scale()
    x = np.arange(0, 5.9, 0.01)
    fig, lin = plt.subplots()
    lin.plot(VX, VY, 'r*')
    lin.plot(X1, spl1, linestyle='-', color='purple')
    lin.plot(X2, spl2, linestyle='-', color='green')
    lin.plot(X3, spl3, linestyle=':', color='yellow')
    lin.legend(['Исходные точки', 'scale = 15', 'scale = 50', 'scale = 100'])
    lin.set_title('Параболическая при scale')
    plt.grid()
    plt.show()
#вывод графиков
chart1()
chart2()
chart3()