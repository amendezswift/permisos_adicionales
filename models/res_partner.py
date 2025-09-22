from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

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
            "permisos_adicionales.terminos_pago_res_partner"
        )
        for record in self:
            record.establece_terminos_pago = has_permission

    @api.depends_context("uid")
    def _compute_establece_listas_precios(self):
        has_permission = self.env.user.has_group(
            "permisos_adicionales.listas_precios_res_partner"
        )
        for record in self:
            record.establece_listas_precios = has_permission