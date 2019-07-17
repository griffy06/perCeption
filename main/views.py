from django.shortcuts import render,redirect
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def main(request):
    if request.method=="GET":
       return render(request, 'main/main_page.html', context=None)
    else:
       text = request.POST.get('data')
       obj = SentimentIntensityAnalyzer()
       sentiment_dict = obj.polarity_scores(text)
       if sentiment_dict['compound'] >= 0.05:
           return redirect('positive')
       elif sentiment_dict['compound'] <= -0.05:
           return redirect('negative')
       else:
           return redirect('neutral')




def about(request):
    return render(request,'main/about_page.html',context=None)