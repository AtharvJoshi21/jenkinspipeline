from flask import Flask, render_template, redirect, request, url_for
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
    url = request.form.get('url')
    email = request.form.get('email')
    scan_type = request.form.get('scan_type')
    generate_report = request.form.get('generate_report')
    try:
        server = jenkins.Jenkins(host, username=username, password=password)
        print("Connected to Jenkins")
        server.build_job('task-1/main',{'PARAM_URL': url, 'PARAM_EMAIL': email, 'PARAM_SCAN_TYPE':scan_type, 'GENERATE_REPORT':generate_report})
    except jenkins.JenkinsException as e:
        print(f"Jenkins error: {e}")
    except Exception as e:
        print(f"General error: {e}")
    return redirect(url_for('success'))

@app.route('/success')
def success():
    return render_template('success.html')
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
