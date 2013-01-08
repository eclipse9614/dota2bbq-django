import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.forms.models import inlineformset_factory
from dota2bbq.models import Hero, Item, Skill, Composition, SkillBuild
from dota2bbq.modelforms import HeroForm, ItemForm, GenereateSkillBuildForm


def index(request):
    if 'next' in request.GET and request.user.is_authenticated():
        return redirect(request.GET['next'])
    else:
	   return render(request, 'dota2bbq/index.html')


def heroes(request):
    enqry = {'heroes': Hero.objects.values('name', 'faction', 'specialty')}
    return render(request, 'dota2bbq/heroes.html', enqry)


def items(request):
    items = Item.objects.exclude(kind = 0).order_by('kind', 'cost').values('id', 'name')
    kinds = Item.get_kinds_display()[:-1]
    enqry = [{'kind': kind[1], 'items': items.filter(kind = kind[0])} for kind in kinds]
    return render(request, 'dota2bbq/items.html', {'item_set': enqry})


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
    if request.method == 'POST':
        username = request.POST['username'] if 'username' in request.POST else ''
        password = request.POST['password'] if 'password' in request.POST else ''
        user = authenticate(username = username, password = password)
        if user and user.is_active:
            login(request, user)
        else:
            request.session['login_error'] = 'wrong username or password'
        return redirect(request.META['HTTP_REFERER']) if "HTTP_REFERER" in request.META else redirect('dota2bbq.views.index')
    else:
        return redirect('dota2bbq.views.index')


def signoff(request):
    if request.method == 'POST':
        logout(request)
        return redirect(request.META['HTTP_REFERER'])
    else:
        return redirect('dota2bbq.views.index')


@login_required
def manage(request):
    heroes = Hero.objects.values('name').order_by('name')
    items = Item.objects.values('name').order_by('name')
    return render(request, 'dota2bbq/manage.html', {'heroes': heroes, 'items': items})


@login_required
def hero_create(request):
    if request.method == 'GET':
        hform = HeroForm()
    elif request.method == 'POST':
        hform = HeroForm(request.POST)
        if hform.is_valid():
            hform.save()
            return redirect('dota2bbq.views.manage')

    return render(request, 'dota2bbq/hero_edit.html', {'HeroForm': hform}) # this happens when GET or POST fails


@login_required
def hero_edit(request, hero_name):
    hero = get_object_or_404(Hero, name = hero_name)
    if request.method == 'GET':
        hform = HeroForm(instance = hero)
    elif request.method == 'POST':
        hform = HeroForm(request.POST, instance = hero)
        if hform.is_valid():
            hform.save()
            return redirect('dota2bbq.views.manage')
    return render(request, 'dota2bbq/hero_edit.html', {'HeroForm': hform}) # this happens when GET or POST fails


@login_required
def hero_delete(request, hero_name):
    hero = get_object_or_404(Hero, name = hero_name)
    hero.delete()
    return redirect('dota2bbq.views.manage')


@login_required
def skill_edit(request, hero_name):
    hero = get_object_or_404(Hero, name = hero_name)
    SkillFormSet = inlineformset_factory(Hero, Skill, extra = 2)
    if request.method == 'GET':
        sforms = SkillFormSet(instance = hero, queryset = hero.skill_set.order_by('number'))
    elif request.method == 'POST':
        sforms = SkillFormSet(request.POST, instance = hero)
        if sforms.is_valid():
            sforms.save()
            return redirect('dota2bbq.views.manage')

    return render(request, 'dota2bbq/skill_edit.html', {'SkillForms': sforms}) # this happens when GET or POST fails


@login_required
def skill_build(request, hero_name):
    hero = get_object_or_404(Hero, name = hero_name)
    mainSkills = list(hero.skill_set.filter(is_main = True).order_by('number').values_list('id', 'name'))
    SkillBuildFormSet = inlineformset_factory(Hero, SkillBuild, extra = 1, form = GenereateSkillBuildForm(mainSkills))
    if request.method == 'GET':
        sforms = SkillBuildFormSet(instance = hero, queryset = hero.skillbuild_set.order_by('number'))
    elif request.method == 'POST':
        sforms = SkillBuildFormSet(request.POST, instance = hero)
        if sforms.is_valid():
            sforms.save()
            return redirect('dota2bbq.views.manage')
    return render(request, 'dota2bbq/skill_build.html', {'SkillBuildForms': sforms}) # this happens when GET or POST fails


@login_required
def item_create(request):
    if request.method == 'GET':
        iform = ItemForm()
        recipe = []

    elif request.method == 'POST':
        recipe = request.POST['recipe']
        if recipe != '':
            recipe = recipe.split('/')
        else:
            recipe = []
        iform = ItemForm(request.POST)
        if iform.is_valid():
            item = iform.save()
            components = []
            for component_name in recipe:
                component = get_object_or_404(Item, name = component_name)
                components.append(component)
            for component in components:
                Composition(whole_id = item.id, component_id = component.id).save()
            return redirect('dota2bbq.views.manage')
    
    # this happens when get or post fails
    items = Item.objects.values('name').order_by('name')
    return render(request, 'dota2bbq/item_edit.html', {'ItemForm': iform, 'Recipe': recipe, 'Items': items})


@login_required
def item_edit(request, item_name):
    item = get_object_or_404(Item, name = item_name)
    if request.method == 'GET':
        iform = ItemForm(instance = item)
        recipe = [Item.objects.get(id = component.component_id).name for component in item.as_a_whole.all()]
    elif request.method == 'POST':
        recipe = request.POST['recipe']
        if recipe != '':
            recipe = recipe.split('/')
        else:
            recipe = []
        iform = ItemForm(request.POST, instance = item)
        if iform.is_valid():
            iform.save()
            components = []
            for component_name in recipe:
                component = get_object_or_404(Item, name = component_name)
                components.append(component)
            item.as_a_whole.all().delete()
            for component in components:
                Composition(whole_id = item.id, component_id = component.id).save()
            return redirect('dota2bbq.views.manage')

    items = Item.objects.values('name').order_by('name')
    return render(request, 'dota2bbq/item_edit.html', {'ItemForm': iform, 'Recipe': recipe, 'Items': items})


@login_required
def item_delete(request, item_name):
    item = get_object_or_404(Item, name = item_name)
    item.delete()
    return redirect('dota2bbq.views.manage')


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