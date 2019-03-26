# © 2019 Elico Corp (https://www.elico-corp.com).
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
from odoo import models, fields, api, _


class DNSDomain(models.Model):
    _inherit = 'dns.domain'

    @api.multi
    def action_connect(self):
        for domain in self:
            params = {
                'format': 'json',
                'domain': domain.name
            }
            if domain.backend_id.token_id and domain.backend_id.login_token:
                login_token = '{},{}'.format(
                    domain.backend_id.token_id,
                    domain.backend_id.login_token
                )
                params.update(login_token=login_token)
            else:
                params.update(login_email=domain.backend_id.login,
                              login_password=domain.backend_id.password)
            domain.sync_dns_records({'params': params})
