import subprocess
from os import path
import os

def delegate(docopt_dict):
    # returns filenames based on docopt output
    if docopt_dict['login']:
        return 'login'
    elif docopt_dict['logout']:
        return 'logout'
    elif docopt_dict['start']:
        return 'start_{}'.format(docopt_dict['<vm_name>'])
    elif docopt_dict['stop']:
        return 'stop_{}'.format(docopt_dict['<vm_name>'])
    elif docopt_dict['status']:
        raise Exception('functionality not existant yet')

def execute(selection='test'):
    file_pth = path.join(os.getcwd(),'{}.ps1'.format(selection)) 
    if not os.path.exists(file_pth):
        raise EnvironmentError('DNE')
    subprocess.call(["powershell", ". \"./{}.ps1\";".format(selection)])
    print 'python reached end of code w/o throwing fatal exception'


def orchestrate(docopt_dict=None): 
  ps_scripts_dir = path.join(path.curdir, 'scripts')
  os.chdir(ps_scripts_dir)
  
  if docopt_dict:
    execute(delegate(docopt_dict))
  else:
	execute()

if __name__ == '__main__':
	orchestrate()


