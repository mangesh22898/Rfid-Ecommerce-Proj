from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

@method_decorator(csrf_exempt, name='dispatch')
class EmailView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            # Simulate sending email
            print("📨 Simulated sending email to:", data.get("email"))
            print("Email content:", data)
            return JsonResponse({"message": "Email sent (mock)"}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
