# C:\Users\V\webroll\dnd_backend\characters\views.py
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Character
from .serializers import CharacterSerializer
from django.http import HttpResponse
import json
from io import BytesIO
from reportlab.pdfgen import canvas

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

@api_view(['GET'])
def export_characters(request):
    characters = Character.objects.all()
    serializer = CharacterSerializer(characters, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def import_characters(request):
    serializer = CharacterSerializer(data=request.data, many=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def generate_pdf(request, pk):
    character = Character.objects.get(pk=pk)
    buffer = BytesIO()
    p = canvas.Canvas(buffer)

    p.drawString(100, 750, f"Name: {character.name}")
    p.drawString(100, 735, f"Race: {character.race}")
    p.drawString(100, 720, f"Class: {character.character_class}")
    p.drawString(100, 705, f"Level: {character.level}")
    p.drawString(100, 690, f"Strength: {character.strength}")
    p.drawString(100, 675, f"Dexterity: {character.dexterity}")
    p.drawString(100, 660, f"Constitution: {character.constitution}")
    p.drawString(100, 645, f"Intelligence: {character.intelligence}")
    p.drawString(100, 630, f"Wisdom: {character.wisdom}")
    p.drawString(100, 615, f"Charisma: {character.charisma}")
    p.drawString(100, 600, f"Hit Points: {character.hit_points}")

    p.showPage()
    p.save()

    buffer.seek(0)
    return HttpResponse(buffer, content_type='application/pdf')
