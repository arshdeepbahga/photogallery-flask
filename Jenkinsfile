pipeline {
    agent any
    environment {
        //AWS_ACCOUNT_ID="YOUR_ACCOUNT_ID_HERE"
        //AWS_DEFAULT_REGION="REGION" 
        IMAGE_REPO_NAME = "photogalleryflaskapp"
        IMAGE_TAG = "latest"
        REPOSITORY_URI = "asbind/${IMAGE_REPO_NAME}"
        DOCKER_USERNAME = "asbind"
        DOCKER_PASSWORD = "Ashu~1983"
        REMOTE_USER = "ubuntu"
        REMOTE_HOST = "34.242.227.57"
    }

    stages {
        stage('Cloning Git') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/arshdeepbahga/photogallery-flask.git']]])
            }
        }

        // Building Docker images
        stage('Building image') {
            steps {
                script {
                    sh "docker build -f Dockerfile -t ${IMAGE_REPO_NAME}:${IMAGE_TAG} ."
                }
            }
        }

        // Uploading Docker images into AWS ECR
        stage('Pushing to DockerHub') {
            steps {
                script {
                    sh "docker login -u=$DOCKER_USERNAME -p=$DOCKER_PASSWORD"
                    sh "docker tag ${IMAGE_REPO_NAME}:${IMAGE_TAG} ${REPOSITORY_URI}:$IMAGE_TAG"
                    sh "docker push ${REPOSITORY_URI}:${IMAGE_TAG}"
                }
            }
        }

        stage ('Deploy') {
            steps {
                sh 'scp deploy.sh ${REMOTE_USER}@${REMOTE_HOST}:~/'
                sh 'ssh ${REMOTE_USER}@${REMOTE_HOST} "chmod +x deploy.sh"'
                sh 'ssh ${REMOTE_USER}@${REMOTE_HOST} ./deploy.sh'
            }
    }
    }
}
