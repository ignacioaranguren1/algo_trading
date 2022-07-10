# algo_trading

CLI implementation of the algorithmic trader test.

## Command description

**Usage**: <br> cli_interface.py [-h] [--verbose] strategies generators

**Positional arguments:**<br>
 - strategies  select the number of strategies
 - generators  select the number of generators

**Optional arguments:**<br>
  &nbsp;&nbsp;&nbsp; -h, --help  show this help message and exit<br>
  &nbsp;&nbsp;&nbsp; --verbose   enable output verbosity. If verbosity is not allowd logs will not be displayed and decisions will not show up. Only interactions with the strategies and generators would be available.
  
 **Example**
 
 python3 cli_interface.py 4 12 --verbose
 
 Creates 4 strategies with 12 generators each.
 
## System init
![alt text](images/initialization.png "Interface")
 
## Interface 
![alt text](images/interface_decisions.png "Interface")

## Decision output
![alt text](images/output_decision.png "Interface")

## Decisions update
![alt text](images/decision_update.png "Interface")

## Kill strategy flow
After selecting action 1 in the interface, a list of the currently available strategies is displayed. Then, the number of the strategy must be introduced to kill the strategy.<br><br>
![alt text](images/kill_strgy_flow.png "Interface")
<br><br>Now information with the updated strategies is displayed.<br><br>
![alt text](images/kill_strgy_result.png "Interface")

## Add strategy flow
After selecting action 2 in the interface, the number of generators of the new strategy must be indicated as input.<br><br>
![alt text](images/add_strgy_flow.png "Interface")
<br><br>Now information with the updated strategies is displayed.<br><br>
![alt text](images/add_strgy_result.png "Interface")

## Kill generator flow
After selecting action 3 in the interface,  a list of the currently available strategies is displayed. Then, the number of the strategy must be introduced. Then, a list displaying all the generators of the selected strategy wil be displayed. Finally, in order to kill the generator the number of one of the generators displyed in the previous step must be displayed.<br><br>
![alt text](images/kill_gen_flow.png "Interface")
<br><br>Now information with the remaining updated is displayed.<br><br>
![alt text](images/kill_gen_result.png "Interface")

## Add generator flow
After selecting action 4 in the interface, a list of the currently available strategies is displayed. Then, the number of the strategy must be introduced and a new genrator will be added to this strategy.<br><br>
![alt text](images/add_gen_flow.png "Interface")
<br><br>Now information with the updated strategies is displayed.<br><br>
![alt text](images/add_gen_result.png "Interface")
 
 ## Print output
 
 Decisions are updated every minute, this can make the interface to not fit in the window. To display the list of actions and strategy info type the action q. <br><br>
 
 ![alt text](images/print_output.png "Interface")
