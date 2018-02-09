import zipfile
import os


class Registro():

    def __init__(self, code, descr, wpl, qty, unit, fam, c_factor ):
        self.code = code
        self.descr = descr
        self.wpl = wpl
        self.qty = qty
        self.unit = unit
        self.fam = fam
        self.c_factor = c_factor


def rellenar_columna_texto(hoja, text, col, leng):
    for i in range(2, leng+2):
        nom_cell = col+str(i)
        hoja[nom_cell] = text


def rellenar_con_lista(hoja, columna, lista):
    i=2
    for l in lista:
        nom_cell=columna+str(i)
        hoja[nom_cell] = l
        i = i+1


def rellenar_num_linea(sheet, ln):
    value = 10
    for i in range(2,ln+2):
        nom_cell = 'A'+str(i)
        sheet[nom_cell] = value
        value= value+10


def extract_xml(filein):
    # Extrae el fichero XML de dentro del .zip y lo coloca en el mismo directorio. Además devuelve el path del XML
    dir, fil = os.path.split(filein)
    nom_fich, ext = fil.split('.')
    nom_fich = nom_fich[4:12] + '.XML'
    fh = zipfile.ZipFile(filein)
    fh.extract(nom_fich, dir)
    return os.path.join(dir, nom_fich)


