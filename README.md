
## Run project 

BASE_PATH=. docker-compose up  --build

## Setup
- setup auth user for n8n 
- import workflow "workflows/code_migrator_v3.json"
- setup gemini (or your llm), github tokens, set these credentials to all required nodes:
![alt text](img/creds.png)

## Example project
https://github.com/pmgridd/cobol-samples/tree/main/src/main/cobol

## Agent input example

1. migrate project {repo} = https://github.com/pmgridd/cobol-samples.git {folder} = /src/main/cobol/ATTRACT.CBL {pl} = "java"

2. migrate project {repo} = https://github.com/pmgridd/cobol-samples.git {folder} = /src/main/cobol/ATTRACT.CBL,/src/main/cobol/BRAKES.CBL {pl} = "java", make sure it uses spring boot and exposes methods as REST APIs

3. migrate project {repo} = https://github.com/pmgridd/cobol-samples.git {folder} = /src/main/cobol/ATTRACT.CBL,/src/main/cobol/BRAKES.CBL {pl} = "python", make sure it uses flask and exposes methods as REST APIs

![alt text](img/general_view.png)

