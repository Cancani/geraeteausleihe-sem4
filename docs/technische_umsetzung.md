# Technische Umsetzung

!!! abstract "Kurzüberblick"
    - Containerisierung des Flask Service (Dockerfile, lokale Tests)
    - CI: PR Checks und Image Build nach GHCR
    - CD: Deployment nach K3s auf AWS EC2 via Kubernetes Manifeste

## Kontext und Ziel

Projekt: Geräteausleihe Microservice  
Ausgangslage: Microservice aus Semesterarbeit 3, umgesetzt mit Python Flask  
Ziel dieser Phase: Cloud Native Betrieb mit Container Image, Kubernetes Deployment auf K3s in AWS EC2, sowie CI und CD Automatisierung über GitHub Actions und GitHub Container Registry

Kernziele

- Containerisierung des bestehenden Services
- Build und Push des Images in GitHub Container Registry
- Betrieb auf AWS EC2 mit K3s
- Kubernetes Ressourcen für Namespace, Deployment, Service, Ingress
- Automatisches Deployment nach erfolgreichem Image Build
- Dokumentation über MkDocs und GitHub Pages

Repository: https://github.com/Cancani/geraeteausleihe-sem4  
Branches: develop für Arbeiten, main für stabile Version, gh pages für GitHub Pages

## Ergebnisstatus

Aktüller Zustand

- Image wird in GHCR erstellt und mit Tags latest sowie Commit SHA veröffentlicht
- K3s läuft auf EC2 und ist erreichbar
- Kubernetes Ressourcen werden angewendet und der Service ist über Ingress erreichbar
- GitHub Actions deployt nach erfolgreichem Container Build automatisch auf die EC2 Instanz
- Endpunkte sind extern testbar

Beispiel Endpoint über nip io

- http://geraeteausleihe.13.223.28.53.nip.io
- http://geraeteausleihe.13.223.28.53.nip.io/healthz
- http://geraeteausleihe.13.223.28.53.nip.io/pdf?borrower=Test&device=Notebook

Hinweis: nip io ist für Tests geeignet. Für Produktivbetrieb sollte eine eigene Domain mit DNS und TLS genutzt werden.

## Repository Struktur

Zielstruktur im Repo

- service  
  - Flask Anwendung, Templates, Static Inhalte, requirements, Gunicorn Entry
- k8s  
  - namespace.yaml  
  - deployment.yaml  
  - service.yaml  
  - ingress.yaml
- .github workflows  
  - container build.yml  
  - deploy k3s.yml  
  - pr checks.yml  
  - docs pages.yml
- docs  
  - MkDocs Inhalte

Warum __init__.py und .gitkeep existieren

- __init__.py markiert Ordner als Python Package. Inhalt kann leer sein, damit Imports funktionieren
- .gitkeep hält leere Ordner im Git Repo, zum Beispiel service app static

## Lokale Ausführung und Tests

### Lokale Ausführung ohne Container

Voraussetzung: Python Umgebung und Abhängigkeiten aus requirements.txt

Befehle

```bash
cd service
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python run.py
```

Tests

```bash
pytest -q test_api.py
```

Wichtige Anpassungen bei Tests

- Bytes Assertion mit Umlaut führte zu SyntaxError, weil bytes literals nur ASCII erlauben
- Lösung: Response Text als String lesen und String Vergleich verwenden

### Container Build und Container Tests

Image baün

```bash
docker build -t geraeteausleihe:test .
```

Tests im Container ausführen

```bash
docker run --rm geraeteausleihe:test sh -c "pip install pytest && cd /srv && pytest -q test_api.py"
```

Hinweise

- pytest muss im Container verfügbar sein, entweder als dependency in requirements.txt oder via pip install im Test Run
- Pytest Cache Warnungen im Container sind reine Rechte Thematik ohne Einfluss auf das Test Ergebnis

## Containerisierung

### Dockerfile

- Base Image python 3.11 slim
- System Libraries für WeasyPrint installiert
- requirements.txt installieren
- service Code nach /srv kopieren
- nicht als root laufen

Ergebnis: Container startet den Microservice über Gunicorn, Port 8080 wird exposed

### .dockerignore

Ziel: Unnötige Dateien aus Build Context entfernen

Beispiele

