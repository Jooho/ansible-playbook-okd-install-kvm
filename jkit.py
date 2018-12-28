#!/usr/bin/env python

import click
import os
import sys
from StringIO import StringIO

@click.command()
@click.option('--provider',
              default='kvm',
              type=click.Choice(['kvm']),
              help='This option specifies provider platform. ',
              show_default=True)
@click.option('--deploy_type',
              default='okd',
              type=click.Choice(['okd']),
              help='This option specifies main commands : deploying a new cluster',
              show_default=True)
@click.option('--op',
              default='deploy',
              type=click.Choice(['provision', 'deploy', 'install', 'start', 'stop', 'teardown' ]),
              help='This option specifies sub commands : provision - creating VM, deploy - creating & installing a new cluster, install - installing a new cluster, start/stop/teardown VMs')
@click.option('--tag',
              help='The tag of cluster used for targeting specific cluster operated to. It will overwrite the value from vars/all ')
@click.option('--okd_version',
              help='openshift verion. Basically, it will come from vars/all file but it can be overwritten ')
@click.help_option('--help', '-h')
@click.option('-v', '--verbose', count=True)
def launch(provider=None,
           deploy_type=None,
           op=None,
           tag=None,
           okd_version=None,
           status=None,
           verbose=0):

    # validate okd deploy_type options
    if deploy_type == 'okd':
        if op not in ['deploy', 'start', 'stop', 'teardown', 'install', 'provision']:
            print "[Not Valid Operate] - '%s' only allowed for okd" %op
            sys.exit(1)

    if verbose > 0:
        verbosity = '-' + 'v' * verbose
    else:
        verbosity = ''

# Create variable list to overwrite
    all_variables_str= ["tag","operate"]
    all_variables_real= [tag, op]
    overwrite_variables=[]
    var_index=0
    sio=StringIO()
    for variable in all_variables_real:
        if variable is not None:
            real_value=str(variable)
            add_value=all_variables_str[var_index]+"="+real_value
            overwrite_variables.append(add_value)
          #  overwrite_variables.append(add_value)
          #  ''.join(overwrite_variables)
          #  print overwrite_variables;

        var_index += 1
    overwrite_variables.append("current_path="+os.getcwd())
    sio.write(' '.join(overwrite_variables))
    print sio.getvalue()

# Construct ansible command
    if deploy_type == 'okd':
        if op in [ 'start', 'stop'] :
            status = os.system(
                'ansible-playbook %s playbooks/vm/operate.yml \
                --extra-vars "@vars/all.yml" \
                --extra-vars "@vars/okd_param.yml" \
                -e "%s" '

                 % (verbosity, sio.getvalue())
              

            )

        if op == 'teardown':
            status = os.system(
                'ansible-playbook %s playbooks/clean.yml \
                --extra-vars "@vars/all.yml" \
                --extra-vars "@vars/okd_param.yml" \
                -e "%s" '

                % (verbosity, sio.getvalue())
              

            )

        if op in [ 'provision', 'deploy'] :
            status = os.system(
                'ansible-playbook %s playbooks/vm/setup_vm.yml \
                --extra-vars "@vars/all.yml" \
                -e "%s" --flush-cache '

                % (verbosity, sio.getvalue())
              
            )

        if op == 'install':
           status = 0
        if status == 0 and op in [ 'install', 'deploy'] :
           status = os.system(
                'ansible-playbook %s -i /etc/ansible/hosts playbooks/okd/install_okd.yml \
                --extra-vars "@vars/all.yml" \
                --extra-vars "@vars/okd_param.yml" \
                -e "%s"  --flush-cache'

                % (verbosity, sio.getvalue())
              
            )

    # Exit appropriately
    if os.WIFEXITED(status) and os.WEXITSTATUS(status) != 0:
        sys.exit(os.WEXITSTATUS(status))


if __name__ == '__main__':
    launch(auto_envvar_prefix='KVM_OKD_DEPLOY')