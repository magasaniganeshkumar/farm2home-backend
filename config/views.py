from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def api_root(request):
    return Response(
        {
            "status": "success",
            "application": "Farm2Home API",
            "version": "v1",
            "docs": "/api/docs/",
            "schema": "/api/schema/",
        }
    )