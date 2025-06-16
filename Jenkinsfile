pipeline {
    agent any
    environment {
        IMAGE= "aravinthexe/aravinthexe/simple_mlflow"
    }

    stages {
        stage('Checkout') {
            steps {
                bat "git pull origin main"
            }
        }

        stage('Create Docker Image') {
            steps {
                script {
                    bat "docker build -t %IMAGE%:latest  --no-cache ."
                }
            }
        }

        stage('Push to docker hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub',
                    passwordVariable: 'DOCKER_PASSWORD',
                    usernameVariable: 'DOCKER_USERNAME'
                )]) {
                    script {
                        bat """
                            echo %DOCKER_PASSWORD% | docker login -u %DOCKER_USERNAME% --password-stdin
                            docker push %IMAGE%:latest
                        """ 
                    }
                }
                
            }
        }
    }
}