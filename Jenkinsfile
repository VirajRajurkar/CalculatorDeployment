pipeline {
    agent { label 'rs1-cpu' }  

    stages {
        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/VirajRajurkar/CalculatorDeployment.git'
            }
        }

        stage('Unit Test') {
            agent {
                docker {
                    image 'python:3.10-slim'
                }
            }
            steps {
                sh '''
                    pip install -r requirements.txt || true  # skip if empty
                    python -m unittest discover tests
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t simple-calc .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run --rm -v $PWD:/app simple-calc'
            }
        }

        stage('Check Output') {
            steps {
                sh 'cat output.txt'
            }
        }
    }
}
