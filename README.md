<p align="center"><strong>Geraeteausleihe Microservice Sem4</strong></p>
<p align="center">Cloud Native Deployment auf AWS mit Kubernetes, K3s auf EC2 und GitHub Actions</p>

[![Python](https://img.shields.io/badge/Python-3.11-3776ab?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![Docker](https://img.shields.io/badge/Docker-2496ed?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-326ce5?style=for-the-badge&logo=kubernetes&logoColor=white)](https://kubernetes.io)
[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088ff?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/features/actions)
[![AWS](https://img.shields.io/badge/AWS-Cloud-ff9900?style=for-the-badge&logo=amazonaws&logoColor=white)](https://aws.amazon.com)

---

## Dokumentation
Die laufende Projektdokumentation ist auf GitHub Pages verfuegbar:  
**GitHub Pages**: https://cancani.github.io/geraeteausleihe-sem4/

---

## Projektdefinition
In dieser Semesterarbeit wird der bestehende Microservice aus dem 3. Semester weitergefuehrt und technologisch erweitert. Ziel ist ein vollautomatisierter Cloud Native Betrieb auf AWS mit Kubernetes, K3s auf EC2 und GitHub Actions.

Das Resultat ist ein skalierbarer, wartbarer und automatisiert bereitgestellter Microservice als praxisnahes Beispiel fuer moderne DevOps Betriebsprozesse.

### Einreichungsformular
Das Einreichungsformular ist im Repository unter `docs` abgelegt:  
`./docs/Efekan_Einreichungsformular_4.SemesterV2.docx`

---

## Projektuebersicht

| Eigenschaft | Details |
| --- | --- |
| **Titel** | Geraeteausleihe Microservice, Cloud Native Deployment auf AWS |
| **Studierender** | Efekan Demirci |
| **Dozenten** | PRJ Corrado Parisi, CNC Philip Stark |
| **Semester** | 4 Semester HF TBZ, ITCNE24 |
| **Zeitraum** | Oktober 2025 bis Januar 2026 |
| **Technologie Stack** | Python Flask, Docker, Kubernetes, K3s, AWS, GitHub Actions |
| **Architektur** | Microservice, CI CD, Infrastructure as Code Grundprinzipien |
| **Repository** | https://github.com/Cancani/geraeteausleihe-sem4 |

---

## Ausgangslage und Problemstellung

### IST Zustand
Der Microservice aus dem 3. Semester wird aktuell manuell auf einer AWS EC2 Instanz betrieben. Deployments erfolgen per Hand ueber Docker Befehle ohne Pipeline und ohne konsistente Versionierung.

Aktueller Ablauf
1 Codeaenderung lokal
2 Docker Image lokal bauen
3 Image hochladen
4 Alten Container stoppen
5 Neuen Container starten

Identifizierte Probleme

| Problem | Auswirkung | Haeufigkeit |
| --- | --- | --- |
| Kein automatisiertes Deployment | Hoher manueller Aufwand | Nach jedem Update |
| Fehlende Skalierbarkeit | Keine automatische Anpassung an Last | Regelmaessig |
| Kein Monitoring | Fehler bleiben unbemerkt | Zufallsabhaengig |
| Kein Versionsmanagement | Unklar welche Version laeuft | Oft |
| Keine Health Checks | Fehler werden nicht automatisch erkannt | Sporadisch |

### SOLL Zustand
Der Microservice wird in Kubernetes betrieben und automatisiert ausgerollt. Codeaenderungen loesen Build, Push in eine Registry und Deployment ins Cluster aus.

Geplanter Ablauf
1 Push auf main
2 GitHub Actions startet automatisch
3 Docker Image wird gebaut und nach GHCR gepusht
4 Deployment im K3s Cluster wird aktualisiert
5 Kubernetes rollt per Rolling Update aus und stellt die neue Version bereit

Verbesserungen gegenueber IST Zustand

| Verbesserung | Nutzen | Automatisierung |
| --- | --- | --- |
| CI CD Pipeline | Kein manuelles Deployment | Vollstaendig |
| Kubernetes Betrieb | Self Healing und Skalierung | Vollstaendig |
| GHCR Images | Versionierte Builds | Vollstaendig |
| Probes | Stabilitaet durch Auto Restart | Teilweise |
| AWS Hosting | Reproduzierbare Infrastruktur | Vollstaendig |

---

## Zielsetzung
Ziel ist die Umsetzung einer automatisierten Deployment Pipeline fuer den Microservice. Das Projekt verbindet Inhalte aus CNC und DevOps mit einem bestehenden Service aus dem 3. Semester.

Schwerpunkte
- Containerisierung und Image Build
- Kubernetes Betrieb mit K3s auf EC2
- Automatisierung per GitHub Actions
- Versionierung und Deployment Nachweis
- Dokumentation ueber GitHub Pages

---

## SMART Ziele

| Ziel | Spezifisch | Messbar | Attraktiv | Realistisch | Terminiert |
| --- | --- | --- | --- | --- | --- |
| **Containerisierung** | Dockerfile und Build Workflow | Image laeuft lokal und im Cluster | Wiederverwendbar | Machbar | Sprint 1 bis 2 |
| **K3s Deployment** | Kubernetes Manifeste | Pods laufen im Cluster | Skalierbar | Machbar | Sprint 2 |
| **CI CD** | Actions Build Push Deploy | Deploy bei Push auf main | Praxisnah | Machbar | Sprint 3 |
| **Health Checks** | Probes und Endpoints | Pods werden ueberwacht | Stabilitaet | Optional | Sprint 2 bis 3 |
| **Dokumentation und Demo** | Pages und Nachweise | Vollstaendig | Bewertungsrelevant | Machbar | Abschluss |

---

## Technologien und Werkzeuge

| Bereich | Technologie | Begruendung |
| --- | --- | --- |
| Backend | Python Flask | Schlankes Framework fuer REST APIs |
| Container | Docker | Portables Build und Laufzeitformat |
| Orchestrierung | Kubernetes, K3s | Betrieb und Rollouts im Cluster |
| CI CD | GitHub Actions | Automatisiertes Build, Push, Deploy |
| Registry | GitHub Container Registry | Versionierte Container Images |
| Cloud | AWS EC2 | Kostenarme und praxisnahe Infrastruktur |
| Projektmanagement | GitHub Projects und Issues | Sprints, Tracking, Nachweise |
| Dokumentation | MkDocs Material und GitHub Pages | Versionierte Doku, oeffentlich lesbar |
