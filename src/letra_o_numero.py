def evaluar(caracter):
    
    if '0' <= caracter <= '9':
        return f"El carácter '{caracter}' es un número."
    
    elif ('a' <= caracter <= 'z') or ('A' <= caracter <= 'Z'):
        return f"El carácter '{caracter}' es una letra."
   
    else:
        return f"El carácter '{caracter}' no es ni una letra ni un número."

if __name__ == '__main__':
    print("Caracter:", end='')
    caracter = input()
        
    respuesta = evaluar(caracter)
    print(respuesta)
