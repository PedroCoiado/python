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
        self.label_name = QLabel("Nome completo: ")
        # Para fazer a formatação o estilo do texto da label, usamos os comando de
        # CSS(Cascade STyle Sheet(Folha de estilo em cascata))
        # com tais as propriedades obtidas:
        # - color -> cor da letra(cor da frente)
        # - font-size -> tamnho da letra, Que pode ser medida em pt(pontos)
        # - font-weight -> peso da fonte(negrito: bold)
        # - text-transform -> altera a altura da caixa(letra):
                # UpperCase -> Maiúscula
                # LowerCAse -> Minúscula
                # Captalize -> Primeira letra de cada palavra Maíuscula
        self.label_name.setStyleSheet("QLabel{color:#440303; font-size:12pt;font-weight:bold;text-transform:upperCase}")


        self.label_email = QLabel("E-Mail: ")
        self.label_cpf = QLabel("CPF: ")
        self.label_sexo = QLabel("Sexo: ")
        self.label_idade = QLabel("Idade:")

        # Adicionar uma caixa de texto
        self.edit_name = QLineEdit()
        # Aplicação do estilo para caixa de texto:
        # backgroud-color -> cor de fundo
        # padding -> margem interna, ou seja, dentro da caixa
        # border-radius -> arredondar os cantos da caixa de texto
        self.edit_name.setStyleSheet("QLineEdit{background-color:#000; color:#fff; padding:10px; border-radius:10px}")
        self.edit_email = QLineEdit()
        self.edit_cpf = QLineEdit()

        # Adicionar combobox
        self.combo_sexo = QComboBox()
        self.combo_idade = QComboBox()

        # Criar uma lista com 2 sexos ou não prefiro dizer
        lst_sexo = [ "----------", "Masculino", "Feminino", "Prefiro não dizer"]
        # Adicionar  a lista a combo_sexo
        self.combo_sexo.addItems(lst_sexo)

        # Criar uma lista para o combo_idade que vai de 16 à 100
        lst_idade = []
        # Para popular a caixa da idade(combobox) da idade com valores 
        # de 16 à 100, estamos usando uma esturuta de 
        # repetição que daz uma contagem 16 à 101 com o comando range.
        # Durante a contagem, cada número é convertido para string,
        # pois a comboBox só aceita lsta de valores em
        # Formato de Texto(string)
        for i in range(16,101):
            lst_idade.append(str(i))
        self.combo_idade.addItems(lst_idade)



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

        layout.addWidget(self.label_email)
        layout.addWidget(self.edit_email)

        layout.addWidget(self.label_cpf)
        layout.addWidget(self.edit_cpf)

        layout.addWidget(self.label_sexo)
        layout.addWidget(self.combo_sexo)
        
        layout.addWidget(self.label_idade)
        layout.addWidget(self.combo_idade)
                                               

        #Adicionar o layout a tela
        self.setLayout(layout)

# Criando um objeto chamado app do QApplication (Responsável por todo o comportamento
# da nossa aplicação). O argumento sys.argv: Informar ao sistema operacional que uma
# aplicação será carregada e estará presente em memória

app = QApplication(sys.argv)
# Inicia a tela, ou seja, carrega a janela em memória
win = Window2()
# exibe a janela em tela
# = Window2 é a classe (class)
win.show()
# O comando app.exec_, executa todos os comandos acima e gerencia o botão de fechar
# para retirar a janela de memória quando for acionado.
app.exec()