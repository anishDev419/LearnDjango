from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.shortcuts import render


def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {'mymembers': mymembers}
    # return HttpResponse(template.render())
    # return HttpResponse(template.render(context, request))
    return render(request, 'all_members.html', context)


def details(request, id):
    mymember = Member.objects.get(id=id)
    # mymember = Member.objects.filter(firstname='Emil').values()
    # mymember = Member.objects.filter(lastname='Refsnes', id=2).values()
    # mymember = Member.objects.filter(firstname='Emil').values() | Member.objects.filter(firstname='Tobias').values()
    # mymember = Member.objects.filter(Q(firstname='Emil') | Q(firstname='Tobias')).values()
    # mymember = Member.objects.filter(firstname__startswith='L').values()
    # mymember = Member.objects.all().order_by('firstname').values()
    # mymember = Member.objects.all().order_by('-firstname').values()
    # mymember = Member.objects.all().order_by('lastname', '-id').values()
    template = loader.get_template("details.html")
    context = {'mymember': mymember}
    # return HttpResponse(template.render(context, request))
    return render(request, 'details.html', context)


def main(request):
    template = loader.get_template('main.html')
    # return HttpResponse(template.render())
    return render(request,'main.html')
