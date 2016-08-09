
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

# Accessing RackHD externally.

By default the Vagrantfile will not expose vm port 8080 to the host. To expose the RackHD
web ui, you will have to set the environment variable `RACKHD_EXTERNAL_PORT`.

    export RACKHD_EXTERNAL_PORT=8080
    vagrant reload rackhd01
    
# PXE GUI

By default, the pxeXX vms will tell virtualbox to show the GUI. You can disable this
with the environment variable `PXE_NOGUI`

    export PXE_NOGUI=True
    vagrant up pxe01
    

    
