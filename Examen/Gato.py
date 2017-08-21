import Animales

class gato(Animales.Animal):
    def TomarAgua(self,cantidadagua):
        self.cantidadagua+=cantidadagua
        print('El gato tiene {0} litros de agua'.format(self.cantidadagua))

    def Alimentar(self,tipoalimento,cantidadalimento):
        if(tipoalimento.lower()=='concentrado'):
            self.cantidadalimento+=cantidadalimento
        else:
            print('Solo me alimento de concentrado')
