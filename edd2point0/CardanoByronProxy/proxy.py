import os
from pathlib import Path
import shutil
import subprocess
import time

class Proxy():
    
    _logfile = None
    _network = None
    _node_path = None
    _process = None
    _working_dir = None

    def __init__(self, path: str, network: str, logfile: str):
        """Initialize a new cardano-byron-proxy

        Args:
            path: a full path to the proxy executable
            logfile: the name of the logfile (remember to add .txt)
        """
        self._logfile = logfile
        self._proxy_path = path
        self._working_dir = os.getcwd()

        try:
            shutil.rmtree(self._working_dir + '/state-node-' + network)
            print('state-node-' + network + ' has been deleted.')
        except:
            print('state-node-' + network + ' not detected.')

    def _start_proxy(self, logfile: str):
        """Run the proxy

        Args:
            logfile: redirects stdout to the logfile specified during initalization
        """
        self._process = subprocess.Popen([self._proxy_path], shell=True, stdout=logfile)

    def stop_proxy(self):
        """Kill the proxy

        """
        self._process.kill()

    def run_proxy(self, run_time: int = 0):
        """Run the proxy for a specified duration

        Args:
            run_time: the number of seconds that the node should run
        """
        with open((self._working_dir + '/logs/proxy/' + self._logfile), "w+") as proxy_logfile:
            self._start_proxy(proxy_logfile)
            if run_time > 0:
                time.sleep(run_time)
                self.stop_proxy()
