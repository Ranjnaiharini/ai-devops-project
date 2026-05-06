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
                sh 'python3 --version'
            }
        }

        stage('Create Virtual Environment') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                . venv/bin/activate
                pip install flask pytest
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                pytest
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ai-devops-app ./app'
            }
        }

    }
}