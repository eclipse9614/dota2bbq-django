import json
from django.shortcuts import render, redirect
from dota2bbq.models import Hero, Item
from django.http import HttpResponse, Http404
from django.contrib.auth import authenticate, login, logout

def index(request):
	return render(request, 'dota2bbq/index.html')


def heroes(request):
    enqry = {'heroes': Hero.objects.values('name', 'faction', 'specialty')}
    return render(request, 'dota2bbq/heroes.html', enqry)


def items(request):
    return render(request, 'dota2bbq/items.html')


def hero(request, hero_name):
    try:
        hero = Hero.objects.get(name = hero_name)
        if hero:
            skills = hero.skill_set.order_by('number')
            entry = dict(hero = hero, skills = skills)
            return render(request, 'dota2bbq/hero.html', entry)
    except Hero.DoesNotExist:
        raise Http404


def signin(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user and user.is_active:
            login(request, user)
        else:
            request.session['login_error'] = 'wrong username or password'
        return redirect(request.META['HTTP_REFERER']) if "HTTP_REFERER" in request.META else redirect('dota2bbq.views.index')
    else:
        return redirect('dota2bbq.views.index')


def signoff(request):
    if request.POST:
        logout(request)
        return redirect(request.META['HTTP_REFERER'])
    else:
        return redirect('dota2bbq.views.index')


def combined_feed(request):
    query = [{'Class': 'Hero', 'Name': row['name']} for row in Hero.objects.values('name')]
    query += [{'Class': 'Item', 'ID': row['id'], 'Name': row['name']} for row in Item.objects.values('id', 'name')]
    return HttpResponse(json.dumps(query))


def items_feed(request):
    items = Item.objects.all()
    if len(items) == 0:
        result = {'Result': 'None'}
    else:
        result = {'Result': 'OK', "Content":
        [{'ID': item.id, 'Name': item.name, 'Cost': item.cost, 'Description': item.description,
        'Usage': item.usage, 'Attributes': item.attributes,
        'Recipe': [Item.objects.get(id = component.component_id).name for component in item.as_a_whole.all()]} for item in items]}
    return HttpResponse(json.dumps(result))