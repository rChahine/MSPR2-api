pipeline {
    agent any

    stages {
        stage('Setup config') {
            steps {
                bat '''

                    type nul > .env
                    
                    echo DATABASE_URL=postgresql://uy5paos4qw9hdpg5mklq:1tjg9DNqUwyPzUQLMwvf@bk0gqvjcvowyhj2azddb-postgresql.services.clever-cloud.com:5432/bk0gqvjcvowyhj2azddb >> .env
                    echo SECRET_KEY=zefuihzefizpaefhzoiefhzeiofhze2342ofhizefzoe >> .env
                    echo TESTING=true >> .env
                '''
            }
        }
        stage('Install latests dependencies') {
            steps {
                bat '''
                    poetry install
                '''
            }
        }
        stage('test') {
            steps {
                sh '''#!/bin/bash
                   poetry run pytest
                '''
            }
        }
    }
    post {
        always {
            echo 'Delete directory'
            deleteDir()
        }
    }
}
