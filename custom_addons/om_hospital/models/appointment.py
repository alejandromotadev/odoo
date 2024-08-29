from odoo import api, fields, models


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread']  # Nos permite trackear las acciones que se apliquen en este modulo/modelo
    _description = 'Hospital Appointment'
    _rec_name = 'patient_id'  # Recupera el valor name del modelo hospital.patient (patient_id viene en el Many2one)

    reference = fields.Char(string='Reference', default="New")
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True, tracking=True)
    date_appointment = fields.Datetime(string='Fecha de la cita', required=True, tracking=True)
    note = fields.Text(string='Notas', tracking=True)
    state = fields.Selection(
        [('draft', 'Archivar'), ('confirmed', 'Confirmado'), ('ongoing', 'En proceso'), ('done', 'Terminado'),
         ('cancelled', 'Cancelado')
         ], string="Estatus", default="draft", tracking=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('reference') or vals['reference'] == "New":
                vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.appointment.sequence')
        return super().create(vals_list)

    def action_archive(self):
        for rec in self:
            rec.state = "draft"

    def action_confirm(self):
        for rec in self:
            rec.state = "confirmed"

    def action_cancel(self):
        for rec in self:
            rec.state = "cancelled"

    def action_done(self):
        for rec in self:
            rec.state = "done"

    def action_ongoing(self):
        for rec in self:
            rec.state = "ongoing"
