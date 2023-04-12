from rest_framework import serializers
from .models import Owner, HH, Room
import requests

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ['id','name']


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields= ['id','hh','name','price_per_night','availability','checkin_time','checkout_time','rules']


class HHSerializer(serializers.ModelSerializer):
    owners = OwnerSerializer(many=True,read_only=True)
    rooms = RoomSerializer(many=True,read_only=True)
    weather = serializers.SerializerMethodField()

    class Meta:
        model = HH
        fields = ['id','name','address','town','owners','rooms','weather']

    def get_weather(self,obj):
        api_key = "d8ab56b8ca5d0a8f901eb327f43104a0"
        url = f'http://api.openweathermap.org/data/2.5/weather?q={obj.town}&appid={api_key}&units=metric'
        response = requests.get(url)    
        if response.status_code == 200:
            data = response.json()
            return {
                'description': data['weather'][0]['description'],
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed']
            }
        else:
            return {}
        

class CreateOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ['name']



class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['hh', 'name','price_per_night', 'availability', 'checkin_time', 'checkout_time','rules']



class CreateHHSerializer(serializers.ModelSerializer):
    owners = CreateOwnerSerializer(many=True)

    class Meta:
        model = HH
        fields = ['name', 'address', 'owners']

    def create(self, validated_data):
        owners_data = validated_data.pop('owners')
        hh = HH.objects.create(**validated_data)
        for owner_data in owners_data:
            owner = Owner.objects.create(hh=hh, **owner_data)
            hh.owners.add(owner)
        return hh
    
