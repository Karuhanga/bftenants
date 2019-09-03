from chalice import Chalice

app = Chalice(app_name='tenants')


@app.route('/', methods=('GET', ))
def index():
    return {
        'login': '/login',
        'tenants': '/tenants',
    }
