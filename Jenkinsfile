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

     stage('Deploy') {
            steps {
                  azureCLI commands: [[
                    exportVariablesString: 'RESOURCE_GROUP,APP_SERVICE_NAME',
                    script: '''
                        az webapp deployment source config-zip \
                          --resource-group $RESOURCE_GROUP \
                          --name $APP_SERVICE_NAME \
                          --src app.zip
                    '''
                ]],
                principalCredentialId: 'azure-service-principal'
                }
            }
        }

    }
}
