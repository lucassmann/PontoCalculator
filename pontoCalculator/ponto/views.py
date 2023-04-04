from django.shortcuts import render

# Create your views here.


def ponto(request):
    # username = None
    if request.user.is_authenticated:
        #     username = request.user.username
        # context = {'username': username}
        return render(request, 'ponto.html')
