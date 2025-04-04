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
                withCredentials([azureServicePrincipal(credentialsId: AZURE_CREDENTIALS_ID)]) {
                    bat '''
                    if exist publish (rmdir /s /q publish)
                    mkdir publish

                    :: Copy .py files and requirements.txt to publish folder
                    for %%f in (*.py) do copy "%%f" publish\\
                    if exist requirements.txt copy requirements.txt publish\\
                    '''
                    bat 'az login --service-principal -u %AZURE_CLIENT_ID% -p %AZURE_CLIENT_SECRET% --tenant %AZURE_TENANT_ID%'
                    bat 'powershell Compress-Archive -Path ./publish/* -DestinationPath ./publish.zip -Force'
                    bat 'az webapp deploy --resource-group %RESOURCE_GROUP% --name %APP_SERVICE_NAME% --src-path ./publish.zip --type zip'
                }
            }
        }

    }
}
