import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'implementations' / 'python'))
from nids import parse

class NIDSTests(unittest.TestCase):
    def test_one_position_destination(self):
        d = parse('OLT-1')
        self.assertIsNone(d['positional']['source'])
        self.assertEqual(d['positional']['destination'], 'OLT-1')
        self.assertIsNone(d['positional']['layer'])

    def test_skipped_layer(self):
        d = parse('source_destination__router_description')
        self.assertEqual(d['positional'], {'source': 'source', 'destination': 'destination', 'layer': None, 'device_function': 'router', 'description': 'description'})

    def test_lists_recover_empty_members(self):
        self.assertEqual(parse('::VLAN:1,2,,3')['metadata']['VLAN'], [1, 2, 3])

    def test_literal_comma(self):
        self.assertEqual(parse("::DESC:'this,is,a,string'")['metadata']['DESC'], 'this,is,a,string')

    def test_apostrophe(self):
        self.assertEqual(parse("::DESC:'Customer''s Link'")['metadata']['DESC'], "Customer's Link")

    def test_ipv6(self):
        self.assertEqual(parse('::IP:[2001:db8::1]')['metadata']['IP'], '2001:db8::1')

    def test_unclosed_quote(self):
        self.assertEqual(parse("::DESC:'Customer Link_VLAN:150")['metadata']['VLAN'], 150)

    def test_flag(self):
        self.assertIs(parse('::DHCP-SNOOPING')['metadata']['DHCP-SNOOPING'], True)

if __name__ == '__main__':
    unittest.main()
