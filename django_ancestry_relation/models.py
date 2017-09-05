from django.db import models
import uuid
from django_ancestry_relation.managers import NodeManager


class Node(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        db_index=True,
        help_text='Primary key. This is a UUID, not a string. When selecting by\
            id, or comparing ids to one another, compare the UUIDs, not the\
            string representations of the UUIDs. It is significantly faster.'
    )
    parent_node = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        help_text='The parent of this Node. Will be None if a root.',
        blank=True,
        null=True,
        db_index=True,
        related_name='node_parent_node'
    )
    root_node = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        help_text='The root node of this tree. If this node is root, this reference self.',
        blank=False,
        null=False,
        related_name='node_root_node'
    )
    level = models.IntegerField(
        null=False,
        db_index=True,
        help_text='The level of the node, in relation to it\'s height in the tree. Starts at root, with level = 1.'
    )
    path = models.TextField(
        db_index=True,
        help_text='A CSV list of the ids leading to this Node. Root will be a list of one item, it\'s own id.'
    )

    objects = NodeManager()

    class Meta:
        abstract = True

    def __str__(self):
        return 'ID: {}\nRoot: {}\nLevel: {}'.format(
            self.id,
            self.root_node.id,
            self.level
        )
