# jenkins-test
Test case to run github and jenkins.

## Mesos/Jenkins Test Case

1. Start a Jenkins slave on mesos cluster
2. Have Jenkins slave pull this repo
3. Have Jenkins slave build Dockerfile
3. Have Jenkins slave run the python scripts in /test using the docker container
5. Have Jenkins slave tag and push docker container to private registry "privaterepo/jenkins-test"


## Automated Test Case

1. Have Jenkins pull this repo on new git commit
2. Run Mesos/Jenkins Test


## Misc

https://github.com/jenkinsci/mesos-plugin

![alt tag](https://ahunnargikar.files.wordpress.com/2014/05/docker_flow1.png)

