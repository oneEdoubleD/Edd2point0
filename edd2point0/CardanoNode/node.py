import os
from pathlib import Path
import shutil
import subprocess
import time


class Node():

    _logfile = None
    _process = None
    _working_dir = os.getcwd()

    def __init__(self, network, logfile):
        self._logfile = logfile
        try:
            shutil.rmtree(self._working_dir + '/state-node-' + network)
            print('state-node-' + network + ' has been deleted.')
        except:
            print('state-node-' + network + ' not detected.')

    def _run_node(self, logfile):
        self._process = subprocess.Popen(["/home/edward/Testing/cardano-node/node"], shell=True, stdout=logfile)

    def _stop_node(self):
        self._process.kill()

    def run_node(self, t=3600):
        with open((self._working_dir + '/logs/' + self._logfile), "w+") as node_logfile:
            self._run_node(node_logfile)
            time.sleep(t)
            self._stop_node()
