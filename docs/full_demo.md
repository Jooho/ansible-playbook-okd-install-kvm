Full Demo
----------
This show full steps to install OKD from the scratch. Follow all steps and you can see OKD!

### Environment
- Fedora 28
- user `jooho`

### Pre-requisites

- Install `click` by pip.
  ```
  pip install click
  ```
- Create user/group
  ```
  sudo groupadd libvirt
  sudo useradd jooho -G libvirt
  ```
- Create working directory
  ```
  mkdir /home/jooho/git
  cd /home/jooho/git
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

 
  # OKD
  
  okd_param_dir: "{{ current_path }}/vars"
  okd_version: 3.11      
  okd_short_version: "{{ okd_version|regex_replace('\\.')}}"
  okd_docker_version: 1.13.1  
  okd_docker_storage_size: 20G 
  okd_docker_storage_disk: vdb       
  okd_interim_dns_use: true
  okd_interim_dns_ip: 192.168.200.1
  okd_dns_domain: example.com
okd_cluster_subdomain: "cloudapps-{{cluster_tag}}.{{okd_dns_domain}}"
okd_master_cluster_hostname: "masters-{{cluster_tag}}.{{okd_dns_domain}}"
okd_vm_recreate: false
okd_ansible_playbook_path: /tmp/openshift-ansible


# OpenShift Cluster VMs
# if infra_node_vms is not specified, it assumes app node have "region=infra" labels
# infra_node_vms
# if etcd_node_vms is not specified, etcd will be deploying on masters
# etcd_node_vms
master_node_vms: 3
master_vm_memory: 2G
infra_node_vms: 3
infra_vm_memory: 4G
app_node_vms: 2
app_vm_memory: 4G
lb_vm_memory: 2G
master_node_prefix: master
infra_node_prefix: infra
app_node_prefix: app
etcd_node_prefix: etcd
lb_node_prefix: lb


# Do not change
prometheus_yaml_path: "{{okd_ansible_playbook_path}}/playbooks/openshift-prometheus/config.yml"
cfme_yaml_path: "{{okd_ansible_playbook_path}}/playbooks/openshift-management/config.yml"
cfme_uninstall_yaml_path: "{{okd_ansible_playbook_path}}/playbooks/openshift-management/uninstall.yml"
metrics_yaml_path: "{{okd_ansible_playbook_path}}/playbooks/openshift-metrics/config.yml"
logging_yaml_path: "{{okd_ansible_playbook_path}}/playbooks/openshift-logging/config.yml"
service_catalog_yaml_path: "{{okd_ansible_playbook_path}}/playbooks/openshift-service-catalog/config.yml"
webconsole_yaml_path: "{{okd_ansible_playbook_path}}/playbooks/openshift-web-console/config.yml"
healthcheck_yaml_path: "{{okd_ansible_playbook_path}}/playbooks/openshift-checks/pre-install.yml"
nfs_yaml_path: "{{okd_ansible_playbook_path}}/playbooks/openshift-nfs/config.yml"
okd_install_yaml_path: "{{okd_ansible_playbook_path}}/playbooks/deploy_cluster.yml"
prequisites_yaml_path: "{{okd_ansible_playbook_path}}/playbooks/prerequisites.yml"
scale_up_node_yaml_path: "{{okd_ansible_playbook_path}}/playbooks/openshift-node/scaleup.yml"
scale_up_master_yaml_path: "{{okd_ansible_playbook_path}}/playbooks/openshift-master/scaleup.yml"
scale_up_etcd_yaml_path: "{{okd_ansible_playbook_path}}/playbooks/openshift-etcd/scaleup.yml"

health_check_yaml_path: "{{okd_ansible_playbook_path}}/playbooks/openshift-checks/pre-install.yml"
glusterfs_install_yaml_path: "{{okd_ansible_playbook_path}}/playbooks/openshift-glusterfs/config.yml"
monitoring_install_yaml_path: "{{okd_ansible_playbook_path}}/playbooks/openshift-monitoring/config.yml"
availability_monitoring_install_yaml_path: "{{okd_ansible_playbook_path}}/playbooks/openshift-monitor-availability/config.yml"
management_install_yaml_path: "{{okd_ansible_playbook_path}}/playbooks/openshift-management/config.yml"
descheduler_install_yaml_path: "{{okd_ansible_playbook_path}}/playbooks/openshift-descheduler/config.yml"
node_problem_detector_install_yaml_path: "{{okd_ansible_playbook_path}}/playbooks/openshift-node-problem-detector/config.yml"
autoheal_install_yaml_path: "{{okd_ansible_playbook_path}}/playbooks/openshift-autoheal/config.yml"

  ```
- Deploy OKD
  ```
  ./jkit.py --op=deploy -vvvv
  ```