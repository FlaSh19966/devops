
pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'sudo docker-compose up --build -d'
            }
        }
    }
}