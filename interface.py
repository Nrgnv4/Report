from flask import Flask, url_for, flash, render_template, request, json
import json
import main

app = Flask(__name__)
app.config.update(dict(
    # DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    DEBUG=True,
    SECRET_KEY='QfTjWnZr4u7w!z%C*F-JaNdRgUkXp2s5v8y/A?D(G+KbPeShVmYq3t6w9z$C&E)H',
    USERNAME='admin',
    PASSWORD='A?D(G+KbPeShVmYq'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        if 'del_empty_digital_signals' in request.form:
            a = {
                'DELETE_EMPTY_DIGITAL_SIGNALS': int(request.form['del_empty_digital_signals']),
                'IMAGE_TRANSPARENT': True,
                'IMAGE_FILENAME': "scope.png"
            }
        if 'image_transparent' in request.form:
            a = {
                'IMAGE_TRANSPARENT': int(request.form['image_transparent'])
            }

        if 'fix' in request.form:
            a = {
                'IMAGE_DPI': int(request.form['dpi']),
                'NUM_START': int(request.form['num_start'])
            }
        main.Helper().rewrite_settings(**a)

    sett = main.Helper().read_settings()
    return render_template(
        'settings.html',
        title='Шаг 1: Проверка настроек',
        **sett
    )

@app.route('/protocol_template', methods=['POST', 'GET'])
def make_protocol():
    json = main.Helper().load_json('tree.tmp')
    return render_template(
        'protocol_template.html',
        tree=json,
        title='Протокол'
    )

@app.route('/tree', methods=['POST', 'GET'])
def tree():
    a = main.Tree()
    tr = a.make_tree()
    return render_template(
        'tree.html',
        tree=tr,
        title='Шаг 2: Создание дерева протокола'
    )


@app.route('/get_len', methods=['GET', 'POST'])
def get_len():
    tree = main.Helper().load_json('checked.tmp')
    return json.dumps({'len': len(list(tree)) - 1})


@app.route('/iter', methods=['GET', 'POST'])
def iter():
    if int(request.form['iter']):
        main.Tree().make_images()
    return json.dumps({"start": 1})


@app.route('/scopes', methods=['POST', 'GET'])
def scopes():
    return render_template(
        'scopes.html',
        title='Шаг 3: Создание картинок осциллограмм'
    )

@app.route('/protocol', methods=['POST', 'GET'])
def protocol():
    return render_template(
        'protocol.html',
        title='Шаг 4: Создание протокола'
    )


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        a = {'username': request.form['username'],
             'password': request.form['password']}
        return render_template('login.html', error=error, **a)
    else:
        flash('New entry')
        error = 'Invalid username/password'
    # следущий код выполняется при методе запроса GET
    # или при признании полномочий недействительными
    return render_template('login.html', error=error)

# @app.route('/user/<username>')
# def profile(username): pass


# with app.test_request_context():
#  print (url_for('index'))
#  print (url_for('login'))
#  print (url_for('login', next='/'))
#  print (url_for('profile', username='John Doe'))
if __name__ == '__main__':
    app.run()
