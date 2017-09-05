from django.contrib import admin
from django.core import urlresolvers
from django.contrib.contenttypes.models import ContentType


class NodeAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'level', 'path', 'parent_node', 'link_parent_node', 'root_node', 'link_root_node')
    search_fields = ('id', 'root_node__id', 'parent_node__id', 'path')

    def link_root_node(self, obj):
        content_type = ContentType.objects.get_for_model(obj.__class__)
        link = urlresolvers.reverse("admin:%s_%s_change" % (content_type.app_label, content_type.model), args=[obj.root_node.id])
        return '<a href="%s" target="_blank">%s</a>' % (link, obj.root_node.id)
    link_root_node.allow_tags = True

    def link_parent_node(self, obj):
        content_type = ContentType.objects.get_for_model(obj.__class__)
        link = urlresolvers.reverse("admin:%s_%s_change" % (content_type.app_label, content_type.model), args=[obj.parent_node.id])
        return '<a href="%s" target="_blank">%s</a>' % (link, obj.parent_node.id)
    link_parent_node.allow_tags = True
