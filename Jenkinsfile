pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps{
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'f7f1aef4-8407-4ff8-9885-89381e80d7df', url: 'https://github.com/stollstoll/devops4.git']])
            }
        }
        stage('Build'){
            steps{
                git branch: 'main', credentialsId: 'f7f1aef4-8407-4ff8-9885-89381e80d7df', url: 'https://github.com/stollstoll/devops4.git'
                // git  credentialsId: 'f7f1aef4-8407-4ff8-9885-89381e80d7df', url: 'https://github.com/stollstoll/devops.git'
                bat 'python calc.py'
                
            }
        }
        stage('Test'){
            steps{
                echo 'test step'
                bat 'python test_calc.py'
            }
        }
    }
}
