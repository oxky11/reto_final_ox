pipeline {
  agent any

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
              // Si es Linux/Unix, usa sh
              sh '''
                #!/bin/bash
                py -m venv venv
                pip install -r ./requirements.txt 
                '''
            } else {
              // Si es Windows, usa PowerShell
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
            // Si es Linux/Unix, usa sh
            sh '''
              #!/bin/bash
              python -m unittest ./app/tests/tests.py  
            '''
          } else {
            // Si es Windows, usa PowerShell
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
              // Si es Linux/Unix, usa sh
              sh '''
                #!/bin/bash
                pip install pylint
                pylint --exit-zero (Get-ChildItem -Recurse -Path .\\app -Filter *.py).FullName 
              '''
            } else {
              // Si es Windows, usa PowerShell
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
            // Si es Linux/Unix, usa sh
            sh '''
            #!/bin/bash
              docker-compose build

              docker-compose up -d 
            '''
          } else {
            // Si es Windows, usa PowerShell
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
        script 
		{
		    def region = 'eu-south-2'
            def accountId = '047719634914'
            def repoName = 'reto_final_ox'
            def imageTag = "${env.BUILD_NUMBER}"

            def ecrImage = "${accountId}.dkr.ecr.${region}.amazonaws.com/${repoName}:${imageTag}"

			if (isUnix()) {
            // Si es Linux/Unix, usa sh
            sh '''
            #!/bin/bash
				aws ecr get-login-password --region ${region} | docker login --username AWS --password-stdin ${accountId}.dkr.ecr.${region}.amazonaws.com

				docker tag miapp:latest ${ecrImage}
				docker push ${ecrImage}
            '''
          } else {
            // Si es Windows, usa PowerShell
            powershell '''
				aws ecr get-login-password --region '${region}' | docker login --username AWS --password-stdin '${accountId}'.dkr.ecr.'${region}'.amazonaws.com

				docker tag miapp:latest '${ecrImage}'
				docker push '${ecrImage}'
            '''
          }
		}
      }
    }
  }
}