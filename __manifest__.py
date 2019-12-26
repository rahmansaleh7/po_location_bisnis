# -*- coding: utf-8 -*-
{
    'name': "vit_po_location_bisnis",

    'summary': """
        Add Field Lokasi dan Bisnis di Line pada stock.picking
        Install Addon vit_rpq_po first
        """,

    'description': """
        Install Addon vit_rpq_po terlebih dahulu
        (Add Unit
        Add Lokasi - Bisnis pada purchase.order)""",

    'author': "Iqbal A - Vitraining",
    'website': "http://www.vitraining.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
                'base',
                'purchase',
                'analytic',
                'stock',
                'account',
                'analytic_tag_dimension',
                'vit_rpq_po',
                ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}