# Technische Umsetzung

## Repository Struktur

| Pfad | Inhalt |
| --- | --- |
| `.github/workflows/` | CI CD Workflows (Build, Deploy, Docs, PR Checks) |
| `docs/` | MkDocs Dokumentation (Markdown, CSS, Mermaid, Screenshots) |
| `k8s/` | Kubernetes Manifeste (Namespace, Deployment, Service, Ingress) |
| `service/` | Python Flask Microservice |
| `Dockerfile` | Container Build |
| `mkdocs.yml` | MkDocs Konfiguration |

---

## Voraussetzungen

| Tool | Zweck |
| --- | --- |
| Docker | Lokaler Build und Tests |
| kubectl | Interaktion mit K3s |
| GitHub Actions | CI CD Ausführung |
| GHCR | Image Registry |
| AWS EC2 | Laufzeit Infrastruktur |
| K3s | Kubernetes Cluster auf EC2 |

---

## Lokale Entwicklung

| Schritt | Befehl oder Aktion | Ergebnis |
| --- | --- | --- |
| Abhängigkeiten installieren | `pip install -r service/requirements.txt` | Lokale Umgebung bereit |
| Service starten | `python service/run.py` | Endpoint lokal erreichbar |
| Smoke Test | `curl http://localhost:PORT/health` | 200 OK |

Hinweis
- Ports und Entry Points können je nach Service Setup abweichen.

---

## Containerisierung

| Schritt | Befehl | Zweck |
| --- | --- | --- |
| Image bauen | `docker build -t geraeteausleihe:local .` | Lokaler Build |
| Container starten | `docker run -p 8080:8080 geraeteausleihe:local` | Lokaler Test |
| Logs prüfen | `docker logs -f <container>` | Fehleranalyse |

---

## Kubernetes Deployment (K3s)

### 1 Manifeste anwenden

| Schritt | Befehl |
| --- | --- |
| Namespace | `kubectl apply -f k8s/namespace.yaml` |
| Deployment | `kubectl apply -f k8s/deployment.yaml` |
| Service | `kubectl apply -f k8s/service.yaml` |
| Ingress | `kubectl apply -f k8s/ingress.yaml` |

### 2 Status verifizieren

| Check | Befehl |
| --- | --- |
| Pods | `kubectl get pods -n <namespace>` |
| Service | `kubectl get svc -n <namespace>` |
| Ingress | `kubectl get ingress -n <namespace>` |
| Logs | `kubectl logs -n <namespace> deploy/<deployment>` |

---

## Ingress und Erreichbarkeit

| Element | Beschreibung |
| --- | --- |
| Ingress Controller | Traefik ist in K3s standardmässig aktiv |
| Hostname | nip io Host, z. B. `geraeteausleihe.<EC2_IP>.nip.io` |
| Test | Browser oder curl gegen den Host |

Beispiel

```bash
curl -i http://geraeteausleihe.<EC2_IP>.nip.io/health
```

---

## CI CD

### Workflows

| Workflow | Aufgabe | Trigger Idee |
| --- | --- | --- |
| `container-build.yml` | Build und Push nach GHCR | Änderungen im Service Bereich |
| `deploy-k3s.yml` | Apply Manifeste und Rollout | Push auf main oder manuell |
| `docs-pages.yml` | MkDocs Build und Publish | Änderungen in `docs/` oder `mkdocs.yml` |
| `pr-checks.yml` | Checks für Pull Requests | PR gegen main |

### Typischer Ablauf

| Schritt | Beschreibung |
| --- | --- |
| 1 | Commit auf `develop` |
| 2 | Pull Request von `develop` nach `main` |
| 3 | GitHub Actions baut Image und pusht nach GHCR |
| 4 | Deploy Workflow wendet Manifeste auf EC2 an |
| 5 | Kubernetes rollt neues Image aus |

---

## Versionierung und Rollback

| Thema | Umsetzung |
| --- | --- |
| Tags | `latest` plus Commit SHA als eindeutiger Tag |
| Rollback | `kubectl rollout undo` oder Image Tag zurücksetzen |
| Nachweis | Workflow Logs und `kubectl rollout status` |

---

## Verifikation und Nachweise

| Nachweis | Beschreibung | Ort |
| --- | --- | --- |
| Build Log | GitHub Actions Run | Actions Tab |
| Image Tag | GHCR Package Übersicht | GHCR |
| Deploy Log | kubectl apply und rollout status | Actions Log oder EC2 Terminal |
| Endpoint Test | /health und /pdf erreichbar | Screenshot oder curl Output |
| Dokumentation | Aktualisierte Seiten | GitHub Pages |

---

## Typische Fehlerbilder

| Problem | Ursache | Lösung |
| --- | --- | --- |
| Image Tag Fehler | Registry Name nicht lowercase | Repo Namen in Workflows prüfen |
| Ingress nicht erreichbar | Host oder Service Port falsch | Ingress Regeln und Service prüfen |
| Pull Image Fehler | Secret fehlt oder Tag existiert nicht | Secret setzen, Tag prüfen |
| Pod CrashLoopBackOff | App Startfehler | Logs prüfen, Health Checks anpassen |
