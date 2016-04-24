from jolla import server
from jolla import plugins
from jolla import session

def index(request):
    return plugins.render('index.html')


def data(request):
    data = {'data':request['data']['ww']}
    return plugins.render_json(data)

def add(request):
    session.add_session('qq','ww')
    return 'yes'


class app(server.WebApp):
    urls = [
        (r'/', index),
        (r'/data', data),
        (r'/add',add)
    ]

if __name__ == '__main__':
    server = server.jolla_server(app)
    server.run_server()