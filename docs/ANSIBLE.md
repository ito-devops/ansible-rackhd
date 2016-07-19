ansible-playbook
----------------

Given ansible=>1.5.5 and this playbook, you can install an operational
rackhd server from packages.

# Inventory and Local Variables

The rackhd playbook has defaults/main.yml with the common defaults included.
However, it purposefully does not include site specific variables.

Create an inventory file containing your rackhd server(s), along with
the group_vars and host_vars directories underneath it for the playbook to run.

The vagrant test instance comes with its own `inventory-vagrant` file defining
localhost in the group "vagrant".  

```
test/ansible/
├── group_vars
│   └── vagrant
└── inventory-vagrant.ini
```

See the ansible.com's Playbooks Best Practices [staging vs production](http://docs.ansible.com/ansible/playbooks_best_practices.html#how-to-differentiate-staging-vs-production) for
more information.

# Running

Assuming you're running on vagrant:

    ansible-playbook -i /vagrant/ansible/inventory-vagrant.ini /opt/ansible/rackhd/playbook.yml

If you're going to run this a lot, you should make an alias or wrapper shell script. In the
vagrant instance, a shortcut command `rackhd-ansible` has been placed in `/usr/bin`. The
remaining examples will have that shorter name.

# Tags

Each task (except some conditional ones) have a unique identifying tag,
and related tasks have common tags. Unique id tags start with id
(ex: `id.packages.rackhd` installs rackhd pacakges). 

**Examples:**

Install rackhd packages:

    rackhd-ansible --tags=id.packages.rackhd

Add key and repo for nodesource:

    rackhd-ansible --tags="id.apt.key.nodesource,id.apt.repo.nodesource"
        
Run all tasks related to installing packages:
        
    rackhd-ansible --tags="packages"
    
Run all tasks related to isc-dhcpd:

    rackhd-ansible --tags="isc.dhcpd"


