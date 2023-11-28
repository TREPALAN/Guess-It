from django.shortcuts import render
from .models import Words
from .serializer import WordsSerializer

# Create your views here.

def index(request):
    # Serialize words
    words = Words.objects.all().order_by('?')[:20]
    serializer = WordsSerializer(words, many=True)
    return render(request, 'what_am_i/index.html',
                  {'words': serializer.data}
                  )
