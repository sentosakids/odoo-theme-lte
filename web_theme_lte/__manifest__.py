9# -*- coding: utf-8 -*-

{
    "name": "AdminLTE Backend Theme AdminLTE",
    "summary": "It provides a mobile theme like adminLTE Bootstrap compliant interface for Odoo Community "
               "web",
    "version": "10.0.0.0.1",
    "category": "Theme",
    "website": "",
    "author": "Santoso SA.",
    "license": "OPL-1",
    "price": "99.99",
    "currency": "EUR",
    "installable": True,
    "depends": [
        'web',        
    ],
    "data": [
        'views/assets.xml',
        'views/web.xml',
    ],
    'qweb': [
        'static/src/xml/form_view.xml',
        'static/src/xml/base.xml',        
    ],
    'images': ['images/main_screenshot.png','images/main_1.png','images/main_2.png']
}
