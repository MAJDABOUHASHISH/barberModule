{
    'name': "barber",
    'version': '1.0',
    'depends': ['base'],
    'author': "MAJD",
    'category': 'Test',
    'description': """
    Register for the barber shop
    """,
    # data files always loaded at installation
    'data': [
        'views/barber.xml',
    ],
#     # data files containing optionally loaded demonstration data
#     'demo': [
#         'demo/demo_data.xml',
#     ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
