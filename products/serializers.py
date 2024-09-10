from rest_framework import serializers
from category.models import Category
from products.models import Product


class Productserializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    category_id = serializers.IntegerField()
    price = serializers.IntegerField()
    quantity = serializers.IntegerField()
    description = serializers.CharField(allow_null=True, allow_blank=True)

    def create(self, validated_data):
        category = Category.objects.get(id=validated_data.pop("category_id"))
        return Product.objects.create(category=category, **validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.price = validated_data.get("price", instance.price)
        instance.quantity = validated_data.get("quantity", instance.quantity)
        instance.description = validated_data.get("description", instance.description)
        instance.save()
        return instance
