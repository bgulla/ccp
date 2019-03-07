# Clarissa Cursing Portal (CCP)

Because 40 days and 40 nights are a long time.


## Docker
### Building 
```bash
git clone https://github.com/bgulla/ccp ccp
docker build -t bgulla/ccp ccp
```
### Running
```bash
docker run --rm \
  -p 5000:5000 \
  bgulla/ccp
```

## Kubernetes Support  
#### lent-ccp-deployment.ccp
```yaml
apiVersion: apps/v1beta2
kind: Deployment
metadata:
  generation: 9
  labels:
    app: deployment-default-lent-ccp
  name: lent-ccp
  namespace: default
spec:
  progressDeadlineSeconds: 600
  replicas: 1
  revisionHistoryLimit: 10
  selector:
    matchLabels:
      app: deployment-default-lent-ccp
  strategy:
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
    type: RollingUpdate
  template:
    spec:
      containers:
      - image: bgulla/ccp
        imagePullPolicy: Always
        name: lent-ccp
        ports:
        - containerPort: 5000
          name: 5000tcp01
          protocol: TCP
        resources:
          limits:
            cpu: "1"
            memory: 128Mi
        securityContext:
          allowPrivilegeEscalation: false
          capabilities: {}
          privileged: false
          readOnlyRootFilesystem: false
          runAsNonRoot: true
        stdin: true
        terminationMessagePath: /dev/termination-log
        terminationMessagePolicy: File
        tty: true
      dnsPolicy: ClusterFirst
      restartPolicy: Always
      schedulerName: default-scheduler
      securityContext: {}
      terminationGracePeriodSeconds: 30
```