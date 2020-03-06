import os
from pathlib import Path
import shutil
import subprocess
import time


class Node():

    _logfile = None
    _network = None
    _node_path = None
    _process = None
    _working_dir = None

    def __init__(self, path: str, network: str, logfile: str):
        """Initialize a new cardano-node

        Args:
            path: a full path to the node executable
            network: staging|testnet|mainnet
            logfile: the name of the logfile (remember to add .txt)
        """
        self._logfile = logfile
        self._network = network
        self._node_path = path
        self._working_dir = os.getcwd()

        try:
            shutil.rmtree(self._working_dir + '/state-node-' + network)
            print('state-node-' + network + ' has been deleted.')
        except:
            print('state-node-' + network + ' not detected.')

    def _run_node(self, logfile: str):
        """Run the node

        Args:
            logfile: redirects stdout to the logfile specified during initalization
        """
        self._process = subprocess.Popen([self._node_path], shell=True, stdout=logfile)

    def _stop_node(self):
        """Kill the node

        """
        self._process.kill()

    def run_node(self, run_time: int = 3600):
        """Run the node for a specified duration

        Args:
            run_time: the number of seconds that the node should run - default is 1 hour
        """
        with open((self._working_dir + '/logs/' + self._logfile), "w+") as node_logfile:
            self._run_node(node_logfile)
            time.sleep(run_time)
            self._stop_node()
