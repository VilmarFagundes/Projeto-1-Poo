from math import pi, sqrt
import warnings

class Ponto():
    
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.setx(x)
        self.sety(y)

    def mudar_x(self, X):
        if self.__x + X < 0:
            warnings.warn("O ponto deve estar no primeiro quadrante")
        else:
            self.__x += X

    def mudar_y(self, Y):
        if self.__y + Y < 0:
            warnings.warn("O ponto deve estar no primeiro quadrante")
        else: 
            self.__y += Y
    
    def Distancia_centro(self):
        DC = sqrt(self.__x**2 + self.__y**2)
        return DC
        
    def setx(self, x):
        if x < 0:
            warnings.warn("O ponto deve estar no primeiro quadrante")
        else: 
            self.__x = x

    def getx(self):
        return self.__x
        
    def sety(self, y):
        if y < 0:
            warnings.warn("O ponto deve estar no primeiro quadrante")
        else: 
            self.__y = y
        
    def gety(self):
        return self.__y
    
    def model(self):
        print(f'---------------------------------------------------------------------')
        print(f'O ponto esta no local: ({self.__x};{self.__y})')
        print(f'Distância do centro: {self.Distancia_centro():.2f}')
        print(f'---------------------------------------------------------------------')    

class SegmentoReta():

    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        self.setx1(x1)
        self.sety1(y1)
        self.setx2(x2)
        self.sety2(y2)

    def TamanhoReta(self):
        D = sqrt((self.__x2 - self.__x1)**2 + (self.__y2 - self.__y1)**2)
        return D
    
    def DistanciaCentroA(self):
        A = sqrt(self.__x1**2 + self.__y1**2)
        return A
    
    def DistanciaCentroB(self):
        B = sqrt(self.__x2**2 + self.__y2**2)
        return B
    
    def MudarA(self, X,Y):
        if self.__x1 + X < 0:
            warnings.warn("O ponto deve estar no primeiro quadrante")
        else: 
            self.__x1 += X
        if self.__y1 + Y < 0:
            warnings.warn("O ponto deve estar no primeiro quadrante")
        else:
            self.__y1 += Y

    def MudarB(self, X,Y):
        if self.__x2 + X < 0:
            warnings.warn("O ponto deve estar no primeiro quadrante")
        else:
            self.__x2 += X
        if self.__y2 + Y < 0:
            warnings.warn("O ponto deve estar no primeiro quadrante")
        else:
            self.__y2 += Y

    def VerificarPonto(self, a, b):
        if (self.getx1() * self.gety2()) + (self.gety1() * a) + (self.getx2() * b) - (self.gety2() * a) - (self.getx1() * b) - (self.getx2() * self.gety1()) == 0:
            return print(f'O ponto ({a},{b}) pertence ao segmento de reta')
        else:
            return print(f'O ponto ({a},{b}) não pertence ao segmento de reta')

    def Model(self):
        print(f'---------------------------------------------------------------------')
        print(f'O segmento de reta possui:')
        print(f'Ponto A: ({self.getx1()},{self.gety1()}). E ponto B: ({self.getx2()},{self.gety2()}).')
        print(f'Seu tamanho é: {self.TamanhoReta():.2f}')
        print(f'A distância do ponto A do centro é: {self.DistanciaCentroA():.2f}')
        print(f'A distância do ponto B do centro é: {self.DistanciaCentroB():.2f}')
        print(f'---------------------------------------------------------------------')

    def setx1(self, x1):
        if x1 < 0:
            warnings.warn("O ponto deve estar no primeiro quadrante")
        else:
            self.__x1 = x1

    def getx1(self):
        return self.__x1
        
    def sety1(self, y1):
        if y1 < 0:
            warnings.warn("O ponto deve estar no primeiro quadrante")
        else:
            self.__y1 = y1
        
    def gety1(self):
        return self.__y1
    
    def setx2(self, x2):
        if x2 < 0:
            warnings.warn("O ponto deve estar no primeiro quadrante")
        else:
            self.__x2 = x2

    def getx2(self):
        return self.__x2
        
    def sety2(self, y2):
        if y2 < 0:
            warnings.warn("O ponto deve estar no primeiro quadrante")
        else:
            self.__y2 = y2
        
    def gety2(self):
        return self.__y2 

