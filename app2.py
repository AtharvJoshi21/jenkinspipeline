from flask import Flask, render_template, redirect, request
import jenkins
import os

host = os.getenv('JENKINS_HOST', 'http://localhost:8080/')
username = os.getenv('JENKINS_USERNAME', 'jenkins')
password = os.getenv('JENKINS_PASSWORD', 'Atharv@21')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def create():
    try:
        server = jenkins.Jenkins(host, username=username, password=password)
        print("Connected to Jenkins")
        server.build_job('task-1/main')
    except jenkins.JenkinsException as e:
        print(f"Jenkins error: {e}")
    except Exception as e:
        print(f"General error: {e}")
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
