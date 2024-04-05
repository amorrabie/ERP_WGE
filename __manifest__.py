# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Custom Product Model',
    'version': '1.1',
    'summary': """""",
    'sequence': 10,
    'author': 'BMG Tech',
    'description': "Modules BMG Technologies Stock",
    'category': 'Accounting/Accounting',
    'website': 'www.bmgtech.tn',
    'website': 'https://www.odoo.com/page/billing',
    'depends': ['base', 'product', 'mrp', 'stock', 'BMG_sale_starter', 'sale', 'report_xlsx', ],
    'data': [
        'report/report.xml',
        'views/artical_view_custom.xml',
        'views/product.xml',
        'views/nomenclature_custom.xml'

    ],
    'demo': [

    ],
    'qweb': [

    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
