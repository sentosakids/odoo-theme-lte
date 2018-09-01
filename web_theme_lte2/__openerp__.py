# -*- coding: utf-8 -*-

{
    "name": "Backend Theme AdminLTE 2",
    "summary": "It provides fully responsive mobile adminLTE Bootstrap for Backend Theme Odoo Community "
               "web",
    "version": "10.0.0.0.2",
    "category": "Theme",
    "price":124,
    "currency": 'EUR',
    "website": "https://santoso21.000webhostapp.com/odoo9",
    "live_test_url": "https://santoso21.000webhostapp.com/odoo9",
    "author": "Santoso SA.",
    "license": "OPL-1",
    "installable": True,
    "depends": [
        'web',        
    ],
    "data": [
        'views/assets.xml',
        'views/web.xml',
    ],
    'qweb': [
        #'static/src/xml/form_view.xml',
        'static/src/xml/base.xml',        
    ],
    'images': ['images/main_screenshot.png', 'images/main_1.png']
}
