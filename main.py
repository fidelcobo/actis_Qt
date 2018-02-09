from PyQt5 import QtGui, QtWidgets
from actis import Ui_Actis
import xml.dom.minidom as xml
import openpyxl
import csv
import os
from manejo_excel import (rellenar_columna_texto, rellenar_con_lista, rellenar_num_linea, extract_xml, Registro)
import sys
import time
import locale

locale.setlocale(locale.LC_ALL, 'FR')


class Conversor(QtWidgets.QDialog, Ui_Actis):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.sps_gen = True

        self.boton_Si.clicked.connect(self.set_sps)
        self.boton_No.clicked.connect(self.unset_sps)
        self.botonBrowse.clicked.connect(self.browse_file)
        self.boton_OK.clicked.connect(self.procesar_fichero)
        self.boton_Cancel.clicked.connect(self.close)

    def set_sps(self):
        self.sps_gen = True

    def unset_sps(self):
        self.sps_gen = False

    def browse_file(self):
        direct = QtWidgets.QFileDialog.getOpenFileName(self, "Elegir archivo OPS")
        self.fichero_Actis.setText(direct[0])

    def csv_from_excel(self, entrada, salida):

        # VARIANTE CON xlrd. Pone los números de línea en float
        # print(entrada)
        # with xlrd.open_workbook(entrada) as wb:
        #     sh = wb.sheet_by_index(0)  # or wb.sheet_by_name('name_of_the_sheet_here')
        #     with open(salida, 'w', newline='') as f:
        #         c = csv.writer(f, delimiter=';', quoting=csv.QUOTE_MINIMAL)
        #         for r in range(sh.nrows):
        #             c.writerow(sh.row_values(r))
        ok = False
        while not ok:
            try:
                wb = openpyxl.load_workbook(entrada)
                sh = wb.get_active_sheet()  # or wb.sheet_by_name('name_of_the_sheet_here')

                with open(salida, 'w', newline='') as f:
                    c = csv.writer(f, dialect='excel', delimiter=';')
                    for r in sh.rows:
                        c.writerow([cell.value for cell in r])
                ok = True

            except PermissionError:
                QtWidgets.QMessageBox.warning(self, 'Conversión a CSV','Fichero CSV de destino ya abierto \n'
                                                    ' Por favor ciérrelo y pulse Aceptar')


    def procesar_fichero(self):
        file_zip = self.fichero_Actis.text()
        if not file_zip:
            pass
        else:
            carpeta, file_actis = os.path.split(file_zip)
            nombre_proy, ext = file_actis.split('.')
            try:                                                   #  path completo y el nombre de ficha, sin ext
                file = extract_xml(file_zip)  # A partir del nombre del fichero .zip deducimos el nombre del XML
            except:
                QtWidgets.QMessageBox.warning(self, "Error", "Fichero no procesable \n Cerramos el programa")
                return

            """
            Este bloque abre el XML y extrae los campos relevantes para pasarlos a Excel. Están en los
            nodos OIS --> OI
            """
            try:
                fh = xml.parse(file)
            except:
                QtWidgets.QMessageBox.warning(self, "Error", "Fichero no procesable \n Cerramos el programa")
                sys.exit('Cabestro')

            lista_nodos = fh.childNodes
            lis_items = lista_nodos[0].getElementsByTagName('OIS')
            for l in lis_items:
                aux = l.getElementsByTagName('OI')

            # Ahora definimos mediante listas los parámetros fundamentales que pasaremos a un fichero Excel
            code = []  # Códigos
            comment = []  # Comentarios internos
            descrip = []  # Descripción de los ítems
            total = []  # Precios totales. No se usa en Direct
            wpl = []  # Precios WPL
            qty = []  # Cantidades de cada ítem
            add_qty = []  # Cantidades añadidas
            unit = []  # Precios unitarios
            cost_factor = []  # Costes logísticos
            familia = []  # Familia del ítem

            # Rellenamos las listas anteriores extrayendo la información del XML

            for x in aux:
                comment.append('ALU Ref #:{}'.format(nombre_proy))
                code.append(x.getAttribute('Ref'))

            for d in aux:
                descrip.append(d.getAttribute('Caption'))

            for d in aux:
                total.append(d.getAttribute('Total'))

            for d in aux:
                gpl = float(d.getAttribute('SMSPrice'))
                gpl = locale.format('%10.2f', round(gpl, 2))
                wpl.append(gpl)

            for d in aux:
                qty.append(d.getAttribute('QtyCfg'))

            for d in aux:
                add_qty.append(d.getAttribute('QtyAdd'))

            for d in aux:
                familia.append(d.getAttribute('WPL'))

            for x in range(len(total)):
                total[x] = float(total[x])
                qty[x] = int(qty[x])
                add_qty[x] = int(add_qty[x])

            for x in range(len(total)):
                qty[x] = qty[x] + add_qty[x]  # Parece que la cantidad total es la Qty + la AddQty, así que las sumo.
                unit.append(locale.format('%10.2f', (total[x] / qty[x])))

            # Ahora repasamos la lista de artículos y en aquellos con familias de HW ponemos el cost factor

            for i in range(len(familia)):
                if (familia[i].find('AA') != -1) or (familia[i].find('DD') != -1) or (familia[i].find('EE') != -1) or \
                                familia[i] == 'FF13':
                    cost_factor.append('1,8')
                else:
                    cost_factor.append(' ')

            # Reordenamos las listas por orden alfabético de familias

            lis_datos = []
            for i in range(len(total)):
                reg = Registro(code[i], descrip[i], wpl[i], qty[i], unit[i], familia[i], cost_factor[i])
                lis_datos.append(reg)

            lis_datos.sort(key=lambda r: r.fam)  # Aquí se reordena la lista general de datos por orden alfabético de familia

            # Ahora pasamos los datos a cada lista particular

            for i in range(len(lis_datos)):
                code[i] = lis_datos[i].code
                descrip[i] = lis_datos[i].descr
                wpl[i] = lis_datos[i].wpl
                qty[i] = lis_datos[i].qty
                unit[i] = lis_datos[i].unit
                familia[i] = lis_datos[i].fam
                cost_factor[i] = lis_datos[i].c_factor

                # Si se ha elegido, cambimoa SPS 3EY por SPS-GEN

            if self.sps_gen:
                for i in range(len(code)):
                    if code[i].startswith('3EY'):
                        code[i] = 'SPS-GEN'

            # Una vez rellenas las listas con los parámetros deseados, los pasamos a una hoja Excel

            actual_dir = os.path.dirname(__file__)
            filen = os.path.join(actual_dir,
                                 'Template ALU.xlsx')  # Este fichero no se toca. Servirá como modelo. Ubicación FIJA
            sheet = 'BOM'
            libro = openpyxl.load_workbook(filen)
            hoja = libro.get_sheet_by_name(sheet)

            rellenar_num_linea(hoja, len(total))  # Numera las filas sumando 10 a la siguiente

            # Ahora rellenamos las columnas que tienen contenido fijo de texto
            rellenar_columna_texto(hoja, 'Alcatel', 'C', len(total))
            rellenar_columna_texto(hoja, '1', 'H', len(total))
            rellenar_columna_texto(hoja, 'EA', 'L', len(total))
            rellenar_columna_texto(hoja, 'EUR', 'M', len(total))
            rellenar_columna_texto(hoja, 'Fixed', 'N', len(total))

            # Y pasamos la información variable de las listas a nuestra hoja Excel
            rellenar_con_lista(hoja, 'O', wpl)
            rellenar_con_lista(hoja, 'P', wpl)
            rellenar_con_lista(hoja, 'AA', comment)
            rellenar_con_lista(hoja, 'G', descrip)
            rellenar_con_lista(hoja, 'Q', unit)
            rellenar_con_lista(hoja, 'F', code)
            rellenar_con_lista(hoja, 'K', qty)
            rellenar_con_lista(hoja, 'S', cost_factor)

            # Sólo quede salvar la hoja en un fichero de nombre resultado. En la misma carpeta que el XML
            fichero_salida_excel = os.path.join(carpeta, 'resultado.xlsx')
            fichero_salida_csv = os.path.join(carpeta, 'resultado.csv')

            libro.save(fichero_salida_excel)
            self.csv_from_excel(fichero_salida_excel, fichero_salida_csv)
            QtWidgets.QMessageBox.information(self, 'Extractor ACTIS', 'Todo OK \n Tarea terminada')
            return
                # carpeta = os.path.abspath(carpeta)
                # subprocess.call(['explorer', carpeta])


def main():
    app = QtWidgets.QApplication(sys.argv)  # A new instance of QApplication
    splash_im = QtGui.QPixmap('G:/python/Curso Qt Designer/Parte 2/actis_Qt/aviso.jpg')
    spl_scr = QtWidgets.QSplashScreen(splash_im)
    spl_scr.show()
    progr = Conversor()  # We set the form to be our ExampleApp (design)
    time.sleep(1)
    spl_scr.hide()
    progr.show()  # Show the form
    app.exec_()  # and execute the app


if __name__ == '__main__':  # if we're running file directly and not importing it
    main()  # run the main function
