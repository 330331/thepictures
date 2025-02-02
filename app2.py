from flask import Flask, render_template, request

app = Flask(__name__)

# 首页路由，展示一个 HTML 表单
@app.route('/')
def home():
    return render_template('index.html')

# 处理表单提交的路由
@app.route('/submit', methods=['POST'])
def submit():
    # 从表单获取数据
    name = request.form.get('name')
    age = request.form.get('age')
    return render_template('result.html', name=name, age=age)

if __name__ == '__main__':
    app.run(debug=True)
