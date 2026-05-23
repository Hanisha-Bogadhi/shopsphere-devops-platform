pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                git 'https://github.com/Hanisha-Bogadhi/shopsphere-devops-platform.git'
            }
        }

        stage('Build') {
            steps {
                sh 'docker compose build'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker compose up -d'
            }
        }
    }
}