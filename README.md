# Password-Manager
A password manager

This application is a password manager built with Flask on the backend serving both an api and a React frontend with data stored in a Microsoft Azure SQL database, containerized in a Docker container to make for easier deployment.

The purose of this application is as follows: 

1. Create a useful full stack application to demonstrate my development skills.
2. Implement as many Azure services as possible to demonstrate my understanding of DevOPs and cloud computing.
3. Build a modern devops pipeline to automate deployments.

## Pipeline

Update the source code. Python server and React frontend are in one docker container, data is stored in Google Firebase Firestore.

        |
        v

Push to development branch.

        |
        v

Once features are ready, push to production

        |
        v

Run github actions 
    run unit tests, 
    build docker image
    push to docker hub.

        |
        v

Automatically deploy to DigitalOcean droplet.  














