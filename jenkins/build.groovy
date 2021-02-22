pipeline {
    agent any

    stages {
        stage('Setup config') {
            steps {
                sh '''#!/bin/bash

                    touch .env
                    echo '
                        DATABASE_URL=postgresql://mspr2:123456789@localhost:5432/mspr2_test
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
                    poetry run alembic upgrade head
                '''
            }
        }
        stage('RunApi') {
            steps {
                sh '''#!/bin/bash
                    poetry run uvicorn api:app --host 0.0.0.0 --port 80
                '''
            }
        }
    }
}