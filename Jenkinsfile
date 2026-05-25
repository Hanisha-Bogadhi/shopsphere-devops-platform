pipeline {

    agent any

    stages {

        stage('Clone Repository') {

            steps {

                git branch: 'main',
                    url: 'https://github.com/Hanisha-Bogadhi/shopsphere-devops-platform.git'
            }
        }

        stage('Cleanup Old Containers') {

            steps {

                sh 'docker compose down -v || true'
            }
        }

        stage('Build Containers') {
            steps {
                sh 'docker-compose build --no-cache'
            }
        }

        stage('Run Containers') {
            steps {
                sh 'docker-compose up -d --force-recreate'
            }
        }
        stage('Verify Running Containers') {

            steps {

                sh 'docker ps -a'
            }
        }
    }
}