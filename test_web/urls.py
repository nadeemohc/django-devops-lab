from django.contrib import admin
from django.http import HttpResponse
from django.urls import path


def home(request):
    return HttpResponse("""
        <html>
            <head><title>My Django DevOps Lab</title></head>
            <body>
                <h1>Hello World!</h1>
                <p>My first Django application.</p>
                <p>Built locally and deployed using Git.</p>
            </body>
        </html>
    """)


urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
]