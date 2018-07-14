# -*- coding: utf-8 -*-

{
    "name": "Web Theme AdminLTE",
    "summary": "It provides a mobile theme like adminLTE Bootstrap compliant interface for Odoo Community "
               "web",
    "version": "10.0.0.0.1",
    "category": "Theme",
    "price":124,    
    "website": "",
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
        'static/src/xml/form_view.xml',
        'static/src/xml/base.xml',        
    ],
}
