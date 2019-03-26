# © 2019 Elico Corp (https://www.elico-corp.com).
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
from odoo import models, fields, api


class DNSDomain(models.Model):
    _inherit = 'dns.domain'

    @api.multi
    def action_connect(self):
        params = {
            'login_token': '88120,ab9df584f40f5e3be54db88c87b39c22',
            'format': 'json'
        }
        for domain in self:
            params.update(domain=domain.name)
            domain.sync_dns_records({'params': params})
