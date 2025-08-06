# app/views.py
from django.http import JsonResponse
from django.views import View

class CatalogView(View):
    def get(self, request):
        cards = [
            {
                "id": 1,
                "name": "Classic",
                "color": "White",
                "preview_url": "/static/previews/classic.png",
                "fields": ["name", "institute", "telephone", "email", "room"]
            },
            {
                "id": 2,
                "name": "Modern",
                "color": "Blue",
                "preview_url": "/static/previews/modern.png",
                "fields": ["name", "institute", "telephone", "email", "room"]
            },
            {
                "id": 3,
                "name": "Premium",
                "color": "Black",
                "preview_url": "/static/previews/premium.png",
                "fields": ["name", "institute", "telephone", "email", "room"]
            }
        ]
        return JsonResponse(cards, safe=False)
