import os
import time

from CardanoNode.node import Node
from Analyser.analyse_logs import Logs
from Analyser.comparer import Comparer

def main():
    time_stamp = str(int(time.time()))
    logfile = 'node-output-' + time_stamp + '.txt'

    node = Node('staging', logfile=logfile)
    node.run_node(10)

    logs = Logs(os.getcwd() + "/logs/" + logfile)
    print(logs.count_logs())

def compare_two_logs():
    dirFiles = os.listdir(os.getcwd() + "/logs/")
    dirFiles.sort()
    sorted(dirFiles)

    l1 = Logs(os.getcwd() + "/logs/" + dirFiles[-1])
    l2 = Logs(os.getcwd() + "/logs/" + dirFiles[-2])

    c = Comparer(l1, l2)
    print(c.compare())
    print(c.find_all_new_logs())

if __name__ == '__main__':
    main()
    main()
    compare_two_logs()
