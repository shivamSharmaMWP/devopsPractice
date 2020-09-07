# devopsPractice
no descccccc

    kubectl -f qa-namespace.yaml,qa-comm-service.yaml,qa-comm-deployment.yaml,qa-ingress.yaml apply
    kubectl -f prod-namespace.yaml,prod-comm-service.yaml,prod-comm-deployment.yaml,prod-ingress.yaml apply


kubectl get logs --all-namespaces
kubectl logs -f <pod_id> -n <namespace_name>


kubectl get ingress --all-namespaces
