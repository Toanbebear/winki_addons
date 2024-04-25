{
    'name': 'CRM Base',
    'version': '1.0',
    'category': 'CRM',
    'author': 'Nguyễn Hữu Toàn',
    'sequence': '1',
    'summary': 'CRM Base',
    'depends': ['base', 'crm'],
    'data': [
        'data/ir_sequence_data.xml',
        'views/view_lead.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [],
    'assets': {
        'web.assets_backend': [
            'winki_crm/static/src/scss/style.scss',
            'winki_crm/static/src/js/field.js',
            'winki_crm/static/src/views/form/form_controller.js',
            'winki_crm/static/src/views/form/form_controller.xml',
        ],

    }
}
