from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import UserProfile, User, Manga
from .serializers import UserProfileSerializer, MangaSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profilo_api(request, user_id):
    try:
        utente = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response({"error": "Utente non trovato"}, status=404)
    profilo = utente.profile
    if profilo:
        lista_manga_ids = profilo.manga_letti.get('id', [])
        lista_manga_obj = Manga.objects.filter(pk__in=lista_manga_ids)
        serializer_profile = UserProfileSerializer(profilo)
        serializer_manga = MangaSerializer(lista_manga_obj, many=True)
        combined_data = {
            "profilo": serializer_profile.data,
            "manga_completati": serializer_manga.data
        }
        return Response(combined_data)
    else:
        return Response({"error": "Profilo non trovato"}, status=404)