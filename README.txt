Features supported:
1.Listing of events using the categories from the EventBrite API
2.List all the relevent events for the selected categories with pagination

Features To Do:
1. Javascript to limit the number of categories to 3.
2. Render a custom bad request page if the category entered in the URL does not exist
3. Generate Authentication tokein for the specific user

Installation Instruction:
---------
 - Install the required packages from the requirements.txt file on the ubuntu:14.04. 
 - Copy the helloworld/, mysite/, manage.py folders to the folder /opt/eventbrite/
 - Run the following command to start the DJango server:
 	"sudo python /opt/eventbrite/manage.py runserver 0.0.0.0:8000" 
 -  Open the browser on the host machine and navigate to the URL to view the running django app:

	http://127.0.0.1:8000/helloworld/index



Docker Version
---------------
I have created a docker Image for ubuntu:14.04 containining all the necessary packages for the App.
Prerequisite: DockerEngine running on the host.

Commands to be execute:
> chmod +x run.sh
> sudo ./run.sh

Contents of the run.sh
```
#!/usr/bin/sh
docker build -t gauree45/eventbrite:v1 .
docker run -it -p 8000:8000 gauree45/eventbrite:v1
```

It will build a docker image and next will run the docker image gauree45/eventbrite:v1. It will also map the port 
8000 of docker container to the host 8000 port.

One can then open the browser on the host machine and navigate to the URL to view the running django app:

http://127.0.0.1:8000/helloworld/index


