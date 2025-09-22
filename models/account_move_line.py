from odoo import models, fields, api


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    establece_precio_unitario = fields.Boolean(
        string="Establece precio unitario",
        compute="_compute_establece_precio_unitario",
    )

    @api.depends("move_id.user_id")
    def _compute_establece_precio_unitario(self):
        for registro in self:
            registro.establece_precio_unitario = self.env.user.has_group(
                "permisos_adicionales.precio_unitario_account_move_line_sale_order_line"
            )
