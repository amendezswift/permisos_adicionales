from odoo import models, fields, api


class AccountPayment(models.Model):
    _inherit = "account.payment"

    establecer_cuenta_destino = fields.Boolean(
        string="Establecer cuenta destino",
        compute="_compute_establecer_cuenta_destino",
    )

    @api.depends_context("uid")
    def _compute_establecer_cuenta_destino(self):
        usuario = self.env.user
        tiene_permiso = usuario.has_group(
            "permisos_adicionales.permitir_cambio_cuenta_destino"
        )

        for registro in self:
            registro.establecer_cuenta_destino = tiene_permiso

    @api.model
    def create(self, vals):
        record = super().create(vals)
        record._compute_establecer_cuenta_destino()
        return record
