
# rackhd-ansible

This is a playbook to install and configure a rackhd server from packages.

It adds the necessary apt repos, installs system dependencies,
dhcpd server, rackhd packages, configures them, and starts services.

See [docs/ANSIBLE.md](docs/ANSIBLE.md) for details on using this playbook.

# Tests Included

Testing is provided using tox and vagrant. 

 - `tox`: Equivalent of `vagrant up rackhd01` and nosetests
 - `tox -e reprovision`: Spins up rackhd01 if necessary, runs vagrant provision, nosetests.
 - `tox -e rebuild`: Destroys rackhd01 and rebuilds/reprovisions it.
