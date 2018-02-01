# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

{
    'name': 'Partner Credit Limit & complement taxes & report',
    'version': '10.0.1.0.0',
    'category': 'Partner & acount & sales',
    'depends': ['base','account', 'sale'],
    'license': 'AGPL-3',
    'author': 'Jamel Nefzi',
    'maintainer': 'Hanente Pvt. Ltd.',
    'summary': 'Set credit limit warning and complement taxes ',
    'description': '''
        Partner Credit Limit'
        Taxes compement'
        Report invoice and sale order
    ''',
    'website': 'http://www.doyoubuzz.com/jamel-nefzi',
    'data': [
        'views/partner_view.xml',
        'views/acount_invoice.xml',
        'views/sales_order.xml',
        'views/order_invoice.xml',


    ],
    'installable': True,
    'auto_install': False,
}
