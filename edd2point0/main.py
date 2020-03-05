from CardanoNode.node import Node

def main():
    n = Node('staging')
    n.run_node(10)

if __name__ == '__main__':
    main()
