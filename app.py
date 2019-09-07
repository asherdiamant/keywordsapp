# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request
from keywords import get_suggestions

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        suggestion_list = get_suggestions(request.form['queryroot'])
    return render_template('keywords.html', suggestion_list = suggestion_list)
@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)