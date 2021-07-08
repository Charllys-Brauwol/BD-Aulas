import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel

#Criação da Classe Principal

class Janela(QMainWindow):
    def __init__(self):
        super().__init__()

        self.topo = 200
        self.esquerda = 200
        self.largura = 500
        self.altura = 500
        self.titulo = "linguagens"
        #Criação do Botão
        bt1 = QPushButton("python", self)
        bt1.move(250, 250)
        bt1.resize(100, 50)
        bt1.setStyleSheet('QPushButton {background-color:#0FB329; font-size:10px}')
        bt1.clicked.connect(self.bt1_click)

        bt2 = QPushButton("Java", self)
        bt2.move(300, 300)
        bt2.resize(100, 50)
        bt2.setStyleSheet('QPushButton {background-color:#0FB329; font-size:10px}')
        bt2.clicked.connect(self.bt2_click)

         # ---> Criação a Label
        self.label_1 = QLabel(self)
        self.label_1.setText("Olá Mundo")
        self.label_1.move(320, 220)
        self.label_1.setStyleSheet("QLabel {color:red; font-size:25px}")
        self.label_1.resize(200, 25)


        self.CarregarJanela()

    def CarregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()
    
    def bt1_click(self):        
        self.label_1.setStyleSheet("QLabel {color:blue; font-size:25px}")
        self.label_1.setText("Botão 1 clicado")

    def bt2_click(self):
        self.label_1.setStyleSheet("QLabel {color:pink; font-size:25px}")
        self.label_1.setText("Botão 2 clicado")

app = QApplication(sys.argv)
j = Janela()
sys.exit(app.exec_())