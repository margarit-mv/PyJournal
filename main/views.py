from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(reguest):
    context = {
        "values": ["test 2", "test 1"]
    }

    return  render(reguest, "main/index.html",context)


