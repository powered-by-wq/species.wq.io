from rest_framework import serializers

from wq.db.contrib.files.serializers import (
    FileAttachmentSerializer, FileAttachedModelSerializer
)
from .models import Photo


class PhotoSerializer(FileAttachmentSerializer):
    class Meta(FileAttachmentSerializer.Meta):
        model = Photo


class ReportSerializer(FileAttachedModelSerializer):
    photos = PhotoSerializer(many=True, required=False)
    first_photo = serializers.SerializerMethodField()

    def get_first_photo(self, instance):
        if instance.photos.count() > 0:
            if instance.photos.all()[0].file:
                return instance.photos.all()[0].file.name
