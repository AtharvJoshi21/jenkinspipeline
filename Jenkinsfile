def scan_type
def target
pipeline {
    agent any
    parameters {
        string(name: 'PARAM_URL', defaultValue: '', description: 'The URL to be used')
        string(name: 'PARAM_EMAIL', defaultValue: '', description: 'The email address to be used')
        string(name: 'PARAM_SCAN_TYPE', defaultValue: '', description: 'Scan that you want to perform on given URL')
        string(name: 'GENERATE_REPORT', defaultValue: '', description: 'Do you wanna generate report')
    }
    stages {
        stage('Pipeline Info') {
            steps {
                script {
                    echo "<--Parameter Initialization-->"
                    echo """
                        The current parameters are:
                        Scan Type: ${params.PARAM_SCAN_TYPE}
                        Target: ${params.PARAM_URL}
                        Generate report: ${params.GENERATE_REPORT}
                     """
                }
            }
        }
        stage('Setting up OWASP ZAP docker container') {
            steps {
                script {
                    echo "Pulling up last OWASP ZAP container --> Start"
                    sh 'docker pull zaproxy/zap-stable'
                    echo "Pulling up last VMS container --> End"
                    echo "Starting container --> Start"
                    sh """
                    docker run -dt --name owasp \
                    zaproxy/zap-stable \
                    /bin/bash
                    """
                }
            }
        }
        stage('Prepare wrk directory') {
            when {
                environment name : 'GENERATE_REPORT', value: 'true'
            }
            steps {
                script {
                    sh """
                        docker exec owasp \
                        mkdir /zap/wrk
                    """
                }
            }
        }
        stage('Scanning target on owasp container') {
            steps {
                script {
                    scan_type = "${params.PARAM_SCAN_TYPE}"
                    echo "----> scan_type: $scan_type"
                    target = "${params.PARAM_URL}"
                    if(scan_type == "Baseline"){
                        sh """
                            docker exec owasp \
                            zap-baseline.py \
                            -t $target \
                            -x report.xml \
                            -I
                        """
                    }
                    else if(scan_type == "APIS"){
                        sh """
                            docker exec owasp \
                            zap-api-scan.py \
                            -t $target \
                            -x report.xml \
                            -I
                        """
                    }
                    else if(scan_type == "Full"){
                        sh """
                            docker exec owasp \
                            zap-full-scan.py \
                            -t $target \
                            //-x report.xml
                            -I
                        """
                         //-x report-$(date +%d-%b-%Y).xml
                    }
                    else{
                        echo "Something went wrong..."
                    }
                }
            }
        }
        stage('Copy Report to Workspace'){
            steps {
                script {
                    sh '''
                        docker cp owasp:/zap/wrk/report.xml ${WORKSPACE}/report.xml
                    '''
                }
            }
        }
    }
    post{
        always{
            echo "Removing container"
                sh '''
                    docker stop owasp
                    docker rm owasp
                '''
        }
        success {
            // Send email with report
            emailext (
                to: "${params.PARAM_EMAIL}",
                subject: "OWASP ZAP Scan Report",
                body: """
                    The OWASP ZAP scan has been completed successfully.
                    lease find the attached report for your review.
                """,
                attachmentsPattern: "report.xml"
            )
        }
        failure {
            emailext (
                to: "${params.PARAM_EMAIL}",
                subject: "OWASP ZAP Scan Failed",
                body: """
                    The OWASP ZAP scan has failed.
                    Please check the Jenkins job for more details.
                """
            )
        }
    }
}
