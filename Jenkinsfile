pipeline {
	agent any
	environment {
		IMAGE_NAME = "taskflow:latest"
		CONTAINER_NAME = "taskflow_container"
		APP_PORT = "8000"
	}
	stages {
		stage('Checkout') {
			steps {
				checkout scm
			}
		}

		stage('Install dependencies') {
			steps {
				sh '''
					python -V || true
					python -m pip install --upgrade pip
					pip install -r requirements.txt
				'''
			}
		}

		stage('Run tests') {
			steps {
				sh 'pytest -q --maxfail=1'
			}
		}

		stage('Build Docker image') {
			steps {
				sh 'docker build -t ${IMAGE_NAME} .'
			}
		}

		stage('Run container') {
			steps {
				sh '''
					if [ "$(docker ps -aq -f name=${CONTAINER_NAME})" ]; then
						docker rm -f ${CONTAINER_NAME} || true
					fi
					docker run -d --name ${CONTAINER_NAME} -p ${APP_PORT}:8000 ${IMAGE_NAME}
					docker ps -a
				'''
			}
		}
	}
	post {
		always {
			sh 'docker images | head -n 20 || true'
		}
		success {
			echo 'Pipeline zakończony pomyślnie'
		}
		failure {
			echo 'Pipeline zakończony niepowodzeniem'
		}
	}
}

