from aiohttp import web
import socketio

cors_allow = '*'
sio = socketio.AsyncServer(cors_allowed_origins='*')
app = web.Application()

rec_path = './rec'

sio.attach(app)

@sio.event
def connect(sid, environ, auth):
    print('connect ', sid)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

@sio.on('recorded-chunk')
def to_file(sid, data):
    filename = data.get('filename')
    chunk = data.get('chunk')
    append_videofile(filename, chunk)
    print('append videofile')
    return dict(response='chunk recorded')

def append_videofile(filename, chunk):
    path = f'{rec_path}/{filename}.webm'
    with open(path, 'ab') as f:
        f.write(chunk)

if __name__ == '__main__':
    web.run_app(app, host='0.0.0.0', port=9011)
