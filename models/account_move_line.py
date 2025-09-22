from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    establece_terminos_pago = fields.Boolean(
        string="Establece terminos de pago",
        compute="_compute_establece_terminos_pago",
    )

    @api.depends_context("uid")
    def _compute_establece_terminos_pago(self):
        has_permission = self.env.user.has_group(
            "permisos_adicionales.terminos_pago_account_move_sale_order"
        )
        for record in self:
            record.establece_terminos_pago = has_permission