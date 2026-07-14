pipeline {
    agent any

    environment {
        IMAGE_NAME = 'taskflow'
        CONTAINER_NAME = 'taskflow-container'
    }

    stages {
        stage('Install dependencies') {
            steps {
                sh '''
                    python3 -V
                    python3 -m venv .venv
                    .venv/bin/python -m pip install --upgrade pip
                    .venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Run tests') {
            steps {
                sh '''
                    .venv/bin/python -m pytest -v
                '''
            }
        }

        stage('Build Docker image') {
            steps {
                sh '''
                    docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} .
                    docker tag ${IMAGE_NAME}:${BUILD_NUMBER} ${IMAGE_NAME}:latest
                '''
            }
        }

        stage('Run container') {
            steps {
                sh '''
                    docker rm -f ${CONTAINER_NAME} 2>/dev/null || true

                    docker run -d \
                        --name ${CONTAINER_NAME} \
                        -p 8000:8000 \
                        ${IMAGE_NAME}:${BUILD_NUMBER}
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline zakończony powodzeniem'
            sh 'docker ps'
        }

        failure {
            echo 'Pipeline zakończony niepowodzeniem'
            sh 'docker ps -a || true'
        }

        always {
            sh 'docker images | head -n 20 || true'
        }
    }
}