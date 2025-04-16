cant=int(input("Ingrese la cantidad de notas: "))
prom = 0
for i in range(1, cant+1):
    nota= float(input("Ingrese la nota N°{}: ".format(i))) #No usar , en input
    prom += nota
prom /= cant
print("tu promedio es de:", prom)