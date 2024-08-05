pipeline {
    agent any
    parameters {
        string(name: 'PARAM_URL', defaultValue: '', description: 'The URL to be used')
        string(name: 'PARAM_EMAIL', defaultValue: '', description: 'The email address to be used')
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building Job....'
            }
        }
        stage('Test'){
            steps {
                echo 'Testing Job....'
            }
        }
        stage('Deploy'){
            steps {
                echo 'Deploying Job....'
            }
        }
        stage('Parameters'){
            steps {
                echo "URL: ${params.PARAM_URL}"
                echo "Email: ${params.PARAM_EMAIL}"
            }
        }
    }
    post{
        always{
            cleanWs()
        } 
    }
}
