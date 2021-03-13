# -*- coding: utf-8 -*-

from odoo import models, fields, api
from lxml import etree

class Contacts(models.Model):
    _inherit = 'res.partner'
    
    
        
    #~ @api.model
    #~ def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        #~ res = super(Contacts, self).fields_view_get(view_id=view_id,
                                                     #~ view_type=view_type,
                                                     #~ toolbar=toolbar,
                                                     #~ submenu=submenu)
        #~ if view_type == 'form':
            #~ show_instructor = self._context.get('show_instructor')
            #~ print("Show Intructorennnnnnnnnnnnnnnnnnnnnnnnnnnn",show_instructor)
            #~ if show_instructor:
                #~ doc = etree.XML(res['arch'])
                #~ for field in res['fields']:
                    #~ for node in doc.xpath("//field[@name='instructor']"):
                        #~ node.set("invisible", "0")
                #~ res['arch'] = etree.tostring(doc)
        #~ return res
    
    instructor = fields.Boolean(string='Instructor')
    attendee = fields.Boolean(string='Attendee')
    course_id = fields.Many2one('course.course',string='Course')
