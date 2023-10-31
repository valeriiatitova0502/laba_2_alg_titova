# Импортирование необходимых библиотек
import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate
from scipy import interpolate
# Определение функции, возвращающей набор данных для интерполяции
def bigData():
    n = 10
    i = np.arange(0, 2 * n + 1)
    # Указание значений Y
    VY = [-1.0, -2.1, -3.2, -4.1, -4.7, -4.9, -4.8, -4.4, -3.7, -2.7,
    -1.6, -0.4, 0.7, 1.7, 2.4, 2.9, 3.0, 2.7, 2.1, 1.2, 0.2]
    # Указание значений X
    VX = 2 * math.pi * i / (2 * n + 1)
    # Указание значений XJ на основе заданных значений VX
    XJ = []
    scale = 100
    J = 0
    while J < scale:
        XJ.append(min(VX) + J * (max(VX) - min(VX)) / scale)
        J = J + 1
    return VY, VX, XJ
# Определение функции, возвращающей набор данных для интерполяции
def smallData():
    # Указание значений Y
    vy = [-1.0, -3.2, -4.7, -4.8, -3.7, -1.6, 0.7, 2.4, 3.0, 2.1, 0.2]
    # Указание значений X
    vx = [0, 0.598399, 1.196797, 1.795196, 2.393594, 2.991993, 3.590392,
          4.18879, 4.787189, 5.385587, 5.983986]
    # Указание значений XJ на основе заданных значений VX
    xj=[]
    scale=100
    j=0
    while j<scale:
        xj.append(min(vx)+j*(max(vx)-min(vx))/scale)
        j=j+1
    return vy, vx, xj
#(параболическое) сплайн-интерполирование на больших данных
def splineParabolicInterpolation(x):
    VY, VX, XJ = bigData()
    f = interpolate.interp1d(VX, VY, kind='quadratic')
    return f(x)
#(параболическое) сплайн-интерполирование на малых данных
def splineParabolicInterpolationSmall(x):
    VY, VX, XJ = smallData()
    f = interpolate.interp1d(VX, VY, kind='quadratic')
    return f(x)
# кусочно - линейная интерполяция
def piecewiseLinearInterpolation(x):
    VY, VX, XJ = smallData()
    f = interpolate.interp1d(VX, VY, kind='linear')
    return f(x)

# сплайн - линейная интерполяция
def splineLinearInterpolation(x):
    VY, VX, XJ = smallData()
    C = interpolate.splrep(VX, VY)
    f = interpolate.splev(x, C)
    return f

# сплайн - кубическая интерполяция
def splineCubicInterpolation(x):
    VY, VX, XJ = smallData()
    f = interpolate.interp1d(VX, VY,'cubic')
    return f(x)
#Определение тригонометрической интерполяции для полных данных
def pbig(x):
    VY_big,VX_big,XJ_big = bigData()
    n = 10
    i = 0
    a0 = 0
    while i < 2 * n + 1:
        a0 += VY_big[i]
        i = i + 1
    a0 = a0 / (2 * n + 1)
    k = 1
    ak = []
    bk = []
    while k < n + 1:
        a = b = 0
        i = 0
        while i < 2 * n + 1:
            a += VY_big[i] * math.cos (k * VX_big[i])
            b += VY_big[i] * math.sin(k * VX_big[i])
            i = i + 1
        ak.append(a / (2 * n + 1))
        bk.append(b / (2 * n + 1))
        k = k + 1
    i = 0
    c = []
    c1 = []
    while i<len(x):
        p = 0
        p1 = 0
        k = 1
        k1 = 0
        while k < n + 1:
            p +=ak[k1] * math.cos(k * x[i])
            p1 += bk[k1] * math.sin(k*x[i])
            k = k + 1
            k1 = k1 + 1
        c.append(p)
        c1.append(p1)
        i= i + 1
    k = 0
    P = []
    while k<len(c):
        P.append((c[k] + c1[k]) * 2 + a0)
        k = k + 1
    return P
