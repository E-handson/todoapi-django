from rest_framework import serializers
from nuxt_api.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        exclude = [
            "created_at",
            "updated_at",
        ]
