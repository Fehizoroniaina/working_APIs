from rest_framework import serializers

from Link.models import Link


class LinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Link
        fields="__all__"