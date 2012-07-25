import urllib
import httplib
import json
from servers.models import Server
from instances.models import Instance, Image, Flavor
from floatingips.models import Floatingip, Pool
import paramiko

host_ip = "10.1.247.77"
token_port = "5000"
compute_port = "8774"

def get_token(tenant_id):
    # arguments

    ## make sure that url is set to the actual hostname/IP address,
    ## port number

    url = "%s:%s" % (host_ip, token_port)

    ## make sure that osuser is set to your actual username, "admin"
    ## works for test installs on virtual machines, but it's a hack

    osuser = "admin"

    ## use something else than "shhh" for you password

    ospassword = "admin"

    params = '{"auth":{"passwordCredentials":{"username":"%s", "password":"%s"}, "tenantId":"%s"}}' % (osuser, ospassword, tenant_id)

    headers = {"Content-Type":"application/json"}

    # HTTP connection

    conn = httplib.HTTPConnection(url)
    conn.request("POST", "/v2.0/tokens", params, headers)

    # HTTP response

    response = conn.getresponse()
    data = response.read()
    dd = json.loads(data)

    conn.close()

    apitoken = dd['access']['token']['id']

    return apitoken

def save_server_detail(tenant_id, token):
    # arguments

    ## make sure that url is set to the actual hostname/IP address,
    ## port number

    url = "%s:%s" % (host_ip, compute_port)

    params = urllib.urlencode({})

    headers = {"X-Auth-Token":"%s" % token, "Content-Type":"application/json"}

    # HTTP connection

    conn = httplib.HTTPConnection(url)
    conn.request("GET", "/v2/%s/servers/detail" % tenant_id, params, headers)

    # HTTP response

    response = conn.getresponse()
    data = response.read()
    dd = json.loads(data)

    conn.close()

    for server in dd['servers']:
        im = Image.objects.get(id=server['image']['id'])
        f = Flavor.objects.get(id=server['flavor']['id'])
        i = Instance(id=server['id'], name=server['name'], image=im, flavor=f)
        i.save()

def save_image_detail(tenant_id, token):
    # arguments

    ## make sure that url is set to the actual hostname/IP address,
    ## port number

    url = "%s:%s" % (host_ip, compute_port)

    params = urllib.urlencode({})

    headers = {"X-Auth-Token":"%s" % token, "Content-Type":"application/json"}

    # HTTP connection

    conn = httplib.HTTPConnection(url)
    conn.request("GET", "/v2/%s/images/detail" % tenant_id, params, headers)

    # HTTP response

    response = conn.getresponse()
    data = response.read()
    dd = json.loads(data)

    conn.close()

    for image in dd['images']:
        i = Image(id=image['id'], name=image['name'])
        i.save()

def save_flavor_detail(tenant_id, token):
    # arguments

    ## make sure that url is set to the actual hostname/IP address,
    ## port number

    url = "%s:%s" % (host_ip, compute_port)

    params = urllib.urlencode({})

    headers = {"X-Auth-Token":"%s" % token, "Content-Type":"application/json"}

    # HTTP connection

    conn = httplib.HTTPConnection(url)
    conn.request("GET", "/v2/%s/flavors/detail" % tenant_id, params, headers)

    # HTTP response

    response = conn.getresponse()
    data = response.read()
    dd = json.loads(data)

    conn.close()

    for flavor in dd['flavors']:
        f = Flavor(id=flavor['id'], name=flavor['name'])
        f.save()

def create_server(tenant_id, token, name, image_ref, flavor_ref):
    # arguments

    ## make sure that url is set to the actual hostname/IP address,
    ## port number

    url = "%s:%s" % (host_ip, compute_port)

    params = '{"server":{"name":"%s", "imageRef":"%s", "flavorRef":"%s"}}' % (name, image_ref, flavor_ref)

    headers = {"X-Auth-Token":"%s" % token, "Content-Type":"application/json"}

    # HTTP connection

    conn = httplib.HTTPConnection(url)
    conn.request("POST", "/v2/%s/servers" % tenant_id, params, headers)

    # HTTP response

    response = conn.getresponse()
    data = response.read()
    dd = json.loads(data)

    conn.close()

def save_floatingip_detail(tenant_id, token):
    # arguments

    ## make sure that url is set to the actual hostname/IP address,
    ## port number

    url = "%s:%s" % (host_ip, compute_port)

    params = urllib.urlencode({})

    headers = {"X-Auth-Token":"%s" % token, "Content-Type":"application/json"}

    # HTTP connection

    conn = httplib.HTTPConnection(url)
    conn.request("GET", "/v2/%s/os-floating-ips" % tenant_id, params, headers)

    # HTTP response

    response = conn.getresponse()
    data = response.read()
    dd = json.loads(data)

    conn.close()

    for floatingip in dd['floating_ips']:
        p = Pool.objects.get(id=floatingip['pool'])
        f = Floatingip(id=floatingip['id'], ip=floatingip['ip'], pool=p, instance_id=floatingip['instance_id'])
        f.save()

def save_pool_detail(tenant_id, token):
    # arguments

    ## make sure that url is set to the actual hostname/IP address,
    ## port number

    url = "%s:%s" % (host_ip, compute_port)

    params = urllib.urlencode({})

    headers = {"X-Auth-Token":"%s" % token, "Content-Type":"application/json"}

    # HTTP connection

    conn = httplib.HTTPConnection(url)
    conn.request("GET", "/v2/%s/os-floating-ip-pools" % tenant_id, params, headers)

    # HTTP response

    response = conn.getresponse()
    data = response.read()
    dd = json.loads(data)

    conn.close()

    for pool in dd['floating_ip_pools']:
        p = Pool(id=pool['name'], name=pool['name'])
        p.save()

def create_floatingip(tenant_id, token, pool):
    # arguments

    ## make sure that url is set to the actual hostname/IP address,
    ## port number

    url = "%s:%s" % (host_ip, compute_port)

    params = '{"pool":"%s"}' % pool

    headers = {"X-Auth-Token":"%s" % token, "Content-Type":"application/json"}

    # HTTP connection

    conn = httplib.HTTPConnection(url)
    conn.request("POST", "/v2/%s/os-floating-ips" % tenant_id, params, headers)

    # HTTP response

    response = conn.getresponse()
    data = response.read()
    dd = json.loads(data)

    conn.close()

def associate_floatingip(tenant_name, ip, instance_id):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host_ip, username="root", password="root123")
    cmd = "nova --os_username admin --os_password admin --os_tenant_name %s --os_auth_url http://localhost:5000/v2.0 add-floating-ip %s %s" % (tenant_name, instance_id, ip)
    ssh.exec_command(cmd)
