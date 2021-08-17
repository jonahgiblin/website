from flask import Flask, Response, send_from_directory, render_template

app = Flask('app', static_url_path='')

@app.route('/style.css')
def stylecss():
 print("hi")
 return send_from_directory('.', path='style.css')

@app.route('/style2.css')
def style2css():
 print("hi")
 return send_from_directory('.', path='style2.css')

@app.route('/images/CharlesOnlyFans1.jpg')
def Charles1():
 return send_from_directory('.', path='CharlesOnlyFans1.jpg')

@app.route('/images/CharlesOnlyFans2.jpg')
def Charles2():
 return send_from_directory('.', path='CharlesOnlyFans2.jpg')

@app.route('/images/CharlesOnlyFans3.jpg')
def Charles3():
 return send_from_directory('.', path='CharlesOnlyFans3.jpg')

@app.route('/images/default-logo.png')
def logo():
 return send_from_directory('.', path='images/default-logo.png')

@app.route('/')
def hello_world():
 response = Response("<!Perhaps this should be in Firefox?>")
 response.headers['link'] = '<style.css>; rel=stylesheet;'
 return response

@app.route('/macktubbies.png')
def macktub():
 return send_from_directory('.', path='images/macketubbies.png')

@app.route('/rickroll')
def astley():
 response = Response(render_template('index.html'))
 response.headers['link'] = '<style2.css>; rel=stylesheet;'
 return response
 



if __name__ == "__main__":
    app.run(debug=True)