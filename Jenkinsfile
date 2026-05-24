pipeline {

    agent any

    stages {

        stage('Clone Repository') {

            steps {

                git 'https://github.com/Hanisha-Bogadhi/shopsphere-devops-platform.git'
            }
        }

        stage('Build Docker Images') {

            steps {

                sh 'docker compose build'
            }
        }

        stage('Stop Existing Containers') {

            steps {

                sh 'docker compose down'
            }
        }

        stage('Run Containers') {

            steps {

                sh 'docker compose up -d'
            }
        }

        stage('Verify Containers') {

            steps {

                sh 'docker ps'
            }
        }
    }
}