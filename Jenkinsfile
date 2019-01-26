pipeline {
  agent {
    node {
      label 'docker-node'
    }

  }
  stages {
    stage('preparation') {
      steps {
        git(url: 'https://github.com/atam84/app-inventory.git', changelog: true)
      }
    }
    stage('code analyses') {
      steps {
        withSonarQubeEnv('SonarQube_3.3') {
          waitForQualityGate true
        }

      }
    }
    stage('build') {
      steps {
        build 'python setup.py build'
      }
    }
  }
}