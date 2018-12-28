# OKD KVM Reference Architecture

This script help deploy OKD on KVM and also provide some more features for reference


## Supported OS
- Fedora 28
- CentOS 7

## Provision Operate Work Flows

- Install KVM
- Deploy Base Image(CentOS 7)
- Upgrade Base Image to latest
- Create VMs for OKD (Cloned from Base image)
- Attach Storage to the new VMs for docker storage
- Install DNSMasq & add records of the new VMs
- Generate Ansible hosts file for OKD
- OKD prerequisites
- Clone official OKD ansible playbook 

## Install Operate Flows

- Execute Prerequisite script
- Execute OKD script


## Neccessary Packages

- click

## Docs

- [JKIT CLI](./docs/jkit.md)
 
### Playbook Information

- [Directory Structure](./docs/directory_structure.md)
 
### Tested Scripts

- [Tested Features](./docs/tested_scripts.md)



- Generate key pair for SSH
- [Update all.yml](./doc/update-variables.md)




