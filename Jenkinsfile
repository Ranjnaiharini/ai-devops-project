pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/Ranjnaiharini/ai-devops-project.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python -m pip install -r app/requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest app/test_app.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ai-devops-app .'
            }
        }
    }
}