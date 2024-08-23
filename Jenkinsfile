def scanType
def targetUrl

pipeline {
    agent any
    parameters {
        string(name: 'PARAM_URL', defaultValue: '', description: 'Target URL for the scan')
        string(name: 'PARAM_EMAIL', defaultValue: '', description: 'Recipient email address for the report')
        string(name: 'PARAM_SCAN_TYPE', defaultValue: '', description: 'Type of scan to perform: Baseline, API, or Full')
        string(name: 'GENERATE_REPORT', defaultValue: 'false', description: 'Set to true if you want to generate a report')
    }
    
    stages {
        stage('Initialization') {
            steps {
                script {
                    echo "Initializing Pipeline with parameters..."
                    echo """
                        Scan Type: ${params.PARAM_SCAN_TYPE}
                        Target URL: ${params.PARAM_URL}
                        Report Generation: ${params.GENERATE_REPORT}
                    """
                }
            }
        }

        stage('Start OWASP ZAP Container') {
            steps {
                script {
                    echo "Pulling the latest OWASP ZAP Docker image..."
                    sh 'sudo docker pull zaproxy/zap-stable'
                    echo "Starting OWASP ZAP container..."
                    sh 'sudo docker run -dt --name owasp zaproxy/zap-stable /bin/bash'
                }
            }
        }

        stage('Prepare Report Directory') {
            when {
                expression { params.GENERATE_REPORT == 'true' }
            }
            steps {
                script {
                    echo "Creating report directory in the container..."
                    sh 'sudo docker exec owasp mkdir -p /zap/wrk'
                }
            }
        }

        stage('Perform Security Scan') {
            steps {
                script {
                    scanType = "${params.PARAM_SCAN_TYPE}"
                    targetUrl = "${params.PARAM_URL}"
                    echo "Executing ${scanType} scan on target: ${targetUrl}"

                    if (scanType == "Baseline") {
                        sh """
                            sudo docker exec owasp zap-baseline.py \
                            -t $targetUrl \
                            -x report.xml \
                            -I
                        """
                    } else if (scanType == "API") {
                        sh """
                            sudo docker exec owasp zap-api-scan.py \
                            -t $targetUrl \
                            -x report.xml \
                            -I
                        """
                    } else if (scanType == "Full") {
                        sh """
                            sudo docker exec owasp zap-full-scan.py \
                            -t $targetUrl \
                            -x report.xml \
                            -I
                        """
                    } else {
                        error "Invalid scan type specified: $scanType"
                    }
                }
            }
        }

        stage('Save Report to Workspace') {
            when {
                expression { params.GENERATE_REPORT == 'true' }
            }
            steps {
                script {
                    echo "Copying report from OWASP ZAP container to Jenkins workspace..."
                    sh 'sudo docker cp owasp:/zap/wrk/report.xml ${WORKSPACE}/report.xml'
                }
            }
        }
    }

    post {
        always {
            script {
                echo "Cleaning up: stopping and removing the OWASP ZAP container..."
                sh 'sudo docker stop owasp && sudo docker rm owasp'
            }
        }

        success {
            script {
                echo "Sending report to ${params.PARAM_EMAIL} via email..."
                emailext(
                    to: "${params.PARAM_EMAIL}",
                    subject: "OWASP ZAP Scan Completed",
                    body: "The OWASP ZAP scan has been successfully completed. Please find the attached report.",
                    attachmentsPattern: 'report.xml'
                )
            }
        }

        failure {
            script {
                echo "Notifying user of failure via email..."
                emailext(
                    to: "${params.PARAM_EMAIL}",
                    subject: "OWASP ZAP Scan Failed",
                    body: "The OWASP ZAP scan encountered an error. Please check the Jenkins logs for further details."
                )
            }
        }
    }
}
