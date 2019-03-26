import logging

from odoo.addons.component.core import Component
from odoo.addons.connector.components.mapper import mapping

_logger = logging.getLogger(__name__)


class DNSPodDomainMapper(Component):
    _name = 'dnspod.domain.mapper'
    _inherit = 'dns.abstract.mapper'
    _apply_on = 'dns.domain'

    @mapping
    def compute_state(self, record):
        if record['status']['code'] != '1':
            _logger.warning(record['status']['message'])
            return {'state': 'exception'}
        else:
            return {'state': 'done'}


class DNSPodRecordMapper(Component):
    _name = 'dnspod.record.mapper'
    _inherit = 'dns.abstract.mapper'
    _apply_on = 'dnspod.record'
