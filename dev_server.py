#!/usr/bin/env python
import config
import app

import bottle

DEV_MODE=True

bottle.run(
    app.app,
    host=config.HTTP_HOST,
    port=config.HTTP_PORT,
    debug=DEV_MODE,
    reloader=DEV_MODE,
)

