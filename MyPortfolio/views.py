from django.shortcuts import render
from .models import Portfolio
# Create your views here.

def index(request):
    portfolios = Portfolio.objects.all()
    context = {
        'portfolios': portfolios
    }
    return render(request, 'index.html', context)


def portfolio_details(request, portfolio_id):
    portfolio = Portfolio.objects.get(id=portfolio_id)
    context = {
        'portfolio': portfolio
    }
    return render(request, 'portfolio_details.html', context)