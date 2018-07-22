from flask import Flask, request, Response

app = Flask(__name__, static_path='/', static_folder='static', static_url_path='/static')

@app.route('/')
def main():
    return app.send_static_file('index.html')

@app.route('/image/<filename>')
def image(filename):
    return app.send_static_file(filename)

if __name__ == '__main__':
    app.run()