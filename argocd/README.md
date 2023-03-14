## ArgoCD Manifests 

Place the ArgoCD manifests in this directory.

### Displays the admin password.
- kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
