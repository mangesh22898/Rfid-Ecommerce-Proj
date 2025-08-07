# app/views.py
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

# Dummy in-memory cart
cart_items = []

@method_decorator(csrf_exempt, name='dispatch')
class CartView(View):
    def get(self, request):
        return JsonResponse(cart_items, safe=False)

    def post(self, request):
        body = json.loads(request.body)
        cart_items.append(body)
        return JsonResponse({"message": "Item added", "cart": cart_items})
