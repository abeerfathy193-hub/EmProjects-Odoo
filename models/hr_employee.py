from odoo import models, fields

class HrEmployee(models.Model):
    _inherit = 'hr.employee' # وراثة الموديل الأصلي
    insurance_number = fields.Char(string='Insurance Number')
    joining_date = fields.Date(string='Joining Date')
    project_ids = fields.Many2many(
        'em.project', 
        string='Assigned Projects'
    )