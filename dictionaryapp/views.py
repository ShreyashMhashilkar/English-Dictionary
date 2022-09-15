from django.shortcuts import render
import json
# Create your views here.
def dictionary(word):
    print(word)
    with open(r"dictionary.json", 'r', encoding='utf-8') as f:
        data = json.loads(f.read())
    if word in data:
        return data[word]
    else:
        return "Not present"

def index(request):
    return render(request, 'index.html')

def word(request):
    search = request.GET.get('search')
    # print(search)
    meaning = dictionary(search)
    result = {
        'meanings':meaning,
    }
    return render(request, 'word.html',result)