n1=float(input("Ingresa numero 1:"))
n2=float(input("Ingresa numero 2:"))
n3=float(input("Ingresa numero 3:"))
prom=(n1 + n2 + n3)/3
prom=round(prom,1) #Round sirve para redondear 
print("El promedio es:",prom)

if prom >= 4:
    print("🎉 Aprobado 🎉")
elif prom >= 3 and prom < 4:
    print("🤕 Examen 🤕")
else: 
    print("💀 Reprobado 💀")