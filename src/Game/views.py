from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Score

# Create your views here.
def homepage(request):
    score = Score.objects.first()

    if not score:
        score = Score.objects.create(heads=0, tails=0)

    context = {
        'heads_count': score.heads,
        'tails_count': score.tails,
    }

    return render(request, "game/index.html", context)

@csrf_exempt
def tails(request):
    if request.method == 'GET':
        score = Score.objects.first()

        if not score:
            score = Score.objects.create(heads=0, tails=0)

        return HttpResponse(score.tails)

    if request.method == 'POST':
        score = Score.objects.first()

        if not score:
            score = Score.objects.create(heads=0, tails=0)

        score.tails += 1

        score.save()

        return HttpResponse(f'Successfully added, tails counter is at {score.tails}')

@csrf_exempt
def heads(request):
    if request.method == 'GET':
        score = Score.objects.first()

        if not score:
            score = Score.objects.create(heads=0, tails=0)

        return HttpResponse(score.heads)

    if request.method == 'POST':
        score = Score.objects.first()

        if not score:
            score = Score.objects.create(heads=0, tails=0)

        score.heads += 1

        score.save()

        return HttpResponse(f'Successfully added, heads counter is at {score.heads}')

@csrf_exempt
def reset(request):
    if request.method == 'DELETE':
        score = Score.objects.first()

        if not score:
            score = Score.objects.create(heads=0, tails=0)

        score.heads = 0
        score.tails = 0

        score.save()

        return HttpResponse('Successful')
