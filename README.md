# Agent Gateway

## Steps to run the docker file
1. Create a data folder inside the root folder
3. docker build /
    -t <container-name> .
2. docker run /
    -p 5000:5000 /
    -v <your-absolute-path-to-data-folder>:/validateAgentOutputAPI/data 
    <container-name>