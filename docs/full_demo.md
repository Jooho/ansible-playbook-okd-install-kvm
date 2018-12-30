Full Demo
----------
This show full steps to install OKD from the scratch. Follow all steps and you can see OKD!

### Environment
- Fedora 28
- user `root`

### Pre-requisites

- Install `click` by pip.
  ```
  pip install click
  ```

- Create working directory
  ```
  mkdir /tmp/Test
  cd /tmp/Test
  ```

- Clone git repository
  ```
  git clone https://github.com/Jooho/ansible-playbook-okd-install-kvm.git
  cd ansible-playbook-okd-install-kvm
  ```
  

### Deploy OKD

- Update variable
  ```
  vi vars/all
  
  # Distinguish Each Cluster
  tag: 311-1220   # <== update
  
  # KVM config
  kvm: 
    ..
    storage_pool_dir: /home/jooho/KVM    <== update or delete (default: /var/lib/libvirt/images)
    ..

  # Base Image Config
  vm_data_dir: /home/jooho/kvm/vms    <== update or delete (default: /root/kvm/vms)

  okd_version: 3.11      # <=== update if version need to be changed
  okd_docker_version: 1.13.1  # <=== update if OKD version need to be changed

  # OpenShift Cluster VMs
  # if etcd_node_vms is not specified, etcd will be deploying on masters
  # etcd_node_vms
  master_node_vms: 1  # <=== update if you don't have enought resource (default 3)
  master_vm_memory: 2G
  infra_node_vms: 1   # <=== update if you don't have enought resource (default 3)
  infra_vm_memory: 4G 
  app_node_vms: 3    # <=== update if you don't have enought resource (default 2)>
  app_vm_memory: 4G
  lb_vm_memory: 2G
  master_node_prefix: master
  infra_node_prefix: infra
  app_node_prefix: app
  etcd_node_prefix: etcd
  lb_node_prefix: lb
  ```

  vi vars/okd_param.yml
  ```
  openshift_logging_install_logging: false  # <== logging need enough memory so when you create vm with more than 6G,please set true
                                            # By default it is false
  ```

- Download Ansible Galaxy Roles
  ```
  ansible-galaxy install -f -r requirements.yml
  ```

- Deploy OKD
  ```
  ./jkit.py --op=deploy -vvvv
  ```