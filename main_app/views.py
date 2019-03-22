from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request, 'index.html', { 'wishes': wishes })

def newwish(request):
   return render(request, 'newwish.html')

class Wish:
    def __init__(self, description, quantity):
        self.description = description
        self.quantity = quantity
      
wishes = [
        Wish('I wish I had a cookie right now', 100)
]

