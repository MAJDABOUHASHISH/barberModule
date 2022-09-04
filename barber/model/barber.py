from odoo import api, fields, models

class Barber(models.Model):
        __name__ = 'barber'
        
        customer_name = fields.Char(string='Customer Name')
        employee_name = fields.Char(string='Employee Name')
        chair_number = fields.Integer(string='Chair Number')
        description = fields.Char(string='Description')
        service_cost = fields.Integer(string='Service Cost')
        chair_status = fields.Char(string='Chair Status')
        form_status = fields.Char(string='Form Status') # empty --(save)> occupied --(done)> done
        
        