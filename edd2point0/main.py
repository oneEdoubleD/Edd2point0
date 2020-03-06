import os
import time

from CardanoByronProxy.proxy import Proxy
from CardanoDBSync.dbsync import DBSync
from CardanoNode.node import Node
from Analyser.analyse_logs import Logs
from Analyser.comparer import Comparer

node_logsdir = os.getcwd() + '/logs/node/'
proxy_logsdir = os.getcwd() + '/logs/proxy/'
dbsync_logsdir = os.getcwd() + '/logs/dbsync/'

network = 'testnet'

# These are tests to check if things work. Will need to create some sort of CLI API. 

def run_node():
    time_stamp = str(int(time.time()))
    logfile = 'node-output-' + time_stamp + '.txt'

    node = Node(path='/home/edward/Testing/cardano-node-' + network + '/node', network=network, logfile=logfile)
    node.run_node(run_time=10)

    logs = Logs(node_logsdir + logfile)
    print(logs.count_logs())

def run_proxy():
    time_stamp = str(int(time.time()))
    logfile = 'proxy-output-' + time_stamp + '.txt'

    proxy = Proxy(path='/home/edward/Testing/proxy-' + network + '/proxy', network=network, logfile=logfile)
    proxy.run_proxy(run_time=10)

    logs = Logs(proxy_logsdir + logfile)
    print(logs.count_logs())

def run_dbsync():
    # Run node
    time_stamp = str(int(time.time()))
    logfile = 'node-output-' + time_stamp + '.txt'

    node = Node(path='/home/edward/Testing/cardano-node-' + network + '/node', network=network, logfile=logfile)
    node.run_node(run_time=0)

    node_logs = Logs(node_logsdir + logfile)
    print(node_logs.count_logs())

    # Run DBSync
    time_stamp = str(int(time.time()))
    logfile = 'dbsync-output-' + time_stamp + '.txt'

    dbsync = DBSync(path='/home/edward/Testing/cardano-db-sync/db-sync-node', network=network, logfile=logfile)
    dbsync.run_dbsync(run_time=120)

    dbsync_logs = Logs(dbsync_logsdir + logfile)
    print(dbsync_logs.count_logs())

    # Kill node
    node.stop_node()

def compare_most_recent_node_logs():
    dirFiles = os.listdir(path=node_logsdir)
    dirFiles.sort()

    logfile1 = Logs(node_logsdir + dirFiles[-1])
    logfile2 = Logs(node_logsdir + dirFiles[-2])

    print(Comparer.compare_logs(logfile1, logfile2))
    print(Comparer.diff(logfile1, logfile2))

if __name__ == '__main__':
    run_proxy()
    run_node()
    run_dbsync()
    compare_most_recent_node_logs()
