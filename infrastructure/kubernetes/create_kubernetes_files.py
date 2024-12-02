# Script to generate Kubernetes YAML files for a Python application
def create_kubernetes_files(app_name="my-python-app", image="my-python-app:latest", port=80, replicas=3):
    # Deployment YAML
    deployment_content = f"""
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: {app_name}-deployment
      labels:
        app: {app_name}
    spec:
      replicas: {replicas}
      selector:
        matchLabels:
          app: {app_name}
      template:
        metadata:
          labels:
            app: {app_name}
        spec:
          containers:
          - name: {app_name}
            image: {image}
            ports:
            - containerPort: {port}
    """
    
    # Service YAML
    service_content = f"""
    apiVersion: v1
    kind: Service
    metadata:
      name: {app_name}-service
    spec:
      selector:
        app: {app_name}
      ports:
      - protocol: TCP
        port: {port}
        targetPort: {port}
      type: LoadBalancer
    """
    
    # Save deployment YAML
    with open("deployment.yaml", "w") as deployment_file:
        deployment_file.write(deployment_content.strip())
    
    # Save service YAML
    with open("service.yaml", "w") as service_file:
        service_file.write(service_content.strip())
    
    print("Kubernetes YAML files have been created successfully!")

# Execute the function to create Kubernetes YAML files
create_kubernetes_files()




#How It Works
#Deployment YAML:

#Creates a Kubernetes Deployment with a specified number of replicas.
#Deploys a Docker container (specified by the image parameter).
#Exposes a port inside the container.
#Service YAML:

#Creates a Kubernetes Service to expose the Deployment.
#Uses a LoadBalancer type to make the service accessible externally.

##############################
# Two files will be generated:
# deployment.yaml
# service.yaml