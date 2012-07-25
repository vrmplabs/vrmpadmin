from django.http import HttpResponseRedirect
from common import api
from instances.models import Instance, Image, Flavor

def index(request):
    tenant_id = '09688e8787a84ab5b103c7721cecb1ce'
    token = api.get_token(tenant_id)

    instances = Instance.objects.all()
    instances.delete()

    api.save_server_detail(tenant_id, token)

    return HttpResponseRedirect('/admin/instances/instance/')

def add(request):
    tenant_id = '09688e8787a84ab5b103c7721cecb1ce'
    token = api.get_token(tenant_id)

    images = Image.objects.all()
    images.delete()
    flavors = Flavor.objects.all()
    flavors.delete()

    api.save_image_detail(tenant_id, token)
    api.save_flavor_detail(tenant_id, token)

    return HttpResponseRedirect('/admin/instances/instance/add/')

def save(request):
    tenant_id = '09688e8787a84ab5b103c7721cecb1ce'
    token = api.get_token(tenant_id)

    name = request.POST['name']
    image = request.POST['image']
    flavor = request.POST['flavor']

    api.create_server(tenant_id, token, name, image, flavor)

    return HttpResponseRedirect('/admin/instances/instance/')
