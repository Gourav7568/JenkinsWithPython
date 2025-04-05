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
                    script: '''
                        echo "Deploying $APP_SERVICE_NAME to $RESOURCE_GROUP"
                        az webapp deploy \
                          --resource-group $RESOURCE_GROUP \
                          --name $APP_SERVICE_NAME \
                          --src-path ./publish.zip \
                          --type zip
                    ''',
                    exportVariablesString: 'RESOURCE_GROUP,APP_SERVICE_NAME'
                ]], principalCredentialId: "${AZURE_CREDENTIALS_ID}"

                }
            }

    }
}
