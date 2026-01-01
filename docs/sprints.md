# Sprints

## Sprint Übersicht

| Milestone | Fällig (geplant) | Fokus |
| --- | --- | --- |
| Sprint 1 Projektstart und Planung | 05.01.2026 | Board, Labels, Milestones, Doku Struktur, Backlog, erste Reviews |
| Sprint 2 K3s Cluster und erster Deploy | 12.01.2026 | EC2, K3s Installation, Kubernetes Manifeste, Ingress, Probes |
| Sprint 3 CI CD Build Push Deploy | 19.01.2026 | GitHub Actions, GHCR, automatisches Deployment nach K3s |
| Abgabe und Doku fertig | 28.01.2026 | Dokumentation final, Demo Ablauf, Endkontrolle, Abgabe Links |

---

## Sprint 1 - Review und Retrospektive

### Sprint Steckbrief

| Punkt | Inhalt |
| --- | --- |
| Milestone | Sprint 1 Projektstart und Planung |
| Ziel | Projektstart, PM Grundlagen, Backlog, Doku Struktur |
| Ergebnis | Kanban Board, Labels, Milestones, erste Doku Seiten |
| Nachweise | GitHub Projects, Issues, erste Sprint Review und Retro |

### Sprint Backlog

| US | Titel | Priorität | Bereich | Status |
| --- | --- | --- | --- | --- |
| US01 | Kanban Board finalisieren | Must | PM | Erledigt |
| US02 | Labels anlegen | Must | PM, Repo | Erledigt |
| US03 | Milestones anlegen | Must | PM, Repo | Erledigt |
| US04 | Issue Template einrichten | Should | PM, Repo | Erledigt |
| US05 | Branching Strategie dokumentieren | Should | Docs, Repo | Erledigt |
| US06 | Sprint 1 Review und Retro dokumentieren | Must | Docs, PM | Erledigt |
| US07 | Architektur Zielbild skizzieren | Should | Docs, Kubernetes | Erledigt |


### Umsetzung im Sprint

| Bereich | Umsetzung | Nachweis |
| --- | --- | --- |
| Kanban Board | Spalten definiert und WIP Regel dokumentiert | Screenshot Board oder Link |
| Issues und User Stories | Backlog erstellt und priorisiert | Issue Liste |
| Labels | Prioritäten, Typen und Bereiche | Labels Übersicht |
| Milestones | Sprint Struktur mit Terminen | Milestones Übersicht |
| Dokumentation | MkDocs Struktur, erste Inhalte | GitHub Pages Startseite |

### Sprint Review

| Lieferobjekt | Status | Bemerkung |
| --- | --- | --- |
| Projektmanagement Dokument | Erledigt | Regeln, Rollen, Definitionen |
| Sprint 1 Review und Retro | Erledigt | Inhalte auf dieser Seite |
| Architektur Zielbild | Erledigt | Grobe Zielarchitektur dokumentiert |

### Sprint Retrospektive

| Was lief gut | Was war schwierig | Verbesserung für Sprint 2 |
| --- | --- | --- |
| Struktur über GitHub Issues und Board | Abgrenzung zwischen Story und Task | Template und Labels strikt nutzen |
| Frühe Dokumentation | Aufwand für saubere Nachweise | Nachweise direkt beim Ticket ablegen |
| Milestones geben Takt vor | Zeitplanung neben technischem Setup | Must Themen zuerst erledigen |

---

## Sprint 2 - Review und Retrospektive

### Sprint Steckbrief

| Punkt | Inhalt |
| --- | --- |
| Milestone | Sprint 2 K3s Cluster und erster Deploy |
| Ziel | K3s auf EC2, Kubernetes Ressourcen, erster End to End Deploy |
| Fokus | Betrieb auf AWS EC2, Traefik Ingress, Manifeste, Verifikation |
| Ergebnis | Erreichbarer Ingress Host, Deployment über GitHub Actions vorbereitet |

### Sprint Backlog

