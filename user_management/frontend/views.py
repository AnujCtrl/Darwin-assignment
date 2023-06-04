from django.shortcuts import render


def test_api(request):
    return render(request, 'frontend/test_api.html')
