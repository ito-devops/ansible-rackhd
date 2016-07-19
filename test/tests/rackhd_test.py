"""
Tests for `rackhd-formula`.
"""

import logging
import fabric.api
import unittest
import vagrant

import helpers

logger = logging.getLogger(__name__)

class TestRackhd(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.v = vagrant.Vagrant()
        self.server = self.v.user_hostname_port('rackhd01')
        fabric.api.env.key_filename = self.v.keyfile('rackhd01')
        fabric.api.env.disable_known_hosts = True
        fabric.api.env.hosts = [self.server]

    def test_rackhd_ports(self):
        fabric.api.execute(helpers.check_rackhd_ports, host=self.server)

    def test_config(self):
        data = fabric.api.execute(helpers.rackhd_config, host=self.server)
        config = data[self.server]
        self.assertTrue(config)
        self.assertEqual(config['httpBindPort'], 8080)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