| US | Titel | Priorität | Bereich | Status |
| --- | --- | --- | --- | --- |
| US08 | EC2 Instanz vorbereiten | Must | AWS, K3s | Erledigt |
| US09 | K3s auf EC2 installieren | Must | K3s, Kubernetes | Erledigt |
| US10 | Namespace und Basis Ressourcen erstellen | Should | Kubernetes | Erledigt |
| US11 | Dockerfile finalisieren | Must | Docker | Technik erledigt, Doku offen |
| US12 | GHCR Push verifizieren | Must | Docker, Repo | Technik erledigt, Doku offen |
| US13 | Kubernetes Deployment manifest erstellen | Must | Kubernetes | Technik erledigt, Doku offen |
| US14 | Kubernetes Service manifest erstellen | Must | Kubernetes | Technik erledigt, Doku offen |
| US15 | Ingress konfigurieren | Should | Kubernetes, K3s | Technik erledigt, Doku offen |
| US16 | Readiness und Liveness Probes definieren | Should | Kubernetes, Testing | Technik erledigt, Doku offen |
| US17 | Sprint 2 Review und Retro dokumentieren | Must | Docs, PM | Offen |


### Umsetzung im Sprint

| Thema | Umsetzung | Ergebnis |
| --- | --- | --- |
| AWS Setup | EC2 Instanz bereitgestellt, Security Group angepasst | SSH Zugriff und Basis Setup |
| K3s Installation | K3s installiert und kubectl konfiguriert | Cluster läuft |
| Kubernetes Ressourcen | Namespace, Deployment, Service, Ingress | Service über Ingress erreichbar |
| Container Build | Docker Image gebaut und getestet | Image lauffähig |
| GHCR Push | Image Build und Push via GitHub Actions | Image in GHCR verfügbar |
| Deployment Workflow | Manifeste auf EC2 angewendet, Image gesetzt | Rollout nachvollziehbar |
| Smoke Tests | Endpoint Tests, Logs kontrolliert | Basis Verifikation durchgeführt |

### Sprint Review

#### Sprintziel erreicht

| Ziel | Status | Hinweis |
| --- | --- | --- |
| K3s Cluster auf EC2 | Erreicht | Basis Betrieb steht |
| Service per Ingress erreichbar | Erreicht | nip io Host verwendet |
| Build und Push nach GHCR | Erreicht | Tags `latest` und Commit SHA geplant |
| Deployment automatisierbar | Teilweise | Trigger und Hardening in Sprint 3 |

#### Lieferobjekte

| Lieferobjekt | Ort |
| --- | --- |
| Kubernetes Manifeste | `k8s/` |
| Workflows | `.github/workflows/` |
| Dokumentation | `docs/` |

#### Offene Punkte

| Thema | Beschreibung | Geplant |
| --- | --- | --- |
| Trigger Logik | Build nur bei Service Änderungen auslösen | Sprint 3 |
| Secrets Handling | GHCR und Cluster Zugriff sauber dokumentieren | Sprint 3 |
| Probes und Limits | Readiness Liveness und Ressourcen definieren | Sprint 3 |
| Nachweise | Mehr Screenshots und Logs im docs Bereich | Abgabe |

### Sprint Retrospektive

| Was lief gut | Was war schwierig | Verbesserung für Sprint 3 |
| --- | --- | --- |
| K3s Setup und Ingress funktioniert | YAML und Workflow Details sind fehleranfällig | Schrittweise Tests, linting, klare Versionierung |
| GHCR Integration | Lowercase Tag Anforderungen | Repo Name konsequent lowercase |
| End to End Test möglich | Unterschied lokal vs Cluster | Standardisierte Smoke Tests in Pipeline |

### Ausblick Sprint 3

| Fokus | Beschreibung |
| --- | --- |
| CI CD sauber trennen | Build Workflow und Deploy Workflow klar definieren |
| Trigger präzise definieren | Paths Filter, PR Flow develop nach main |
| Stabilisierung | Probes, Limits, Rollback Strategie, Sicherheit |
| Dokumentation | Nachweise finalisieren, Demo Ablauf vorbereiten |

