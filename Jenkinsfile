pipeline {
    agent any

    stages {

        stage('Prepare Env') {
            steps {
                withCredentials([file(credentialsId: 'recipecloud-env', variable: 'ENVFILE')]) {
                    sh 'cp $ENVFILE .env'
                }
            }
        }

        stage('Build') {
            steps {
                sh '''
                docker build -t recipecloud:latest .
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                docker compose down || true
                docker compose up --build -d
                '''
            }
        }
    }

    post {
        success {
            echo "Pipeline executed successfully!"
        }
        failure {
            echo "Pipeline failed."
        }
    }
}
