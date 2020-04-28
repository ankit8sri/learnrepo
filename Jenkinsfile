pipeline {
    agent { label 'dockerserver' }
    stages {
        stage('Build') {
            agent {
                docker {
                    label 'dockerserver'
                    image 'python:2.7'
                }
            }
            steps {
                sh 'python code27.py'
                stash(name: 'compiled-results', includes: '*.py*')
            }
        }
        stage('Test') { 
            agent {
                docker {
                    label 'dockerserver'
                    image 'qnib/pytest' 
                }
            }
            steps {
                sh 'py.test --junit-xml test-reports/results.xml code27.py' 
            }
            post {
                always {
                    junit 'test-reports/results.xml' 
                }
            }
        }
    }
}
