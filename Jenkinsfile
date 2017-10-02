pipeline {
  agent any
  stages {
    stage('Initialize') {
      steps {
        sh ' source bin/activate'
        git(branch: 'jenkins', url: 'git@github.com:Fettah/library.git', poll: true)
      }
    }
  }
}