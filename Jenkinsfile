pipeline {
    agent any
    parameters {
        string(name: 'PARAM_URL', defaultValue: '', description: 'The URL to be used')
        string(name: 'PARAM_EMAIL', defaultValue: '', description: 'The email address to be used')
        string(name: 'PARAM_SCAN_TYPE', defaultValue: '', description: 'Scan that you want to perform on given URL')
        string(name: 'GENERATE_REPORT', defaultValue: '', description: 'Do you wanna generate report')
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building Job....'
            }
        }
        stage('Parameters'){
            steps {
                echo "URL: ${params.PARAM_URL}"
                echo "Email: ${params.PARAM_EMAIL}"
                echo "Scan Type: ${params.PARAM_SCAN_TYPE}"
                echo "Generate Report: ${params.GENERATE_REPORT}"
            }
        }
    }
    post{
        always{
            cleanWs()
        }
    }
}
