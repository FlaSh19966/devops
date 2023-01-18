
pipeline {
    agent any
    stages {
        stage('back-end') {
            steps {
                sh 'sudo docker-compose stop'
                sh 'sudo docker-compose up --build -d'
            }
        }
        stage('front-end') {
            steps {
                sh 'echo "hello"'
            }
        }
    }
}