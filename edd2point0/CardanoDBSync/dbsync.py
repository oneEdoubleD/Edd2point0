import os
from pathlib import Path
import shutil
import subprocess
import time


class DBSync():

    _logfile = None
    _network = None
    _dbsync_path = None
    _process = None
    _working_dir = None

    def __init__(self, path: str, network: str, logfile: str):
        """Initialize a new cardano-node

        Args:
            path: a full path to the dbsync executable
            network: staging|testnet|mainnet
            logfile: the name of the logfile (remember to add .txt)
        """
        self._logfile = logfile
        self._network = network
        self._dbsync_path = path
        self._working_dir = os.getcwd()

    def _start_dbsync(self, logfile: str):
        """Run the dbsync

        Args:
            logfile: redirects stdout to the logfile specified during initalization
        """

        # Need to manually add staging :(
        if self._network == 'staging':
            explorer_config_path = '/home/edward/Testing/cardano-db-sync/config/explorer-staging-config.yaml'
            genesis_path = '/home/edward/Testing/cardano-node-staging/configuration/mainnet-staging-short-epoch-genesis.json'
            node_socket_path = '/home/edward/Testing/cardano-node-staging/state-node-staging/node.socket'
            schema_path = '/home/edward/Testing/cardano-db-sync/schema/'
        elif self._network == 'testnet':
            explorer_config_path = '/home/edward/Testing/cardano-db-sync/config/explorer-testnet-config.yaml'
            genesis_path = '/home/edward/Testing/cardano-node-staging/configuration/testnet-genesis.json'
            node_socket_path = '/home/edward/Testing/cardano-node-testnet/state-node-testnet/node.socket'
            schema_path = '/home/edward/Testing/cardano-db-sync/schema/'
        elif self.network == 'mainnet':
            explorer_config_path = '/home/edward/Testing/cardano-db-sync/config/explorer-mainnet-config.yaml'
            genesis_path = '/home/edward/Testing/cardano-node-staging/configuration/mainnet-genesis.json'
            node_socket_path = '/home/edward/Testing/cardano-node-mainnet/state-node-mainnet/node.socket'
            schema_path = '/home/edward/Testing/cardano-db-sync/schema/'

        # Set-up the psql database for the new Explorer run
        subprocess.Popen(["scripts/postgresql-setup.sh", "--dropdb"], cwd='/home/edward/Testing/cardano-db-sync').wait()
        subprocess.Popen(["scripts/postgresql-setup.sh", "--createdb"], cwd='/home/edward/Testing/cardano-db-sync').wait()

        self._process = subprocess.Popen(['PGPASSFILE=config/pgpass', 
                                          'db-sync-node/bin/cardano-db-sync', 
                                          '--config', explorer_config_path, 
                                          '--genesis-file', genesis_path, 
                                          '--socket-path', node_socket_path, 
                                          '--schema-dir', schema_path], 
                                          cwd='/home/edward/Testing/cardano-db-sync', 
                                          shell=True, 
                                          stdout=logfile)

    def stop_dbsync(self):
        """Kill the dbsync

        """
        self._process.kill()

    def run_dbsync(self, run_time: int = 0):
        """Run dbsync for a specified duration

        Args:
            run_time: the number of seconds that the dbsync should run
        """
        with open((self._working_dir + '/logs/dbsync/' + self._logfile), "w+") as dbsync_logfile:
            self._start_dbsync(dbsync_logfile)
            if run_time > 0:
                time.sleep(run_time)
                self.stop_dbsync()
