# Simple Python Flask Dockerized Application#

Build the image using the following command

```bash
$ docker build -t simple-flask-app:latest .
```

Run the Docker container using the command shown below.

```bash
$ docker run -d -p 5000:5000 simple-flask-app
```

The application will be accessible at http:127.0.0.1:5000 or if you are using boot2docker then first find ip address using `$ boot2docker ip` and the use the ip `http://<host_ip>:5000`


    create configmap from files
    https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/#create-configmaps-from-files

    using the ConfigMap or Secret to store environmental and security configurations.
    https://kubernetes.io/docs/concepts/configuration/secret/#use-cases
    https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/#configure-all-key-value-pairs-in-a-configmap-as-container-environment-variables


    creating configmap,

    the path i have followed is
        - there is a env file already present in our system.
        - converted that to ConfigMap, which ultimately has every key-value pairs.
        - convert that ConfigMap to Secret.
        - load that secret onto kubernetes.
        - now every deployment.yaml will use this secret configuration as envFrom.

    kubectl create configmap simpleconf --from-file=env
    kubectl get configmaps simpleconf -o yaml
