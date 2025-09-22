from odoo import api, fields, models


class AccountPayment(models.Model):
    _inherit = "account.payment"

    establecer_cuenta_destino = fields.Boolean(
        string="Establecer cuenta destino",
        compute="_compute_establecer_cuenta_destino",
    )

    @api.depends_context("uid")
    def _compute_establecer_cuenta_destino(self):
        has_permission = self.env.user.has_group(
            "permisos_adicionales.permitir_cambio_cuenta_destino"
        )
        for record in self:
            record.establecer_cuenta_destino = has_permission

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        records._compute_establecer_cuenta_destino()
        return records