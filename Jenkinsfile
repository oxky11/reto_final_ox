pipeline {
    agent any

    environment {
        AWS_ACCESS_KEY_ID     = credentials('aws-access-key-id')
        AWS_SECRET_ACCESS_KEY = credentials('aws-secret-access-key')
        AWS_DEFAULT_REGION  = 'eu-south-2'
        accountId = '047719634914'
        repoName = 'reto_final_ox'
        imageTag = "${env.BUILD_NUMBER}"
        ECR_URL = "${accountId}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com"
        ecrImage = "${accountId}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${repoName}:latest"
    }

    stages {
        stage('Clonado GIT') {
            steps {
                git url: 'https://github.com/oxky11/reto_final_ox.git', branch: 'main'
            }
        }

        stage('Construcción') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    script {
                        if (isUnix()) {
                            sh '''
                                #!/bin/bash
                                py -m venv venv
                                pip install -r ./requirements.txt 
                            '''
                        } else {
                            powershell '''
                                py -m venv venv 
                            '''
                            bat '''
                                pip install -r ./requirements.txt 
                            '''
                        }
                    }
                }
            }
        }

        stage('Ejecución Tests') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            #!/bin/bash
                            python -m unittest ./app/tests/tests.py  
                        '''
                    } else {
                        powershell '''
                            python -m unittest ./app/tests/tests.py 
                        '''
                    }
                }
            }
        }

        stage('Linting') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    script {
                        if (isUnix()) {
                            sh '''
                                #!/bin/bash
                                pip install pylint
                                pylint --exit-zero (Get-ChildItem -Recurse -Path .\\app -Filter *.py).FullName 
                            '''
                        } else {
                            powershell '''
                                pip install pylint
                            '''
                            powershell '''
                                pylint --exit-zero (Get-ChildItem -Recurse -Path .\\app -Filter *.py).FullName
                            '''
                        }
                    }
                }
            }
        }

        stage('Crear imagen docker') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            #!/bin/bash
                            docker-compose build
                            docker-compose up -d 
                        '''
                    } else {
                        powershell '''
                            docker-compose build
                            docker-compose up -d 
                        '''
                    }
                }
            }
        }

        stage('Registry') {
            steps {
                script {
                    
                    def ecrUrl = "${env.accountId}.dkr.ecr.${env.AWS_DEFAULT_REGION}.amazonaws.com"
                    def ecrImage = "${ecrUrl}/${env.repoName}:${env.BUILD_NUMBER}"
            
            
                    if (isUnix()) {
                        sh """
                            aws sts get-caller-identity
                            aws ecr get-login-password --region ${env.AWS_DEFAULT_REGION} | docker login --username AWS --password-stdin ${ecrUrl}
                            docker build -t reto_final_ox .
                            docker tag reto_final_ox:latest ${ecrImage}
                            docker push ${ecrImage}
                        """
                    } else {
                        bat script:  """
                            aws sts get-caller-identity
                            aws ecr get-login-password --region %AWS_DEFAULT_REGION% | docker login --username AWS --password-stdin %ecrUrl%
                            docker build -t reto_final_ox .
                            docker tag reto_final_ox:latest ${env.ecrImage}
                            docker push ${env.ecrImage}
                         """
                    }
                }
            }
        }
    }
}