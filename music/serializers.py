from rest_framework import serializers
from .models import Music


class MusicSerializer(serializers.ModelSerializer):
    queryset = Music.objects.all()
    created_at = serializers.DateTimeField(format='%d/%m/%Y %H:%M:%S', read_only=True)

    class Meta:
        model = Music
        fields = '__all__'