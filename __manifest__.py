# -*- coding: utf-8 -*-
{
    'name': "l10n_cl_hr_method",

    'summary': """
            Modulo que extiendo personalisa el modulo l10n_cl_hr con las siguientes funcionalidades:
            1.- Agrega AFP Uno a los indicadores previsionales 
        """,

    'description': """
        1.- Agrega AFP Uno a los indicadores previsionales
    """,

    'author': "Method",
    'website': "http://www.openmethod.cl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','l10n_cl_hr','hr_payroll','hr_payroll_account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'data/l10n_cl_hr_method_payroll_data.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}