import sys
import re
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate
from GUI import Ui_MainWindow  # Asegúrate de que GUI es el módulo que contiene tu diseño

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(0)

        # Conecta los botones a sus respectivas funciones
        self.btn_lista.clicked.connect(self.ir_a_lista)
        self.bt_registrartrabajador.clicked.connect(self.ir_a_form_personal)
        self.btn_personal.clicked.connect(self.validar_inputs)
        self.btn_laboral.clicked.connect(self.validar_form_laboral)
        self.btn_principal.clicked.connect(self.ir_a_inicio)
        self.btn_emergencia.clicked.connect(self.validar_form_emergencia)
        self.pushButton_6.clicked.connect(self.ir_a_form_personal)
        self.pushButton_6.clicked.connect(self.limpiar_campos)  # Conectar el botón para limpiar campos
        self.btn_buscar.clicked.connect(self.ir_a_filtro)
        self.btnAtras1.clicked.connect(self.ir_a_form_personal)
        self.btnAtras1_2.clicked.connect(self.ir_a_laboral)
        self.btn_salir.clicked.connect(self.cerrar_programa)
        

    def cerrar_programa(self):
        QtWidgets.QApplication.quit()

    def ir_a_laboral(self):
        self.stackedWidget.setCurrentIndex(5)

    def ir_a_filtro(self):
        self.stackedWidget.setCurrentIndex(2)

    def ir_a_inicio(self):
        self.stackedWidget.setCurrentIndex(0)

    def ir_a_lista(self):
        self.stackedWidget.setCurrentIndex(1)  # Cambia a la página de la lista en el QStackedWidget

    def ir_a_form_personal(self):
        self.stackedWidget.setCurrentIndex(4)  # Cambia a la página form_personal en el QStackedWidget

    def validar_inputs(self):
        nombre = self.input_nombre.text().strip()
        rut = self.input_rut.text().strip()
        direccion = self.input_dire.text().strip()
        telefono = self.input_tel.text().strip()
        sexo = self.input_sexo.currentText()  # Obtener el texto seleccionado del combo box
        valid = True

        # Validar el campo de nombre
        if len(nombre) == 0:
            self.error_nombre.setText("El nombre no puede estar vacío.")
            valid = False
        elif any(char.isdigit() for char in nombre):
            self.error_nombre.setText("El nombre no puede contener números.")
            valid = False
        else:
            self.error_nombre.setText("")  # Borrar mensaje de error

        # Validar el campo de teléfono
        if len(telefono) == 0:
            self.error_telefono.setText("Ingrese un número de teléfono.")
            valid = False
        elif not telefono.isdigit() or len(telefono) != 9:
            self.error_telefono.setText("El teléfono debe tener 9 dígitos y sin letras.")
            valid = False
        else:
            self.error_telefono.setText("")  # Borrar mensaje de error

        # Validar el campo de RUT
        if len(rut) == 0:
            self.error_rut.setText("Ingrese un RUT.")
            valid = False
        elif not re.match(r"^\d{7,8}-\d{1}$", rut):
            self.error_rut.setText("Formato incorrecto de RUT. Ejemplo: 12345678-9")
            valid = False
        else:
            self.error_rut.setText("")  # Borrar mensaje de error

        # Validar el campo de dirección
        if len(direccion) == 0:
            self.error_dire.setText("Ingrese una dirección.")
            valid = False
        else:
            self.error_dire.setText("")  # Borrar mensaje de error

        # Validar el campo de sexo
        if sexo == "-":
            self.error_sexo.setText("Seleccione un sexo.")
            valid = False
        else:
            self.error_sexo.setText("")  # Borrar mensaje de error

        if valid:
            self.stackedWidget.setCurrentIndex(5)  # Cambiar a la página form_laboral si todo es válido

    def validar_form_laboral(self):
        cargo = self.input_cargo.text().strip()
        departamento = self.input_departamento.text().strip()
        fecha = self.input_fecha.date()
        laboral = self.input_laboral.currentText()  # Obtener el texto seleccionado del combo box
        valid = True

        # Validar el campo de cargo
        if len(cargo) == 0:
            self.error_cargo.setText("Ingrese un cargo.")
            valid = False
        else:
            self.error_cargo.setText("")  # Borrar mensaje de error

        # Validar el campo de departamento
        if len(departamento) == 0:
            self.error_departamento.setText("Ingrese un departamento.")
            valid = False
        else:
            self.error_departamento.setText("")  # Borrar mensaje de error

        # Validar el campo de fecha
        if fecha > QDate.currentDate():
            self.error_fecha.setText("La fecha no puede ser superior a la actual.")
            valid = False
        else:
            self.error_fecha.setText("")  # Borrar mensaje de error

        # Validar el campo de laboral
        if laboral == "-":
            self.error_laboral.setText("Seleccione una opción de contrato laboral.")
            valid = False
        else:
            self.error_laboral.setText("")  # Borrar mensaje de error

        if valid:
            self.stackedWidget.setCurrentIndex(7)  # Cambiar a la página form_emergencia si todo es válido

    def validar_form_emergencia(self):
        telefono_emergencia = self.input_telefonoemergencia.text().strip()
        nombre_emergencia = self.input_nombreemergencia.text().strip()
        parentesco = self.input_parentesco.text().strip()
        valid = True

        # Validar el campo de teléfono de emergencia
        if len(telefono_emergencia) == 0:
            self.error_telefonoemergencia.setText("Ingrese un número de teléfono de emergencia.")
            valid = False
        elif not telefono_emergencia.isdigit() or len(telefono_emergencia) != 9:
            self.error_telefonoemergencia.setText("El teléfono de emergencia debe tener 9 dígitos y sin letras.")
            valid = False
        else:
            self.error_telefonoemergencia.setText("")  # Borrar mensaje de error

        # Validar el campo de nombre de emergencia
        if len(nombre_emergencia) == 0:
            self.error_nombrecontacto.setText("Ingrese un nombre de emergencia.")
            valid = False
        elif any(char.isdigit() for char in nombre_emergencia):
            self.error_nombrecontacto.setText("El nombre de emergencia no puede contener números.")
            valid = False
        else:
            self.error_nombrecontacto.setText("")  # Borrar mensaje de error

        # Validar el campo de parentesco
        if len(parentesco) == 0:
            self.error_parentesco.setText("Ingrese el parentesco.")
            valid = False
        else:
            self.error_parentesco.setText("")  # Borrar mensaje de error

        if valid:
            self.stackedWidget.setCurrentIndex(8)  # Cambiar a la página siguiente si todo es válido

    def limpiar_campos(self):
        # Limpiar campos del formulario personal
        self.input_nombre.clear()
        self.input_rut.clear()
        self.input_dire.clear()
        self.input_tel.clear()
        self.input_sexo.setCurrentIndex(0)
        self.error_nombre.clear()
        self.error_rut.clear()
        self.error_dire.clear()
        self.error_telefono.clear()
        self.error_sexo.clear()

        # Limpiar campos del formulario laboral
        self.input_cargo.clear()
        self.input_departamento.clear()
        self.input_fecha.setDate(QDate.currentDate())
        self.input_laboral.setCurrentIndex(0)
        self.error_cargo.clear()
        self.error_departamento.clear()
        self.error_fecha.clear()
        self.error_laboral.clear()

        # Limpiar campos del formulario de emergencia
        self.input_telefonoemergencia.clear()
        self.input_nombreemergencia.clear()
        self.input_parentesco.clear()
        self.error_telefonoemergencia.clear()
        self.error_nombrecontacto.clear()
        self.error_parentesco.clear()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
