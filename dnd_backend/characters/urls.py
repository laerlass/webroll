# C:\Users\V\webroll\dnd_backend\characters\urls.py
from django.urls import path, include
from .views import export_characters, generate_pdf, import_characters
from rest_framework.routers import DefaultRouter
from .views import CharacterViewSet

router = DefaultRouter()
router.register(r'characters', CharacterViewSet)

# C:\Users\V\webroll\dnd_backend\characters\urls.py
urlpatterns = [
    path('', include(router.urls)),
    path('export/', export_characters, name='export_characters'),
    path('import/', import_characters, name='import_characters'),
    path('pdf/<int:pk>/', generate_pdf, name='generate_pdf'),       #path('generate-pdf/<int:character_id>/', generate_pdf, name='generate_pdf'),
]

