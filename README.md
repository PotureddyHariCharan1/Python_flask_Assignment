# Python_flask_Assignment

## Installation

> How to Install Flask on Ubuntu 20.04

`` https://linuxize.com/post/how-to-install-flask-on-ubuntu-20-04/``

> Install jenkins

`` https://www.digitalocean.com/community/tutorials/how-to-install-jenkins-on-ubuntu-20-04 ``

## Initail Tasks

> Steps done ..

>> After pip and flask instalation we can write simple `hello,world program` and save it as `hello.py` or `app.py`

>> Make that program to run on `port 8080` 'flask run -p 8080' now we can check buy running ## `http//localhost:8080/` or ## `http://127.0.0.1:8080/`

>> push the code to github public repo  and at the time of creation it self made settings to only main branch can merge.

>> After jenkins instalation on machine deploying jenkins on `8080` port with `public ip of machine`. ## `http://172.52.X.X:8080/`

>> After adding plugins and login credentals we will be able to see a home page of jenkins.

>> Create a freestyle job and add git public repo link to it and also need to add login access credentals to jenkins machine

>> After creation of successfull Ci pipeline , search for "Delivery Pipeline" & Build pipeline plugins. Select `Delivery Pipeline & Build pipeline` plugin and click on Install without Restart.

### Delivery Pipeline

   >>> To see the Delivery Pipeline in action, click on `+`  `symbol` in the tab next to the `All tab` on the Jenkins Dashboard screen.

   >>> Give the View name and select Delivery Pipeline View. Click on OK button.

   >>>  Make sure "Show static analysis results" option is checked.
   
   >>> Make sure the option "Show total build time" is checked.
   
   >>> In the Pipelines section for the Initial job enter the `Helloworld project` as the first job which should build.    
   
   >>> Give`flask` as name for the Pipeline
   
   >>> Click the Apply and OK button.
    
### Build Pipeline

   >>> In the View name option, enter job name as `Build_Pipeline` and choose the Build Pipeline View Option.
   
   >>> Leave all the default option and scroll down. In the Upstream/downstream config section enter the name of the `HelloWorld` project for the select initial job option. Then click on the OK button.
   
### WEBHOOK

>> Now we need to create a webhook to out git hub repo so that if any changes are made it will auto trigger the build 

>> give payload URL as `public_machine_IP` along with host port address followed by `/github-webhook/` to make github and jenkins recognize that given link is a WEBHOOK link n the `Content type` select: `application/json` and leave the ‘Secret’ field empty.
###### example:http://172.52.X.X:8080/github-webhook/

>> Choose ‘Let me select individual events.’ Then, check ‘Pull Requests’ and ‘Pushes’. At the end of this option, make sure that the ‘Active’ option is checked and click on ‘Add webhook’.

>> In jenkins Click on the `Build Triggers` tab and then on the `GitHub hook trigger for GITScm polling`.

>> now if any changes are made on given github repo link it will auto triggers the build's
