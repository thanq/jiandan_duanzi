# -*- coding:utf-8 -*-

from functools import wraps
from flask import session, redirect, url_for, render_template, request
import time


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        print session.get('user')
        if session.get('user') is None:
            return redirect(url_for('user.login'))
        return f(*args, **kwargs)
    return decorated_function


def templated(template=None):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            template_name = template
            if template_name is None:
                template_name = request.endpoint \
                    .replace('.', '/') + '.html'
            ctx = f(*args, **kwargs)
            if ctx is None:
                ctx = {}
            elif not isinstance(ctx, dict):
                return ctx
            return render_template(template_name, **ctx)
        return decorated_function
    return decorator

class PageObj(object):
    pass

def case_from_request(Clazz=None, limit=False, ispage=False):
    '''
    生成Clazz对象, request里的参数会注入为该对象的属性
    '''
    if Clazz == None:
        o = PageObj()
    else:
        o = Clazz()
    _dict = []
    if limit:#如果要求生成的对象里不能包含类定义以外的参数
        _dict = [d for d in Clazz.__dict__ if not d.startswith('_')]

    for r in request.values.keys():
        if (not limit) or (r in _dict):
            o.__setattr__(r, request.values.get(r))

    if ispage: #如果需要分页
        if 'page' not in o.__dict__:
            o.__setattr__('page', 1)
        if 'rows' not in o.__dict__:
            o.__setattr__('rows', 30)
        o.page = int(o.page)
        o.rows = int(o.rows)
        o.__setattr__('offset', (o.page - 1) * o.rows )
    return o


#生成easy_ui grid可辨识的json格式
def json_page(total, rows):
    return '{"total":' + str(total) + ',"rows":' + str(rows) + '}'


