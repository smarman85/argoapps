# argoapps

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
