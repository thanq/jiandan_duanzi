# -*- coding:utf-8 -*-


import os
import jd_web_config as config

from flask import Flask

app = Flask(__name__)

if os.environ.get('PRODUCTION') != "PRODUCTION":
    app.config.from_object(config.DevelopmentConfig)
else:
    app.config.from_object(config.ProductionConfig)

import jiandan_web.controller.root_controller