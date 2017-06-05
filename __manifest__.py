# -*- coding: utf-8 -*-
{
    'name': 'Colombia - Restaurante',
    'category': 'Localization',
    'version': '1.0.0',
    'author': 'DREAMSOFT',
    'license': 'AGPL-3',
    'maintainer': '',
    'website': '',
    'summary': 'Colombia Restaurante: Extended hotel_restaurant'
               'Contact Module - Odoo 10.0',
    'images': [],
    'depends': ['l10n_co_dreamsoft_hotel','hotel_restaurant'],
    'data': [
        'views/hotel_reservation_order_inherit_view.xml',
        'views/hotel_restaurant_reservation.xml',
        'views/hotel_restaurant_order_inherit_view.xml',

    ],
    'qweb': [],
    'installable': True,
}
