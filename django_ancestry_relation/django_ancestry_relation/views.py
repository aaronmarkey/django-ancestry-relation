from django.views.generic import TemplateView
from django_ancestry_relation.models import TestNode
from django_ancestry_relation.utilities import node_str
from django.http import HttpResponse
import logging
logger = logging.getLogger('print_log')
from random import randint
from datetime import datetime
from django.shortcuts import render


class TestView(TemplateView):
    template_view = 'django_ancestry_relation.templates.tree.html'

    def get(self, request):
        logger.debug('at TestView.get')

        # create a test tree
        if 'create' in request.GET:
            start_time = datetime.now()
            logger.debug('creating test tree')
            nodes = []
            count = 1500
            root_node = TestNode.objects.create_node(
                data='1'
            )
            nodes.append(root_node)
            for x in range(count):
                parent = nodes[randint(0, x)]
                node = TestNode.objects.create_node(
                    parent_node=parent,
                    root_node=root_node,
                    data='test node'
                )
                nodes.append(node)
                node_str(node)
                count += 1
            TestNode.objects.create_tree(nodes)
            end_time = datetime.now()
            logger.debug('test tree created')
            logger.debug('create time: {}'.format(
                end_time - start_time
            )
            )
            rand_node = nodes[randint(1, 1300)]
            logger.debug('index: {}'.format(
                nodes.index(rand_node)
            )
            )

        # get a whole tree and root ancestry
        # start_time = datetime.now()
        # rand_root = TestNode.objects.filter(level=1).first()
        # whole_tree = TestNode.objects.decendents(rand_root)
        # ancestors = TestNode.objects.ancestral_nodes(rand_root)
        # end_time = datetime.now()
        # logger.debug('random whole size: {}\ntime: {}'.format(
        #     len(whole_tree),
        #     end_time - start_time
        # )
        # )
        # logger.debug('ascentor node count: {}'.format(len(ancestors)))

        # organize a whole tree
        # start_time = datetime.now()
        # tree = TestNode.objects.flat_structured_tree_slower(rand_root)
        # end_time = datetime.now()
        # logger.debug('organization time (flat 1): {}'.format(
        #     end_time - start_time
        # )
        # )

        import uuid
        blah = TestNode.objects.get(id=uuid.UUID('aab5f6eb-d182-4bc4-87c3-b4e8caff0749'))
        start_time = datetime.now()
        small_tree = TestNode.objects.decendents(blah)
        end_time = datetime.now()
        logger.debug('random small tree: {}\ntime: {}'.format(
            len(small_tree),
            end_time - start_time
        )
        )
        start_time = datetime.now()
        tree = TestNode.objects.flat_structured_tree(blah)
        end_time = datetime.now()
        logger.debug('organization time (flat 2): {}'.format(
            end_time - start_time
        )
        )
        return render(request, self.template_view, {'tree': tree})
