import os
import time

from CardanoNode.node import Node
from CardanoNode.analyse_logs import Logs

def main():
    time_stamp = str(int(time.time()))
    logfile = 'node-output-' + time_stamp + '.txt'

    node = Node('staging', logfile=logfile)
    node.run_node(10)

    logs = Logs(os.getcwd() + "/logs/" + logfile)
    print(logs.find_errors())

if __name__ == '__main__':
    main()
