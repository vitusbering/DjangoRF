import io

from rest_framework import serializers  # base class for inheritance MenSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


from .models import Men

class MenSerializer(serializers.ModelSerializer): # ModelSerializer - base class. It works with models
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Men
        # fields = ('title', 'content', 'cat')
        fields = "__all__"



# class MenModel():
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


# class MenSerializer(serializers.Serializer): # inheritance from base class Serializer
#     title = serializers.CharField(max_length=200)
#     content = serializers.CharField()
#     time_create = serializers.DateTimeField(read_only=True)
#     time_update = serializers.DateTimeField(read_only=True)
#     cat_id = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return Men.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get("title", instance)
#         instance.content = validated_data.get("content", instance)
#         instance.time_update = validated_data.get("time_update", instance)
#         instance.cat_id = validated_data.get("cat_id", instance)
#         instance.save()
#         return instance

# def encode():
#     model = MenModel('Lew Yashin', 'Content: Lew Yashin')
#     model_sr = MenSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
# def decode():
#     stream = io.BytesIO(b'{"title":"Lew Yashin","content":"Content: Lew Yashin"}')
#     data = JSONParser().parse(stream)
#     serializer = MenSerializer(data=data)
#     serializer. is_valid()
#     print(serializer.validated_data)