# -*- coding: utf-8 -*-
from odoo.addons.component.core import Component
from odoo.addons.connector.components.mapper import mapping


class DNSPodDomainMapper(Component):
    _name = 'dnspod.domain.mapper'
    _inherit = 'dns.abstract.mapper'
    _apply_on = 'dns.domain'

    @mapping
    def compute_state(self, record):
        if record['status']['code'] != 1:
            return {'state': 'exception'}
        else:
            return {'state': 'done'}


class DNSPodRecordMapper(Component):
    _name = 'dns.record.mapper'
    _inherit = 'dns.abstract.mapper'
    _usage = 'import.mapper'
