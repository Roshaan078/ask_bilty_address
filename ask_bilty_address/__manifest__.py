{
    'name': "Bilty Address",
    'summary': "Shipping Address on Gate pass",
    'description': """This module adds bilty address field on delivery order""",
    'author': "Asksol",
    'website': "https://www.asksol.pk",
    'category': 'Sales',
    'version': '19.0.1.0',
    
    'depends': ['stock','sale_management'],
    'data': [
        'report/delivery_slip_report.xml',
        'views/bilty_address_view.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
    'images': ['static/description/banner.png'],
}

