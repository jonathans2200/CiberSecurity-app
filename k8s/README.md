# Despliegue de Aplicación en Kubernetes

## Descripción

Este proyecto contiene la configuración necesaria para desplegar una aplicación compuesta por servicios FastAPI, Vue.js y Kong API Gateway en un cluster Kubernetes local utilizando Minikube, simulando un ambiente de producción.

## Requisitos Previos

### Software Obligatorio

- [Docker Desktop](https://www.docker.com/products/docker-desktop) (v20.10+)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/) (v1.30+)
- [kubectl](https://kubernetes.io/docs/tasks/tools/) (compatible con tu versión de Kubernetes)

### Dependencias de Desarrollo

- [Python](https://www.python.org/downloads/) 3.9 o superior
- [Node.js](https://nodejs.org/) 16.x o superior
- [Docker Compose](https://docs.docker.com/compose/install/) (generalmente incluido con Docker Desktop)

### Verificación de Versiones

Ejecuta estos comandos para verificar las versiones instaladas:

```bash
# Verificar versiones críticas
python --version
node --version
docker --version
minikube version
kubectl version --client
```
## Despliegue localmente en Kubernates 
### 1. Iniciar Minikube
```bash
minikube start --driver=docker 
```
### 2. Configurar el entorno Docker (si construiste imágenes localmente)
Windows
```bash
minikube docker-env | Invoke-Expression
docker info --format "{{.Name}}"
```

Previo a aplicar los archivos se deben compilar las imagenes necesarias

### 3. Aplicar los archivos en orden
Infraestructura básica
```bash
kubectl apply -f 1_namespace.yml
kubectl apply -f 2_persistentVolumeClaim.yml
kubectl apply -f 3_secrets.yml
```

Configuraciones
```bash
kubectl apply -f kong-configmap.yml
kubectl apply -f db-mcp-configmap.yml
```

Bases de datos
```bash
kubectl apply -f 4_1_db_main_backend.yml
kubectl apply -f 4_2_db_mcp.yml
```

Microservicios
```bash
kubectl apply -f 5_fastapi_vt.yml
kubectl apply -f 6_fastapi_mcp.yml
```

Capa de presentación
```bash
kubectl apply -f 7_kong.yml
kubectl apply -f 8_adminer.yml
kubectl apply -f 9_frontend.yml
```

### 4. Verificar el estado
Vista general
```bash
kubectl get all -n app-virustotal
```

Monitoreo continuo de pods
```bash
kubectl get pods -n app-virustotal -w
```

### 5. Acceder a la aplicación
Listar todos los servicios disponibles
```bash
minikube service list -n app-virustotal
```

Abrir el frontend en el navegador predeterminado
```bash
minikube service frontend-app -n app-virustotal
```

### 6. Administración y solución de problemas
Ver logs de un pod específico:
```bash
kubectl logs <pod-name> -n app-virustotal
```

Reiniciar un deployment:
```bash
kubectl rollout restart deployment/<deployment-name> -n app-virustotal
```

Eliminar completamente el namespace:

```bash
kubectl delete namespace app-virustotal
```