from django.shortcuts import render
from PyDictionary import PyDictionary

# Create your views here.


def index(request):
	return render(request, "dictionary.html")


def meaning(request):
	word = request.GET.get('word')
	dictionary = PyDictionary()
	mean = dictionary.meaning(word)
	syn = dictionary.synonym(word)
	ant = dictionary.antonym(word)
	data = {'mean': mean, 'ant':ant, 'syn': syn, 'word': word}
	return render(request, "word.html", data)