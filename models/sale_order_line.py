from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    establece_precio_unitario = fields.Boolean(
        string="Establece precio unitario",
        compute="_compute_establece_precio_unitario",
    )

    @api.depends_context("uid")
    def _compute_establece_precio_unitario(self):
        has_permission = self.env.user.has_group(
            "permisos_adicionales.precio_unitario_account_move_line_sale_order_line"
        )
        for record in self:
            record.establece_precio_unitario = has_permission