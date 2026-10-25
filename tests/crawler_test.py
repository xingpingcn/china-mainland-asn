import asyncio
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, patch

import main as crawler_module


ASN_NAMES = {
    '4134': 'CHINANET',
    '9808': 'China Mobile',
    '4837': 'China Unicom',
    '4538': 'CERNET',
    '7497': 'CSTNET',
    '65000': 'Independent Network',
}
HTML = '<table>' + ''.join(
    f'<tr><td><a href="/AS{asn}" title="{name}">AS{asn}</a></td></tr>'
    for asn, name in ASN_NAMES.items()
) + '</table>'


class CrawlerTest(unittest.TestCase):
    def test_he_net_parser(self):
        crawler = crawler_module.main()
        with patch('main.requests.get', return_value=Mock(text=HTML)) as get:
            crawler.res_from_he_net()
        get.assert_called_once_with(
            'https://bgp.he.net/country/CN',
            headers=crawler_module.headers,
            timeout=10,
        )
        self.assertEqual(set(crawler.asn_dict), set(ASN_NAMES))
        for asn, name in ASN_NAMES.items():
            self.assertIn(name, crawler.asn_dict[asn])

    def test_classification_and_output_formats(self):
        expected = {
            'chinanet.txt': ['4134'],
            'cmcc.txt': ['9808'],
            'unicom.txt': ['4837'],
            'cernet.txt': ['4538'],
            'cstnet.txt': ['7497'],
            'other.txt': ['65000', '65001'],
        }
        html = HTML + (
            '<tr><td><a href="/AS65001" title="Another Network">'
            'AS65001</a></td></tr>'
        )
        for newline in (False, True):
            with self.subTest(output_newline=newline), tempfile.TemporaryDirectory() as directory:
                previous_directory = os.getcwd()
                try:
                    os.chdir(directory)
                    with patch('main.requests.get', return_value=Mock(text=html)), patch.object(
                        crawler_module, 'output_newline', newline
                    ):
                        asyncio.run(crawler_module.main().run())
                    files = {path.name for path in Path('asn_txt').glob('*.txt')}
                    self.assertEqual(files, set(expected))
                    for filename, asns in expected.items():
                        content = (Path('asn_txt') / filename).read_text(encoding='utf8')
                        header, body = content.split('\n', 1)
                        self.assertTrue(header.startswith('// Updated date: UTC+0 '))
                        separator = '\n' if newline else ','
                        self.assertEqual(body, separator.join(asns))
                finally:
                    os.chdir(previous_directory)


if __name__ == '__main__':
    unittest.main()
