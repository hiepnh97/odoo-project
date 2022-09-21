# -*- coding: utf-8 -*-
{
    'name': "demo_view_product",
    'summary': """Show list product by webview""",
    'description': """TODO""",
    'author': "My Company",
    'website': "http://www.yourcompany.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '15.0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'sale_management',
        'website_sale'
    ],

    # always loaded
    'data': [
        ### security ###
        # 'security/ir.model.access.csv',

        ### VIEWS ###
        # 'views/views.xml',
        # 'views/templates.xml',

    ],
    'application': True
}
