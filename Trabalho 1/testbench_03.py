from package.maths.terms import Ponto

def workspace():
    P1 = Ponto(4, 2)
    P1.model()
    P2 = Ponto(3,5)
    P2.model()
    P2.mudar_x(2)
    P2.mudar_y(-3)
    P2.model()
if __name__ == "__main__":
    workspace()