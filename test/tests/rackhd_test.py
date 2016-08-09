"""
Tests for `rackhd-formula`.
"""

import logging
import fabric.api
import unittest
import vagrant

import helpers

logging.basicConfig()
logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)

class TestRackhd(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.v = vagrant.Vagrant()
        self.server = self.v.user_hostname_port('rackhd01')
        self.hosts = [self.server]
        fabric.api.env.key_filename = self.v.keyfile('rackhd01')
        fabric.api.env.disable_known_hosts = True
        fabric.api.env.hosts = [self.server]

    def test_rackhd_ports(self):
        fabric.api.execute(helpers.check_rackhd_ports, hosts=self.hosts)

    def test_config(self, httpbindport=8080):
        data = fabric.api.execute(helpers.rackhd_config, hosts=self.hosts)
        config = data[self.server]
        self.assertTrue(config)
        self.assertEqual(config['httpBindPort'], httpbindport)

    def test_packages(self):
        # Just list the packages.
        data = fabric.api.execute(helpers.list_packages, hosts=self.hosts)
        logger.warn('Packages: \n{0}'.format(data[self.server]))

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
