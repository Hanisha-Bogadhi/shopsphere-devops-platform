pipeline {

    agent any

    stages {

        stage('Clone Repository') {

            steps {

                git branch: 'main',
                    url: 'https://github.com/Hanisha-Bogadhi/shopsphere-devops-platform.git'
            }
        }

        stage('Deploy Containers') {

            steps {

                sh 'docker-compose down || true'

                sh 'docker-compose up -d --build'
            }
        }

        stage('Verify Running Containers') {

            steps {

                sh 'docker ps'
            }
        }
    }
}