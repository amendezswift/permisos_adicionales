from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    establece_terminos_pago = fields.Boolean(
        string="Establece terminos de pago",
        compute="_compute_establece_terminos_pago",
    )

    establece_listas_precios = fields.Boolean(
        string="Establece listas de precios",
        compute="_compute_establece_listas_precios",
    )

    @api.depends_context("uid")
    def _compute_establece_terminos_pago(self):
        has_permission = self.env.user.has_group(
            "permisos_adicionales.terminos_pago_account_move_sale_order"
        )
        for record in self:
            record.establece_terminos_pago = has_permission

    @api.depends_context("uid")
    def _compute_establece_listas_precios(self):
        has_permission = self.env.user.has_group(
            "permisos_adicionales.listas_precios_sale_order"
        )
        for record in self:
            record.establece_listas_precios = has_permission