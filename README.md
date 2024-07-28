# Platform Engineer Case Study

Python project that extracts links from URLs provided in the arguments. The output is displayed weither as one absolute url per line or as a JSON hash.

## Repository tree

.  
├── .github/  
│   └── workflows/  
├── img/  
├── kube/  
├── src/  
├── Dockerfile  
├── README.md  
└── .gitignore  

`.github/workflows/` : github actions workflows that build, push and scan the image for vulnerabilities, then deploy it to a Kubernetes (GKE) cluster.  
`img/`: proofs of executions at each step of the project.  
`kube/`: deployment used to deploy the app into the GKE cluster.  
`src/` : python script + string manipulation shell commands.  
`Dockerfile` : used to package the script into a docker image.  
`README.md` : the file you are currently reading.  
`.gitignore` : gitignore file.