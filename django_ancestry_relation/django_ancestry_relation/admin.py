from django.contrib import admin
from django_ancestry_relation.models import TestNode

# Register your models here.


@admin.register(TestNode)
class TestNodeAdmin(admin.ModelAdmin):
    readonly_fields = ('level', 'path', 'parent_node', 'root_node')
