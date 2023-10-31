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
# кусочно - линейная интерполяция
def piecewiseLinearInterpolation(x):
    VY, VX, XJ = bigData()
    f = interpolate.interp1d(VX, VY, kind='linear')
    return f(x)
# сплайн - линейная интерполяция
def splineLinearInterpolation(x):
    VY, VX, XJ = bigData()
    C = interpolate.splrep(VX, VY)
    f = interpolate.splev(x, C)
    return f
# сплайн - кубическая интерполяция
def splineCubicInterpolation(x):
    VY, VX, XJ = bigData()
    f = interpolate.interp1d(VX, VY,'cubic')
    return f(x)
# сплайн - пабаробилческая интерполяция
def splineParabolicInterpolation(x):
    VY, VX, XJ = bigData()
    f = interpolate.interp1d(VX, VY, kind='quadratic')
    return f(x)
# кусочно - линейная экстраполяция
def piecewiseLinearExtrapolation(x):
    VY, VX, XJ = bigData()
    f = interpolate.interp1d(VX, VY, kind='linear', fill_value='extrapolate')
    return f(x)
# сплайн - кубическая экстрополяция
def splineCubicExtrapolation(x):
    VY, VX, XJ = bigData()
    f = interpolate.interp1d(VX, VY,'cubic', fill_value='extrapolate')
    return f(x)
# сплайн - параболическая экстрополяция
def splineParabolicExtrapolation(x):
    VY, VX, XJ = bigData()
    f = interpolate.interp1d(VX, VY, kind='quadratic', fill_value='extrapolate')
    return f(x)
# сплайн - линейная экстрополяця
def cspline(x):
    VY, VX, XJ = bigData()
    C = interpolate.splrep(VX, VY)
    spl=interpolate.splev(x, C)
    return spl
# график кусочно - линейной интерполяции
def chart1():
    VY, VX, XJ = bigData()
    x = np.arange(0, 5.980, 0.01)
    fig, lin = plt.subplots()
    lin.plot(VX, VY, 'r*')
    lin.plot(x, piecewiseLinearInterpolation(x), '-b')
    lin.legend(['Исходные точки', 'Кусочно - линейная интерполяция'])
    lin.set_title('Кусочно - линейная интерполяция')
    plt.grid()
    plt.show()
# график сравнения кусочно - линейной и сплайн - линейной интерполяции
def chart2():
    VY, VX, XJ = bigData()
    x = np.arange(0, 5.980, 0.01)
    fig, lin = plt.subplots()
    lin.plot(VX, VY, 'r*')
    lin.plot(x, piecewiseLinearInterpolation(x), '-b')
    lin.plot(x, splineLinearInterpolation(x), '-g')
    lin.legend(['Исходные точки', 'Кусочно - линеная', 'Сплайн - линейная'])
    lin.set_title('Cравнения кусочно - линейной и сплайн - линейной интерполяции')
    plt.grid()
    plt.show()
# сравнение 3 видов сплайн интерполяции
def chart3():
    VY, VX, XJ = bigData()
    x = np.arange(0, 5.980, 0.01)
    fig, lin = plt.subplots()
    lin.plot(VX, VY, 'r*')
    lin.plot(x, splineLinearInterpolation(x), '--b')
    lin.plot(x, splineParabolicInterpolation(x), ':g')
    lin.plot(x, splineCubicInterpolation(x), ':y')
    lin.legend(['Исходные точки', 'Линейная', 'Кубическая', 'Параболическая'])
    lin.set_title('Сравнение сплайн интерполяций')
    plt.grid()
    plt.show()
# сравнение 3 видов сплайн интерполяции на изгибе
# график интерполяции вне диапазона
def chart5():
    VY, VX, XJ = bigData()
    x = np.arange(5, 8, 0.01)
    fig, lin = plt.subplots()
    range1, range2, range3 = calculationsOutARange()
    lin.plot(VX, VY, 'r*')
    lin.plot(7, range1, 'b*')
    lin.plot(7, range2, 'g*')
    lin.plot(7, range3, 'y*')
    lin.plot(x, piecewiseLinearExtrapolation(x), '-b')
    lin.plot(x, splineCubicExtrapolation(x), '-g')
    lin.plot(x, splineParabolicExtrapolation(x), '-y')
    plt.xlim(5, 8)
    plt.ylim(-5, 10)
    lin.legend(['Исходные точки','Кус-лин точка при х=7', 'Куб точка при х=7', 'Параб точка при х=7', 'Кусочно - линейная', 'Сплайн - кубическая', 'Сплайн - параболическая'])
    lin.set_title('Интерполяция вне диапозона')
    plt.grid()
    plt.show()
# вычисление значений в узле и между узлами
def calculationsNode():
    print("Интерполяция в узле (0.598)")
    print("Кусочно - линеная: ", piecewiseLinearInterpolation(0.598))
    print("Сплайн - линейная: ", splineLinearInterpolation(0.598))
    print("Сплайн - кубическая: ", splineCubicInterpolation(0.598))
    print("Сплайн - параболическая: ", splineParabolicInterpolation(0.598))
    print("Интерполяция между узлами (4.78)")
    print("Кусочно - линейная: ", piecewiseLinearInterpolation(4.78))
    print("Сплайн - линейная: ", splineLinearInterpolation(4.78))
    print("Сплайн - кубическая: ", splineCubicInterpolation(4.78))
    print("Сплайн - параболическая: ", splineParabolicInterpolation(4.78))
    print("Интерполяция вне диапазона (7)")
    print("Кусочно - линеная: ", piecewiseLinearInterpolation(7))
    print("Сплайн - линейная: ", splineLinearInterpolation(7))
    print("Сплайн - кубическая: ", splineCubicInterpolation(7))
    print("Сплайн - параболическая: ", splineParabolicInterpolation(7))
    return
# Определение функции для расчета значение вне диапазона
def calculationsOutARange():
    range1 = piecewiseLinearExtrapolation(7)
    range3 = splineCubicExtrapolation(7)
    range2 = splineParabolicExtrapolation(7)
    return [range1, range2, range3]
# Строим графики
chart1()
chart2()
chart3()
chart5()
# Проводим расчеты
calculationsNode()
calculationsOutARange()
