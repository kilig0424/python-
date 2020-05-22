from rest_framework import serializers
from goods.models import Goods,GoodsCategory

#
# class GoodsSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(required=True,max_length=100)
    # click_num = serializers.IntegerField(default=0)
    # goods_front_image = serializers.ImageField()
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = '__all__'

class GoodsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Goods
        fields = '__all__'