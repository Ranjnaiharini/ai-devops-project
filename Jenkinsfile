pipeline {
    agent {
        docker {
            image 'python:3.10'
        }
    }

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main',
                url: 'https://github.com/Ranjnaiharini/ai-devops-project.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r app/requirements.txt'
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