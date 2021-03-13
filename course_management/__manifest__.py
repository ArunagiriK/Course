# -*- coding: utf-8 -*-
{
    'name': "course_management",
    'summary': """
			
			Course Management	
        """,
    'description': """
        Course Managment and manage attendees 
    """,
    'author': "Arunagiri",
    'website': "http://www.yourcompany.com",
    'category': 'Education',
    'version': '0.1',
    'depends': ['base','contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/course_views.xml',
        'views/contact_view.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
}
