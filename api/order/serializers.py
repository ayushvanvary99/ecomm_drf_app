from rest_framework import serializers

from .models import Order


class OrderSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Order
        fields =('user')
        # TODO: