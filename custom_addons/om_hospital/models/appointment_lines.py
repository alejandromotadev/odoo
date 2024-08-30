from odoo import api, fields, models


class HospitalAppointmentLines(models.Model):
    _name = 'hospital.appointment.lines'
    _description = 'Hospital Appointment Lines'
    _inherit = ['mail.thread']

    appointment_id = fields.Many2one('hospital.appointment', string='Citas')
    med_id = fields.Many2one('hospital.meds', string='Medicamento')
    qty = fields.Float(string='Cantidad')
