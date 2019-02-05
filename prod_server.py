#!/usr/bin/env python
import config
import app

import bottle

bottle.run(
    app.app,
    host=config.HTTP_HOST,
    port=config.HTTP_PORT,
    debug=False,
    reloader=False,
)

