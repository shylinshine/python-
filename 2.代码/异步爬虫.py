from flask import Flask
# 实例化一个app
app=Flask(__name__)
# 创建视图函数和路由地址
@app.route('/bobo')
def index_1():
    return 'hello bobo'


@app.route('/jay')
def index_2():
    return

if __name__=="__main__":
    app.run(debug=True)
