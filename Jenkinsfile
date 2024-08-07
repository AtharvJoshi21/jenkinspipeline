pipeline {
    agent{
        dockerfile {
            filename 'Dockerfile'
        }
    }
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
        stage('Security Scan') {
            steps {
                script {
                    echo 'Running ZAP Security Scan...'
                    sh '''
                    # Ensure Docker is running
                    docker info
                    zap -version
                    '''

                    // # Pull the ZAP Docker image
                    // docker pull owasp/zap2docker-stable

                    // # Run ZAP in daemon mode
                    // docker run -u zap -d --name zap -p 8080:8080 \
                    // owasp/zap2docker-stable zap.sh -daemon -port 8080 -host 0.0.0.0 -config api.disablekey=true

                    // # Wait for ZAP to start
                    // sleep 30

                    // # Run the ZAP quick scan
                    // docker exec zap zap-cli quick-scan --self-contained --start-options '-config api.disablekey=true' ${params.PARAM_URL}

                    // # Generate the ZAP report
                    // docker exec zap zap-cli report -o /zap/wrk/zap_report.html -f html

                    // # Copy the report from the container to the host
                    // docker cp zap:/zap/wrk/zap_report.html .

                    // # Stop and remove the ZAP container
                    // docker stop zap
                    // docker rm zap
                    // '''
                }
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
            node('master') {
                cleanWs()
            }
        } 
    }
}
