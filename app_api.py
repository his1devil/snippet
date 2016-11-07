# -*- coding: utf-8 -*-
from flask import Flask, jsonify
from flask.views import MethodView

# 基于调度方法的视图
# flask.views.MethodView 对每个HTTP方法执行不同的函数 开发RESTful API
app = Flask(__name__)


class UserAPI(MethodView):
    def get(self):
        return jsonify({
            'username': 'fake',
            'avatar': 'http://#/'
        })

    def post(self):
        return 'UNSUPPORTED'

app.add_url_rule('/user', views.func=UserAPI.as_view('userview'))

