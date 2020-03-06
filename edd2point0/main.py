import os
import time

from CardanoNode.node import Node
from Analyser.analyse_logs import Logs
from Analyser.comparer import Comparer

logdir = os.getcwd() + '/logs/'

def run_node():
    time_stamp = str(int(time.time()))
    logfile = 'node-output-' + time_stamp + '.txt'

    node = Node('/home/edward/Testing/cardano-node-staging/node', 'staging', logfile=logfile)
    node.run_node(run_time=10)

    logs = Logs(logdir + logfile)
    print(logs.count_logs())

def compare_most_recent_logs():
    dirFiles = os.listdir(logdir)
    dirFiles.sort()

    logfile1 = Logs(logdir + dirFiles[-1])
    logfile2 = Logs(logdir + dirFiles[-2])

    print(Comparer.compare_logs(logfile1, logfile2))
    print(Comparer.diff(logfile1, logfile2))

if __name__ == '__main__':
    run_node()
    run_node()
    compare_most_recent_logs()
