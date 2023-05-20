from rest_framework import serializers

class AddUserSerializer(serializers.Serializer):
    address = serializers.CharField()
    handle = serializers.CharField()
    token = serializers.CharField()
    twitter_url = serializers.CharField()
    hometown = serializers.CharField()
    disc_handle = serializers.CharField()
    interests = serializers.CharField()

    def create(self, validated_data):
        # Perform any additional processing if needed
        return validated_data
    
class ReturnUserSerializer(serializers.Serializer):
    address = serializers.CharField()

    def create(self, validated_data):
        # Perform any additional processing if needed
        return validated_data
    
# class DeleteUserSerializer(serializers.Serializer):
#     address = serializers.CharField()

#     def create(self, validated_data):
#         # Perform any additional processing if needed
#         return validated_data

class UpdateHometownSerializer(serializers.Serializer):
    address = serializers.CharField()
    hometown = serializers.CharField()

    def create(self, validated_data):
        # Perform any additional processing if needed
        return validated_data
    
class UpdateInterestsSerializer(serializers.Serializer):
    address = serializers.CharField()
    interests = serializers.CharField()

    def create(self, validated_data):
        # Perform any additional processing if needed
        return validated_data
    
class TwitterTrackingSerializer(serializers.Serializer):
    token = serializers.IntegerField()
    handle = serializers.CharField()

    def create(self, validated_data):
        # Perform any additional processing if needed
        return validated_data
    
