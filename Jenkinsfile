pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/YOUR_REPO_LINK'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }

    }
}
