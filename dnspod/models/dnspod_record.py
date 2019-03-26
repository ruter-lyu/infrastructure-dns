# © 2019 Elico Corp (https://www.elico-corp.com).
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
from odoo import models, fields, api


class DNSRecord(models.Model):
    _name = 'dnspod.record'
    _inherit = 'dns.binding'
    _inherits = {'dns.record': 'odoo_id'}
    _description = 'DNSPod records'

    @api.model
    def _type_select_version(self):
        res = [('A', 'A'), ('CNAME', 'CNAME'), ('MX', 'MX'),
               ('TXT', 'TXT'), ('NS', 'NS'), ('AAAA', 'AAAA'),
               ('SRV', 'SRV'), ('Visible URL', '显性URL'),
               ('Invisible URL', '隐现URL')]
        return res

    @api.model
    def _line_select_version(self):
        res = [('默认', '默认'), ('B', '电信'), ('C', '联通'),
               ('D', '教育网'), ('E', '百度'), ('F', '搜索引擎')]
        return res

    odoo_id = fields.Many2one(comodel_name='dns.record',
                              string='DNS Record',
                              required=True,
                              ondelete='restrict')
