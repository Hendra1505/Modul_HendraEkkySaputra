# -*- coding: utf-8 -*-
{
    'name': "Training",

    'summary': """ Modul Odoo 14 """,

    'description': """
        Module ini dibuat sebagai bentuk dari salah satu Upaya untuk memudahkan
        Pembelajaran atau Pelatihan ke para Peserta dan Instruktur dalam mengurus Jadwal, Akun, Dan sebagainya
    """,

    'author': "Hendra Ekky Saputra",
    'website': "https://www.hashmicro.com/id/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'productivity',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/partner_views.xml',
        'views/menuitem_views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'application': True,
}