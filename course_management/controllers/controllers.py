# -*- coding: utf-8 -*-
# from odoo import http


# class CourseManagement(http.Controller):
#     @http.route('/course_management/course_management/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/course_management/course_management/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('course_management.listing', {
#             'root': '/course_management/course_management',
#             'objects': http.request.env['course_management.course_management'].search([]),
#         })

#     @http.route('/course_management/course_management/objects/<model("course_management.course_management"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('course_management.object', {
#             'object': obj
#         })
