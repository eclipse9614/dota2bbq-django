import json
import urllib2
from django.http import HttpResponse
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from dota2bbq.models import Hero, Item



def combined(request):
    query = [{'Class': 'Hero', 'Name': row['name']} for row in Hero.objects.values('name')]
    query += [{'Class': 'Item', 'ID': row['id'], 'Name': row['name']} for row in Item.objects.values('id', 'name')]
    return HttpResponse(json.dumps(query))


def items(request):
    items = Item.objects.all()
    if len(items) == 0:
        result = {'Result': 'None'}
    else:
        result = {'Result': 'OK', "Content":
        [{'ID': item.id, 'Name': item.name, 'Cost': item.cost, 'Description': item.description,
        'Usage': item.usage, 'Attributes': item.attributes,
        'Recipe': [Item.objects.get(id = component.component_id).name for component in item.as_a_whole.all()]} for item in items]}
    return HttpResponse(json.dumps(result))


def feed(request):
    if request.method == 'GET':
        result = {}
        if 'url' in request.GET:
            url = request.GET['url']
            validateFeedUrl = URLValidator(verify_exists = True)
            try:
                validateFeedUrl(url)
            except ValidationError:
                result['Result'] = 'ERROR'
                result['Content'] = 'Please provide right URL for the feed.'
                return HttpResponse(json.dumps(result))

            try:
                content = urllib2.urlopen(url)
            except urllib2.URLError, urllib2.HTTPError:
                result['Result'] = 'ERROR'
                result['Content'] = 'Something wrong with the connection.'
                return HttpResponse(json.dumps(result))
            result['Result'] = 'SUCCESS'
            result['Content'] = content.read()
        else:
            result['Result'] = 'ERROR'
            result['Content'] = 'Please provide URL for the feed'
        return HttpResponse(json.dumps(result))