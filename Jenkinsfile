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
            steps {
                git 'https://github.com/VirajRajurkar/CalculatorDeployment.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build -t simple-calc .
                '''
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                    docker run --rm -v $PWD:/app simple-calc
                '''
            }
        }

        stage('Check Output') {
            steps {
                sh 'cat output.txt'
            }
        }
    }
}
