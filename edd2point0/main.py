import os
import time

from CardanoByronProxy.proxy import Proxy
from CardanoNode.node import Node
from Analyser.analyse_logs import Logs
from Analyser.comparer import Comparer

node_logsdir = os.getcwd() + '/logs/node/'
proxy_logsdir = os.getcwd() + '/logs/proxy/'

# These are tests to check if things work. Will need to create some sort of CLI API. 

def run_node():
    time_stamp = str(int(time.time()))
    logfile = 'node-output-' + time_stamp + '.txt'

    node = Node(path='/home/edward/Testing/cardano-node-staging/node', network='staging', logfile=logfile)
    node.run_node(run_time=10)

    logs = Logs(node_logsdir + logfile)
    print(logs.count_logs())

def run_proxy():
    time_stamp = str(int(time.time()))
    logfile = 'proxy-output-' + time_stamp + '.txt'

    proxy = Proxy(path='/home/edward/Testing/proxy-staging/proxy', network='staging', logfile=logfile)
    proxy.run_proxy(run_time=10)

    logs = Logs(proxy_logsdir + logfile)
    print(logs.count_logs())

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
    run_node()
    compare_most_recent_node_logs()