class Circulo(Ponto):

    def __init__(self, raio, x, y):
        super().__init__(x, y)
        self.__raio = raio
        self.setRaio(raio)

    def Circunferencia(self):
        C = 2*pi*self.getraio()
        return C
    
    def Area(self):
        A = pi*self.getraio()**2
        return A
    
    def Diametro(self):
        D = 2*self.getraio()
        return D
    
    def PontoPertence_circulo(self, a, b):
        if sqrt((self.getx() - a)**2 + (self.gety() - b)**2) == self.getraio():
            return print(f'O ponto ({a},{b}) pertence a circulo')
        elif sqrt((self.getx() - a)**2 + (self.gety() - b)**2) <= self.getraio():
            return print(f'O ponto ({a},{b}) pertence ao domínio restrito do circulo')
        else:
            return print(f'O ponto ({a},{b}) não pertence a circulo')

    def Distancia_centro(self):
        return super().Distancia_centro()
    
    def mudar_x_circulo(self, X):
        return super().mudar_x(X)
    
    def mudar_y_circulo(self, Y):
        return super().mudar_y(Y)
    
    def model(self):
        print(f'---------------------------------------------------------------------')
        print(f'O círculo possui:')
        print(f'raio: {self.getraio()}')
        print(f'Circunferencia: {self.Circunferencia():.2f}')
        print(f'Área: {self.Area():.2f}')
        print(f'Diâmetro: {self.Diametro()}')
        print(f'Coordenadas do centro: ({self.getx()}, {self.gety()})')
        print(f'Distância do centro: {self.Distancia_centro():.2f}')
        print(f'---------------------------------------------------------------------')

    def getraio(self):
        return self.__raio

    def setRaio(self, raio):
        if raio < 0:
            warnings.warn("O raio deve ser maior que zero.")
        elif raio > self.getx():
            warnings.warn("O círculo esta invadindo os outros quadrantes.")
        elif raio > self.gety():
            warnings.warn("O círculo esta invadindo os outros quadrantes.")
        else:
            self.__raio = raio
    
class Retangulo(Ponto):

    def __init__(self, b, h, x=0, y=0):
        super().__init__(x, y)
        self._b = b
        self._h = h
        self.setbase(b)
        self.seth(h) 
    
    def Area(self):
        A = self._b*self._h 
        return A
    
    def Perimetro(self):
        P = 2*(self._b + self._h)
        return P
    
    def Diagonal(self):
        D = sqrt(self._b**2 + self._h**2)
        return D
    
    def mudar_x_retangulo(self, X):
        return super().mudar_x(X)
    
    def mudar_y_retangulo(self, Y):
        return super().mudar_y(Y)
    
    def PontoPertence_retangulo(self, a, b):
        if a == self.getx() - (self.getbase()/2) or a == self.getx() + (self.getbase()/2) and b >= self.gety() - (self.geth()/2) and b <= self.gety() + (self.geth()/2):
            return print(f'O ponto ({a}, {b}) pertence ao retângulo')
        elif b == self.gety() - (self.geth()/2) or b == self.gety() + (self.geth()/2) and a >= self.getx() - (self.getbase()/2) and a <= self.getx() + (self.getbase()/2):
            return print(f'O ponto ({a}, {b}) pertence ao retângulo')
        elif a > self.getx() - (self.getbase()/2) and a < self.getx() + (self.getbase()/2) and b >= self.gety() - (self.geth()/2) and b <= self.gety() + (self.geth()/2):
            return print(f'O ponto ({a}, {b}) pertence ao domínio restrito do retângulo')
        else:
            return print(f'O ponto ({a}, {b}) não pertence ao retângulo')
    
    def Distancia_centro(self):
        DC = sqrt((self.getx() + self._b / 2)**2 + (self.gety() + self._h / 2)**2)
        return DC
    
    def model(self):
        print(f'---------------------------------------------------------------------')
        print(f'O retangulo possui:')
        print(f'Base: {self._b:.2f}')
        print(f'Altura: {self._h:.2f}')
        print(f'Area: {self.Area():.2f}')
        print(f'Perimetro: {self.Perimetro():.2f}')
        print(f'Diagonal: {self.Diagonal():.2f}')
        print(f'Coordenadas do centro: ({self.getx()}, {self.gety()})')
        print(f'Distancia do centro: {self.Distancia_centro():.2f}')
        print(f'---------------------------------------------------------------------')

    def getbase(self):
        return self.__b

    def setbase(self, b):
        if b <= 0:
            warnings.warn("A base deve ser maior que zero.")
        elif b/2 >= self.gety():
            warnings.warn("O retangulo esta invadindo os outros quadrantes.")
        else:
            self.__b = b

    def geth(self):
        return self.__h

    def seth(self, h):
        if h <= 0:
            warnings.warn("A altura deve ser maior que zero.")
        elif h/2 >= self.getx():
            warnings.warn("O retangulo esta invadindo os outros quadrantes.")
        else:
            self.__h = h

