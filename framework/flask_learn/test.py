from flask import Flask, current_app, g, request, session
# current_app 当前应用实例
# g 处理请求时的临时存储对象 每次请求都会重设
# request 请求对象
# session 会话对象

app = Flask(__name__)

@app.route('/')
def hello_world():
  print(current_app)
  return 'hello world'

@app.route('/user/<username>')
def show_user(username):
  return 'hello %s' %(username)

@app.route('/page/')
@app.route('/page/<page>')
def show_page(page=None):
  return 'page is %s' %(page)