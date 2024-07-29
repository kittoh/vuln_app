from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('x', '')
    return render_template('search.html', query=query)

if __name__ == '__main__':
    app.run(debug=True)
