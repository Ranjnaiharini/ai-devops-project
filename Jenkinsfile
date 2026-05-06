pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main',
                url: 'https://github.com/Ranjnaiharini/ai-devops-project.git'
            }
        }

        stage('Check Python') {
            steps {
                sh 'python --version || python3 --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r app/requirements.txt || pip3 install -r app/requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ai-devops-app ./app'
            }
        }

    }
}