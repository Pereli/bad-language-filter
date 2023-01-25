from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from spanlp.palabrota import Palabrota
from spanlp.domain.countries import Country
from spanlp.domain.strategies import JaccardIndex, Preprocessing, TextToLower, RemoveAccents, NumbersToVowelsInLowerCase
import json



def index(request):
    return HttpResponse("Language Analysis API")

@csrf_exempt
def censor(request):
    body = json.loads(request.body)
    text = body['speak']


    original_text = text
    strategies = [RemoveAccents(), TextToLower(), NumbersToVowelsInLowerCase()]
    cleaned = Preprocessing().clean(data=original_text, clean_strategies=strategies)


    palabrota = Palabrota()
    offensive = palabrota.contains_palabrota(cleaned)


    if offensive == True:
        jaccard = JaccardIndex(
                                threshold=0.7, 
                                normalize=True, 
                                n_gram=1, 
                                clean_strategies=strategies)
        palabrota = Palabrota(
                                    censor_char="*", 
                                    countries=[
                                        Country.ESPANA, 
                                        Country.VENEZUELA], 
                                    distance_metric=jaccard)
        censored = palabrota.censor(cleaned)
        return JsonResponse({'text': censored})


    else:
        return JsonResponse({'text': original_text})