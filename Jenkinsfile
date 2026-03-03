pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                sh '''
                echo "Building Docker image..."
                docker build -t recipecloud:latest .
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                echo "Deploying application using Docker Compose..."
                docker compose down || true
                docker compose up --build -d
                '''
            }
        }
    }

    post {
        success {
            echo "CI/CD pipeline executed successfully."
        }
        failure {
            echo "CI/CD pipeline failed."
        }
    }
}
