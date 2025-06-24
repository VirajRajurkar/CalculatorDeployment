pipeline {
    agent { label 'rs1-cpu' }  // or 'anton-cpu', whichever has DIND

    stages {
        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/VirajRajurkar/CalculatorDeployment.git'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m unittest discover tests'
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