- .venv
- __pycache__
- .pytest_cache
- .git

### .gitignore

Ziel: Lokale Artefakte nicht committen

Beispiele

- .venv
- __pycache__
- .pytest_cache
- .vscode
- *.log

## GitHub Actions

Es wurden mehrere Workflows erstellt, um Build, Tests und Deployment zu automatisieren.

### PR Checks

Ziel

- Bei Pull Requests werden Tests und Lint Checks ausgeführt
- Dadurch wird verhindert, dass fehlerhafte Änderungen in main landen

### Container Build zu GHCR

Ziel

- Bei Push auf main wird das Image gebaut und in GHCR gepusht

Kritische Anpassung

- GHCR Repository Namen müssen lowercase sein
- github.repository liefert Owner Repo und kann Grossbuchstaben enthalten
- Lösung: repository in lowercase umwandeln

Tags

- latest
- Commit SHA

### Deployment zu K3s auf EC2

Ziel

- Nach erfolgreichem container build Workflow wird automatisch deployt
- Kubernetes Manifeste werden via scp auf die EC2 kopiert
- Anschliessend werden die Ressourcen angewendet
- Image wird auf das neü Tag gesetzt
- Rollout wird abgewartet

Secrets in GitHub

Diese Secrets wurden in GitHub Actions Repository Secrets hinterlegt

- EC2_HOST
- EC2_USER
- EC2_SSH_KEY

Hinweis: Secrets gehören in Actions Secrets, nicht in Environment Secrets, sofern kein Environment genutzt wird.

## AWS Setup und K3s Installation

### AWS Setup

Umgebung: AWS Academy Learner Lab  
Region: us east

EC2

- Instance Typ: t3 small
- Ubuntu 22.04
- Elastic IP zugewiesen

Security Group Ports

- 22 für SSH
- 80 für HTTP
- optional 443 für HTTPS

Wichtig: SSH nicht daürhaft offen lassen. Best Practice ist Einschränkung auf feste Source IP oder Nutzung von VPN und Bastion Konzept.

### K3s Installation

Installation auf EC2 wurde bewusst manüll ausgeführt, damit der Ablauf sichtbar und testbar ist. Automatisierung wäre später mit Terraform und Cloud Init oder Ansible möglich.

Befehle

```bash
curl -sfL https://get.k3s.io | sh -
```

Kubeconfig Berechtigung

Kubectl Zugriff für ubuntu Nutzer

```bash
sudo chmod 644 /etc/rancher/k3s/k3s.yaml
mkdir -p ~/.kube
sudo cp /etc/rancher/k3s/k3s.yaml ~/.kube/config
sudo chown $(id -u):$(id -g) ~/.kube/config
```

Cluster Check

```bash
kubectl get nodes
kubectl get pods -A
```

Träfik ist bei K3s standardmässig aktiv und übernimmt Ingress.

## Kubernetes Deployment

### Namespace

- Eigener Namespace geräteausleihe

### Deployment

- 1 Replica
- Container Image aus GHCR
- Container Port 8080
- Readiness und Liveness Probes für healthz

### Service

- ClusterIP Service auf Port 80
- Target Port 8080

### Ingress

- IngressClass träfik
- Host wird auf nip io gesetzt

Wichtig: Ein Platzhalter wie CHANGE_ME ist kein gültiger Host und verhindert das Anlegen des Ingress. Wenn der Ingress nicht erstellt wird, kann er danach auch nicht gepatcht werden.

## Manülles Deployment auf EC2

Manülles Deployment diente zur Verifikation von YAML Dateien und zur Fehlersuche.

Repo holen

```bash
git clone https://github.com/Cancani/geraeteausleihe-sem4.git
cd geraeteausleihe-sem4
```

Manifeste anwenden

```bash
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/ingress.yaml
```

Ingress prüfen

```bash
kubectl -n geraeteausleihe get ingress
```

Wichtig beim Pfad

Wenn man im Ordner k8s steht, darf der apply Pfad nicht erneut k8s enthalten. Beispiel

- korrekt: kubectl apply -f ingress.yaml
- falsch: kubectl apply -f k8s/ingress.yaml

## Automatisiertes Deployment und Verifikation

### Typischer Ablauf

