pipeline {
    agent {
        docker {
            
            image 'docker:24.0.0'   // base image with Docker CLI
            args '-v /var/lib/docker' // optional: ephemeral in-pipeline DIND
        }
    }

    environment {
        DOCKER_BUILDKIT = 1
    }

    stages {
        stage('Clone') {
            agent {label 'rs1-gpu'}
            steps {
                git 'https://github.com/VirajRajurkar/CalculatorDeployment.git'
            }
        }

        stage('Build Docker Image') {
            agent {label 'rs1-gpu'}
            steps {
                sh '''
                    docker build -t simple-calc .
                '''
            }
        }

        stage('Run Container') {
            agent {label 'rs1-gpu'}
            steps {
                sh '''
                    docker run --rm -v $PWD:/app simple-calc
                '''
            }
        }

        stage('Check Output') {
            agent {label 'rs1-gpu'}
            steps {
                sh 'cat output.txt'
            }
        }
    }
}
