# -*- coding: utf-8 -*-
{
    'name': 'Most Viewed and Sold Products',
    'version': '16.0.1.0.0',
    'category': 'Website',
    'summary': 'Most Viewed and Sold Products Snippet',
    'description': 'Most Viewed and Sold Products Snippet',
    'author': 'Fouzan M',
    'depends': ['base', 'website'],
    'data': [
        'views/sold_products_snippet.xml',
        'views/viewed_products_snippet.xml',
    ],
    'assets': {
            'web.assets_frontend': [
                '/most_viewed_and_sold_products/static/src/xml/sold_products_carousel.xml',
                '/most_viewed_and_sold_products/static/src/xml/viewed_products_carousel.xml',
                '/most_viewed_and_sold_products/static/src/js/most_sold_products.js',
                '/most_viewed_and_sold_products/static/src/js/most_viewed_products.js',
            ]
        },
    'application': True,
    'license': 'LGPL-3'
}