1. Änderungen auf develop committen und pushen
2. Pull Request von develop nach main
3. PR Checks laufen und müssen grün sein
4. Merge nach main
5. container build Workflow baut Image und pusht nach GHCR
6. deploy k3s Workflow läuft und aktualisiert Deployment in K3s

### Verifikation auf GitHub

Auf der Actions Seite prüfen

- container build ist success
- deploy k3s ist success

In Logs prüfen

- kubectl apply ohne Fehler
- kubectl set image setzt korrektes Image, kein ghcr.io/:tag

### Verifikation auf EC2

Ressourcen Check

```bash
kubectl -n geraeteausleihe get all
kubectl -n geraeteausleihe get ingress
kubectl -n geraeteausleihe get deploy geraeteausleihe -o jsonpath='{.spec.template.spec.containers[0].image}{"\n"}'
```

Pod Details bei Fehlern

```bash
kubectl -n geraeteausleihe describe pod <podname>
kubectl -n geraeteausleihe logs <podname>
```

Extern Test

```bash
curl -i http://geraeteausleihe.13.223.28.53.nip.io/healthz
curl -I "http://geraeteausleihe.13.223.28.53.nip.io/pdf?borrower=Test&device=Notebook"
```

## Typische Fehler und Lösungen

### GHCR Tag Fehler repository name must be lowercase

Ursache

- github.repository enthält Grossbuchstaben

Lösung

- in tags und in deploy script den Repo Namen in lowercase verwenden, zum Beispiel ${GITHUB_REPOSITORY,,}

### InvalidImageName und Image ghcr.io/:

Ursache

- Image String wurde falsch zusammengesetzt, dadurch fehlte repository path

Lösung

- IMAGE="ghcr.io/${GITHUB_REPOSITORY,,}:${DEPLOY_SHA}"
- danach set image auf den Container Namen anwenden

### Ingress nicht vorhanden nach apply

Ursache

- Host im Ingress war ungültig, zum Beispiel CHANGE_ME

Lösung

- Host direkt gültig definieren oder Ingress erst mit gültigem Host erstellen, danach optional patchen

### kubectl permission denied auf /etc rancher k3s k3s yaml

Ursache

- Kubeconfig ist root only

Lösung

- Kubeconfig kopieren und Berechtigung für ubuntu Nutzer setzen, siehe Abschnitt Kubeconfig Berechtigung

### WeasyPrint unter Windows bei local pytest

Ursache

- WeasyPrint benötigt native Libraries wie gobject und pango, die unter Windows nicht automatisch vorhanden sind

Lösung

- Tests in Docker Container ausführen oder WeasyPrint Abhängigkeiten auf Windows korrekt installieren

## PowerApps Integration

Der PDF Endpoint wird aus PowerApps über Launch mit Qüry Parametern aufgerufen. Der Host muss auf den Ingress Endpoint zeigen.

Beispiel URL

http://geraeteausleihe.13.223.28.53.nip.io/pdf?borrower=Demirci%20Efekan&device=HP%20Elitebook%20860%20G6&staff=Efekan%20Demirci

## Erledigte Arbeitspakete und User Stories

Basierend auf dem aktüllen Stand wurden folgende Bereiche umgesetzt

- US10 Namespace und Basis Ressourcen
- US11 Dockerfile finalisieren
- US12 GHCR Push verifizieren
- US13 Kubernetes Deployment Manifest
- US14 Kubernetes Service Manifest
- US15 Ingress konfigurieren
- US16 Readiness und Liveness Probes
- US18 GitHub Actions Build und Push nach GHCR
- US20 CD Workflow Deployment nach K3s

Zusätzlich

- Test Setup mit pytest
- .gitignore ergänzt, damit .venv nicht versioniert wird
- Troubleshooting und Fixes für GHCR Tags, Ingress Host und Image Referenzen

## Nächste Schritte

Empfehlungen für die nächsten technischen Schritte

- Härtung der EC2 Security Group, SSH Source IP einschränken
- Eigene Domain und TLS, zum Beispiel über Träfik und Let s Encrypt
- Automatisiertes Provisioning, zum Beispiel Terraform plus Cloud Init, optional Ansible
- Observability, zum Beispiel logs und metrics Erweiterung, optional Prometheus und Grafana
- Helm Chart oder Kustomize für strukturierte Deployments
