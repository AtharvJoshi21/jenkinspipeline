pipeline {
    agent any
    parameters {
        string(name: 'PARAM_URL', defaultValue: '', description: 'The URL to be used')
        string(name: 'PARAM_EMAIL', defaultValue: '', description: 'The email address to be used')
    }
    environment {
        TARGET_URL = "${params.PARAM_URL}"  
        ZAP_URL = 'http://localhost:8081/zap/'
        REPORT_PATH = '/zap/reports/zap_report.html' 
        RECIPIENT_EMAIL = "${params.PARAM_EMAIL}"  
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building Job....'
            }
        }
        stage('Run ZAP Scan') {
            steps {
                script {

                    // Start the scan
                    sh "curl -v '${ZAP_URL}/JSON/ascan/action/scan/?url=${TARGET_URL}&recurse=true&inScopeOnly=true'"

                    // Wait for the scan to complete (example, adjust as needed)
                    sleep(time: 90, unit: 'SECONDS')

                    
                    // Generate the ZAP report
                    sh "curl '${ZAP_URL}/OTHER/core/other/htmlreport/?formMethod=GET' -o ${REPORT_PATH}"
                
                }
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
    }
    post{
        always{
            emailext (
                to: "${RECIPIENT_EMAIL}",
                subject: "ZAP Security Report for ${TARGET_URL}",
                body: "Please find the attached ZAP security report for ${TARGET_URL}.",
                attachmentsPattern: "/var/jenkins_home/zap-reports/zap_report.html",  // Path in Jenkins container
                mimeType: 'text/html'
            )
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
