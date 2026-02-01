NIMBUS PLATFORM - KUBERNETES SETUP OVERVIEW
==========================================

This project is a small Internal Developer Platform (IDP) built on Kubernetes.
It uses GitOps, Ingress routing, monitoring, and authentication tools.

--------------------------------------------------
KUBERNETES
--------------------------------------------------
Runs all applications (frontend, backend, monitoring, auth) as Pods using
Deployments, Services, and Ingress resources.

--------------------------------------------------
TRAEFIK (INGRESS CONTROLLER)
--------------------------------------------------
Traefik is the entry point to the cluster.
It receives traffic from the browser and routes it to the correct service
based on Ingress rules.

Flow:
Browser -> Traefik -> Service -> Pod

--------------------------------------------------
INGRESS
--------------------------------------------------
Ingress defines routing rules using hostnames.

Examples:
frontend.local  -> frontend service
backend.local   -> backend service
grafana.local   -> grafana service
keycloak.local  -> keycloak service

Works together with Traefik.

--------------------------------------------------
SERVICE
--------------------------------------------------
Service provides a stable internal DNS name and load balances traffic to Pods.

Example:
backend service routes traffic to backend Pods.

Frontend calls backend using:
http://backend/api/people

--------------------------------------------------
FRONTEND (UI)
--------------------------------------------------
Web application that displays data from the backend API.

Flow:
Browser -> Traefik -> frontend service -> frontend pod
Frontend -> backend service -> backend pod

--------------------------------------------------
BACKEND (API)
--------------------------------------------------
REST API that returns people data at /api/people.

Connected to:
- PostgreSQL database
- Frontend UI
- Exposed via Ingress (backend.local)

--------------------------------------------------
POSTGRESQL (DATABASE)
--------------------------------------------------
Stores backend data.
Only backend service communicates with database using service name "postgres".

--------------------------------------------------
ARGO CD (GITOPS)
--------------------------------------------------
Argo CD automatically deploys everything from GitHub into Kubernetes.

Flow:
GitHub Repo -> ArgoCD -> Kubernetes Cluster

Benefits:
- Single source of truth
- Auto sync
- Rollbacks
- No manual kubectl apply

--------------------------------------------------
PROMETHEUS (MONITORING)
--------------------------------------------------
Collects metrics from nodes and workloads.

Metrics include:
- CPU
- Memory
- Pods
- Network
- Health status

--------------------------------------------------
GRAFANA (DASHBOARDS)
--------------------------------------------------
Visualizes Prometheus metrics using dashboards.

Shows:
- Cluster health
- Pod resource usage
- Node metrics
- Application performance

Accessible via grafana.local

--------------------------------------------------
KEYCLOAK (AUTHENTICATION)
--------------------------------------------------
Identity and access management system.

Provides:
- Login system
- Users and roles
- Tokens (JWT)
- Can secure frontend and backend APIs

Flow:
User -> Keycloak -> token -> frontend/backend

--------------------------------------------------
CERT-MANAGER (TLS / HTTPS)
--------------------------------------------------
Creates TLS certificates automatically for HTTPS.

Used for:
- frontend.local
- backend.local
- grafana.local
- keycloak.local

--------------------------------------------------
METALLB (LOADBALANCER)
--------------------------------------------------
Provides an external IP address for Traefik in the local network.

Example:
192.168.18.240

--------------------------------------------------
DNS (/etc/hosts)
--------------------------------------------------
Maps domain names to Traefik external IP.

Example:
192.168.18.240 frontend.local
192.168.18.240 backend.local
192.168.18.240 grafana.local
192.168.18.240 keycloak.local

--------------------------------------------------
OVERALL TRAFFIC FLOW
--------------------------------------------------
Browser
   |
Traefik (Ingress Controller)
   |
Ingress Rule (host routing)
   |
Service
   |
Pod (Frontend / Backend / Grafana / Keycloak)

--------------------------------------------------
REPOSITORY STRUCTURE
--------------------------------------------------
argocd/applications/
  frontend.yaml
  backend.yaml
  grafana.yaml
  traefik.yaml
  keycloak.yaml

apps/
  frontend/
  backend/
  keycloak/

--------------------------------------------------
PURPOSE OF THIS PLATFORM
--------------------------------------------------
- Learn Kubernetes networking
- Learn GitOps with ArgoCD
- Learn Ingress and Services
- Learn monitoring (Prometheus and Grafana)
- Learn authentication (Keycloak)
- Simulate production-like architecture

--------------------------------------------------
COMPONENT SUMMARY
--------------------------------------------------
Traefik      : Entry point, routes traffic using Ingress
Ingress      : Maps hostnames to services
Service      : Stable internal endpoint for Pods
Frontend     : UI calling backend API
Backend      : REST API service
Postgres     : Database for backend
ArgoCD       : GitOps deployment tool
Prometheus   : Metrics collection
Grafana      : Monitoring dashboards
Keycloak     : Authentication provider
MetalLB      : External IP for Traefik
Cert-manager : HTTPS certificates
