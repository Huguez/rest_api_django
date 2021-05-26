from rest_framework import serializers
from tutorials.models import Tutorials

class TutorialSerializers( serializers.ModelSerializer ):
    class Meta:
        model = Tutorials
        fields = ( 'id', 'title', 'description', 'published' )

