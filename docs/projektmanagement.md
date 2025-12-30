# Projektmanagement

## Zweck und Umfang
Dieses Dokument beschreibt die organisatorische Umsetzung der Semesterarbeit. Das Projekt wird sprintbasiert umgesetzt. Planung, Tracking und Nachweise erfolgen im GitHub Repository über Issues, Milestones und ein Kanban Board.

 
Der Geräteausleihe Microservice wird auf AWS in einem K3s Cluster auf EC2 betrieben und per CI CD Pipeline automatisiert gebaut, veröffentlicht und ins Cluster ausgerollt.

## Vorgehensmodell
Das Projekt folgt einer sprintbasierten Arbeitsweise mit diesen Elementen:
1. Product Backlog als GitHub Issues
2. Sprint Planung über Milestones
3. Umsetzung mit Kanban Board Status
4. Sprint Review und Sprint Retro als Dokumentationseinträge pro Sprint

## Rollen und Verantwortlichkeiten
| Rolle | Person | Verantwortung |
| --- | --- | --- |
| Projektleitung und Umsetzung | Efekan Demirci | Planung, Umsetzung, Dokumentation, Sprint Reviews |
| Dozent PRJ | Corrado Parisi | Feedback zu Projektmanagement, Board, Reviews |
| Dozent CNC | Philip Stark | Feedback zu Cloud Native Umsetzung und Architektur |

## Tools und Artefakte
| Bereich | Tool | Artefakt |
| --- | --- | --- |
| Repository und Tracking | GitHub | Code, Issues, Milestones, Project Board |
| Dokumentation | Markdown und GitHub Pages | Dokumentationsseiten unter docs |
| CI/CD | GitHub Actions | Workflows für Build, Push, Deploy |
| Container Registry | GHCR | Versionierte Images |
| Runtime | AWS EC2 mit K3s | Kubernetes Cluster für Deployment |

## Kanban Board Setup
### Spalten
1. Backlog  
2. Ready  
3. In Progress  
4. Review  
5. Done  

### Arbeitsregeln
1. WIP Limit in In Progress maximal 2 Issues gleichzeitig  
2. Ein Issue darf erst nach Ready, wenn Akzeptanzkriterien und Definition of Done im Issue stehen  
3. Review bedeutet technische Kontrolle, Dokumentation aktualisiert, Nachweise vorhanden  
4. Done bedeutet Definition of Done vollständig abgehakt und Milestone bleibt gesetzt  

## Schätzung
Für die Grobplanung werden Story Points verwendet:
**1 2 3 5 8**

Orientierung:
1 bis 30 Minuten  
2 bis 1 Stunde  
3 bis 2 Stunden  
5 bis 4 Stunden  
8 bis 1 Arbeitstag  

## Labels
Die Labels sind so aufgebaut, dass Priorität, Bereich und Typ klar getrennt sind.

### Priorität
Must  
Should  
Could  

### Bereich
PM  
Docs  
Repo  
Pages  
AWS  
K3s  
Docker  
Kubernetes  
CI  
Security  
Testing  

### Typ
Story  
Task  
Bug  

## Milestones
Pro Sprint existiert ein Milestone. Zusätzlich gibt es einen Milestone für den Abschluss.

Milestones im Repository:
1. Sprint 1 Projektstart und Planung  
2. Sprint 2 K3s Cluster und erster Deploy  
3. Sprint 3 CI CD Build Push Deploy  
4. Abgabe und Doku fertig  

Die konkreten Due Dates sind im GitHub Milestone gesetzt.

## Issue Struktur
Alle Issues werden als User Stories geführt. Jede Story enthält Akzeptanzkriterien als Checkboxen und eine Definition of Done als Checkboxen.

### Standard Inhalt pro Issue
1. User Story Satz mit Als möchte ich damit  
2. Kurzbeschreibung
3. Akzeptanzkriterien Checkboxen
4. Definition of Done Checkboxen

### Definition of Done
Diese DoD wird in jedes Issue übernommen:
1. Code oder Dokumentation ist committed und gepusht  
2. Akzeptanzkriterien sind abgehakt  
3. Nachweis ist in docs abgelegt, Screenshot oder Logauszug  
4. Issue ist im Board korrekt verschoben  

### Definition of Ready
Ein Issue gilt als Ready, wenn:
1. Beschreibung ist eindeutig  
2. Akzeptanzkriterien sind vorhanden  
3. DoD ist vorhanden  
4. Milestone ist gesetzt  
5. Priorität ist gesetzt  

## Sprint Planung
### Sprint 1 Projektstart und Planung
**Ziel** 
Projektsetup, Board Struktur, Labels, Milestones, erste Dokumentationsstruktur und initialer Backlog.

**Lieferobjekte:**
1. Board und Regeln
2. Labels und Milestones
3. Erste User Stories
4. Erste Sprint Review und Retro Dokumentation

### Sprint 2 K3s Cluster und erster Deploy
**Ziel**  
EC2 bereitstellen, K3s installieren, Container vorbereiten, Kubernetes Manifeste erstellen, erster funktionierender Deploy.

**Lieferobjekte:**
1. EC2 Instanz und Zugriff
2. K3s Cluster und kubectl Zugriff
3. Dockerfile und Image in GHCR
4. Kubernetes Deployment, Service und optional Ingress
5. Probes und Nachweise

### Sprint 3 CI CD Build Push Deploy
**Ziel**  
Automatisierung von Build, Push nach GHCR und Deployment nach K3s.

