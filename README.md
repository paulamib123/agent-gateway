# Agent Gateway

## Steps to run the Agent-Gateway

### • Creating the .env file

1. Create a .env file in the root folder

2. Mention the following variables in .env file

```
    DATABASE_USERNAME=<database-username>
    DATABSE_PASSWORD=<database-password>
    DATABSE_HOST=<database-host>
    DATABSE_PORT=<database-host>
    DATABASE_NAME=<database-name>
```

### • Running the DockerFile
1. Create a data folder and a logs folder inside the root folder

2. Run the following docker commands inside the root folder.

3. Build the docker file 

```  
    docker build /
    -t <container-name> . 
```

4. Run the docker file 

```
    docker run /
    -p 5000:5000 /
    -v <your-absolute-path-to-data-folder>:/server/data /
    -v <your-absolute-path-to-logs-folder>:/server/logs /
    --env-file <your-absolute-path-to-.env-file>
    <container-name>
```
