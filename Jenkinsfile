pipeline {

    agent any

    stages {

        stage('Clone Repository') {

            steps {

                git branch: 'main',
                    url: 'https://github.com/Hanisha-Bogadhi/shopsphere-devops-platform.git'
            }
        }

        stage('Build Containers') {

            steps {

                sh 'docker compose build'
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