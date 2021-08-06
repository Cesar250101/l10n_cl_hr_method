# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _
from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime
import logging
import requests


_logger = logging.getLogger(__name__)
MONTH_LIST= [('1', 'Enero'),
        ('2', 'Febrero'), ('3', 'Marzo'),
        ('4', 'Abril'), ('5', 'Mayo'),
        ('6', 'Junio'), ('7', 'Julio'),
        ('8', 'Agosto'), ('9', 'Septiembre'),
        ('10', 'Octubre'), ('11', 'Noviembre'),
        ('12', 'Diciembre')]


class Indicadores(models.Model):
    _inherit = 'hr.indicadores'

    tasa_afp_uno = fields.Float('Uno', help="Tasa AFP Uno")
    tasa_sis_uno = fields.Float('SIS', help="Tasa SIS Uno")
    tasa_independiente_uno = fields.Float('SIS', help="Tasa Independientes Uno")


    @api.one
    def update_document(self):
        super(Indicadores, self).update_document()
        self.update_date = datetime.today()
        try:
            html_doc = urlopen('https://www.previred.com/web/previred/indicadores-previsionales').read()
            soup = BeautifulSoup(html_doc, 'html.parser')

            letters = soup.find_all("table")

            def clear_string(cad):
                cad = cad.replace(".", '').replace("$", '').replace(" ", '')
                cad = cad.replace("Renta", '').replace("<", '').replace(">", '')
                cad = cad.replace("=", '').replace("R", '').replace("I", '').replace("%", '')
                cad = cad.replace(",", '.')
                cad = cad.replace("1ff8","")
                return cad
        except ValueError:
            return ""

        def string_divide(cad, cad2, rounded):
            return round(float(cad) / float(cad2), rounded)
        try:
            self.tasa_afp_modelo = clear_string(letters[7].select("strong")[25].get_text())
            self.tasa_sis_modelo = clear_string(letters[7].select("strong")[26].get_text())
        except ValueError:
            return ""
