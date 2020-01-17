# Scale up App Node 

## Steps

This step is for creating app node *app2.example.com*. By default, there is only 1 app node.

Most steps are updated by default except ansible hosts file but please check all before you proceed.

If you want to scale up app nodes "app2.example.com"

- Update `app_num: 2` from ./playbooks/scaleup/provision.yaml
- Update `new_nodes` from /etc/ansible/hosts
  ```
  [OSEv3:children]
  masters
  etcd
  nodes
  new_nodes   #<== ADD

  ...

  [new_nodes]
  app2.example.com   openshift_node_group_name='node-config-compute'   # <== ADD

  ```

- Execute Commands:
  - `ansible-playbook ./playbooks/scaleup/provision.yaml -vvvv -e @../../vars/all.yml`
  - `ansible-playbook -i /etc/ansible/hosts ./playbooks/scaleup/install-prerequisites.yaml -vvvv -e @../../vars/all.yml`
  - `ansible-playbook -i /etc/ansible/hosts playbooks/openshift-node/scaleup.yml` 

