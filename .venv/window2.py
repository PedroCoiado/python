# Impoera os controles(QtWidgets) para biblioteca gráfica
# PyQt5. Neste exemplo estamos utilizando o comando prompt
# com a opção asterisco(*) que importa todos os controles
# da biblioteca;
from PyQt5.QtWidgets import * 

# Importação da biblioteca de sistema para abrir e fechar a janela que será construida. 
# Ao fechar a janela, também estremos retirando - a da memória;
import sys

# Criação da estrutura geral da nossa janela.
# A janela e seus controles estão sendo criadas de forma agrupada dentro de uma classe
# A classe Window2 está herdando todas as 
# configurações QWidget. Está classe edefine os botões: 
# minimiza, maximizar e fechar. Alem de apresentar um título para a janela;
class Window2(QWidget):
    # init (inicialização) é o start do q?, por exemplo (self)

    # O comando def(definition -> definição) define uma função
    # Neste caso estamos definindo uma função d einicializaço da classe
    # init(__init__). Essa função realiza o start(coloca para funcionar)
    # a classe Window2. Na função __init__ passamos como
    # parâmetro o comando selg que indica a classe que teremos 
    # controles que devme ser usados por ela. Portanto, todo
    # controle que está com o prefixo "self", faz referência a própria
    # classe. Ex.: self.label.name = Qlabel : O qual indica para a classe 
    # Window2 que a Label pára o nome pertence a ela, assim como os demoais controles
    # (label, line edit, setlayout).

    def __init__(self):
        super().__init__()
        #Adicionar um texto ao título da janela

        self.setWindowTitle("Janela de Cadastro")

        # Configurar posição e tamanho 
        # O primeiro valor é a posição x medida em pixel
        # O seguendo valor é a posição y medida em pixel
        # O terceiro valor é a largura(width) medida em pixel
        # O quarto valor é a altura(height) medida em pixel
        self.setGeometry(50,200,500,200)

        # Adicionar uma label a janela
        # Uma label(rótulo) é um texto que é apresentado 
        # em uma janela para indicar o que deve ser feita a frente(geralmente uma caixa de texto).
        # No exemplo abaixo estamos criando uma label para apresentar o texto
        # Nome completo, isso indica ao usuário que ele deve escrever o nome em uma caixa
        # de texto a frente, Geralmente, uma label é usada em combinação uma caixa texto 
        # (QLineEdit)
        self.label_name = QLabel("Nome completo:")

        # Adicionar uma caixa de texto
        self.edit_name = QLineEdit()

        # Adicionar layout para organizar os elementos
        # Estamos usando o gerenciador de layout vertical(QVBoxlayout)
        # ele é utilizado para organizar os controles que irão aparecer na Window2. 
        # O QVBoxlayout foi utilizado par adispor os controles um abaixo do outro.
        # para exibir um ao lado do outro usamos o comando QHBoxLayout.
        layout = QVBoxLayout()
        
        # Para adicionar a label_name e o edit_name ao 
        # organizador(layout) vertical, usamos o comando add (adicionar) Widget(controle). 
        # Assim os controles irão  aparecer um abaixo do outro, pois este organizador é do tipo vertical
        
        layout.addWidget(self.label_name)
        layout.addWidget(self.edit_name)

        #Adicionar o layout a tela
        self.setLayout(layout)

app = QApplication(sys.argv)
win = Window2()
# = Window2 é a classe (class)
win.show() 
app.exec()