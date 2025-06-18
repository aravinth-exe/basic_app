pipeline {
    agent any
    environment {
        IMAGE = "aravinthexe/simple_mlflow"
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
                    bat "docker build -t ${env.IMAGE}:latest --no-cache ."
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
                            docker login -u ${env.DOCKER_USERNAME} -p ${env.DOCKER_PASSWORD}
                            docker push ${env.IMAGE}:latest
                        """
                    }
                }
            }
        }
    }

    // ECS deploy stage (commented)
}
