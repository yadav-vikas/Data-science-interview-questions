## Data-science-interview-questions

#### Hi! , if you guys have any comments please do mention or raise issues
 or if you would to add your content please let me know as well!
 
 ###The content in this repository will have topics
 
''-Probabilty''

''-Stats''

''-Maths''

''-Coding questions''

''-Machine learning''

''-Data ananlysis and cleaning''

''SQL''
 
 ##### Have fun!!!
 
 ### An example of Data science process
 
 https://content.codecademy.com/programs/code-foundations-path/ds-survey/lesson-2/Survey-of-DS-Lesson02-Code.html
 
 
 def img
pipeline {
    environment {
        registry = "vikasyadav859/pythonapp"
        registryCredential = "docker-hub login"
        dockerImage = ''
    }
    agent any
    stages {
        stage("clonig our git") {
            steps {
                git "https://github.com/yadav-vikas/viral_app.git"
            }
        }
        stage("building our image") {
            steps {
                script {
                    img = registry + ":${env.BUILD_ID}"
                    println("${img}")
                    dockerImage = docker.build("${img}")
                }
            }
        }
        stage("Testing - running in Jenkins Node") {
            steps {
                sh "docker run -d --name ${JOB_NAME} -p 5000:5000 ${img}"
            }
        }
        stage("deploy our image") {
            steps {
                script {
                    docker.withRegistry( 'https://hub.docker.com', registryCredential) {
                        dockerImage.push()
                    }
                }
            }
        }
        stage("running in staging") {
            steps {
                script {
                    def stopcontainer = "docker stop ${JOB_NAME}"
                    def delcontName = "docker rm ${JOB_NAME}"
                    def delimages = "docker image prune -a --force"
                    def drun = "docker run -d --name ${JOB_NAME} -p 5000:5000 ${img}"
                    sshagent(['docker-test']) {
                        sh returnStatus: true, script: 'ssh -o StrictHostKeyChecking=no docker@172.17.0.1 ${stopcontainer}'
                        sh returnStatus: true, script: 'ssh -o StrictHostKeyChecking=no docker@172.17.0.1 ${delcontName}'
                        sh returnStatus: true, script: 'ssh -o StrictHostKeyChecking=no docker@172.17.0.1 ${delimages}'
                        sh 'ssh -o StrictHostKeyChecking=no docker@172.17.0.1 ${drun}'
                    }
                }
            }
        }
        stage('cleaning up') {
            steps {
                sh "docker rmi $registry:$BUILD_NUMBER"
            }
        }
    }
}
