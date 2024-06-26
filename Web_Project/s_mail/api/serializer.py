from rest_framework import serializers
from . import models


class MessageSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    subject = serializers.CharField(max_length=255)
    folder = serializers.PrimaryKeyRelatedField(queryset=models.Folder.objects.all())
    body = serializers.CharField()
    sender = serializers.PrimaryKeyRelatedField(queryset=models.User.objects.all())
    recipient = serializers.PrimaryKeyRelatedField(queryset=models.User.objects.all())
    sent_at = serializers.DateTimeField(read_only=True)
    read = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return models.Message.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.subject = validated_data.get('subject', instance.subject)
        instance.body = validated_data.get('body', instance.body)
        instance.sender = validated_data.get('sender', instance.sender)
        instance.recipient = validated_data.get('recipient', instance.recipient)
        instance.read = validated_data.get('read', instance.read)
        instance.save()
        return instance


class MailboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Mailbox
        fields = '__all__'


class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Folder
        fields = '__all__'

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()

    def create(self, validated_data):
        """
        Create and return a new User instance, given the validated data.
        """
        return models.User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing User instance, given the validated data.
        """
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Attachment
        fields = '__all__'