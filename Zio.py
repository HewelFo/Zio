from io import open
from datetime import datetime

hora = datetime.now()
order = " yuju"
take = hora.strftime("%d/%m/%Y")
#take = "%s/%s/%s " % (hora.day, hora.month, hora.year)
def InsertTask(order):
    wo = open('test.txt','a')    
    oracion = take + order
    wo.write(oracion)
    wo.close()
    
def Deplet():
    #lectura del archivo
    arch = open('test.txt','r')
    # toma el dia actal
    Dnow = int(hora.strftime("%d"))
    #Mnow = int(hora.strftime("%m"))
    #crea una lista de con las lineas del archivo
    lis = arch.readlines()
    # el for evalua cada una de las lineas
    #cuando encuentra que una tarea tiene mas de un mes la elemina 
    for le in range(len(lis)):
        prub = lis.read(2)
        if prub - Dnow > 0:
            lis.pop(le)
    #vuelve a guardar el archivo con la o las lisas eliminadas
    arch.writelines(lis)
    arch.close()
    

