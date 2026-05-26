pipeline {

    agent any

    stages {

        stage('Verify Workspace') {
            steps {
                sh 'pwd'
                sh 'ls -la'
            }
        }

        stage('Cleanup Old Containers') {
            steps {
                sh 'docker rm -f nginx frontend cart-service product-service prometheus grafana || true'
            }
        }

        stage('Deploy Containers') {
            steps {

                sh 'docker compose down || true'

                sh 'docker compose up -d --build'
            }
        }

        stage('Verify Running Containers') {
            steps {
                sh 'docker ps'
            }
        }
    }
}