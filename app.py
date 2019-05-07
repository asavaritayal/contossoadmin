from flask import Flask, redirect, url_for
from flask_dance.contrib.github import make_github_blueprint, github
import requests

from pprint import pprint as pp
from flask import Flask, flash, redirect, render_template, request, url_for
# from weather import query_api

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asavari'

@app.route('/')
def index():
    return render_template(
        'index.html',
        data=[{'name':'azure-functions'}, {'name':'azure-functions-host'}, {'name':'azure-functions-core-tools'}, {'name':'azure-functions-python-worker'}, {'name':'azure-functions-python-library'}])

github_blueprint = make_github_blueprint(client_id='9f3766fa9dc141a8f6fc',client_secret='8e9e4acd5418e8c0d1719ab36bc6486631e214e4')
app.register_blueprint(github_blueprint, url_prefix='/github_login')

@app.route('/github', methods=['GET', 'POST'])
def github_login():
	if not github.authorized:
		return redirect(url_for('github.login'))

	select = request.form.get('comp_select')
	commit_info = github.get(f'/repos/azure/{select}/commits')

	if commit_info.ok:
		commits = len(commit_info.json())
		print(commits)
		hours = commits

		cups = requests.get(f'https://coffeeandcodeatbuild.azurewebsites.net/api/HttpTrigger?hours={hours}')

		return render_template(
        	'result.html',
			hours = hours,
        	cups=int(cups.json()))

	return '<h1>Request failed!</h1>'

if __name__ == '__main__':
	app.run(debug=True)
