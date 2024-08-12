from package.maths.terms import Ponto, SegmentoReta, Circulo, Retangulo, TipoTriangulo, Triangulo

class menu:
    
    def __init__(self):
        self.actions = {
            '1': self.criar,
            '2': self.checar_interferencias,
            '3': exit
        }
        self.criar_actions = {
            '1': self.criar_ponto,
            '2': self.criar_segmento,
            '3': self.criar_circulo,
            '4': self.criar_retangulo,
            '5': self.criar_triangulo
        }
        self.inferencias_actions = {
            '1': self.checar_ponto,
            '2': self.checar_segmento,
            '3': self.checar_circulo,
            '4': self.checar_retangulo,
            '5': self.checar_triangulo
        }
        self.ponto_actions = {
            '1': self.mudar_x,
            '2': self.mudar_y,
            '3': self.statusP
        }
        self.segmento_actions = {
            '1': self.mudar_A,
            '2': self.mudar_B,
            '3': self.verificar_ponto,
            '4': self.statusS
        }
        self.circulo_actions = {
            '1': self.mudar_centro_x,
            '2': self.mudar_centro_y,
            '3': self.ponto_pertence_circulo,
            '4': self.statusC
        }
        self.retangulo_actions = {
            '1': self.mudar_x_retangulo,
            '2': self.mudar_y_retangulo,
            '3': self.ponto_pertence_retangulo,
            '4': self.statusR
        }
        self.triangulo_actions = {
            '1': self.ponto_pertence_triangulo,
            '2': self.statusT
        }
        self.ponto = None
        self.segmento = None
        self.circulo = None
        self.retangulo = None
        self.triangulo = None

    def criar_ponto(self):
        print("----------------------------------------")
        x = float(input("Escolha a posição do eixo x: "))
        y = float(input("Escolha a posição do eixo y: "))
        print("-----------------------------------------")
        P = Ponto(x, y)
        if x >= 0 and y >= 0:
            print("Ponto criado com sucesso")
            self.ponto = P
            print("----------------------------------")
        return self.ponto, self.run()
        
    def criar_segmento(self):
        print("----------------------------------------------------")
        x1 = float(input("Escolha a posição do eixo x do ponto A: "))
        y1 = float(input("Escolha a posição do eixo y do ponto A: "))
        x2 = float(input("Escolha a posição do eixo x do ponto B: "))
        y2 = float(input("Escolha a posição do eixo y do ponto B: "))
        print("----------------------------------------------------")
        S = SegmentoReta(x1, y1, x2, y2)
        if x1 == x2 and y1 == y2:
            print("Não é possível construir o segmento com os pontos no mesmo local")
        elif x1 >= 0 and y1 >= 0 and x2 >= 0 and y2 >= 0:
            print("Segmento de reta criado com sucesso")
            self.segmento = S
        print("-----------------------------------------")
        return self.segmento, self.run()

    def criar_circulo(self):
        print("-------------------------------------------------------------")
        raio = float(input("Escolha o tamanho do raio do círculo: "))
        x = float(input("Escolha a posição do centro em relação ao eixo x: "))
        y = float(input("Escolha a posição do centro em relação ao eixo y: "))
        print("-------------------------------------------------------------")
        C = Circulo(raio, x, y)
        if x >= 0 and y >= 0 and raio >= 0 and raio <= x and raio <= y: 
            print("Círculo criado com sucesso")
            self.circulo = C
        print("----------------------------------")
        return self.circulo, self.run()

    def criar_retangulo(self):
        print("--------------------------------------------------------------")
        b = float(input("Escolha o tamanho da base do retângulo: "))
        h = float(input("Escolha o tamanho da altura do retângulo: "))
        x = float(input("Escolha a posição do centro em relação ao eixo x: "))
        y = float(input("Escolha a posição do centro em relação ao eixo y: "))
        print("---------------------------------------------------------------")
        R = Retangulo(b, h, x, y)
        if b > 0 and b/2 <= y and h > 0 and h/2 <= x:
            print("Retângulo criado com sucesso")
            self.retangulo = R
        print("------------------------------------")
        return self.retangulo, self.run()

    def criar_triangulo(self):
        print("-------------------------------------------------------------------")
        xa = float(input("Escolha a posição do vértice 'a' em relação ao eixo x: "))
        ya = float(input("Escolha a posição do vértice 'a' em relação ao eixo y: "))
        xb = float(input("Escolha a posição do vértice 'b' em relação ao eixo x: "))
        yb = float(input("Escolha a posição do vértice 'b' em relação ao eixo y: "))
        xc = float(input("Escolha a posição do vértice 'c' em relação ao eixo x: "))
        yc = float(input("Escolha a posição do vértice 'c' em relação ao eixo y: "))
        print("--------------------------------------------------------------------")
        T = Triangulo(xa, ya, xb, yb, xc, yc)
        if xa == xb and ya == yb or xa == xc and ya == yc or xb == xc and yb == yc:
            print("Não é possível construir o triângulo com 2 ou mais vértices no mesmo local")
            print("-----------------------------------------------------------------------------")
        elif xa == xb == xc or ya == yb == yc:
            print("Não é possível construir o triângulo")
            print("-------------------------------------------")
        elif xa >= 0 and ya >= 0 and xb >= 0 and yb >= 0 and xc >= 0 and yc >= 0:
            print("Triângulo criado com sucesso")
            self.triangulo = T
        print("-------------------------------------------")
        return self.triangulo, self.run()
    
    def checar_ponto(self):
        if self.ponto is not None:
            while True:
                print("Escolha uma das opções:")
                print("1. Mudar a posição em relação ao eixo x")
                print("2. Mudar a posição em relação ao eixo y")
                print("3. Status do objeto")
                print("4. Voltar")

                option= input("Digite o número da opção desejada: ")
                print("-----------------------------------------------")

                if option.isdigit() and float(option) in range(1, 5):
                    if option == '4':
                        break
                    self.ponto_actions[option]()
                else:
                    print("Opção inválida! Tente novamente.")
                    continue   
        else:
            print("O objeto não foi criado")
        
    def mudar_x(self):
        x = float(input("Insira o valor para incrementar ou diminuir a distancia em relação ao eixo x: "))
        if self.ponto.getx() + x >= 0:
            print("Posição mudada com sucesso")
            print("------------------------------")
            return self.ponto.mudar_x(x)
        else:
            print("O ponto está invadindo outros quadrantes")
            print("----------------------------------------------")

    def mudar_y(self):
        y = float(input("Insira o valor para incrementar ou diminuir a distancia em relação ao eixo y: "))
        if self.ponto.gety() + y >= 0:
            print("Posição mudada com sucesso")
            print("------------------------------")
            return self.ponto.mudar_y(y)
        else:
            print("O ponto está invadindo outros quadrantes")
            print("----------------------------------------------")
    
    def statusP(self):
        return self.ponto.model()
    
    def checar_segmento(self):
        if self.segmento is not None:
            while True:
                print("Escolha uma das opções:")
                print("1. Mudar o ponto A")
                print("2. Mudar o ponto B")
                print("3. Verificar se um ponto pertence a reta")
                print("4. Status")
                print("5. Voltar")

                option= input("Digite o número da opção desejada: ")
                print("------------------------------------------------")

                if option.isdigit() and float(option) in range(1, 6):
                    if option == '5':
                        break
                    self.segmento_actions[option]()
                else:
                    print("Opção inválida! Tente novamente.")
                    continue
        else:
            print("O objeto não foi criado")

    def mudar_A(self):
        x = float(input("Insira o valor para incrementar ou diminuir a distancia do eixo x em relação ao centro do ponto A: "))
        y = float(input("Insira o valor para incrementar ou diminuir a distancia do eixo y em relação ao centro do ponto A: "))
        if self.segmento.getx1() + x >= 0 and self.segmento.gety1() + y >= 0:
            print("Posição mudada com suceso")
            print("----------------------------")
            return self.segmento.MudarA(x, y)
        else:
            print("O segmento de reta está invadindo outros quadrantes")
            print("------------------------------------------------------")

    def mudar_B(self):
        x = float(input("Insira o valor para incrementar ou diminuir a distancia do eixo x em relação ao centro do ponto B: "))
        y = float(input("Insira o valor para incrementar ou diminuir a distancia do eixo y em relação ao centro do ponto B: "))
        if self.segmento.getx2() + x >= 0 and self.segmento.gety2() + y >= 0:
            print("Posição mudada com suceso")
            print("----------------------------")
            return self.segmento.MudarB(x, y)
        else:
            print("O segmento de reta está invadindo outros quadrantes")
            print("------------------------------------------------------")
        

    def verificar_ponto(self):
        x = float(input("Insira o valor da coordenada em relação ao eixo x: "))
        y = float(input("Insira o valor da coordenada em relação ao eixo y: "))
        return self.segmento.VerificarPonto(x, y)
    
    def statusS(self):
        return self.segmento.Model()

    def checar_circulo(self):
        if self.circulo is not None:
            while True:
                print("Escolha uma das opções:")
                print("1. Mudar posição do centro do círculo em relação ao eixo x")
                print("2. Mudar posição do centro do círculo em relação ao eixo y")
                print("3. Verificar se um ponto pertence ao círculo")
                print("4. Status")
                print("5. Voltar")

                option= input("Digite o número da opção desejada: ")
                print("-------------------------------------------------")

                if option.isdigit() and float(option) in range(1, 6):
                    if option == '5':
                        break
                    self.circulo_actions[option]()
                else:
                    print("Opção inválida! Tente novamente.")
                    continue
        else:
            print("O objeto não foi criado")

    def mudar_centro_x(self):
        x = float(input("Insira o valor para incrementar ou diminuir a distancia do eixo x em relação ao centro: "))
        if self.circulo.getx() + x >= 0 and self.circulo.getx() + x > self.circulo.getraio():
            print("Posição mudada com sucesso")
            print("------------------------------")
            return self.circulo.mudar_x_circulo(x)
        else:
            print("O círculo está invadindo outros quadrantes")
            print("---------------------------------------------")

    def mudar_centro_y(self):
        y = float(input("Insira o valor para incrementar ou diminuir a distancia do eixo y em relação ao centro: "))
        if self.circulo.gety() + y >= 0 and self.circulo.gety() + y > self.circulo.getraio():
            print("Posição mudada com sucesso")
            print("------------------------------")
            return self.circulo.mudar_y_circulo(y)
        else:
            print("O círculo está invadindo outros quadrantes")
            print("--------------------------------------------")

    def ponto_pertence_circulo(self):
        x = float(input("Insira o valor da coordenada em relação ao eixo x: "))
        y = float(input("Insira o valor da coordenada em relação ao eixo y: "))
        return self.circulo.PontoPertence_circulo(x, y)
    
    def statusC(self):
        return self.circulo.model()

    def checar_retangulo(self):
        if self.retangulo is not None:
            while True:
                print("Escolha uma das opções:")
                print("1. Mudar posição do centro do retângulo em relação ao eixo x")
                print("2. Mudar posição do centro do retângulo em relação ao eixo y")
                print("3. Verificar se um ponto pertence ao retângulo")
                print("4. Status")
                print("5. Voltar")

                option= input("Digite o número da opção desejada: ")
                print("-----------------------------------------------")

                if option.isdigit() and float(option) in range(1, 6):
                    if option == '5':
                        break
                    self.retangulo_actions[option]()
                else:
                    print("Opção inválida! Tente novamente.")
                    continue
        else:
            print("O objeto não foi criado")

    def mudar_x_retangulo(self):
        x = float(input("Insira o valor para incrementar ou diminuir a distancia do eixo x em relação ao centro: "))
        if self.retangulo.getx() + x >= 0 and self.retangulo.getbase()/2 < self.retangulo.getx() + x:
            print("Posição mudada com sucesso")
            print("------------------------------")
            return self.retangulo.mudar_x_retangulo(x)
        else:
            print("O quadrado está invadindo outros quadrantes")
            print("---------------------------------------------")
        

    def mudar_y_retangulo(self):
        y = float(input("Insira o valor para incrementar ou diminuir a distancia do eixo y em relação ao centro: "))
        if self.retangulo.gety() + y >= 0  and self.retangulo.geth()/2 < self.retangulo.gety() + y:
            print("Posição mudada com sucesso")
            print("------------------------------")
            return self.retangulo.mudar_y_retangulo(y)
        else:
            print("O quadrado está invadindo outros quadrantes")
            print("---------------------------------------------")
        
    def ponto_pertence_retangulo(self):
        x = float(input("Insira o valor da coordenada em relação ao eixo x: "))
        y = float(input("Insira o valor da coordenada em relação ao eixo y: "))
        return self.retangulo.PontoPertence_retangulo(x, y)

    def statusR(self):
        return self.retangulo.model()

    def checar_triangulo(self):
        if self.triangulo is not None:
            while True:
                print("Escolha uma das opções:")
                print("1. Verificar se um ponto pertence ao triângulo")
                print("2. Status")
                print("3. Voltar")

                option= input("Digite o número da opção desejada: ")
                print("----------------------------------------------")

                if option.isdigit() and float(option) in range(1, 4):
                    if option == '3':
                        break
                    self.triangulo_actions[option]()
                else:
                    print("Opção inválida! Tente novamente.")
                    continue
        else:
            print("O objeto não foi criado")

    def ponto_pertence_triangulo(self):
        x = float(input("Insira o valor da coordenada em relação ao eixo x: "))
        y = float(input("Insira o valor da coordenada em relação ao eixo y: "))
        return self.triangulo.PontoPertence_triangulo(x, y)
    
    def statusT(self):
        return self.triangulo.Model()

    def criar(self):
        while True:
            print("Escolha uma das opções:")
            print("1. Ponto")
            print("2. Segmento de reta" )
            print("3. Círculo")
            print("4. Retângulo")
            print("5. Triângulo")
            print("6. Voltar")

            option= input("Digite o número da opção desejada: ")
            print("----------------------------------------------")

            if option.isdigit() and float(option) in range(1, 7):
                if option == '6':
                    break
                self.criar_actions[option]()
            else:
                print("Opção inválida! Tente novamente.")
                continue
        
    def checar_interferencias(self):
        while True:
            print("Escolha uma das opções:")
            print("1. Ponto")
            print("2. Segmento de reta" )
            print("3. Círculo")
            print("4. Retângulo")
            print("5. Triângulo")
            print("6. Voltar")

            option= input("Digite o número da opção desejada: ")
            print("-----------------------------------------------")

            if option.isdigit() and float(option) in range(1, 7):
                if option == '6':
                    break
                self.inferencias_actions[option]()
            else:
                print("Opção inválida! Tente novamente.")
                continue

    def run(self):
        while True:
            print("Escolha uma das opções:")
            print("1. Criar forma geométrica")
            print("2. Verificar intereferência entre as formas geométricas")
            print("3. Sair")

            option= input("Digite o número da opção desejada: ")
            print("----------------------------------------------")

            if option.isdigit() and float(option) in range(1, 4):
                self.actions[option]()
            else:
                print("Opção inválida! Tente novamente.")
                continue