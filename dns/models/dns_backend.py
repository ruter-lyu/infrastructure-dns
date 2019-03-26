# © 2019 Elico Corp (https://www.elico-corp.com).
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
from odoo import models, fields, api


class DNSBackend(models.Model):
    _name = 'dns.backend'
    _inherit = 'connector.backend'
    _description = 'DNS Connector Backend'

    @api.model
    def _selection_version(self):
        return [('1.0', '1.0')]

    login = fields.Char('Username or Email')
    password = fields.Char('Password')
    api_path = fields.Char('API URL', help="URL to DNS Provider API")
    version = fields.Selection(_selection_version, string='Backend Version')
    company_id = fields.Many2one('res.company', string='Company')
    is_default = fields.Boolean('Is Default Backend')
    import_date = fields.Datetime('Import Date')
    export_date = fields.Datetime('Export Date')

    def sync(self, model, external_id):
        self.ensure_one()
        self.env[model].with_delay().sync_dns_records(self, external_id)
