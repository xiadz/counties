import bottle

app = bottle.Bottle()

@app.get('/')
def root():
    return 'hello there'