class TipoTriangulo(SegmentoReta):
    def __init__(self, xa, ya, xb, yb, xc, yc): #pontos de cada vertice
        super().__init__(xa, ya, xb, yb)
        self.__xc = xc
        self.__yc = yc
        self.__base = self.TamanhoReta()
        self.__lado1 = sqrt((self.__xc - self.getx1())**2 + (self.__yc - self.gety1())**2)
        self.__lado2 = sqrt((self.__xc - self.getx2())**2 + (self.__yc - self.gety2())**2)
        self.__tipo = self.Classificar_triangulo()
        self.setxa(xa)
        self.setya(ya)
        self.setxb(xb)
        self.setyb(yb)
        self.setxc(xc)
        self.setyc(yc)
        
    def Classificar_triangulo(self):
        if self.__lado1 == self.__lado2 and self.__base != self.__lado1:
            return 'Triângulo isósceles'
        elif self.__base == self.__lado1 == self.__lado2:
            return 'Triângulo equilatero'
        elif self.__base**2 == self.__lado1**2 + self.__lado2**2 or self.__lado1**2 == self.__base**2 + self.__lado2**2 or self.__lado2**2 == self.__base**2 + self.__lado1**2:
            return 'Triângulo retangulo'
        else:
            return 'Triângulo escaleno'
        
    def setxa(self, xa):
        if xa < 0:
            warnings.warn("O ponto deve estar no primeiro quadrante")
        else:
            self.__xa = xa

    def getxa(self):
        return self.__xa
        
    def setya(self, ya):
        if ya < 0:
            warnings.warn("O ponto deve estar no primeiro quadrante")
        else:
            self.__ya = ya
        
    def getya(self):
        return self.__ya
    
    def setxb(self, xb):
        if xb < 0:
            warnings.warn("O ponto deve estar no primeiro quadrante")
        else:
            self.__xb = xb

    def getxb(self):
        return self.__xb
        
    def setyb(self, yb):
        if yb < 0:
            warnings.warn("O ponto deve estar no primeiro quadrante")
        else:
            self.__yb = yb
        
    def getyb(self):
        return self.__yb
        
    def setxc(self, xc):
        if xc < 0:
            warnings.warn("O ponto deve estar no primeiro quadrante")
        else:
            self.__xc = xc

    def getxc(self):
        return self.__xc
        
    def setyc(self, yc):
        if yc < 0:
            warnings.warn("O ponto deve estar no primeiro quadrante")
        else:
            self.__yc = yc
        
    def getyc(self):
        return self.__yc

    def getTipo(self):
        return self.__tipo
            
    def getBase(self):
        return self.__base
    
    def getLado1(self):
        return self.__lado1
    
    def getLado2(self):
        return self.__lado2

class Triangulo(TipoTriangulo):

    def __init__(self, xa, ya, xb, yb, xc, yc): #pontos de cada vertice
        super().__init__(xa, ya, xb, yb, xc, yc)
        self.getTipo()
    
    def Perimetro(self):
        return self.getBase() + self.getLado1() + self.getLado2()

    def Area(self):
        s = (self.getBase() + self.getLado1() + self.getLado2()) / 2
        area = sqrt(s * (s - self.getBase()) * (s - self.getLado1()) * (s - self.getLado2()))
        return area
    
    def Altura(self):
        area = self.Area()
        h = ( 2* area)/self.getBase()
        return h
    
    def PontoPertence_triangulo(self, a, b):
        if (self.getxa() * self.getyb()) + (self.getya() * a) + (self.getxb() * b) - (self.getyb() * a) - (self.getxa() * b) - (self.getxb() * self.getya()) == 0:
            return print(f'O ponto ({a},{b}) pertence ao triângulo')
        elif (self.getxb() * self.getyc()) + (self.getyb() * a) + (self.getxc() * b) - (self.getyc() * a) - (self.getxb() * b) - (self.getxc() * self.getyb()) == 0:
            return print(f'O ponto ({a},{b}) pertence ao triângulo')
        elif (self.getxa() * self.getyc()) + (self.getya() * a) + (self.getxc() * b) - (self.getyc() * a) - (self.getxa() * b) - (self.getxc() * self.getya()) == 0:
            return print(f'O ponto ({a},{b}) pertence ao triângulo')
        else:
            return print(f'O ponto ({a},{b}) não pertence ao triângulo')

    def Model(self):
        print(f'---------------------------------------------------------------------')
        print(f'O triângulo é do tipo: {self.getTipo()}')
        print(f'Possui base : {self.getBase():.2f}. E lados: {self.getLado1():.2f} e {self.getLado2():.2f}')
        print(f'Altura: {self.Altura():.2f}')
        print(f'Perímetro: {self.Perimetro():.2f}')
        print(f'Área: {self.Area():.2f}')
        print(f'---------------------------------------------------------------------')