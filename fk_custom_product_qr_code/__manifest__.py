{
    'name': 'FK Product QR Code',
    'version': '18.0.1.0.0',
    'summary': 'Automatically generate QR codes for products',
    'description': """
Automatically generates a QR code for a product when the product is created.
    """,
    'author': 'Sher Fayaz',
    'category': 'Inventory',
    'license': 'LGPL-3',
    'depends': ['base', 'product'],
    'data': [
        'views/views.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    # External dependencies are discouraged on Odoo Apps
    'external_dependencies': {
        'python': ['qrcode', 'Pillow'],
    },
}
