from django.shortcuts import render

from .models import Result

# Create your views here.
def homepage(request):
    # Récupérer le nombre actuel de "pile" et "face" depuis la base de données
    result = Result.objects.first()  # Supposant qu'il n'y ait qu'une seule entrée dans la table Result

    # Si aucune entrée n'existe, crée une nouvelle instance
    if not result:
        result = Result.objects.create(heads=0, tails=0)

    # Passer les valeurs à la page HTML
    context = {
        'heads_count': result.heads,
        'tails_count': result.tails,
    }

    return render(request, "game/index.html", context)
