# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    evidence_status = fields.Selection(
        [("more", "Need More"), ("done", "Done")], string="Evidence Status"
    )

    evidence_text = fields.Char()

    @api.multi
    def action_get_attachment_view(self):
        self.ensure_one()
        res = self.env["ir.actions.act_window"].for_xml_id("base", "action_attachment")
        res["domain"] = [
            ("res_model", "=", "stock.picking"),
            ("res_id", "in", self.ids),
        ]
        res["context"] = {
            "default_res_model": "stock.picking",
            "default_res_id": self.id,
        }
        return res
