from rest_framework import serializers
from .models import Music, Album


class MusicSerializer(serializers.ModelSerializer):
    queryset = Music.objects.all()
    created_at = serializers.DateTimeField(format='%d/%m/%Y %H:%M:%S', read_only=True)

    class Meta:
        model = Music
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    queryset = Album.objects.all()

    class Meta:
        model = Album
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Music
        fields = '__all__'


# class MusicListListSerializer:
#     queryset = Music.objects.all()
#     created_at = serializers.DateTimeField(format='%d/%m/%Y %H:%M:%S', read_only=True)
#
#     class Meta:
#         model = Music
#         fields = '__all__'
#
#
# class MusicDetailSerializer:
#     queryset = Music.objects.all()
#     created_at = serializers.DateTimeField(format='%d/%m/%Y %H:%M:%S', read_only=True)
#
#     class Meta:
#         model = Music
#         fields = '__all__'