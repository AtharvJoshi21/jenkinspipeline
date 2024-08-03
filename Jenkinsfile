pipeline {
    agent any

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
        stage('Relese'){
            steps {
                echo 'Relesing Job....'
            }
        }
    }
    post{
        cleanWs()
    }
}
