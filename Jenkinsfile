pipeline {
    agent any

    environment {
        AZURE_CREDENTIALS_ID = 'azure-service-principal'
        RESOURCE_GROUP = 'rg-jenkins'
        APP_SERVICE_NAME = 'pythonwebapp'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Gourav7568/JenkinsWithPython.git'
            }
        }

        stage('Build') {
    steps {
        bat '"C:\\Users\\gaura\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" -m pip install -r requirements.txt'
    }
}


        stage('Publish') {
            steps {
                bat 'powershell Compress-Archive -Path * -DestinationPath app.zip -Force'
            }
        }

    stage('Deploy to Azure') {
               steps {
                   withCredentials([azureServicePrincipal('azure-service-principal')]) {
                       sh 'az login --service-principal -u $AZURE_CREDENTIALS_USR -p $AZURE_CREDENTIALS_PSW --tenant $AZURE_CREDENTIALS_TEN'
                       sh 'az webapp up --name myPythonApp --resource-group myResourceGroup --runtime "PYTHON:3.9" --src-path .'
                   }
               }
           }
    }
}
