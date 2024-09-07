def evaluar(peso, estatura, edad):
    
    imc = peso / (estatura ** 2)
    
    
    if imc < 18.5:
        estado = "Bajo peso"
    elif 18.5 <= imc < 24.9:
        estado = "Normal"
    elif 25 <= imc < 29.9:
        estado = "Sobrepeso"
    else:
        estado = "Obesidad"
    
   
    return f"Tu IMC es: {imc:.2f}. Estado: {estado}."

if __name__ == '__main__':
    print("Peso (kg):", end="")
    peso = int(input())
    print("Estatura (m):", end="")
    estatura = float(input())
    print("Edad:", end="")
    edad = int(input())
        
    respuesta = evaluar(peso, estatura, edad)
    print(respuesta)

