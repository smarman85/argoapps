# argoapps

## localhost set up:
```bash
$ kubectl port-forward svc/argocd-server -n argocd 8080:443
```

## Init apps via crd:
```bash
$ kubectl apply -f crds/apps.yaml
```

## Init apps:
```bash
$ argocd app create apps \
--dest-namespace argocd \
--dest-server https://kubernetes.default.svc \
--repo https://github.com/smarman85/argoapps.git \
--path apps
```

## Sync apps:
```bash
$ argocd app sync gosite
```

## Sync app:
```bash
$ argocd app sync gosite
```
