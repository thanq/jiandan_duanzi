# -*- coding:utf-8 -*-


import os
import jd_web_config as config

from flask import Flask

app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)

import jiandan_web.controller.root_controller