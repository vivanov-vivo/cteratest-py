__How to get Build Info from Jenkins in python script.__
Script my_script_with_args.py shows how build information can be taken from Jenkins using python-jenkins api.
Before running script:
   - verify the path to python in the script;
   - replace Jenkins details in the necxt line:
      server = jenkins.Jenkins('http://<jenkins_host>:<jenkins_port>', username='<jenkins_user>', password='<jenkins_password>')
   - make sure your usage is correct:
      Usage: ./<Script_name> <Job_name> <Build_num>
      
 Output of the file :
Job    ctera_pipeline
     Build number :11    started by:   admin
     Build status:    SUCCESS
     Build duration :   0:00:44.615000
     Artifacts number is  2 : 
          -      Reports_Build_11.zip
          -      my-app-1.0-SNAPSHOT.jar
 
