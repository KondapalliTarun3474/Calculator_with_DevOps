pipeline {
    agent any 
    
    // Define environment variables for the build
    environment {
        DOCKER_IMAGE = "kondapallitarun3474/scientific-calculator" // Replace <DOCKER_USER>
        DOCKER_CREDENTIALS_ID = 'docker-hub-credentials' // ID of your Docker Hub secret credentials in Jenkins
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Assuming you have configured SCM (GitHub) in the pipeline job settings
                echo 'Cloning repository...'
                git branch: 'main', url: 'https://github.com/KondapalliTarun3474/Calculator_with_DevOps'
            }
        }

        stage('Test Code') {
            steps {
                echo 'Running PyUnit tests...'
                // Execute tests using the Python runtime available in the environment
                sh 'python3 -m unittest test_calculator.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image ${env.DOCKER_IMAGE}:${env.BUILD_NUMBER}"
                // Build the image using the Dockerfile in the workspace
                sh "docker build -t ${env.DOCKER_IMAGE}:${env.BUILD_NUMBER} ."
            }
        }

        stage('Push to Docker Hub') {
            steps {
                // Log in to Docker Hub using stored credentials
                withCredentials([usernamePassword(credentialsId: env.DOCKER_CREDENTIALS_ID, passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                    sh "echo ${DOCKER_PASSWORD} | docker login -u ${DOCKER_USERNAME} --password-stdin"
                    
                    // Push the versioned image
                    sh "docker push ${env.DOCKER_IMAGE}:${env.BUILD_NUMBER}"
                    
                    // Tag and push as 'latest' for deployment simplicity
                    sh "docker tag ${env.DOCKER_IMAGE}:${env.BUILD_NUMBER} ${env.DOCKER_IMAGE}:latest"
                    sh "docker push ${env.DOCKER_IMAGE}:latest"
                }
            }
        }

        stage('Deploy with Ansible') {
            steps {
                echo 'Triggering Ansible deployment...'
                // Execute the Ansible playbook on the control node
                // Requires Ansible to be installed and the playbook file to be present
                sh "ansible-playbook -i inventory.ini deploy_calculator.yml"
            }
        }
    }
}