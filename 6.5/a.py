import csv
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np
def func(x, a, b):
    return a * x + b
def main():
    csv_reader=csv.reader(open('data3.csv',encoding="utf-8"))
    s = []
    x = []
    y = []
    jindu = 0
    weidu = 0
    for i in csv_reader:
        if jindu == 0:
            jindu = float(i[12])
            weidu = float(i[13])
        print(i[12])
        if i[2] == "2" and int(i[10]) > 2000 and jindu - float(i[12]) < 0.01 and weidu - float(i[13]) < 0.01:  
            x.append(int(i[8]))
            y.append(int(i[1]))
    x = np.array(x)
    y = np.array(y)
    popt, pcov = curve_fit(func, x, y)
    yvals = func(x, popt[0], popt[1])
    plot1 = plt.plot(x, y, 's',label='original values')
    plot2 = plt.plot(x, yvals, 'r',label='polyfit values')
    plt.show()
if __name__ == "__main__":
    main()