#Определение тригонометрической интерполяции для малых данных
def psmall(x):
    VY_small, VX_small, XJ_small = smallData()
    n = len(VY_small) - 1
    i = 0
    a0 = 0
    while i < n + 1:
        a0 += VY_small[i]
        i = i + 1
    a0 = a0 / (n + 1)
    k = 0
    ak = []
    bk = []
    while k < n + 1:  # use equal number of components as data points
        a = b = 0
        i = 0
        while i < n + 1:
            a += VY_small[i] * math.cos (2 * k * np.pi * VX_small[i]/(n+1))  # normalize multiplied angles
            b += VY_small[i] * math.sin(2 * k * np.pi * VX_small[i]/(n+1))
            i = i + 1
        ak.append(a / (n + 1))
        bk.append(b / (n + 1))
        k = k + 1
    i = 0
    c = []
    c1 = []
    while i<len(x):
        p = 0
        p1 = 0
        k = 1
        k1 = 0
        while k < n + 1:
            p +=ak[k1] * math.cos(2 * k * np.pi * x[i]/(n+1))
            p1 += bk[k1] * math.sin(2 * k * np.pi * x[i]/(n+1))
            k = k + 1
            k1 = k1 + 1
        c.append(p)
        c1.append(p1)
        i= i + 1
    k = 0
    P = []
    while k<len(c):
        P.append((c[k] + c1[k]) * 2 + a0)
        k = k + 1
    return P
#Общая функция для тригонометрической интерполяции
def trigonometricinterpolation(x):
    VY, VX, _ = smallData()
    poly = interpolate.lagrange(VX, VY)
    return poly(x)

#Функция для сравнения тригонометрической интерполяции на полном и малом наборе данных
def sravnenietrigonometric():
    # Получить данные
    VY_big, VX_big, XJ_big = bigData()
    VY_small, VX_small, XJ_small = smallData()

    P_big = pbig(XJ_big)
    P_small = psmall(XJ_small)
    Trigonometric = trigonometricinterpolation(np.array(XJ_small))

    # Создать график
    plt.figure('Сравнение данных')
    plt.plot(VX_big, VY_big, 'go', label='Полный набор точек', markersize=5)
    plt.plot(VX_small, VY_small, 'ro', label='Малый набор точек', markersize=5)
    plt.plot(XJ_big, P_big, 'g-', label='Триг инт полного набора')
    plt.plot(XJ_small, Trigonometric, 'b-', label='Триг инт малого набора')

    plt.legend()
    plt.title('Сравнение тригонометрической интерполяции при полном и малом наборе данных')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()


sravnenietrigonometric()

# тригонометрическая интерполяция полный набор данных
def chart1():
    VY, VX, XJ = bigData()
    x = np.arange(0, 5.980, 0.01)
    fig, lin = plt.subplots()
    lin.plot(VX, VY, 'r*')
    lin.plot(x, pbig(x), linestyle='-', color='firebrick')
    lin.legend(['Исх. т.', 'Триг. инт.'])
    lin.set_title('Тригонометрическая интерполяция полный набор данных')
    plt.grid()
    plt.show()

#Сравнение различных видов интерполяции при малом наборе данных
def chart5():
    VY, VX, XJ = bigData()
    VY, VX, XJ = smallData()
    x = np.arange(0, 5.980, 0.01)
    fig, lin = plt.subplots()
    lin.plot(VX, VY, 'r*')
    lin.plot(x, splineParabolicInterpolationSmall(x), ':r')
    lin.plot(x, splineLinearInterpolation(x), '--b')
    lin.plot(x, splineCubicInterpolation(x), '--g')
    lin.legend(['Исходные точки', 'Параболическая', 'Линейная', 'Кубическая'])
    lin.set_title('Интерполяции при неполном наборе данных')
    plt.grid()
    plt.show()
#Сравнение параболических интерполяций при полном и малом наборе данных
def chart6():
    VY, VX, XJ = bigData()
    vy, vx, xj = smallData()
    x = np.arange(0, 5.980, 0.01)
    fig, lin = plt.subplots()
    lin.plot(VX, VY, 'r*')
    lin.plot(vx, vy, 'g*')
    lin.plot(x, splineParabolicInterpolationSmall(x), ':r')
    lin.plot(x, splineParabolicInterpolation(x), ':b')
    lin.legend(['Исходные точки полный наб.','Исходные точки малый наб.', 'Пароболическая полн', 'Параболическая неполн'])
    lin.set_title('Сравнение пароболических интерполяций при неполн и полн')
    plt.grid()
    plt.show()
#Строим графики
chart1()
chart5()
chart6()

