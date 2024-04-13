from rest_framework import serializers
from .models import Products , Brand

class ProductListSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()

    review_count = serializers.SerializerMethodField()

    class Meta:
        model = Products
        fields = '__all__'

    def get_review_count(self,object):
        reviews = object.reviews_product.all().count() #  (العلاقهreviews_product)كدا هنرجع بكل التقيمات و عددهم للمنتج الواحد
        return reviews

class ProductDetailsSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()

    class Meta:
        model = Products
        fields = '__all__'

class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class BrandDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
