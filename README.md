# algo_trading

In order to run the software, a CLI has been implemented. 

## Command description

usage: cli_interface.py [-h] [--verbose] strategies generators

positional arguments:
  strategies  select the number of strategies
  generators  select the number of generators

optional arguments:
  -h, --help  show this help message and exit
  --verbose   enable output verbosity. If verbosity is not allowd logs will not be displayed and decisions will not show up. Only interactions with the strategies and generators would be available.
  
 **Example**
 
 python3 cli_interface.py 4 12 --verbose
 
 Creates 4 strategies with 12 generators each.
 
 
## Interface 


  
