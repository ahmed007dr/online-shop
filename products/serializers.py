from rest_framework import serializers
from .models import Products , Brand

class ProductListSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()

    review_count = serializers.SerializerMethodField()
    avrg_rate = serializers.SerializerMethodField(method_name='get_avr_rate')
    class Meta:
        model = Products
        fields = '__all__'

    def get_review_count(self,object):
        reviews = object.reviews_product.all().count() #  (العلاقهreviews_product)كدا هنرجع بكل التقيمات و عددهم للمنتج الواحد
        return reviews
    
    def get_avr_rate(self,object): # عدد متوسط التقيمات
        total = 0
        reviews = object.reviews_product.all()
        if len(reviews) > 0:
            for item in reviews:
                total += item.rate
            
            avg= total / len(reviews)
        else :
            avg =0
        return avg

class ProductDetailsSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()

    review_count = serializers.SerializerMethodField(method_name='get_review_count') # anther way

    class Meta:
        model = Products
        fields = '__all__'


    def get_review_count(self,object):
        reviews = object.reviews_product.all().count() #  (العلاقهreviews_product)كدا هنرجع بكل التقيمات و عددهم للمنتج الواحد
        return reviews

class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class BrandDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
