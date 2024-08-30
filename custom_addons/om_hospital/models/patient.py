from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread']  # Nos permite trackear las acciones que se apliquen en este modulo/modelo
    _description = 'Hospital Patient'

    name = fields.Char(string='Nombre', required=True, tracking=True)
    last_name = fields.Char(string='Apellidos', required=True, tracking=True)
    date_of_birth = fields.Date(string='Fecha de nacimiento', required=True, tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Género', required=True, tracking=True)
    tag_ids = fields.Many2many('patient.tag', 'patient_tag_rel', 'patient_id', 'tag_id', string="Tags")

    def _compute_display_name(self):
        for rec in self:
            rec.display_name = f"{rec.name} {rec.last_name}"
