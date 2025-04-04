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
                   sh 'pip install -r requirements.txt'
               }
           }
           stage('Publish') {
               steps {
                   sh 'zip -r app.zip .'
               }
           }
           stage('Deploy') {
            steps {
                withCredentials([azureServicePrincipal(credentialsId: AZURE_CREDENTIALS_ID)]) {
                    bat "az login --service-principal -u $AZURE_CLIENT_ID -p $AZURE_CLIENT_SECRET --tenant $AZURE_TENANT_ID"
                    bat "powershell Compress-Archive -Path ./publish/* -DestinationPath ./publish.zip -Force"
                    bat "az webapp deploy --resource-group $RESOURCE_GROUP --name $APP_SERVICE_NAME --src-path ./publish.zip --type zip"
                }
            }
          }
       }
   }
