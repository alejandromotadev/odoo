from odoo import api, fields, models


class HospitalMeds(models.Model):
    _name = 'hospital.meds'
    _description = 'Hospital meds'
    _inherit = ['mail.thread']

    name = fields.Char(string='Medicamento')
    description = fields.Text(string='Descripcion')

