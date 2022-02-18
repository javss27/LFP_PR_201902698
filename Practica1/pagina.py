from hashlib import new
from typing import List
from jinja2 import Environment, select_autoescape
from jinja2.loaders import FileSystemLoader
from os import startfile

from Token import Token
from Token import Error

class asd:
    def process_file(listaTokens: List[Token], listaErrores: List[Error]):
        env = Environment(loader=FileSystemLoader('plantilla'),
                      autoescape=select_autoescape(['html']))
        template = env.get_template('plantillaReporte.html')
        #para ordenar de mayor a menor
        newlist = sorted(listaTokens, key=lambda x: x.columna, reverse=True)
        #para sacar el mas vendido
        masVendido = newlist[0] 
        #para sacar el menos vendido
        menosVendido = newlist[len(newlist)-1]
        html_file = open('Reporte.html', 'w+', encoding='utf-8')
        #mostrando todo en el HTML
        html_file.write(template.render(tokens = newlist, errs=listaErrores, masVendido = masVendido, menosVendido = menosVendido ))
        html_file.close()
        startfile('Reporte.html')


        