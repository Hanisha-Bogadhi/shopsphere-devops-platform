pipeline {

    agent any

    stages {

        stage('Clone Repository') {

            steps {

                git branch: 'main',
                    url: 'https://github.com/Hanisha-Bogadhi/shopsphere-devops-platform.git'
            }
        }

        stage('Check Monitoring Files') {

            steps {

                sh 'pwd'
                sh 'ls -la'
                sh 'ls -la monitoring'
            }
        }

        stage('Build Docker Images') {

            steps {

                sh 'docker-compose build'
            }
        }

        stage('Stop Existing Containers') {

            steps {

                sh 'docker-compose down || true'
            }
        }

        stage('Run Containers') {

            steps {

                sh 'docker-compose up -d'
            }
        }

        stage('Verify Containers') {

            steps {

                sh 'docker ps'
            }
        }
    }
}