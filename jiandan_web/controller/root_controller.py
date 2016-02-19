# -*- coding:utf-8 -*-
from flask import render_template, redirect, url_for, request, session, Markup
from jiandan_web import app
from jiandan_web.controller import case_from_request
from datacenter.duanzi_web_service import get_duanzi_by_page
from datacenter.duanzi_web_service import total_counts
from datacenter.duanzi_web_service import get_oneday_100zan_req
from datacenter.duanzi_web_service import get_key_when_no_today_key
from util.jsonutil import json_to_list


@app.route('/duan')
def index():
    page_size = app.config.get("PAGE_SIZE")
    page = request.values.get('page')
    seq = []
    if page == None:
        page = 1
    try :
        page = int(page)
        seq = get_duanzi_by_page(page, page_size)
    except:
        pass

    if seq == [] and page != 1:
        return redirect(url_for("index"))

    return render_template('index.html', page_size=page_size, page=page, seq=seq,
                           total_counts=total_counts())


# 每日新破百段子
# @app.route('/new_duan')
# def new_duan():
#     return ''

#
# @app.route('/get_oneday_100zan')
# def get_oneday_100zan():
#     day = request.values.get('day')
#     if not day:
#         day = get_key_when_no_today_key()
#     return get_oneday_100zan_req(day)
