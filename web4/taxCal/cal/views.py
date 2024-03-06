from django.shortcuts import render

from django.http import HttpResponse

tax_rate = 0.15

def default(request) :
   return HttpResponse("ch1>This is a site to calculate tax</h1>")


def calculate_total_price(request, num):
 total_price = num * (1 + tax_rate)
 return HttpResponse(f"<h1>Total Price after {tax_rate*100} % tax:{total_price}</h1>")

def tax_rate_view (request) :
 return render (request, 'tax_calculator/tax_rate.html', {'tax_rate': tax_rate})
