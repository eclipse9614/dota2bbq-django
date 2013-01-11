from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib.auth import authenticate, login, logout
from django.forms.models import inlineformset_factory
from dota2bbq.models import Hero, Item, Skill, Composition, SkillBuild



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


def community(request):
    return render(request, 'dota2bbq/community.html')


def hero(request, hero_name):
    try:
        hero = Hero.objects.get(name = hero_name)
        if hero:
            skills = hero.skill_set.order_by('number')
            skillbuilds = hero.skillbuild_set.order_by('number')
            skillmapper = {skill.id:skill.name for skill in skills}
            skillmapper[0] = u'Stats' #add stats for skill build
            for skillbuild in skillbuilds:
                skillbuild.build = skillbuild.build.split(',')
                skillbuild.build = [skillmapper[int(skill)] for skill in skillbuild.build]

            entry = dict(hero = hero, skills = skills, skillbuilds = skillbuilds)
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

