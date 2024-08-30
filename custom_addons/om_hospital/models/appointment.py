from odoo import api, fields, models


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread']  # Nos permite trackear las acciones que se apliquen en este modulo/modelo
    _description = 'Hospital Appointment'
    _rec_name = 'patient_id'  # Recupera el valor name del modelo hospital.patient (patient_id viene en el Many2one)
    _rec_names_search = ['patient_id', 'reference', 'date_appointment', 'appointment_lines_ids'] # Para las busquedas, agregar los fields a buscar

    reference = fields.Char(string='Reference', default="New")
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True, tracking=True)
    appointment_lines_ids = fields.One2many('hospital.appointment.lines', 'appointment_id', string='Lines')
    date_appointment = fields.Datetime(string='Fecha de la cita', required=True, tracking=True)
    note = fields.Text(string='Notas', tracking=True)
    state = fields.Selection(
        [('draft', 'Archivar'), ('confirmed', 'Confirmado'), ('ongoing', 'En proceso'), ('done', 'Terminado'),
         ('cancelled', 'Cancelado')
         ], string="Estatus", default="draft", tracking=True)
    total_qty = fields.Float(compute="_compute_total_qty_", string='Cantidad Total') #si este compute field se quiere guardar en la bd, agregar el parametro "store=True"
    related_date_of_birth = fields.Date(string='Fecha de nacimiento del paciente', related='patient_id.date_of_birth')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('reference') or vals['reference'] == "New":
                vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.appointment.sequence')
        return super().create(vals_list)
    @api.depends('appointment_lines_ids', 'appointment_lines_ids.qty')
    def _compute_total_qty_(self):
        for rec in self:
            total_qty = 0
            for line in rec.appointment_lines_ids:
                total_qty += line.qty
            rec.total_qty = total_qty

    def _compute_display_name(self):
        for rec in self:
            rec.display_name = f"[{rec.reference}],{rec.patient_id.name} {rec.patient_id.last_name}"
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
