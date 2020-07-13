# -*- encoding: utf-8 -*-
{
    "name": "Website Product Stock",
    "category": "Website",
    'summary': 'Display stock of product on website.',
    'author': 'Aktiv Software',
    'website': 'www.aktivsoftware.com',
    'version': '9.0.1.0.0',
    'license': 'AGPL-3',
    'description': """
        This module allows to display stock of product on display.
    """,
    "depends": [
        'website_sale', 'stock'
    ],
    'data': [
        "views/templates.xml",
    ],
    'images': ['static/description/banner.jpg'],
    "installable": True,
    'auto_install': False,
    'website': False,
    'licence': False
}
