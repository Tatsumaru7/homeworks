from django.contrib.auth.models import User
from rest_framework import serializers
from advertisements.models import Advertisement,AdvertisementStatusChoices


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name',)

class AdvertisementSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator', 'status', 'created_at', 'updated_at')

    def create(self, validated_data):
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        user = self.context["request"].user
        open_advertisements = Advertisement.objects.filter(creator=user, status='OPEN').count()

        if open_advertisements >= 10 and data.get('status') != AdvertisementStatusChoices.CLOSED:
            raise serializers.ValidationError("У вас уже есть максимальное количество открытых объявлений.")

        return data

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance