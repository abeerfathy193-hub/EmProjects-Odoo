from odoo import models, fields

class EmProject(models.Model):
    _name = 'em.project'
    _description = 'Project Records'
    # الوراثة دي هي اللي بتفتح لك أبواب الـ Chatter والنشاطات
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char(string='Project Name', required=True)
    description = fields.Text(string='Description')
    # علاقة Many2many مع الموظفين
    # أودو هيكريه جدول وسيط في الداتابيز لوحده يربط الـ IDs ببعض
    employee_ids = fields.Many2many(
        'hr.employee',          # الموديل اللي بنربط معاه
        string='Employees',     # الاسم اللي هيظهر لليوزر
        tracking=True           # تفعيل تتبع التغييرات في هذا الحقل
    )