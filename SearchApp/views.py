from django.shortcuts import render
from django.http import JsonResponse

from .backend.triestructure import Trie
import pickle

import os
from django.conf import settings


# Custom Unpickler to rewrite module names during load
class FixUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        if module == "triestructure":
            module = "SearchApp.backend.triestructure"
        return super().find_class(module, name)

file_path = os.path.join(os.path.dirname(__file__), 'backend', 'trie.pkl')

with open(file_path, 'rb') as f:
    trie = FixUnpickler(f).load()

def home(request) :
    return render(request, 'index.html')

def fetch_data(request) :
    data = request.GET.get('query').strip()

    if(data == "") :
        return JsonResponse({"result" : []})
    
    top_words = trie.get_top_k(data)

    return JsonResponse({"result" : top_words})
# Create your views here.
