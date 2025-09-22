from odoo import models, fields, api


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

    @api.depends("user_id")
    def _compute_establece_terminos_pago(self):
        for registro in self:
            registro.establece_terminos_pago = self.env.user.has_group(
                "permisos_adicionales.terminos_pago_res_partner"
            )

    @api.depends("user_id")
    def _compute_establece_listas_precios(self):
        for registro in self:
            registro.establece_listas_precios = self.env.user.has_group(
                "permisos_adicionales.listas_precios_res_partner"
            )
