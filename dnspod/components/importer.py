import httplib2
import json
from urllib.parse import urlencode

from odoo.addons.component.core import Component


class DNSPodDomainImporter(Component):
    _name = 'dnspod.domain.importer'
    _inherit = 'dns.abstract.importer'
    _apply_on = 'dns.domain'

    def _send_request(self, signal):
        headers = {
            "Content-type": "application/x-www-form-urlencoded",
            "Accept": "text/json",
            "User-Agent": "DNSPod-Odoo/0.01 (webmaster@my-odoo.com)"
        }
        api_path = self.backend_record.api_path
        conn = httplib2.HTTPSConnectionWithTimeout(api_path)
        conn.request('POST', '/Domain.Create',
                     urlencode(signal.get('params')), headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
        if response.status == 200:
            return json.loads(data.decode('utf-8'))
        else:
            return None


class DNSPodRecordImporter(Component):
    _name = 'dnspod.record.importer'
    _inherit = 'dns.abstract.importer'
    _apply_on = 'dnspod.record'

    def _before_import(self):
        print('import start')

    def _after_import(self):
        print('import done')

    def _send_request(self, signal):
        print('hello world')
