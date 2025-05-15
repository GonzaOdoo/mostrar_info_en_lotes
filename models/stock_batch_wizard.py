from odoo import models, fields,api
from collections import defaultdict
class InfoWizard(models.TransientModel):
    _name = 'stock.batch.info'
    _description = 'Wizard de Resumen de Productos'
    
    message = fields.Html(string="Resumen", readonly=True)
    batch_id = fields.Many2one('stock.picking.batch', string="Lote")
    
    @api.model
    def default_get(self, fields):
        res = super().default_get(fields)
        if self._context.get('active_id'):
            batch = self.env['stock.picking.batch'].browse(self._context['active_id'])
            res['batch_id'] = batch.id
            
            # Calcular resumen de productos
            product_summary = defaultdict(lambda: {'count': 0, 'qty': 0.0})
            for line in batch.move_line_ids:
                if line.product_id:
                    product_summary[line.product_id]['count'] += 1
                    product_summary[line.product_id]['qty'] += line.quantity or 0
            
            # Generar HTML del resumen
            html_lines = []
            for product, data in product_summary.items():  # Cambiado qty por data
                html_lines.append(f"""
                <tr>
                    <td>{product.display_name}</td>
                    <td style="text-align: right;">{data['count']}</td>
                    <td style="text-align: right;">{data['qty']:.2f}</td>
                    <td>{product.uom_id.name}</td>
                </tr>
                """)
            
            res['message'] = f"""
            <div style='padding: 10px;'>
                <h4>Resumen de Productos</h4>
                <table class="table table-bordered">
                    <thead>
                        <tr>
                            <th>Producto</th>
                            <th>Transferencias</th>
                            <th style="text-align: right;">Cantidad</th>
                            <th>Unidad</th>
                        </tr>
                    </thead>
                    <tbody>
                        {''.join(html_lines)}
                    </tbody>
                </table>
            </div>
            """
        return res

class StockPickingBatch(models.Model):
    _inherit='stock.picking.batch'

    def action_open_batch_info_wizard(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Resumen de Productos',
            'res_model': 'stock.batch.info',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_batch_id': self.id,
                'active_id': self.id,
            },
            'views': [(False, 'form')],
        }