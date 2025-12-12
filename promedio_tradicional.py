# Programación Tradicional
# Ejemplo: Promedio semanal del clima

# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    print("Ingrese las temperaturas de los 7 días de la semana:")
    
    for i in range(7):
        temp = float(input(f"Día {i+1}: "))
        temperaturas.append(temp)
    
    return temperaturas

# Función para calcular el promedio de la semana
def calcular_promedio(temps):
    total = sum(temps)
    promedio = total / len(temps)
    return promedio

# Programa principal usando programación tradicional
temperaturas_semana = ingresar_temperaturas()
promedio = calcular_promedio(temperaturas_semana)

print("\n--- RESULTADOS (Programación Tradicional) ---")
print("Temperaturas ingresadas:", temperaturas_semana)
print(f"Promedio semanal: {promedio:.2f} °C")
