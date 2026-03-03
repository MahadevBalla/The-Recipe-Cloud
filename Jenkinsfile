node {
    try {

        stage('Prepare Env') {
            withCredentials([file(credentialsId: 'recipecloud-env', variable: 'ENVFILE')]) {
                sh 'cp $ENVFILE .env'
            }
        }

        stage('Build') {
            sh '''
                docker build -t recipecloud:latest .
            '''
        }

        stage('Deploy') {
            sh '''
                docker compose down || true
                docker compose up --build -d
            '''
        }

        echo "Pipeline executed successfully!"

    } catch (Exception e) {
        echo "Pipeline failed."
        throw e
    }
}
