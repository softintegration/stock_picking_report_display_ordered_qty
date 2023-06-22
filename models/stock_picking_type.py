# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class PickingType(models.Model):
    _inherit = "stock.picking.type"

    report_display_ordered_qty = fields.Boolean(
        string='Display ordered qty in report', default=True,
        help="If this case is checked,the system will display the ordered qty in the report.")

