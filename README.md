# Agent Gateway

## Steps to run the docker file

1. Create a data folder inside the root folder

2. Run the commands inside the root folder.

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
    <container-name>
```
