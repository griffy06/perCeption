from django.shortcuts import render


def positive(request):
    return render(request, 'result/positive_page.html', context=None)

def negative(request):
    return render(request, 'result/negative_page.html', context=None)

def neutral(request):
    return render(request, 'result/neutral_page.html', context=None)
