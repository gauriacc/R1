pipeline {
  agent any
  stages {
    stage('copy file to csv') {
      steps {
        sh 'cd $WORKSPACE'
        sh 'pwd'
        sh 'cat $WORKSPACE/tbs_space_check/text.txt >> /home/ansiblecontrol/predicttbs/predict.csv'
      }
    }
  } 
}
