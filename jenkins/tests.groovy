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
                    sudo /etc/poetry/bin/poetry install
                '''
            }
        }
        stage('test') {
            steps {
                sh '''#!/bin/bash
                   echo "Running tests ..."
                   sudo /etc/poetry/bin/poetry run pytest
                '''
            }
        }
    }
}
