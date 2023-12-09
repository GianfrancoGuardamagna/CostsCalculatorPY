import matplotlib.pyplot as plt

varHogar = float(820)
varSuper = float(273.67 + 119.87)
varTransporte = float(218.6 + 23.90)
varComida_afuera = float(120.37 + 24.75)
varTurismo_entradas = float(66.5)
varGastos_varios = float(28.2 + 25.63 + 11.97)
varSalud = float(64.5)

varGastos = [varHogar, varSuper, varTransporte, varComida_afuera, varTurismo_entradas, varGastos_varios]

gastos = ["Hogar","Super","Transporte","Comida en la calle","Turismo y entradas","Gastos Varios"]

diccionario = {}

for value,key in zip(varGastos,gastos):
    porcentaje = (value * 100) / (sum(varGastos))
    diccionario[key] = porcentaje

plt.bar(diccionario.keys(), diccionario.values(), color='blue')

plt.xlabel('Categorías de Gastos')
plt.ylabel('Porcentaje del Gasto Total')
plt.title(f"(Total del gasto mensual: {sum(varGastos)} euros.)")

plt.show()