import numpy as np
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp
import uncertainties as unc
from scipy.optimize import curve_fit


#Rauschunterdrückung Photodetek
filler, amplitude2 = np.genfromtxt('Daten2.txt', unpack = True)
abstand = np.linspace(30, 110, 17)

def g(abstand, e, f):
    return e*(1/abstand**2)+f

params2, filler2 = curve_fit(g, abstand, amplitude2)
uncertainties = np.sqrt(np.diag(filler2))


abstand_plot = np.linspace(abstand[0], abstand[-1], 1000)

print(*params2)
print(*uncertainties)

plt.plot(abstand, amplitude2, '.', label = 'Messwerte')
plt.plot(abstand_plot, g(abstand_plot, *params2), label = 'Regressionkurve')

plt.xlabel(r'$x/cm$')
plt.ylabel(r'$U/V$')

plt.legend()
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
#.savefig('Graph_2.pdf')