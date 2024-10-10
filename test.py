import numpy as np
import matplotlib.pyplot as plt
mu = 0        # Mittelwert
sigma = 400    # Breitere Standardabweichung
max_value = 100  # Maximaler Wert für die Kurvenspitze

# x-Werte erzeugen (von -1000 bis 1000 in 0.1er-Schritten für mehr Datenpunkte)
x_values = np.arange(-1500, 1500, 0.1)

# Berechnung der y-Werte
y_values = max_value * np.exp(-0.5 * ((x_values - mu) / sigma) ** 2)



for values in y_values:
    print(round(values/100, 3))


plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='Breitere Gaußkurve', color='blue')
plt.title('Gaußsche Verteilung (breiter)')
plt.xlabel('x-Werte')
plt.ylabel('y-Werte')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid()
plt.legend()
plt.xlim(-1500, 1500)
plt.ylim(0, max_value + 10)
plt.show()
