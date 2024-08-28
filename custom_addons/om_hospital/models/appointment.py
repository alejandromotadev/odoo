from odoo import api, fields, models

class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread'] # Nos permite trackear las acciones que se apliquen en este modulo/modelo
    _description = 'Hospital Appointment'
    _rec_name = 'patient_id' # Recupera el valor name del modelo hospital.patient (patient_id viene en el Many2one)

    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True, tracking=True)
    date_appointment = fields.Datetime(string='Fecha de la cita', required=True, tracking=True)
    note = fields.Text(string='Notas', tracking=True)



