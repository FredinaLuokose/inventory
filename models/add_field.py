from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    order_priority = fields.Selection([
        ('Net_Banking', 'Net Banking'),
        ('Cash_on_Delivery', 'Cash on Delivery'),], 
        string='Payment Method')

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        self._update_picking_priorities()
        for order in self:
            order.picking_ids.write({'picking_priority': order.order_priority})
        return res

    def _update_picking_priorities(self):
        for order in self:
            pickings = self.env["stock.picking"].search([("origin", "=", order.name)])
            pickings.write({"picking_priority": order.order_priority})
