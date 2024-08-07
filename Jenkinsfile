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
        stage('Test Docker') {
            steps {
                sh '''
                whoami
                ls
                // docker exec -u root -it jenkins
                // docker --version
                // docker run hello-world
                '''
            }
        }
        // stage('ZAP Security Scan') {
        //     steps {
        //         script {
        //             // Ensure the ZAP docker image is available
        //             def zapImage = 'owasp/zap2docker-stable:latest'
        //             def zapPort = '8080'
        //             def targetUrl = params.PARAM_URL
        //             def reportFile = 'zap_report.html'
                    
        //             // Run ZAP Proxy using Docker
        //             sh """
        //                 docker run -d -u zap -p ${zapPort}:8080 --name zap ${zapImage} zap.sh -daemon -host 0.0.0.0 -port ${zapPort}
        //                 docker exec zap zap.sh -cmd -quickurl ${targetUrl} -out /zap/wrk/${reportFile}
        //             """

        //             // Wait for the scan to complete
        //             sleep time: 5, unit: 'MINUTES'

        //             // Copy the report from the container to the workspace
        //             sh "docker cp zap:/zap/wrk/${reportFile} ."

        //             // Stop and remove the ZAP container
        //             sh "docker stop zap && docker rm zap"
        //         }
        //     }
        // }
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
        // success {
        //     script {
        //         // Send the ZAP report via email
        //         emailext(
        //             to: params.PARAM_EMAIL,
        //             subject: 'OWASP ZAP Security Report',
        //             body: 'Please find the attached OWASP ZAP security report.',
        //             attachmentsPattern: 'zap_report.html'
        //         )
        //     }
        // }
        // failure {
        //     echo 'The job has failed. No report will be sent.'
        // }
    }
}
