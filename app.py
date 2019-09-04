import os

import django
from chalice import Chalice, ConflictError, UnprocessableEntityError, NotFoundError
from django.db import IntegrityError


def create_app():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chalicelib.data.settings")
    django.setup()
    return Chalice(app_name='tenants')


app = create_app()


from chalicelib.data.models.models import Tenant


@app.route('/', methods=('GET', ))
def index():
    return {
        'login': '/login',
        'tenants': '/tenants',
    }


@app.route('/tenants', methods=('POST',))
def tenant_new():
    request = app.current_request
    data = request.json_body
    try:
        tenant = Tenant(name=data['name'])
        tenant.save()
    except KeyError:
        raise UnprocessableEntityError('Tenant object missing attribute "name"')
    except IntegrityError:
        raise ConflictError('A tenant with this name already exists')
    return tenant.to_dict()


@app.route('/tenants', methods=('GET',))
def tenant_list():
    return [tenant.to_dict() for tenant in Tenant.objects.all()]


@app.route('/tenants/{tenant_id}', methods=('GET',))
def tenant_retrieve_one(tenant_id):
    try:
        return Tenant.objects.get(pk=tenant_id).to_dict()
    except Tenant.DoesNotExist:
        raise NotFoundError(f'Tenant with id: {tenant_id} was not found')
