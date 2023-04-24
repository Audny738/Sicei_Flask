pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                checkout scmGit(branches: [[name: '*/test']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/Audny738/Sicei_Flask']])
                echo 'Cloning...'
            }
        }
        stage('Test') {
            steps {
                bat 'python -m unittest'
            }
        }
        stage('Deploy') {
            steps {
                bat '''@ECHO OFF
                    FOR /f "tokens=*" %%i IN (\'docker ps -q\') DO docker stop %%i'''
                bat '''docker container ls -a'''
                bat '''docker build . -t sicei-%BUILD_NUMBER%-%GIT_BRANCH%'''
                bat '''docker image ls -a'''
                bat '''docker run -p 5000:5000 sicei-%BUILD_NUMBER%-%GIT_BRANCH%'''
                
            }
        }
    }
}