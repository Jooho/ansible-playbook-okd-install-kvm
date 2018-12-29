Tested Scripts
--------------


| Main Command | Scenario                           | Tested |
| ------------ | ---------------------------------- | ------ |
| deploy       | Install KVM/Create VMs/Install OKD | O      |
| install      | install OKD                        | O      |
| provision    | Install KVM/create VMs             | O      |
| start        | start VMs                          | O      |
| stop         | stop VMs                           | O      |
| suspend      | pause VMs                          | X(bug) |
| destroy      | force shutdown VMs                 | O      |
| teardown     | Delete VMs                         | O      |



|Main Command| Practise Command|Memo|
|-------------|----|---|
| deploy cluster| --deploy_type=okd --op=deploy| deploy_type can skip|
| deploy cluster| --deploy_type=okd --op=deploy --tag=311-1228| deploy_type can skip|
| stop cluster| --deploy_type=okd --op=stop| deploy_type can skip|
| start cluster| --deploy_type=okd --op=start| deploy_type can skip|
| suspend cluster| --deploy_type=okd --op=suspend| deploy_type can skip|
| destroy cluster| --deploy_type=okd --op=destroy| deploy_type can skip|
| teardown cluster| --deploy_type=okd --op=teardown| deploy_type can skip|


>./jkit.py \$Main_Command \$Sub_Command

```
jkit.py --deploy_type=ocp --operate=deploy
```