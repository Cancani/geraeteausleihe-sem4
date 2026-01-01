<p align="center"><strong>Geräteausleihe Microservice Sem4</strong></p>
<p align="center">Cloud Native Deployment auf AWS mit Kubernetes, K3s auf EC2 und GitHub Actions</p>

[![Python](https://img.shields.io/badge/Python-3.11-3776ab?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![Docker](https://img.shields.io/badge/Docker-2496ed?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-326ce5?style=for-the-badge&logo=kubernetes&logoColor=white)](https://kubernetes.io)
[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088ff?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/features/actions)
[![AWS](https://img.shields.io/badge/AWS-Cloud-ff9900?style=for-the-badge&logo=amazonaws&logoColor=white)](https://aws.amazon.com)

---

## Kurzlinks

| Bereich | Link |
| --- | --- |
| Repository | https://github.com/Cancani/geraeteausleihe-sem4 |
| GitHub Projects Board | https://github.com/users/Cancani/projects/3/views/1 |
| GitHub Pages | https://cancani.com/geraeteausleihe-sem4 |
| Einreichungsformular | `./docs/Efekan_Einreichungsformular_4.SemesterV2.docx` |

---

## Projektdefinition

In dieser Semesterarbeit wird der bestehende Microservice aus dem 3. Semester weitergeführt und technologisch erweitert. Ziel ist ein weitgehend automatisierter Cloud Native Betrieb auf AWS mit Kubernetes. Der Betrieb läuft auf einem K3s Cluster auf einer EC2 Instanz, Deployments erfolgen über GitHub Actions.

Das Resultat ist ein skalierbarer, wartbarer und reproduzierbar bereitgestellter Microservice als praxisnahes Beispiel für moderne DevOps Betriebsprozesse.

---

## Projektübersicht

| Eigenschaft | Details |
| --- | --- |
| Titel | Geräteausleihe Microservice, Cloud Native Deployment auf AWS |
| Studierender | Efekan Demirci |
| Dozenten | PRJ Corrado Parisi, CNC Philip Stark |
| Semester | 4. Semester HF TBZ, ITCNE24 |
| Zeitraum | Oktober 2025 bis Januar 2026 |
| Technologie Stack | Python Flask, Docker, Kubernetes, K3s, AWS, GitHub Actions |
| Architektur | Microservice, CI CD, Infrastructure as Code Grundprinzipien |
| Repository | https://github.com/Cancani/geraeteausleihe-sem4 |

---

## Ausgangslage und Problemstellung

### IST Zustand

Der Microservice aus dem 3. Semester wird initial manuell auf einer AWS EC2 Instanz betrieben. Deployments erfolgen per Hand über Docker Befehle ohne konsistente Versionierung und ohne reproduzierbare Abläufe.

| Schritt | Manuell |
| --- | --- |
| 1 | Codeänderung lokal |
| 2 | Docker Image lokal bauen |
| 3 | Image hochladen |
| 4 | Alten Container stoppen |
| 5 | Neuen Container starten |

| Problem | Auswirkung | Häufigkeit |
| --- | --- | --- |
| Kein automatisiertes Deployment | Hoher manueller Aufwand | Nach jedem Update |
| Fehlende Skalierbarkeit | Keine automatische Anpassung an Last | Regelmässig |
| Kein Monitoring | Fehler bleiben unbemerkt | Zufallsabhängig |
| Kein Versionsmanagement | Unklar welche Version läuft | Oft |
| Keine Health Checks | Fehler werden nicht automatisch erkannt | Sporadisch |

### SOLL Zustand

Der Microservice wird in Kubernetes betrieben und automatisiert ausgerollt. Codeänderungen lösen Build, Push in eine Registry und Deployment ins Cluster aus.

| Schritt | Automatisiert |
| --- | --- |
| 1 | Push auf `main` |
| 2 | GitHub Actions startet |
| 3 | Docker Image wird gebaut und nach GHCR gepusht |
| 4 | Deployment im K3s Cluster wird aktualisiert |
| 5 | Kubernetes rollt per Rolling Update aus |

| Verbesserung | Nutzen | Automatisierung |
| --- | --- | --- |
| CI CD Pipeline | Kein manuelles Deployment | Vollständig |
| Kubernetes Betrieb | Self Healing und Skalierung | Vollständig |
| GHCR Images | Versionierte Builds | Vollständig |
| Probes | Stabilität durch Auto Restart | Teilweise |
| AWS Hosting | Reproduzierbare Infrastruktur | Vollständig |

---

## Zielsetzung

Ziel ist die Umsetzung einer automatisierten Deployment Pipeline für den Microservice. Das Projekt verbindet Inhalte aus CNC und DevOps mit einem bestehenden Service aus dem 3. Semester.

Schwerpunkte
- Containerisierung und Image Build
- Kubernetes Betrieb mit K3s auf EC2
- Automatisierung per GitHub Actions
- Versionierung und Deployment Nachweis
- Dokumentation über GitHub Pages

---

## SMART Ziele

| Ziel | Spezifisch | Messbar | Attraktiv | Realistisch | Terminiert |
| --- | --- | --- | --- | --- | --- |
| Containerisierung | Dockerfile und Build Workflow | Image läuft lokal und im Cluster | Wiederverwendbar | Machbar | Sprint 1 bis 2 |
| K3s Deployment | Kubernetes Manifeste | Pods laufen im Cluster | Skalierbar | Machbar | Sprint 2 |
| CI CD | Actions Build Push Deploy | Deploy bei Push auf main | Praxisnah | Machbar | Sprint 3 |
| Health Checks | Probes und Endpoints | Pods werden überwacht | Stabilität | Optional | Sprint 2 bis 3 |
| Dokumentation und Demo | Pages und Nachweise | Vollständig | Bewertungsrelevant | Machbar | Abschluss |

---

## Technologien und Werkzeuge

| Bereich | Technologie | Begründung |
| --- | --- | --- |
| Backend | Python Flask | Schlankes Framework für REST APIs |
| Container | Docker | Portables Build und Laufzeitformat |
| Orchestrierung | Kubernetes, K3s | Betrieb und Rollouts im Cluster |
| CI CD | GitHub Actions | Automatisiertes Build, Push, Deploy |
| Registry | GitHub Container Registry | Versionierte Container Images |
| Cloud | AWS EC2 | Kostenarme und praxisnahe Infrastruktur |
| Projektmanagement | GitHub Projects und Issues | Sprints, Tracking, Nachweise |
| Dokumentation | MkDocs Material und GitHub Pages | Versionierte Doku, öffentlich lesbar |

---

## Ablauf und Termine

| Datum (ca.) | Inhalt |
| --- | --- |
| 01.10.2025 | Ablauf Semesterarbeiten und Themenübersicht |
| 20.10.2025 | Abgabe Einreichungsformular |
| 27.10.2025 | Freigabe Semesterarbeit und Start Umsetzung |
| 17.11.2025 | Einzelbesprechung 1 mit Feedback |
| 15.12.2025 | Einzelbesprechung 2 mit Feedback |
| 23.01.2026 | Einzelbesprechung 3 mit Feedback |
| 28.01.2026 | Abgabe, Abnahme, Schlusspräsentation |

---

## Weiterführende Seiten

| Seite | Inhalt |
| --- | --- |
| [Projektmanagement](projektmanagement.md) | Vorgehen, Rollen, Regeln, Backlog Struktur, Nachweise |
| [Sprints](sprints.md) | Sprint Reviews und Retrospektiven, Status und Ausblick |
| [Architektur](architektur.md) | Zielbild, Komponenten, Schnittstellen, Kubernetes Ressourcen |
| [Technische Umsetzung](technische_umsetzung.md) | Setup, Manifeste, CI CD, Deploy Ablauf, Verifikation |

