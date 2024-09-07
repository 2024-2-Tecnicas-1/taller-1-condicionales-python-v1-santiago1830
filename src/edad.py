import datetime

def evaluar(dia, mes, anno):
    
    fecha_actual = datetime.datetime.now()
    
   
    fecha_nacimiento = datetime.datetime(anno, mes, dia)
    
   
    edad = fecha_actual.year - fecha_nacimiento.year
    
  
    if (fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
        edad -= 1
    
    return f"Tu edad es: {edad} años."

if __name__ == '__main__':
    print("Ingrese su fecha de nacimiento")
    print("Día:", end="")
    dia = int(input())
    print("Mes:", end="")
    mes = int(input())
    print("Año:", end="")
    anno = int(input())
        
    respuesta = evaluar(dia, mes, anno)
    print(respuesta)

