from django.shortcuts import render, redirect
from user_activity.models import EmailSubscription, Newsletter, FAQ, TermsCondition

def email_subscribe(request):
    if request.method == 'POST':
        if email := request.POST.get('email'):
            EmailSubscription(email=email).save()
    return redirect('index')

def news_letter(request):
    if request.method == 'POST':
        if email := request.POST.get('email'):
            if name := request.POST.get('email'):
                Newsletter(name = name,email=email).save()
    return redirect('index')

def faq_view(request):
    context = {}
    faq_list = FAQ.objects.filter(status=True)
    context.update({'faqs':faq_list})
    
    return render(request, 'common/faq.html', context)

def about_us_view(request):
    context = {}
    
    return render(request, 'common/about_us.html', context)

def terms_conditions(request):
    context = {}    
    term_list = TermsCondition.objects.filter(status=True)
    context.update({'terms':term_list})
    return render(request, 'common/terms.html', context)