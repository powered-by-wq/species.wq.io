from rest_framework import serializers
from wq.db.patterns import serializers as patterns
from .models import Report, Photo


class PhotoSerializer(patterns.AttachmentSerializer):
    class Meta(patterns.AttachmentSerializer.Meta):
        model = Photo
        exclude = ('report',)
        object_field = 'report'


class ReportSerializer(patterns.AttachedModelSerializer):
    photos = PhotoSerializer(many=True, required=False)
    first_photo = serializers.SerializerMethodField()

    def get_first_photo(self, instance):
        photo = instance.photos.first()
        if photo and photo.file:
            return photo.file.name

    class Meta:
        model = Report
        fields = "__all__"
