pipeline {

    agent any

    stages {

        stage('Clone Repository') {

            steps {

                git branch: 'main',
                    url: 'https://github.com/Hanisha-Bogadhi/shopsphere-devops-platform.git'
            }
        }

        stage('Cleanup') {

            steps {

                sh 'docker compose down -v || true'
            }
        }

        stage('Build Docker Images') {

            steps {

                sh 'docker compose build --no-cache'
            }
        }

        stage('Run Containers') {

            steps {

                sh 'docker compose up -d --build --force-recreate'
            }
        }

        stage('Verify Containers') {

            steps {

                sh 'docker ps -a'
            }
        }
    }
}