**Lieferobjekte:**
1. GitHub Actions Workflow für Build und Push
2. Secrets und Zugriff auf Cluster
3. CD Schritt mit kubectl apply oder rollout
4. Dokumentierter Pipeline Testlauf

### Abschluss Abgabe und Doku fertig
**Ziel**  
Dokumentation finalisieren, Demo Ablauf definieren, Endkontrolle und Abgabe Paket erstellen.

**Lieferobjekte:**
1. Vollständige Doku auf GitHub Pages
2. Demo Ablauf und Nachweise
3. Endkontrolle Checkliste
4. Abgabe Links und Repository Stand auf main

## Backlog Umsetzung in GitHub
### Automatisierte Erstellung über GitHub CLI
Um Labels, Milestones und Issues effizient zu erzeugen, wurde GitHub CLI verwendet.

Beispiele zur Prüfung:
```powershell
gh auth status
gh label list -R Cancani/geraeteausleihe-sem4 --limit 50
gh issue list -R Cancani/geraeteausleihe-sem4 --limit 50
gh api "repos/Cancani/geraeteausleihe-sem4/milestones?state=open&per_page=100" --jq '.[] | "\(.number) \(.title)"'
```

### Ergebnis
Im Repository wurden 27 Issues als User Stories angelegt und den Sprint Milestones zugeordnet:
US01 bis US07 **Sprint 1**  
US08 bis US17 **Sprint 2**  
US18 bis US23 **Sprint 3**  
US24 bis US27 **Abschluss**  

## Kommunikations und Dokumentationskonzept
1. Dokumentation wird versioniert im Repository gepflegt
2. Sprint Review und Retro werden je Sprint als Markdown Eintrag dokumentiert
3. Technische Nachweise werden als Screenshots oder Logauszüge unter docs abgelegt
4. Links zu Board, Milestones, Actions Runs und GHCR werden in der Doku gesammelt

## Qualitäts und Risikomanagement
### Qualitätssicherung
1. Akzeptanzkriterien pro Issue
2. DoD pro Issue
3. Review Spalte im Board für Kontrolle
4. Nachweise für wichtige Schritte wie Deployment und Rollouts

### Risiken und Massnahmen
| Risiko | Auswirkung | Massnahme |
| --- | --- | --- |
| Cluster Zugriff aus CI schlägt fehl | CD blockiert | Kubeconfig als Secret prüfen, Zugriff lokal verifizieren |
| Deployment schlägt fehl durch fehlende Ressourcen | Service nicht erreichbar | Minimal Setup, schrittweise Manifeste, Rollout Status prüfen |
| Zeitdruck | Scope zu gross | Must Issues priorisieren, Should nur wenn Zeit |
| Kosten AWS | Budgetüberschreitung | K3s auf EC2, kleine Instanz, Ressourcen begrenzen |

## Branching und Merge Regeln
### Branches
```
main  
develop  
feature branches  
gh pages branch für die Dokumentation
```

### Grundregeln
1. Entwicklung erfolgt auf develop oder feature branches
2. Merge nach main per Pull Request
3. main bleibt stabil und entspricht dem Stand für Abgabe und Demo
4. gh pages wird nur durch Workflow aktualisiert

## Nachweise für Dozenten
Empfohlene Nachweise, die in der Dokumentation verlinkt werden:
1. Screenshot Project Board Spalten und WIP Regel
2. Screenshot Milestones Übersicht
3. Screenshot Actions Run für Build und Deploy
4. kubectl Ausgaben für Pods, Services, Ingress
5. GHCR Image Tags Übersicht

## Branching Strategie und Regeln

### Ziel
Ein stabiler main Branch fuer Demo und Abgabe. Entwicklung findet auf develop oder feature branches statt. Dokumentation wird ueber GitHub Pages aus dem main Branch gebaut.

### Branches
main  
Stabiler Stand fuer Demo und Abgabe. Merge nur via Pull Request.

develop  
Integrationsbranch fuer laufende Arbeit. Feature branches werden hier gemerged.

feature branches  
Kurzlebige branches fuer einzelne Issues, zB feature/us08-k3s-ec2.

gh-pages  
Wird nur durch den GitHub Pages Workflow beschrieben. Kein manuelles Arbeiten in diesem Branch.

### Merge Flow
1 Neue Arbeit startet auf feature branch aus develop  
2 Pull Request von feature nach develop  
3 Wenn ein Sprint Stand stabil ist, Pull Request von develop nach main  
4 GitHub Pages baut die Doku nur bei Aenderungen an docs oder mkdocs yml auf main

### Branch Schutz und Regeln
1 Force Push ist blockiert auf main und gh-pages  
2 Direkt Push auf main ist eingeschraenkt, Merge via Pull Request  
3 Status Checks muessen bestehen, wenn Workflows vorhanden sind  
4 gh-pages darf nur vom GitHub Actions Workflow aktualisiert werden

### Commit Konvention
Konvention: type scope: message

Beispiele:
docs(pm): update sprint documentation  
docs(arch): add target architecture overview  
ci(pages): enable manual docs deployment  
ci(cd): deploy to k3s on push to main  
feat(k8s): add deployment and service manifests  
fix(ci): correct ghcr image tag

### Definition of Done fuer Branching Doku
1 Dokumentation ist committed und gepusht  
2 Regeln sind im README oder docs referenziert  
3 Issue US05 ist im Board auf Done
