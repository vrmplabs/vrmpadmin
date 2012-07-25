from django.http import HttpResponseRedirect
from common import api
from floatingips.models import Floatingip, Pool
from instances.models import Instance
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    tenant_id = '09688e8787a84ab5b103c7721cecb1ce'
    token = api.get_token(tenant_id)

    floatingips = Floatingip.objects.all()
    floatingips.delete()

    api.save_floatingip_detail(tenant_id, token)

    return HttpResponseRedirect('/admin/floatingips/floatingip/')

def add(request):
    tenant_id = '09688e8787a84ab5b103c7721cecb1ce'
    token = api.get_token(tenant_id)

    pools = Pool.objects.all()
    pools.delete()

    api.save_pool_detail(tenant_id, token)

    return HttpResponseRedirect('/admin/floatingips/floatingip/add/')

def save(request): 
    tenant_id = '09688e8787a84ab5b103c7721cecb1ce'
    token = api.get_token(tenant_id)

    pool = request.POST['pool']

    api.create_floatingip(tenant_id, token, pool)

    return HttpResponseRedirect('/admin/floatingips/floatingip/')

def associate(request):
    tenant_id = '09688e8787a84ab5b103c7721cecb1ce'
    token = api.get_token(tenant_id)

    ip = request.GET['ip']

    instances = Instance.objects.all()
    instances.delete()

    api.save_server_detail(tenant_id, token)

    instance_list = Instance.objects.all()

    return render_to_response('admin/floatingip_associate.html', {'ip':ip, 'instance_list':instance_list}, context_instance=RequestContext(request))

def associate_save(request):
    tenant_name = 'demo'

    ip = request.POST['ip']
    instance = request.POST['instance']

    api.associate_floatingip(tenant_name, ip, instance)

    return HttpResponseRedirect('/admin/floatingips/floatingip/')
