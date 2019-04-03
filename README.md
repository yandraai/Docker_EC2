Cloud_Project01
===================

Problem Statement
------------------
- Dockerizing the REST API and the dynamic UI built and hosted on Amazon_EC2.

Step 1: Installation Steps
------------------------------
- sudo yum update -y
- sudo yum install -y docker
- sudo service docker start
- sudo usermod -a -G docker ec2-user
- docker login -u yandraai
- docker pull python:3.5

Step 2: Create Requirements.txt 
-------------------------------
- Provided all the libraries used for the project -flask, flask_restplus, flask_api. 


Step 3: Create Docker File
--------------------------
- Used a base image : Python
- Provided my requirements.txt
- CMD for running the python file.

Step 4: Build Docker Image
--------------------------
- docker build -t Image_name .

Step 5: Run Docker Image
--------------------------
- docker run -d --name Container_Name 5000:80 Image_name

Step 6: Tag Docker Image
--------------------------
- docker tag Image_ID yourhubusername/Imagename

Step 7: Push Docker Image
--------------------------
- docker push yourhubusername/Image_name

How to pull and Run:
---------------------
- docker pull "yandraai/applicationfirst:latest"
- docker run -d test 5000:80 yandraai/applicationfirst




