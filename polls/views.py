from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from .models import *
from .forms import *

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf

def index(request):
    offer_list=Offer.objects.order_by('-price')[:5] #Question.objects.order_by('-pub_date')[:5]
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'offer_list': offer_list, 'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)



def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

# %%%%%%%%%%%%%%%%%%%% KOSZYK %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
from django.contrib.auth.models import User
def bucket_add(request,pk,un):
    p = get_object_or_404(Offer, pk=pk)

    q=get_object_or_404(User,username=un)
    list=Bucket.objects.filter(buyerUsername=q.username,offer=p)
    if(len(list)==0):
        Bucket.objects.create(buyerUsername=q.username,offer=p)
        my_bucket=Bucket.objects.filter(buyerUsername=un)
        context = {'my_bucket': my_bucket}
        return render(request, 'bucket.html',context)

    else :
        my_bucket=Bucket.objects.filter(buyerUsername=un)
        context = {'my_bucket': my_bucket}
        return render(request, 'bucket_invalid.html',context)




def bucket(request):
    print(Bucket.objects.all())
    return HttpResponseRedirect('/bucket/')


def bucket(request,un):
    my_bucket=Bucket.objects.filter(buyerUsername=un)
    context = {'my_bucket': my_bucket}
    return render(request, 'bucket.html',context)


def bucket_invalid(request,un):

    my_bucket=Bucket.objects.filter(buyerUsername=un)
    context = {'my_bucket': my_bucket}
    return render(request, 'bucket.html',context)

def bucket_delete(request,pk,un):
    p = get_object_or_404(Offer, pk=pk)
    Bucket.objects.filter(buyerUsername=un,offer=p).delete()
    my_bucket=Bucket.objects.filter(buyerUsername=un)
    context = {'my_bucket': my_bucket}
    return render(request, 'bucket.html',context)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% OFERTY %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def offer_details(request,pk):
    offer=get_object_or_404(Offer, pk=pk)
    context1={'offer': offer}

    if(len(Flat.objects.filter(local=offer.local))!=0):
        flat=get_object_or_404(Flat,local=offer.local)
        context={'offer': offer,'flat': flat}
        return render(request, 'offer/detailsF.html',context)

    elif(len(Home.objects.filter(local=offer.local))!=0):
        home=get_object_or_404(Home,local=offer.local)
        context={'offer': offer,'home': home}
        return render(request, 'offer/detailsH.html',context1)
    elif(len(Office.objects.filter(local=offer.local))!=0):
        office=get_object_or_404(Flat,local=offer.local)
        context={'offer': offer,'office': office}
        return render(request, 'offer/detailsO.html',context1)
    else:
        another=get_object_or_404(Another,local=offer.local)
        context={'offer': offer,'another': another}
        return render(request, 'offer/detailsA.html.html',context1)

local=LocalMy.objects.all()
def wyszukaj(request):

    if request.POST:
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            find_list=[]
            city = request.POST.get('city', '')
            if(city!=""):
                q=list(Offer.objects.filter(city=city).values())
                find_list=wstaw(find_list,q)
            sizeMin=request.POST.get('sizeMin', '')
            if(sizeMin>0):
                localM=LocalMy.objects.filter(size__gt=sizeMin)
                for i in localM:
                    q=list(Offer.objects.filter(local=i))
                    find_list=wstaw(find_list,q)
            sizeMax=request.POST.get('sizeMax', '')
            if(sizeMax>0):
                localM=LocalMy.objects.filter(size__lt=sizeMax)
                for i in localM:
                    q=list(Offer.objects.filter(local=i))
                    find_list=wstaw(find_list,q)
            minRooms=request.POST.get('minRooms', '')
            if(minRooms>0):
                localM=LocalMy.objects.filter(numberOfRooms__gt=minRooms)
                for i in localM:
                    q=list(Offer.objects.filter(local=i))
                    find_list=wstaw(find_list,q)
            maxRooms=request.POST.get('maxRooms', '')
            if(maxRooms>0):
                localM=LocalMy.objects.filter(numberOfRooms__lt=maxRooms)
                for i in localM:
                    q=list(Offer.objects.filter(local=i))
                    find_list=wstaw(find_list,q)
            priceMin=request.POST.get('priceMin', '')
            if(priceMin>0):
                q=list(Offer.objects.filter(price__gt=priceMin))
                find_list=wstaw(find_list,q)
            priceMax=request.POST.get('priceMax', '')
            if(priceMax>0):
                q=list(Offer.objects.filter(price__lt=priceMax))
                find_list=wstaw(find_list,q)
            elevator=request.POST.get('elevator', '')
            if(elevator):
                flatM=Flat.objects.filter(elevator=True)
                officeM=Office.objects.filter(elevator=True)
                for i in flatM:
                    q=list(Offer.objects.filter(local=i.local))
                    find_list=wstaw(find_list,q)
                for i in officeM:
                    q=list(Offer.objects.filter(local=i.local))
                    find_list=wstaw(find_list,q)
            balcony=request.POST.get('balcony', '')
            if(balcony):
                flatM=Flat.objects.filter(balcony=True)
                homeM=Home.objects.filter(numberOfBalcony__gt=0)
                for i in flatM:
                    q=list(Offer.objects.filter(local=i.local))
                    find_list=wstaw(find_list,q)
                for i in homeM:
                    q=list(Offer.objects.filter(local=i.local))
                    find_list=wstaw(find_list,q)
            gardenSizeMin=request.POST.get('gardenSizeMin', '')
            if(gardenSizeMin>0):
                homeM=Home.objects.filter(gardenSize__gt=gardenSizeMin)
                for i in homeM:
                    q=list(Offer.objects.filter(local=i.local))
                    find_list=wstaw(find_list,q)
            gardenSizeMax=request.POST.get('gardenSizeMax', '')
            if(gardenSizeMax>0):
                homeM=Home.objects.filter(gardenSize__lt=gardenSizeMax)
                for i in homeM:
                    q=list(Offer.objects.filter(local=i.local))
                    find_list=wstaw(find_list,q)

            local=find_list
            context={'local': local}
            return render_to_response('wyniki.html',context)
    else:
        form = ArticleForm()

    args = {}
    args.update(csrf(request))
    args['form'] = form

    return render_to_response('wyszukiwarka.html', args)
def wstaw(find,lista):
    for i in lista:
        a=0
        for j in find:
            if j==i:
                a=1
        if a==0:
            find.append(i)
    return find

def wyniki(request):
    print("DUPA")
    context={'local':local}
    return render_to_response('wyniki.html',context)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% LOGOWANIE I REJESTRACJA %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/accounts/invalid/')

def loggedin(request):
    return render_to_response('loggedin.html',
                              {'full_name': request.user.username})

def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


from django.contrib.auth.forms import UserCreationForm
def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success/')

    else:
        form = UserCreationForm()
    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('register.html', args)



def register_success(request):
    return render_to_response('register_success.html')



#############################formularz####################################################


from .forms import BuyerForm
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404





def form_new(request):

    # list=Buyer.objects.filter(user=request.user)
    # if(len(list)==0):

        if request.method == "POST":
            form = BuyerForm(request.POST)
            if form.is_valid():

                post = form.save(commit=False)
                post.user = request.user
                post.save()
                return render(request, 'form.html', {'form': form})
               # return redirect('views.post_detail', pk=post.pk)

        else:


            form = BuyerForm()

        return render(request, 'form_edit.html', {'form': form})