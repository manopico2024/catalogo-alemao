from PyQt5 import QtCore, QtGui, QtWidgets


class Funcoes_dos_botoes():
    def botao_cadastrar(self):
        print("Botão pressionado!!")


class Ui_root(object):
    def setupUi(self, root):
        root.setObjectName("root")
        root.setFixedSize(313, 339)
        root.setStyleSheet("background-color: rgb(40, 135, 119);")

        # Central Widget
        self.centralwidget = QtWidgets.QWidget(root)
        self.centralwidget.setObjectName("centralwidget")
        root.setCentralWidget(self.centralwidget)

        # Top Frame
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 313, 60))
        self.frame.setStyleSheet("background-color: rgb(71, 231, 146);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setObjectName("frame")

        # Title Label
        self.label_title = QtWidgets.QLabel(self.frame)
        self.label_title.setGeometry(QtCore.QRect(20, 15, 150, 30))
        self.label_title.setObjectName("label_title")
        self.label_title.setText("<span style='font-size:19pt;'>Catálogo</span>")

        # Form Fields and Labels
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(10, 80, 71, 21))
        self.label_name.setObjectName("label_name")
        self.label_name.setText("<span style='font-size:16pt; font-weight:600; color:#ffffff;'>Nome:</span>")

        self.entry_name = QtWidgets.QLineEdit(self.centralwidget)
        self.entry_name.setGeometry(QtCore.QRect(90, 85, 211, 25))
        self.entry_name.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entry_name.setObjectName("entry_name")

        self.label_login = QtWidgets.QLabel(self.centralwidget)
        self.label_login.setGeometry(QtCore.QRect(10, 120, 81, 31))
        self.label_login.setObjectName("label_login")
        self.label_login.setText("<span style='font-size:16pt; font-weight:600; color:#ffffff;'>Login:</span>")

        self.entry_login = QtWidgets.QLineEdit(self.centralwidget)
        self.entry_login.setGeometry(QtCore.QRect(90, 125, 211, 25))
        self.entry_login.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entry_login.setObjectName("entry_login")

        # Cadastrar Button
        self.button_cadastrar = QtWidgets.QPushButton(self.centralwidget)
        self.button_cadastrar.setGeometry(QtCore.QRect(110, 200, 100, 35))
        self.button_cadastrar.setObjectName("button_cadastrar")
        self.button_cadastrar.setStyleSheet("background-color: rgb(255, 255, 255); font-weight: bold;")
        self.button_cadastrar.setText("Cadastrar")

        # Instância da classe Funcoes_dos_botoes
        self.funcoes_botoes = Funcoes_dos_botoes()

        # Connect Button to Method
        self.button_cadastrar.clicked.connect(self.on_button_cadastrar_clicked)
        self.button_cadastrar.clicked.connect(self.funcoes_botoes.botao_cadastrar)

    def on_button_cadastrar_clicked(self):
        # Retrieve values from input fields
        name = self.entry_name.text()
        login = self.entry_login.text()

        # Validate input fields
        if not name or not login:
            QtWidgets.QMessageBox.warning(None, "Erro", "Por favor, preencha todos os campos!")
            return

        # Generate a .txt file
        try:
            with open("dados_cadastrados.txt", "a", encoding="utf-8") as file:
                file.write(f"Nome: {name}\nLogin: {login}\n")

            QtWidgets.QMessageBox.information(None, "Sucesso", "Dados salvos no arquivo 'dados_cadastrados.txt'.")
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Erro", f"Erro ao salvar o arquivo: {e}")


# Main execution
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    root = QtWidgets.QMainWindow()
    ui = Ui_root()
    ui.setupUi(root)
    root.show()
    sys.exit(app.exec_())
