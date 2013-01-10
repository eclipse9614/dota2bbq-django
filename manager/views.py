from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms.models import inlineformset_factory
from dota2bbq.models import Hero, Item, Skill, Composition, SkillBuild
from manager.modelforms import HeroForm, ItemForm, GenereateSkillBuildForm


@login_required
def manage(request):
    heroes = Hero.objects.values('name').order_by('name')
    items = Item.objects.values('name').order_by('name')
    return render(request, 'manager/manage.html', {'heroes': heroes, 'items': items})


@login_required
def hero_create(request):
    if request.method == 'GET':
        hform = HeroForm()
    elif request.method == 'POST':
        hform = HeroForm(request.POST)
        if hform.is_valid():
            hform.save()
            return redirect('manager.views.manage')

    return render(request, 'manager/hero_edit.html', {'HeroForm': hform}) # this happens when GET or POST fails


@login_required
def hero_edit(request, hero_name):
    hero = get_object_or_404(Hero, name = hero_name)
    if request.method == 'GET':
        hform = HeroForm(instance = hero)
    elif request.method == 'POST':
        hform = HeroForm(request.POST, instance = hero)
        if hform.is_valid():
            hform.save()
            return redirect('manager.views.manage')
    return render(request, 'manager/hero_edit.html', {'HeroForm': hform}) # this happens when GET or POST fails


@login_required
def hero_delete(request, hero_name):
    hero = get_object_or_404(Hero, name = hero_name)
    hero.delete()
    return redirect('manager.views.manage')


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
            return redirect('manager.views.manage')

    return render(request, 'manager/skill_edit.html', {'SkillForms': sforms}) # this happens when GET or POST fails


@login_required
def skillbuild_edit(request, hero_name):
    hero = get_object_or_404(Hero, name = hero_name)
    mainSkills = list(hero.skill_set.filter(is_main = True).order_by('number').values_list('id', 'name'))
    SkillBuildFormSet = inlineformset_factory(Hero, SkillBuild, extra = 1, form = GenereateSkillBuildForm(mainSkills))
    if request.method == 'GET':
        sforms = SkillBuildFormSet(instance = hero, queryset = hero.skillbuild_set.order_by('number'))
    elif request.method == 'POST':
        sforms = SkillBuildFormSet(request.POST, instance = hero)
        if sforms.is_valid():
            sforms.save()
            return redirect('manager.views.manage')
    return render(request, 'manager/skillbuild_edit.html', {'SkillBuildForms': sforms}) # this happens when GET or POST fails


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
            return redirect('manager.views.manage')
    
    # this happens when get or post fails
    items = Item.objects.values('name').order_by('name')
    return render(request, 'manager/item_edit.html', {'ItemForm': iform, 'Recipe': recipe, 'Items': items})


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
            return redirect('manager.views.manage')

    items = Item.objects.values('name').order_by('name')
    return render(request, 'manager/item_edit.html', {'ItemForm': iform, 'Recipe': recipe, 'Items': items})


@login_required
def item_delete(request, item_name):
    item = get_object_or_404(Item, name = item_name)
    item.delete()
    return redirect('manager.views.manage')