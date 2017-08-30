def node_str(node):
    '''
    Get a string representation of a Node object.

    ARGS
    ----
    node: Node
        The node...
    '''
    return 'node: ({})\nParent: {}\nRoot: {}\nLevel: {}\nPath: {}\nData: {}\n\n'.format(
        node.id,
        node.parent_node.id if node.parent_node else 'None',
        node.root_node.id,
        node.level,
        node.path,
        node.data
    )
