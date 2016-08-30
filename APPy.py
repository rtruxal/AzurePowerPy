"""AzurePowerPy

Usage:
  APPy.py login
  APPy.py logout
  APPy.py status <vm_name>
  APPy.py start <vm_name>
  APPy.py stop <vm_name> [-d <sec> | --delay=<sec>]
  APPy.py [-h | --help]
  
Arguments:
  <vm_name>                 What it sounds like.
  <sec>                     Delay time in seconds.
  
Options:
  -h --help                 Show this screen.
  -d <sec> --delay=<sec>    Set delay time before shutdown. [default: 0]
  
"""

from docopt import docopt

if __name__ == '__main__':
  from orchestrator import orchestrate
  arguments = docopt(__doc__)
  orchestrate(arguments)


