pipeline {
    agent any
    environment {
        IMAGE = "aravinthexe/basic_app"
        AWS_ECR_URI = "414028192219.dkr.ecr.eu-north-1.amazonaws.com/aravinthexe/basic_app"
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

        stage('Deploy to ECS') {
            steps {
                withCredentials([
                string(credentialsId: 'aws-access-key-id', variable: 'AWS_ACCESS_KEY_ID'),
                string(credentialsId: 'aws-secret-access-key', variable: 'AWS_SECRET_ACCESS_KEY')
                ]) {
                script {
                    bat """
                    aws configure set aws_access_key_id %AWS_ACCESS_KEY_ID%
                    aws configure set aws_secret_access_key %AWS_SECRET_ACCESS_KEY%
                    aws ecs update-service ^
                        --cluster basic_app_cluster ^
                        --service basic_app-service-rsy0hhl8 ^
                        --force-new-deployment ^
                        --region %REGION%
                    """
                }
                }
            }
        }
    }
}
