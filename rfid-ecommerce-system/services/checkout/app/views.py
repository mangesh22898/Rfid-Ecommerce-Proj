from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

@method_decorator(csrf_exempt, name='dispatch')
class CheckoutView(View):
    def post(self, request):
        try:
            order = json.loads(request.body)
            # Here you'd validate and forward to order DB/service
            return JsonResponse({"message": "Order received", "order": order}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
