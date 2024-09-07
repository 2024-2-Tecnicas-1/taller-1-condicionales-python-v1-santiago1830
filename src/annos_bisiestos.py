import unittest

def evaluar(anno):
   
    if anno % 4 == 0:
        
        if anno % 100 == 0:
            if anno % 400 == 0:
                return "Año bisiesto"
            else:
                return "No es un año bisiesto"
        else:
            return "Año bisiesto"
    else:
        return "No es un año bisiesto"


if __name__ == '__main__':
    print("Año:", end="")
    anno = int(input())

    respuesta = evaluar(anno)
    print(respuesta)



