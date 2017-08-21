import Conejo
import Elefante
import Gato

def ConstruirConejo(CantidadReproduccion,CantidadAnimales):
    c=Conejo.conejo(CantidadReproduccion,CantidadAnimales)
    return c

def ConstruirElefante(CantidadReproduccion,CantidadAnimales):
    e=Elefante.elefante(CantidadReproduccion,CantidadAnimales)
    return e

def ConstruirGato(CantidadReproduccion,CantidadAnimales):
    g=Gato.gato(CantidadReproduccion,CantidadAnimales)
    return g

def ImprimirMenu():
    print('1 Agregar Nuevo Animal\n2 Animal pregnados\n3 Alimentar Animales\n4 Dar de beber')
    print('5 Salir')
    accion= int(input('Ingrese el numero de la accion que desea hacer '))
    return accion

def ImprimirAnimales():
    print('1 Conejo\n2 Elefante\n3 Gato')
    accion=int(input('Ingrese el numero de la accion que desea hacer '))
    return accion

conejoconstruido=False
elefanteconstruido=False
gatoconstruido=False
salir=False

while not salir:
    accion=ImprimirMenu()
    if(accion==1):
        tipoanimal=ImprimirAnimales()
        if(tipoanimal==1):
            cantidadanimales=int(input('Ingrese la cantidad de conejos que tiene '))
            cantidadreproduccion=int(input('Ingrese la cantidad de animales por parto que puede tener un conejo '))
            conejoconstruido=ConstruirConejo(cantidadreproduccion,cantidadanimales)
        elif(tipoanimal==2):
            cantidadanimales=int(input('Ingrese la cantida de elefantes que tiene '))
            cantidadreproduccion=int(input('Ingrese la cantidad de animales por parto que puede tener un elefante '))
            elefanteconstruido=ConstruirElefante(cantidadreproduccion,cantidadanimales)
        elif(tipoanimal==3):
            cantidadanimales=int(input('Ingrese la cantida de gatos que tiene '))
            cantidadreproduccion=int(input('Ingrese la cantidad de animales por parto que puede tener un gato '))
            gatoconstruido=ConstruirGato(cantidadreproduccion,cantidadanimales)
        else:
            print('El comando ingresado no se reconoce')
    elif(accion==2):
        tipoanimal=ImprimirAnimales()
        if(tipoanimal==1):
            if(conejoconstruido!=False):
                cantidadanimalespreniados=int(input('Ingrese la cantida de animales pregnados '))
                conejosconstruido.Reproduccion(cantidadanimalespreniados)
            else:
                print('No tiene conejos en su granja')
        elif(tipoanimal==2):
            if(elefanteconstruido!=False):
                cantidadanimalespreniados=int(input('Ingrese la cantida de animales pregnados '))
                elefanteconstruido.Reproduccion(cantidadanimalespreniados)
            else:
                print('No tiene elefantes en su granja')
        elif(tipoanimal==3):
            if(gatoconstruido!=False):
                cantidadanimalespreniados=int(input('Ingrese la cantida de animales pregnados '))
                Gatoconstruido.Reproduccion(cantidadanimalespreniados)
            else:
                print('No tiene gatos en su granja')
    elif(accion==3):
        tipoanimal=ImprimirAnimales()
        if(tipoanimal==1):
            if(conejoconstruido!=False):
                tipoalimento=input('Ingrese el tipo de alimento que da a los conejos ')
                cantidadalimento=int(input('Ingrese la cantidad de alimento '))
                conejoconstruido.Alimentar(tipoalimento,cantidadalimento)
            else:
                print('No tiene conejos en su granja')
        elif(tipoanimal==2):
            if(elefanteconstruido!=False):
                tipoalimento=input('Ingrese el tipo de alimento que da a los elefantes ')
                cantidadalimento=int(input('Ingrese la cantidad de alimento '))
                elefanteconstruido.Alimentar(tipoalimento,cantidadalimento)
            else:
                print('No tiene elefantes en su granja')
        elif(tipoanimal==3):
            if(gatoconstruido!=False):
                tipoalimento=input('Ingrese el tipo de alimento que da a los gatos ')
                cantidadalimento=int(input('Ingrese la cantidad de alimento '))
                gatoconstruido.Alimentar(tipoalimento,cantidadalimento)
            else:
                print('No tiene gatos en su granja')
        else:
            print('No se reconoce el comando ingresado')
    elif(accion==4):
        tipoanimal=ImprimirAnimales()
        if(tipoanimal==1):
            if(conejoconstruido!=False):
                print("No puede dar de beber a los conejos")
            else:
                print("No tiene conejos en su granja")
        elif(tipoanimal==2):
            if(elefanteconstruido!=False):
                cantidadagua=int(input("Ingrese la cantidad de agua para los elefantes"))
                elefanteconstruido.TomarAgua(cantidadagua)
            else:
                print("No tiene elefantes para su graja")
        elif(tipoanimal==3):
            if(gatoconstruido!=False):
                cantidadagua=int(input("Ingrese la cantidad de agua para los gatos"))
                gatoconstruido.TomarAgua(cantidadagua)
            else:
                print("No tiene gatos para su graja")
        else:
            print("Como ingresado desconocido")
    elif(accion==5):
        salir=True
    else:
        print("El comando ingresado no se reconoce")
