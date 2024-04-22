{
    'name': 'CRM Base',
    'version': '1.0',
    'category': 'CRM',
    'author': 'Nguyễn Hữu Toàn',
    'sequence': '1',
    'summary': 'CRM Base',
    'depends': ['base', 'crm'],
    'data': [
        'views/view_lead.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [],
}
