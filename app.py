from flask import Flask, redirect, url_for
from flask_dance.contrib.github import make_github_blueprint, github
import requests

from pprint import pprint as pp
from flask import Flask, flash, redirect, render_template, request, url_for
import os

from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asavari'

id = os.environ['CLIENT_ID']
secret = os.environ['CLIENT_SECRET']
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

github_blueprint = make_github_blueprint(client_id=id ,client_secret=secret)
app.register_blueprint(github_blueprint, url_prefix='/github_login')

@app.route('/')
def index():
    return render_template(
        'index.html',
        data=[{'name':'azure-functions'}, {'name':'azure-functions-host'}, {'name':'azure-functions-core-tools'}, {'name':'azure-functions-python-worker'}, {'name':'azure-functions-python-library'}])

@app.route('/github', methods=['GET', 'POST'])
def github_login():
	if not github.authorized:
		return redirect(url_for('github.login'))

	select = request.form.get('comp_select')
	last_date_time = (datetime.now() - timedelta(hours = 240)).isoformat()
	last_date_time = last_date_time[:19]+"Z"

	commit_info = github.get(f'/repos/azure/{select}/commits?since={last_date_time}')

	if commit_info.ok:
		commits = len(commit_info.json())
		hours = commits * 10

		cups = requests.get(f'https://coffeeandcodeatbuild.azurewebsites.net/api/HttpTrigger?hours={hours}')

		return render_template(
        	'result.html',
			hours = hours,
        	cups=int(cups.json()))

	return '<h1>Request failed!</h1>'

if __name__ == '__main__':
	app.run(debug=True)
