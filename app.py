import bottle
import us

app = bottle.Bottle()

@app.get('/')
@bottle.view('index.tpl')
def app_root():
    return dict(name="hhh")

@app.get('/fips')
@bottle.view('fips.tpl')
def app_fips():
    states = list(us.STATES)
    return dict(states=states)


@app.get('/static/<filepath:path>')
def app_static(filepath):
    return bottle.static_file(filepath, root='static/')
