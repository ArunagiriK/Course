# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CourseManagement(models.Model):
    _name = 'course.course'
    _description = 'Course Management'
    
    name = fields.Char(string='Course Name',required=True)
    instructor_id = fields.Many2one('res.partner',string='Instructor')
    lesson = fields.Many2one('course.lesson',string='Lesson')
    attendees_ids = fields.One2many('res.partner','course_id',string='Attendees',domain="[('attendee','=',True)]")
    room = fields.Many2one('course.room',string='Room')
    
    
    @api.onchange('lesson')
    def onchange_lesson(self):
        for rec in self:
            if rec.lesson:
               rec.room = rec.lesson.room_id.id
    

class CourseRoom(models.Model):
    _name = 'course.room'
    _description = 'Course Room'
    
    name = fields.Char(string='Room',required=True)
    no_of_attendees = fields.Integer('No Of Attendees')
    


class CourseLesson(models.Model):
    _name = 'course.lesson'
    _description = 'Course Lesson'
    
    name = fields.Char(string='Lesson',required=True)
    room_id = fields.Many2one('course.room',string='Room')
 
