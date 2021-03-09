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
                    sudo /etc/poetry/bin/poetry install
                '''
            }
        }
        stage('SetupDatabase') {
            steps {
                sh '''#!/bin/bash

                    echo "Clear Database ..."
                    sudo -u postgres psql -c "DROP DATABASE IF EXISTS mspr2_test;"
                    
                    echo "Setup new Database ..."
                    sudo -u postgres psql -c "CREATE DATABASE mspr2_test OWNER mspr2;"
                '''
            }
        }
        stage('MigrateDatabase') {
            steps {
                sh '''#!/bin/bash
                    sudo /etc/poetry/bin/poetry run alembic upgrade head
                '''
            }
        }
        stage('RunApi') {
            steps {
                sh '''#!/bin/bash
                    sudo /etc/poetry/bin/poetry run uvicorn api:app
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
