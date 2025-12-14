# Programación Orientada a Objetos (POO)
# Ejemplo: Promedio semanal del clima

class ClimaSemanal:
    def __init__(self):
        # Atributo encapsulado (lista de temperaturas)
        self.__temperaturas = []

    # Método para ingresar las temperaturas
    def ingresar_temperaturas(self):
        print("Ingrese las temperaturas de los 7 días de la semana:")
        for i in range(7):
            temp = float(input(f"Día {i+1}: "))
            self.__temperaturas.append(temp)

    # Método para calcular el promedio semanal
    def calcular_promedio(self):
        total = sum(self.__temperaturas)
        promedio = total / len(self.__temperaturas)
        return promedio
    
    # Método para mostrar la lista
    def mostrar_temperaturas(self):
        return self.__temperaturas

# Uso de la clase ClimaSemanal
clima = ClimaSemanal()
clima.ingresar_temperaturas()
promedio = clima.calcular_promedio()

print("\n--- RESULTADOS (POO) ---")
print("Temperaturas ingresadas:", clima.mostrar_temperaturas())
print(f"Promedio semanal: {promedio:.2f} °C")

