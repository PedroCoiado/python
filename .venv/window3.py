from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel
import sys

class Window3(QWidget):
    def __init__(self):
        super().__init__()

        # Definir o texto que ira aparecer no título da janela
        self.setWindowTitle("Cadastrar Usuário")
        # Definir a posição e tamanho da janela
        self.setGeometry(10,10,500,400)
        #criar as labels para nome de usuário, email, senha e nivel acess
        self.label_name_user = QLabel("Nome de usuário: ")
        self.label_email = QLabel("E-mail: ")
        self.label_password = QLabel("Senha: ") 
        self.label_nivel_acess = QLabel("Nível de Acesso: ")

        #Criação das LineEdits
        self.edit_name_user = QLineEdit()
        self.edit_password = QLineEdit()

        self.edit_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.edit_email = QLineEdit()
        self.edit_nivel_acess = QLineEdit()

        #Criar o botão
        self.button_cadastrar = QPushButton("Cadastrar")
        self.button_cadastrar.clicked.connect(self.mensage)
        #Criar o layout vertical para organizar os controles
        layout = QVBoxLayout()
        # Adicionar os controles ao layout
        layout.addWidget(self.label_name_user)
        layout.addWidget(self.edit_name_user)

        layout.addWidget(self.label_email)
        layout.addWidget(self.edit_email)

        layout.addWidget(self.label_password)
        layout.addWidget(self.edit_password)

        layout.addWidget(self.label_nivel_acess)
        layout.addWidget(self.edit_nivel_acess)

        layout.addWidget(self.button_cadastrar)

        self.setLayout(layout)
    def mensage(self):
        print(self.edit_name_user.text())
        print(self.edit_email.text())
        print(self.edit_password.text())
        print(self.edit_nivel_acess.text())

app = QApplication(sys.argv)
window = Window3()
window.show()
app.exec_()



