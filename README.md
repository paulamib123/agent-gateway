# Agent Gateway

## Steps to run the docker file

1. Create a data folder inside the root folder

2. Build the docker file 

```  
    docker build /
    -t <container-name> . 
```

3. Run the docker file 

```
    docker run /
    -p 5000:5000 /
    -v <your-absolute-path-to-data-folder>:/server/data
    <container-name>
```
