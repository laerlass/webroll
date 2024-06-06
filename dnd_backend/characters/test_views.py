# C:\Users\V\webroll\dnd_backend\characters\test_views.py
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Character

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_character():
    return Character.objects.create(
        name='Test Character',
        race='Human',
        character_class='Warrior',
        level=1,
        strength=15,
        dexterity=14,
        constitution=13,
        intelligence=12,
        wisdom=10,
        charisma=8,
        hit_points=10,
    )

@pytest.mark.django_db
def test_export_characters(api_client, create_character):
    url = reverse('export_characters')
    response = api_client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['name'] == 'Test Character'

@pytest.mark.django_db
def test_import_characters(api_client):
    url = reverse('import_characters')
    character_data = [
        {
            'name': 'Imported Character',
            'race': 'Elf',
            'character_class': 'Mage',
            'level': 1,
            'strength': 8,
            'dexterity': 14,
            'constitution': 10,
            'intelligence': 15,
            'wisdom': 12,
            'charisma': 14,
            'hit_points': 6,
        }
    ]
    response = api_client.post(url, character_data, format='json')
    assert response.status_code == 201
    assert Character.objects.count() == 1
    assert Character.objects.get().name == 'Imported Character'

@pytest.mark.django_db
def test_generate_pdf(api_client, create_character):
    url = reverse('generate_pdf', args=[create_character.id])
    response = api_client.get(url)
    assert response.status_code == 200
    assert response['Content-Type'] == 'application/pdf'
