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
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Publish') {
            steps {
                bat 'powershell Compress-Archive -Path * -DestinationPath app.zip -Force'
            }
        }

        stage('Deploy') {
            steps {
                withCredentials([
                    usernamePassword(credentialsId: 'azure-service-principal', usernameVariable: 'AZURE_CLIENT_ID', passwordVariable: 'AZURE_CLIENT_SECRET'),
                    string(credentialsId: 'azure-tenant-id', variable: 'AZURE_TENANT_ID'),
                    string(credentialsId: 'azure-subscription-id', variable: 'AZURE_SUBSCRIPTION_ID')
                ]) {
                    bat '''
                        az login --service-principal -u %AZURE_CLIENT_ID% -p %AZURE_CLIENT_SECRET% --tenant %AZURE_TENANT_ID%
                        az account set --subscription %AZURE_SUBSCRIPTION_ID%
                        az webapp deploy --resource-group %RESOURCE_GROUP% --name %APP_SERVICE_NAME% --src-path app.zip --type zip
                    '''
                }
            }
        }
    }
}
