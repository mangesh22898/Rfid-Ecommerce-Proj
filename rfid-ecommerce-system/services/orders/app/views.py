from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

# Temporary in-memory DB
orders = []

@method_decorator(csrf_exempt, name='dispatch')
class OrdersView(View):
    def get(self, request):
        return JsonResponse(orders, safe=False)

    def post(self, request):
        try:
            data = json.loads(request.body)
            orders.append(data)
            return JsonResponse({"message": "Order stored", "orders": orders}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
