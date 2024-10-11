import numpy as np
import matplotlib.pyplot as plt

# Puntos de altitud en pies y las temperaturas correspondientes en grados Fahrenheit
h = np.array([5000, 10000, 15000, 20000])  # Altitudes en pies (ejemplo)
T = np.array([203, 194, 185, 176])  # Temperaturas de ebullición correspondientes en °F (ejemplo)

# Función de interpolación de Lagrange
def interpolacion_lagrange(x_valor, x_datos, y_datos):
    resultado = 0
    n = len(x_datos)
    for i in range(n):
        termino = y_datos[i]
        for j in range(n):
            if i != j:
                termino *= (x_valor - x_datos[j]) / (x_datos[i] - x_datos[j])
        resultado += termino
    return resultado

# Puntos de estimación
altitud_5000m = 16404.2
altitud_LaPaz = 11942.2
altitud_ElAlto = 13615.4

# Crear gráfica
plt.figure(figsize=(8,6))
plt.plot(h, T, 'bo-', label='Datos conocidos')

# Estimar las temperaturas usando la interpolación de Lagrange
T_5000m = interpolacion_lagrange(altitud_5000m, h, T)
plt.plot(altitud_5000m, T_5000m, 'ro', label=f'Estimación a 5000m: {T_5000m:.2f} °F')

T_ElAlto = interpolacion_lagrange(altitud_ElAlto, h, T)
plt.plot(altitud_ElAlto, T_ElAlto, 'go', label=f'Estimación en El Alto: {T_ElAlto:.2f} °F')

T_LaPaz = interpolacion_lagrange(altitud_LaPaz, h, T)
plt.plot(altitud_LaPaz, T_LaPaz, 'mo', label=f'Estimación en La Paz: {T_LaPaz:.2f} °F')

# Configurar títulos y etiquetas
plt.title('Temperatura de Ebullición vs Altitud', fontsize=14)
plt.xlabel('Altitud (pies)', fontsize=12)
plt.ylabel('Temperatura de Ebullición (°F)', fontsize=12)
plt.grid(True)
plt.legend()

# Guardar la gráfica en un archivo PNG
plt.savefig('EstimacionEbullicion.png', dpi=300)

# Mostrar la gráfica
plt.show()
