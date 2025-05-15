# -*- coding: utf-8 -*-
{
    'name': "Resumen de Productos por Lote",

    'summary': """
        Este modulo simplemente permite ver un resumen de los productos por lote""",

    'description': """
        Este modulo simplemente permite ver un resumen de los productos por lote
        en la vista de lote de entrega. Se agrega un boton que abre un wizard
        mostrando un resumen de los productos en el lote, incluyendo nombre,
        referencia, unidad y cantidad. El resumen se muestra en una tabla
        con los productos agrupados por nombre y sumando las cantidades.
    """,

    'author': "GonzaOdoo",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['stock_picking_batch'],

    # always loaded
    "data": ["security/ir.model.access.csv",
             "views/wizard_views.xml",
            ],
}