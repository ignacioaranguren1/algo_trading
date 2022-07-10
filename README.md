# algo_trading

In order to run the software, a CLI has been implemented. 

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
After selecting action 1 in the interface, a list of the currently available strategies is displayed. Then, the number of the strategy must be introduced to kill the strategy.
![alt text](images/kill_strgy_flow.png "Interface")
<br>Now information with the updated strategies is displayed.
![alt text](images/kill_strgy_result.png "Interface")

## Add strategy flow
After selecting action 2 in the interface, the number of generators of the new strategy must be indicated as input.
![alt text](images/add_strgy_flow.png "Interface")
<br>Now information with the updated strategies is displayed.
![alt text](images/add_strgy_result.png "Interface")

## Kill generator flow
After selecting action 3 in the interface,  a list of the currently available strategies is displayed. Then, the number of the strategy must be introduced. Then, a list displaying all the generators of the selected strategy wil be displayed. Finally, in order to kill the generator the number of one of the generators displyed in the previous step must be displayed.
![alt text](images/kill_gen_flow.png "Interface")
<br>Now information with the remaining updated is displayed.
![alt text](images/kill_gen_result.png "Interface")

## Add generator flow
After selecting action 4 in the interface, a list of the currently available strategies is displayed. Then, the number of the strategy must be introduced and a new genrator will be added to this strategy.
![alt text](images/add_gen_flow.png "Interface")
<br>Now information with the updated strategies is displayed.
![alt text](images/add_gen_result.png "Interface")
  
