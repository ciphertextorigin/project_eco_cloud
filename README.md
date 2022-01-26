[![Run tests on any Push event](https://github.com/cforcross/toney_int/actions/workflows/test.yml/badge.svg)](https://github.com/cforcross/toney_int/actions/workflows/test.yml)

### Setup For Server
- Build the Web Server using Flask. 


- creat virtual env
`python3 -m venv venv`

-Install requirements.txt
`pip3 install -r requirements.txt`

### Run Server

move to src directory
`flask run`

##### To Test

- All test are being run using `Unittest`
`python app_test`

#### Build Docker Image

- Move to base directory 
`sudo docker build -t favouriteflower .`


## Minikube

* Start the Minikube
`minikube start`

* check if Minikube is running locally
`minikube get nodes`

* Enable Ingress Controller
`minikube addons enable ingress`

# Create K8s for deploy
`kubectl apply -f deployment.yaml`

# Create Service CMD
`kubectl apply service.yaml`

# Run the app 
`minikube service flask-service --url`

* Create Ingress for k8s
`kubectl apply -f nginx-service.yaml`

- Next we adjust our hosts file => `etc/hosts` as  follows
`our ip`  `local.ecosia.org/tree` 
So we can access our app from http://local.ecosia.org/tree

# Run full deployment script with
- `chmod u+x build-and-deploy.sh`
- then
- `./build-and-deploy.sh`

## Configure github actions
Configure github actions to build image, push to dockerhub and run deployment script
