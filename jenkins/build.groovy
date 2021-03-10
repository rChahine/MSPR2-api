pipeline {
    agent any

    stages {
        stage('Setup config') {
            steps {
                sh '''#!/bin/bash

                    touch .env
                    echo '
                        DATABASE_URL=postgresql://uy5paos4qw9hdpg5mklq:1tjg9DNqUwyPzUQLMwvf@bk0gqvjcvowyhj2azddb-postgresql.services.clever-cloud.com:5432/bk0gqvjcvowyhj2azddb
                        SECRET_KEY=zefuihzefizpaefhzoiefhzeiofhze2342ofhizefzoe
                        TESTING=true
                    ' > .env
                '''
            }
        }
        stage('Install latests dependencies') {
            steps {
                sh '''#!/bin/bash
                    poetry install
                '''
            }
        }
        
        stage('MigrateDatabase') {
            steps {
                sh '''#!/bin/bash
                    poetry run alembic upgrade head
                '''
            }
        }
        stage('RunApi') {
            steps {
                sh '''#!/bin/bash
                    poetry run uvicorn api:app
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
