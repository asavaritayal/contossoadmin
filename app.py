from flask import Flask, redirect, url_for
from flask_dance.contrib.github import make_github_blueprint, github
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asavari'

github_blueprint = make_github_blueprint(client_id='9f3766fa9dc141a8f6fc',client_secret='8e9e4acd5418e8c0d1719ab36bc6486631e214e4')

app.register_blueprint(github_blueprint, url_prefix='/github_login')

@app.route('/github')
def github_login():
	if not github.authorized:
		return redirect(url_for('github.login'))

	commit_info = github.get('/repos/azure/azure-functions-host/commits')

	if commit_info.ok:
		commits = len(commit_info.json())
		hours = commits

		cups = requests.get(f'https://coffeeandcodeatbuild.azurewebsites.net/api/HttpTrigger?hours={hours}')

		return str(cups.json())

	return '<h1>Request failed!</h1>'

if __name__ == '__main__':
	app.run(debug=True)
