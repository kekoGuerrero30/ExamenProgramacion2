import datetime
class Animal:
    def __init__(self,reproduccion,cantidadanimales):
        self.AnimalesReproduccion =reproduccion
        self.cantidadAnimales = cantidadanimales
        self.nacimiento = []
        self.fechanacimiento=[]
        self.tipoalimentos=""
        self.cantidadalimentos=0
        self.cantidadagua=0

    def __Nacimiento(self, hembrasprenadas):
        nacidos = (self.AnimalesReproduccion*hembrasprenadas)
        self.CantidadAnimales+=nacidos
        self.fechanacimiento.append(datetime.datetime.today())
        self.nacimiento.append(nacidos)
        print("La cantidad de animales nacidos es {0} ahora tiene {1} animales".frmat(nacidos,self.CantidadAnimales))

    def Reproduccion(self,cantidadanimales):
        if(self.CantidadAnimales>cantidadanimales):
            self.__Nacimiento(cantidadanimales)
        else:
            print("La cantida de animales en reprtoduccion no puede ser mayor a la cantida de animales existentes")

    def Decesos(self,cantidaddecesos):
        self.CantidadAnimales-=cantidaddecesos
        print("La cantidad actual de animales es {0}".format(self.CantidadAnimales))

    def ImprimirTodo(self):
        rango =len(self.nacimiento)
        print("Cantidad\tFecha de nacimiento")
        if(rango>0):
            for elemento in range(rango):
                print("{0}\t\t{1}".format(self.nacimiento[elemento],self.fechanacimiento[elemento]))
        elif(rango==0):
            print("{0}\t\t{1}".format(self.nacimiento[0],self.fechanacimiento[0]))
        else:
            print("No existen partos recientes")
