from package.maths.terms import Ponto, SegmentoReta, Circulo, Retangulo, TipoTriangulo, Triangulo
from package.maths.controler import menu

def workspace():
    r = menu()
    r.run()

if __name__ == "__main__":
    workspace()