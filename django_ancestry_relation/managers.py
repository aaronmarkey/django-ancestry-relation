from django.db import models


class NodeManager(models.Manager):
    def create_node(self, *args, **kwargs):
        '''
        Create a Node object. Generates level and path automatically if ones are
        not supplied in kwargs.

        RETURNS
        -------
        node: Node
            The Node object, unsaved.
        '''
        node = self.model(**kwargs)
        # generate level
        if 'level' not in kwargs:
            if node.parent_node_id:
                node.level = node.parent_node.level + 1
            else:
                node.level = 1

        # generate path
        if 'path' not in kwargs:
            if node.parent_node:
                node.path = '{},{}'.format(
                    node.parent_node.path,
                    node.id
                )
            else:
                node.path = '{}'.format(
                    node.id
                )
        if node.level == 1:
            node.root_node = node
        return node

    def create_tree(self, nodes=[]):
        '''
        Save a list of nodes to the database.

        ARGS
        ----
        nodes: [Node,]
            A list of Node objects

        RETURNS
        -------
        Bool
            False if nodes is empty or save to DB failed, True if saved to DB
            successfully
        '''
        if nodes:
            try:
                self.bulk_create(nodes)
                return True
            except:
                return False
        return False

    def ancestral_nodes(self, node):
        '''
        Get a list of all nodes that are ascendants or descendants of the given
        node.

        ARGS
        ----
        node: Node
            The node.

        RETURNS
        -------
        QuerySet:
            A QuerySet of Node Objects, ordered by level.
        '''
        node_ids = node.path.split(',')
        return self.filter(id__in=node_ids).order_by('level')

    def descendants(self, node):
        '''
        Get a complete list of all nodes that inheiret from the given node.

        ARGS
        ----
        node: Node
            The node.

        RETURNS
        -------
        QuerySet:
            A QuerySet of Node Objects, ordered by level.
        '''
        return self.filter(
            root_node=node.root_node,
            path__contains=str(node.id)
        ).order_by('level')

    def children(self, node):
        '''
        Get the immediate children of the given node.

        ARGS
        ----
        node: Node
            The node.

        RETURNS
        -------
        QuerySet:
            A QuerySet of Node objects.
        '''
        return self.filter(
            parent_node=node
        ).order_by('level')

    def leaves(self, node):
        if node.id != node.root_node_id:
            raise Exception('node must be a root level node.')
        else:
            leaves = self.raw(
                '''
                SELECT * FROM django_ancestry_relation_testnode n1
                WHERE (SELECT count(*) FROM django_ancestry_relation_testnode n2
                    WHERE n2.parent_node_id = n1.id) = 0
                AND n1.root_node_id = '{}'
                ORDER BY n1.level ASC
                '''.format(str(node.id))
            )
        return leaves

    def hierarchical_(self, node):
        '''
        Get a structured representation of Nodes. Uses the StructuredNode class
        found at classes.StructuredNode.

        ARGS
        ----
        node: Node
            The root of the tree being requested. This is be the root
            kStructuredNode.

        RETURNS
        -------
        tree: StructuredNode
            A single StructuredNode object.

        NOTE
        ----
        This is slow. Do not use if descendants_ordered() can be used in any way.
        '''
        from django_ancestry_relation.classes import StructuredNode
        children_count = self.children(node).count()
        tree = StructuredNode.StructuredNode(
            data=node
        )
        if children_count > 0:
            children = self.children(node)
            for child in children:
                tree.children.append(
                    self.hierarchical_structured_tree(
                        child
                    )
                )
        return tree

    def descendants_ordered(self, node):
        '''
        Retrieve a flat list of node descendents, ordered according to their
        placement in the hierarchy.

    ARGS
        ----
        node: Node
            The root Node of this tree/subtree.

        RETURNS
        -------
        nodes: [Node,]
            A QuerySet of Node objects.
        '''
        nodes = self.descendants(node).order_by('path')
        return nodes

    def delete_tree(self, node):
        '''
        Just a wrapper for Django Model .delete method. Will delete a node and
        all of it's descendents.
        '''
        node.delete()
