pipeline {
  agent any
  stages {
    stage('copy file to csv') {
      steps {
        sh 'cat $WORKSPACE/text.txt >> /home/ansiblecontrol/predicttbs/predict.csv'
      }
    }
  } 
}
