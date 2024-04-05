import base64

from odoo import models
from odoo.tools.misc import xlsxwriter
from PyPDF2 import PdfFileWriter
import xlsxwriter
import base64
import io


class ArticleListXlsx(models.AbstractModel):
    _name = 'report.product_inherit_views.report_article_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, articles):

        bold = workbook.add_format({'bold': True})
        format1 = workbook.add_format({'font_size': 14, 'align': 'center', 'bold': True})

        for obj in articles:
            sheet = workbook.add_worksheet(obj.name)
            row = 0
            col = 0
            sheet.set_column('B:B', 20)
            sheet.set_column('A:A', 20)

            sheet.merge_range(row, col, row, col + 1, obj.name, format1)
            # sheet.write(row, col, 'Nom de l article : ', bold)
            # sheet.write(row, col + 1, obj.name)
            row += 1
            if obj.image_1920:
                product_image = io.BytesIO(base64.b64decode(obj.image_1920))
                sheet.insert_image(row, col, "image.png", {'image_data': product_image, 'x_scale': 0.3, 'y_scale': 0.3})
                row += 6

            sheet.write(row, col, 'Type d article : ', bold)
            sheet.write(row, col + 1, obj.type)
            # row += 1
            # sheet.write(row, col, 'Catégorie d article : ', bold)
            # sheet.write(row, col + 1, obj.categ_id)
            row += 1
            sheet.write(row, col, 'Coût : ', bold)
            sheet.write(row, col + 1, obj.standard_price)
            row += 1
            sheet.write(row, col, 'Type d article : ', bold)
            sheet.write(row, col + 1, obj.type)
            row += 1
            sheet.write(row, col, 'Prix de vente : ', bold)
            sheet.write(row, col + 1, obj.list_price)
            row += 1
            sheet.write(row, col, 'Quantité en stock : ', bold)
            sheet.write(row, col + 1, obj.qty_available)
            row += 1
            sheet.write(row, col, 'Quantité En Main Non Réservée : ', bold)
            sheet.write(row, col + 1, obj.qty_available_not_res)
            row += 1
            sheet.write(row, col, 'Quantité prévue : ', bold)
            sheet.write(row, col + 1, obj.virtual_available)
            row += 2
            # sheet.write(row, col, 'Unité de mesure : ', bold)
            # sheet.write(row, col + 1, obj.uom_id)
