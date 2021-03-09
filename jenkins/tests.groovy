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
        stage('test') {
            steps {
                sh '''#!/bin/bash
                   echo "Running tests ..."
                   sudo /etc/poetry/bin/poetry run pytest
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
