# Projektdefinition

## Einreichungsformular

Das Einreichungsformular kann hier entnommen werden:  
[ITCNE24 Semesterarbeit 4 Einreichungsformular](./Efekan_Einreichungsformular_4.SemesterV2.docx)

---

## Projektübersicht

| Eigenschaft | Details |
|---|---|
| **Titel** | Geräteausleihe Microservice, Cloud Native Deployment auf AWS |
| **Studierender** | Efekan Demirci |
| **Dozenten** | PRJ Corrado Parisi, CNC Philip Stark |
| **Semester** | 4 Semester HF TBZ, ITCNE24 |
| **Zeitraum** | Oktober 2025 bis Januar 2026 |
| **Technologie Stack** | Python Flask, Docker, K3s auf AWS EC2, GitHub Actions, GHCR, MkDocs |
| **Architektur** | Microservice, Container, Kubernetes Deployment, Ingress Routing |
| **Repository** | https://github.com/Cancani/geraeteausleihe-sem4 |
| **GitHub Pages** | https://cancani.com/geraeteausleihe-sem4/ |
| **Project Board** | https://github.com/users/Cancani/projects/3/views/1 |

Die bestehende Geräteausleihe Lösung aus der vorherigen Semesterarbeit dient als Ausgangsbasis. In dieser Arbeit steht nicht die fachliche Erweiterung im Vordergrund, sondern die Cloud Native Transformation: Containerisierung, automatisierte CI/CD Pipelines sowie der Betrieb in einem Kubernetes Cluster auf AWS.

**Key Features**

* Container Build und Push nach GHCR
* Automatisiertes Deployment nach K3s auf AWS EC2 via GitHub Actions
* Ingress Routing über Traefik und Hostname ueber nip.io
* Extern erreichbare Endpoints healthz und pdf
* Laufende Dokumentation über MkDocs und GitHub Pages

---

## Ausgangslage und Problemstellung

### Ist Zustand

Der Service war zwar technisch lauffähig, der Betrieb und das Deployment waren jedoch zu wenig standardisiert und zu wenig automatisiert. 

Typische Nachteile im Ist Zustand:
* Deployment Updates waren fehleranfällig und schwer nachvollziehbar
* Kein konsistentes Release und Tagging Konzept
* Keine Kubernetes Eigenschaften wie Self Healing und deklarative Deployments
* Nachweise für Stakeholder fehlten oder wurden erst spät nachgetragen

**Ist Workflow**


```mermaid
flowchart LR
  A[Lokale Änderung am Code] --> B[Manueller Build oder uneinheitlicher Build]
  B --> C[Manuelles Deployment]
  C --> D[Service läuft, Status schwer nachvollziehbar]
```


---

### Soll Zustand

Ziel ist ein durchgängig automatisierter Workflow vom Commit bis zum laufenden Pod im Cluster. Jede relevante Änderung soll ein Image bauen, in die Registry pushen und anschliessend automatisiert im K3s Cluster deployed werden.

**Soll Workflow**


```mermaid
flowchart LR
  subgraph GitHub
    A[Repository] --> B[GitHub Actions]
    B --> C[GHCR Image]
    B --> D[GitHub Pages Doku]
  end

  subgraph AWS
    E[AWS EC2] --> F[K3s Cluster]
    F --> G[Traefik Ingress]
    G --> H[Microservice Pod]
  end

  C --> H
  B --> E
```

___ 

**Soll Verbesserungen**

| Verbesserung | Nutzen | Umsetzung |
|---|---|---|
| Automatisierter Build und Push | Reproduzierbar, nachvollziehbar | GitHub Actions, GHCR |
| Automatisierter Deploy | Schneller und konsistent | GitHub Actions, kubectl apply |
| Deklarative Kubernetes Manifeste | Standardisiertes Deployment | Namespace, Deployment, Service, Ingress |

---

## Zielsetzung

Die Arbeit hat das Ziel, den bestehenden Microservice in eine Cloud Native Betriebsumgebung zu überfuehren. Der Fokus liegt auf CI und CD, Kubernetes Deployment, stabiler Erreichbarkeit über Ingress sowie einer laufenden Dokumentation, die den Fortschritt und die Qualität belegt.

---

### SMART Ziele

| Ziel | Spezifisch | Messbar | Attraktiv | Realistisch | Terminiert |
|---|---|---|---|---|---|
| CI Build und Push | Container Image wird gebaut und nach GHCR gepusht | Erfolgreiche Actions Runs und sichtbare Tags | DevOps Nutzen | Mit GitHub Actions umsetzbar | Sprint 2 und 3 |
| CD Deploy nach K3s | Manifeste werden applied und Image wird aktualisiert | Pods laufen, Service extern erreichbar | Automatisierung | Mit K3s auf EC2 umsetzbar | Sprint 2 und 3 |
| Ingress und Endpoints | Health und PDF funktionieren extern | HTTP 200, PDF Response | Demo fähig | Traefik und nip.io vorhanden | Sprint 2 |

---

## Technologien und Werkzeuge

| Bereich | Technologie | Begründung |
|---|---|---|
| Backend | Python Flask | Schlankes Framework für Microservices |
| Containerisierung | Docker | Portabilität und reproduzierbarer Betrieb |
| Orchestrierung | K3s | Kubernetes Betrieb auf einer EC2 Instanz |
| Cloud Hosting | AWS EC2 | Realistische Zielumgebung für DevOps Deployment |
| Registry | GHCR | In GitHub integriert, einfache Distribution |
| CI und CD | GitHub Actions | Automatisierung von Build, Push und Deploy |
| Ingress | Traefik | Routing im Cluster und externe Erreichbarkeit |
| Dokumentation | MkDocs, GitHub Pages | Versionierte und laufend publizierte Doku |
| Projektmanagement | GitHub Projects, Issues | Backlog, Schätzungen, Priorisierung, DoD |

---

# Projektmanagement

## Projektmethodik

Das Projekt folgt einem agilen, scrumähnlichen Vorgehen mit iterativer Entwicklung und regelmässigen Review Zyklen. Die Planung und Nachverfolgung erfolgt vollständig in GitHub.

**Gewählte Methodik: Sprint basierte Entwicklung**

Die Entscheidung für ein iteratives Vorgehen basiert auf folgenden Punkten:

* Neue technische Themen wie Kubernetes, K3s und CI CD benötigen experimentelles Vorgehen mit kurzen Feedback Schleifen
* Technische Abhängigkeiten werden oft erst während der Umsetzung sichtbar, zum Beispiel Ingress, Host Routing und Secrets Handling
* Dozenten Feedback kann direkt in die nächsten Tasks und in die Dokumentation einfliessen
* Risiken werden früh sichtbar, statt erst am Schluss

**Kernprinzipien der angewandten Methodik**

* Iterative Entwicklung mit funktionsfähigen Zwischenständen
* Kontinuierliches Feedback und Anpassung der Prioritäten
* Laufende Nachweisführung, damit der Projektstand jederzeit nachvollziehbar ist
* Klare Definition of Done pro Ticket inklusive Evidence Anforderungen

### Sprintstruktur im Detail

**Sprint Planning (Sprintbeginn):**
* Definition von User Stories mit klaren Akzeptanzkriterien
* Aufwandsschätzung in Story Points
* Festlegung des Sprintziels als ein Satz Outcome und der Deliverables
* Sprint Scope im GitHub Project Board zuweisen, Sprint Feld und Milestone setzen

**Sprint Execution (Durchführung):**
* Kontinuierliche Arbeit an den definierten User Stories
* GitHub Issues für Aufgaben Tracking und Statusupdates
* Regelmässige Commits und Pushes, kleine Änderungen statt grosse Sprünge
* Ticket Status aktuell halten, WIP Limit in Progress maximal 2

**Sprint Review (Sprintende):**
* Abgleich gegen Sprintziel
* Review Gespräche mit Dozenten zur Qualitätssicherung
* Bewertung der Zielerreichung und Identifikation von Verbesserungspotenzialen
* Evidence Pflicht, Screenshots und Links werden direkt pro Sprint Review dokumentiert

**Sprint Retrospektive:**
* Reflexion des Arbeitsprozesses mit dem Starfish Modell
* Identifikation von Start Doing, Stop Doing, Keep Doing, More Of, Less Of

**Vorteile der gewählten Methodik:**
* Flexibilität, schnelle Anpassung an neue Erkenntnisse, zum Beispiel Ingress Routing oder CI CD Details
* Qualitätssicherung, regelmässige Reviews verhindern späte Richtungsänderungen
* Motivation, sichtbare Fortschritte nach jedem Sprint
* Lernoptimierung, Retrospektiven führen zu kontinuierlicher Prozessverbesserung

## Projektphasen und Meilensteine

Das Projekt ist in drei Sprints gegliedert. Die Sprintzeiträume entsprechen der ursprünglichen Planung. Inhalte aus Sprint 1 und Sprint 2 wurden in einem späteren Zeitraum konzentriert nachgezogen. Die Dokumentation wird nun strukturiert und evidenzbasiert ergänzt, damit der Stand jederzeit nachvollziehbar ist.

### Sprint Progression im Überblick

**Sprint 1 Projektbasis:**  
Aufbau der Projektbasis mit Board Struktur, Labels, Milestones, Issue Standards und erstem Architektur Zielbild.

**Sprint 2 Cluster und Deploy:**  
Aufbau der Laufzeitumgebung auf AWS EC2 mit K3s, Kubernetes Ressourcen und Ingress über Traefik. Erste externe Tests der Endpoints.

**Sprint 3 CI CD und Nachweise:**  
Stabilisierung von Build und Deploy Workflows mit GitHub Actions, saubere Versionierung,
 Rollback Vorgehen.
 
 Laufende Nachweise pro Sprint durchgehend.

![Sprintuebersicht](./screenshots/Sprintuebersicht.png)

### Zeitplan

| Sprint       | Zeitraum                  | Fokus                                                                                      | Status        |
| ------------ | ------------------------- | ------------------------------------------------------------------------------------------ | ------------- |
| **Sprint 1** | 27.10.2025 bis 17.11.2025 | Projektbasis, Board Setup, Standards, Architektur Zielbild                                 | Abgeschlossen |
| **Sprint 2** | 18.11.2025 bis 15.12.2025 | AWS EC2 und K3s Setup, Kubernetes Manifeste, Ingress, erste externe Tests                  | Abgeschlossen |
| **Sprint 3** | 16.12.2025 bis 21.01.2026 | CI CD stabilisieren, Evidence pro Sprint, Dokumentation Finalisierung, Abgabe Vorbereitung | In Arbeit     |

---

## Anpassung der Sprint Planung

In der praktischen Umsetzung wurden zentrale Inhalte aus Sprint 1 und Sprint 2 in einem späteren Zeitraum konzentriert nachgezogen. Gründe dafür waren parallele Verpflichtungen und die Priorisierung des technischen Fortschritts vor der finalen Dokumentationsform.

Die Sanierung erfolgt durch folgende Massnahmen:

* Backlog wird konsequent priorisiert und geschätzt
* Definition of Done wird strikt eingehalten, closed Tickets werden bei offenen DoD Punkten wieder geöffnet
* Sprint Reviews enthalten ab jetzt konkrete Nachweise, nicht nur Text
* Status Updates erfolgen regelmässig, inklusive Links auf Board und Dokumentation

---

## Issues und User Stories

Das Projekt umfasst 27 User Stories, US01 bis US27. Alle Stories werden als GitHub Issues geführt und im [GitHub Project Board](https://github.com/users/Cancani/projects/3) verwaltet.

### Standards pro Issue

* User Story Text
* Akzeptanzkriterien als Checkboxen
* Definition of Done als Checkboxen
* Labels für Priorität und Bereich
* Milestone Zuordnung zu Sprint

### Project Board Felder

Die Steuerung erfolgt über folgende Felder im GitHub Project:

| Feld | Zweck |
|---|---|
| Status | Backlog, Ready, In Progress, Review, Done |
| Story Points | Aufwandsschätzung |
| Priorität | Must, Should, Could |
| Sprint | Sprint 1, Sprint 2, Sprint 3 |
| DoD erfüllt | Ja, Nein |

### Board Workflow

| Spalte | Bedeutung |
|---|---|
| Backlog | Neue Anforderungen, noch nicht priorisiert |
| Ready | Priorisiert und bereit zur Umsetzung |
| In Progress | Aktive Umsetzung, WIP Limit beachten |
| Review | DoD Kontrolle, Evidence prüfen |
| Done | Abgeschlossen und dokumentiert |

### Aufwandsschätzung und Story Points (Issues und User Stories)

Die Aufwände der einzelnen Issues und User Stories wurden mit Story Points geschätzt.
Story Points stellen bewusst **keine Zeitangaben** dar, sondern dienen als relative Bewertung
von Aufwand, Komplexität und Risiko.

Die Schätzung basiert auf folgenden Kriterien:
- Technische Komplexität der Aufgabe
- Anzahl beteiligter Komponenten (Service, CI/CD, Kubernetes, Cloud)
- Grad der Unsicherheit oder Neuartigkeit der Technologie
- Erwarteter Analyse-, Test- und Debuggingaufwand
- Abhängigkeiten zu anderen Tasks

Es wurde bewusst auf eine Schätzung in Stunden verzichtet,
da diese insbesondere bei technischen Aufgaben mit hohem Lern- und Analyseanteil
eine Scheingenauigkeit erzeugen würde.

### Priorisierung

Die Priorisierung der Issues erfolgt zentral im GitHub Project Board
und ist unabhängig von einzelnen Sprints.
Ziel der Priorisierung ist es,
den Fokus auf fachlich und technisch kritische Aufgaben zu legen
und Abhängigkeiten frühzeitig zu berücksichtigen.

Die Priorisierung basiert auf folgenden Kriterien:
- Technische Abhängigkeiten zu anderen Tasks
- Risiko für den Projektfortschritt oder Betrieb
- Kritikalität für einen lauffähigen End to End Betrieb
- Rückmeldungen und Anforderungen der Dozenten

Die Priorität wird pro Issue explizit festgelegt
und bleibt über mehrere Sprints hinweg sichtbar.
Dadurch ist jederzeit nachvollziehbar,
warum bestimmte Aufgaben früher umgesetzt wurden als andere.

Die Priorisierung wird im Project Board visuell dargestellt.
Issues mit der Priorität **Must** sind im Backlog ganz oben angeordnet,
darunter folgen Issues mit der Priorität **Should**,
während Issues mit der Priorität **Could** bewusst am unteren Ende des Backlogs platziert sind.

Diese Anordnung stellt sicher, dass fachlich und technisch zwingend notwendige Aufgaben jederzeit klar erkennbar sind und zuerst in die Sprint Planung einfliessen.

![Board Priorität](screenshots/Board_Prio.png)

---

### Verwendete Story-Point-Skala

| Story Points | Bedeutung |
|-------------|----------|
| 1 | Sehr kleiner Task, klar abgegrenzt, kaum Risiko |
| 2 | Kleiner Task mit überschaubarem Aufwand |
| 3 | Mittlerer Task mit mehreren Schritten oder Abhängigkeiten |
| 5 | Komplexer Task oder neue Technologie mit erhöhtem Debuggingaufwand |
| 8 | Sehr komplexer Task mit hohem Risiko oder vielen Unbekannten |

Die Story Points werden direkt pro Issue im GitHub Project Board gepflegt.
Zusätzlich ist in jedem Issue eine kurze Begründung der Schätzung dokumentiert.
Änderungen an Schätzungen wurden transparent im jeweiligen Issue festgehalten.

---

## Sprint Planungen, Reviews & Retrospektiven

Die nachfolgenden Abschnitte dokumentieren den vollständigen Projektverlauf und machen Fortschritte, Entscheidungen und Herausforderungen transparent nachvollziehbar.

---

### Sprint 1 Planung, Review und Retrospektive

#### Sprint Zeitraum

27.10.2025 bis 17.11.2025

#### Sprintziel

Projektbasis schaffen, damit Fortschritt und Qualität transparent nachvollziehbar sind. Fokus liegt auf Board Setup, Standards und erstem Architektur Zielbild.

![Sprint 1 Milestone & Issues](./screenshots/Sprint1_1.png)

---

#### Sprint 1 User Stories

Die folgenden User Stories gehören zu Sprint 1:

[Link zu Issues auf GitHub Projects](https://github.com/Cancani/geraeteausleihe-sem4/milestone/1)

| US | Titel | Bereich | Story Points |
|---|---|---|---|
| US01 | Kanban Board finalisieren | Projektmanagement | 1 |
| US02 | Labels anlegen | Projektmanagement | 1 |
| US03 | Milestones anlegen | Projektmanagement | 1 |
| US04 | Issue Template einrichten | Projektmanagement | 2 |
| US05 | Branching Strategie dokumentieren | Dokumentation | 2 |
| US06 | Sprint 1 Review und Retro dokumentieren | Dokumentation | 2 |
| US07 | Architektur Zielbild skizzieren | Architektur | 3 |

**Geplanter Aufwand Sprint 1:** **12 Story Points**

**WIP Regel**

In Progress maximal 2 parallel laufende Issues.

#### Evidence Standard für Sprint 1

Für Sprint 1 werden mindestens folgende Nachweise geplant:

* Screenshot Project Board Übersicht
* Screenshot Labels
* Screenshot Milestones
* Screenshot Issue Template
* Link zur Branching Dokumentation
* Architektur Zielbild als Diagramm

---

### Sprint 1 Review

**Reviewgespräch Hinweis**
Für Sprint 1 fand kein Reviewgespräch statt. Rückmeldungen und Hinweise wurden schriftlich via Microsoft Teams ausgetauscht.


#### Review Ergebnis

Sprint 1 wurde umgesetzt. Die Projektbasis ist vorhanden und bildet die Grundlage für Sprint 2 und Sprint 3.

| Review Punkt | Ergebnis |
|---|---|
| Board Struktur vorhanden und nachvollziehbar | Erfüllt |
| Labels vorhanden und konsistent genutzt | Erfüllt |
| Milestones für Sprints vorhanden | Erfüllt |
| Issue Template mit Akzeptanzkriterien und DoD vorhanden | Erfüllt |
| Branching Strategie dokumentiert | Erfüllt |
| Architektur Zielbild skizziert | Erfüllt |

**Umgesetzter Aufwand:** **12 von 12 Story Points**

![Sprint 1 erledigt](./screenshots/Sprint1_2.png)


#### Board und Planung

* Project Board Overview  

![Project Board Sprint 1](./screenshots/Projectboard_Sprint_1.png)

* Labels  

![Issue Labels](./screenshots/Issue_Labels.png)

* Milestones 

![Milestones](./screenshots/Milestones_Uebersicht.png)

* Issue Template  
![Issue Template](./screenshots/Issue_Template_1.png)
![Issue Template 2](./screenshots/Issue_Template_2.png)


### Sprint 1 Retrospektive


![Starfish Retrospektive Sprint 1](./screenshots/Sprint_1_Retro.png)

Die Retrospektive wurde mithilfe des Starfish-Modells durchgeführt und reflektiert die Erfahrungen des ersten Sprints.

### Zusammenfassung

Positiv hervorzuheben ist, dass die Projektbasis sauber aufgebaut wurde und damit eine nachvollziehbare Grundlage für die nächsten Sprints entstand. Die Aufgaben wurden konsequent als Issues erfasst, über ein Kanban Board gesteuert und durch definierte Standards wie Akzeptanzkriterien und Definition of Done strukturiert. Dadurch war der Fortschritt bereits in Sprint 1 transparent sichtbar.

Gleichzeitig zeigte Sprint 1, dass Projektmanagement nicht nur aus der Board Struktur besteht, sondern vor allem aus laufender Evidenz und aktiver Kommunikation. Rückmeldungen erfolgten in Sprint 1 ausschliesslich schriftlich via Teams und ohne separates Reviewgespräch. Dadurch fehlte zeitweise eine klare gemeinsame Standortbestimmung. Ebenfalls wurde deutlich, dass Nachweise und Dokumentation früher und kontinuierlicher gepflegt werden müssen, damit Stakeholder den Projektfortschritt jederzeit prüfen können.

Für die kommenden Sprints wurde festgehalten, dass visuelle Hilfsmittel wie Starfish, Risiko Matrix und Architektur Grafiken konsequent eingesetzt werden sollen. Zudem muss Dozentenfeedback nicht nur gelesen, sondern direkt als Issue erfasst, priorisiert und nachvollziehbar umgesetzt werden. Die Sprint Planung soll ausserdem klar definierte Sprint Goals enthalten, welche am Sprintende explizit überprüft werden.

## Empfehlungen für die nächsten Sprints

- Mehr Zeitpuffer beim Sprintbeginn einplanen und Aufgaben früh schätzen  
- Retrospektiven konsequent visuell dokumentieren und konkrete Massnahmen ableiten  
- Nachweise pro erledigtem Ticket sofort ergänzen und nicht erst am Sprintende  
- Dozentenfeedback direkt als Issue erfassen, priorisieren und mit Belegen abschliessen
  
---

### Sprint 2 Planung

#### Sprint Zeitraum

18.11.2025 bis 15.12.2025 (Wurde am 07.01.2025 durch Feedback von Fachdozenten verbessert)

#### Sprint Ziel

Technische Umsetzung für den Cloud Native Betrieb liefern und gleichzeitig die Nachvollziehbarkeit massiv verbessern. Der Fokus liegt auf einem lauffähigen End to End Betrieb mit Container, GHCR, K3s, Kubernetes und Ingress sowie auf sauberen Nachweisen, realistischen Schätzungen und einem sichtbar priorisierten Backlog.

![Sprint 2 Milestone und Issues](./screenshots/Sprint_2_Issues.png)

**Reviewgespräch Hinweis**  
Für Sprint 2 fand kein Reviewgespräch statt. Feedback erfolgte schriftlich via Microsoft Teams durch Corrado Parisi.

#### Sprint 2 Scope

Die folgenden Umsetzungspakete gehören zu Sprint 2:

| Bereich | Inhalt |
|---|---|
| Service | Bestehenden Flask Service aufbereiten, Requirements bereinigen und Tests ausführbar machen |
| Containerisierung | Dockerfile erstellen sowie Image lokal bauen und testen |
| Registry | Build und Push nach GitHub Container Registry (GHCR) mit sinnvollen Tags wie latest und Commit SHA |
| Kubernetes | Namespace, Deployment, Service und Ingress Manifeste erstellen |
| Infrastruktur | AWS EC2 bereitstellen, K3s installieren und Traefik Ingress nutzen |
| Deployment | Manuelles Deployment verifizieren und anschliessend GitHub Actions Deployment auf EC2 umsetzen |
| Nachweise | Pro abgeschlossenem Punkt Belege erfassen wie Screenshots, Logs, curl Ausgaben, kubectl Status und Actions Runs |
| PM Verbesserungen | Board Sichtbarkeit sicherstellen, Schätzungen und Priorisierung einführen sowie DoD in Tickets konsequent schliessen |
| Dokumentation | MkDocs Struktur pflegen, Navigation bereinigen und Grafiken ergänzen |

---

#### Sprint 2 User Stories

Die folgenden User Stories gehören zu Sprint 2:

[Link zu Issues auf GitHub Projects](https://github.com/Cancani/geraeteausleihe-sem4/milestone/2)

| US | Titel | Bereich | Story Points |
|---|---|---|---|
| US08 | EC2 Instanz vorbereiten | Infrastruktur | 3 |
| US09 | K3s auf EC2 installieren | Infrastruktur | 5 |
| US10 | Namespace und Basis Ressourcen erstellen | Kubernetes | 2 |
| US11 | Dockerfile finalisieren | Containerisierung | 3 |
| US12 | GHCR Push verifizieren | Registry | 2 |
| US13 | Kubernetes Deployment Manifest erstellen | Kubernetes | 3 |
| US14 | Kubernetes Service Manifest erstellen | Kubernetes | 2 |
| US15 | Ingress konfigurieren | Kubernetes | 5 |
| US16 | Readiness und Liveness Probes definieren | Kubernetes | 3 |
| US17 | Sprint 2 Review und Retro dokumentieren | Dokumentation | 2 |

**Geplanter Aufwand Sprint 2:** **30 Story Points**

#### WIP Regel

In Progress sind maximal zwei parallel laufende Issues erlaubt.


#### Evidence Standard für Sprint 2

Für Sprint 2 werden mindestens folgende Nachweise geplant und laufend in die technische Dokumentation ergänzt:

- Screenshot des GHCR Packages mit Tags latest und Commit SHA  
- Screenshot oder Link zu GitHub Actions Runs für Container Build und Deployment  
- Screenshot oder Output von Docker Build und lokalen Tests mit pytest  
- kubectl get nodes und kubectl get pods -A als Nachweis, dass K3s läuft  
- kubectl -n geraeteausleihe get all und get ingress als Nachweis für ein korrektes Deployment  
- curl Nachweise extern  
  - /healthz  
  - /pdf mit Content Disposition Header  
- Screenshots der relevanten Dokumentationsseiten wie Technische Umsetzung, Projektmanagement und Sprint Review  
- Mindestens eine Grafik für die Architektur und eine Grafik für den CI CD Ablauf  
- Eine Risiko Matrix wird als Grafik erstellt und eingebunden  

---

### Sprint 2 Review

**Reviewgespräch Hinweis**  
Für Sprint 2 fand kein Reviewgespräch statt. Feedback erfolgte schriftlich via Microsoft Teams durch Corrado Parisi.

#### Review Ergebnis

Sprint 2 wurde umgesetzt. Der Microservice läuft stabil auf AWS EC2 in einem K3s Cluster und ist extern über Traefik Ingress erreichbar. Build und Push nach GHCR funktionieren, sowie ein automatisiertes Deployment per GitHub Actions.


| Review Punkt | Ergebnis |
|---|---|
| Service läuft lokal und im Container | Erfüllt |
| Tests sind reproduzierbar im Container ausführbar | Erfüllt |
| Docker Image ist gebaut und lauffähig | Erfüllt |
| GHCR enthält Tags latest und Commit SHA | Erfüllt |
| AWS EC2 bereitgestellt und erreichbar | Erfüllt |
| K3s läuft und kubectl Zugriff ist möglich | Erfüllt |
| Kubernetes Namespace Deployment Service Ingress angewendet | Erfüllt |
| Externer Zugriff über nip io Host funktioniert | Erfüllt |
| Deployment Workflow setzt Image und prüft Rollout | Erfüllt |
| Nachweise sind zentral dokumentiert | Erfüllt |

**Umgesetzter Aufwand:** **27 von 27 Story Points**

![Sprint 2 erledigt](./screenshots/Sprint_2_Done.png)

---

#### Dozentenfeedback und Einbau in Review

Das schriftliche Feedback von Corrado Parisi wurde im Verlauf von Sprint 2 aktiv verarbeitet und in Dokumentation sowie Projektorganisation integriert. Die folgenden Punkte wurden umgesetzt und sind in der Dokumentation und im Project Board nachvollziehbar.

| Feedback Punkt | Umsetzung in Sprint 2 |
|---|---|
| Risikomatrix fehlt | Risikomatrix erstellt, bewertet und in der Dokumentation eingebunden |
| Board Link liefert 404 und Board ist nicht sichtbar | Project Link aktualisiert und Sichtbarkeit überprüft |
| Sprints sind unterschiedlich lang | Sprintlängen wurden korrigiert |
| Zu wenig Überblick über Projektstand | Massnahmen seit Feedback am Montag, 05.01.2026 umgesetzt, Status und Nachweise werden laufend gepflegt |
| Retro könnte noch mehr Struktur haben | Retrospektive visuell verbessert und klarer dokumentiert |
| Sprint Goals besser formulieren | Sprint Goals in der Dokumentation präziser formuliert und am Sprintende überprüfbar gestaltet |
| Wie schätzt du deine Tasks | Story Points pro Issue dokumentiert und Aufwand transparent gemacht |
| Priorisierung im Backlog sichtbar machen | Issues nach Priorität im Kanban Board sichtbar gemacht und nach Must Should Could gefiltert |

---

### Sprint 2 Retrospektive

![Starfish Retrospektive Sprint 2](./screenshots/Sprint_2_Retro.png)

Die Retrospektive wurde mithilfe des Starfish Modells durchgeführt und reflektiert die Erfahrungen aus Sprint 2. Zusätzlich wurde das schriftliche Dozentenfeedback von Corrado Parisi einbezogen, um konkrete Verbesserungen für Transparenz, Nachvollziehbarkeit und technische Stabilität abzuleiten.

### Zusammenfassung

Positiv hervorzuheben ist, dass der Cloud Native Betrieb technisch umgesetzt und stabil lauffähig gemacht wurde. Der Flask Microservice läuft containerisiert, Images werden automatisiert nach GHCR gepusht und der Service ist auf AWS EC2 in einem K3s Cluster über Traefik Ingress extern erreichbar. Damit ist der zentrale Sprint 2 Anspruch erfüllt, einen End to end Betrieb aufzubauen, der über reale Requests von aussen verifiziert werden kann. Ebenso wurde die technische Dokumentation deutlich ausgebaut, sodass wichtige Schritte und Entscheide nachvollziehbar sind.

Gleichzeitig zeigte Sprint 2 klar, dass technische Umsetzung allein nicht genügt, wenn der Projektstand für Stakeholder nicht jederzeit sichtbar ist. Corrado hat insbesondere fehlende Transparenz kritisiert, zum Beispiel fehlender Überblick über Ziele und Herausforderungen, ein zeitweise nicht zugängliches Board sowie uneinheitliche Sprintlängen. Diese Punkte wurden aufgenommen und korrigiert. Der Board Link wurde aktualisiert, die Sprintlängen wurden konsistenter gestaltet und der Überblick in der Dokumentation wurde verbessert, indem Status, Ziele und nächste Schritte klarer beschrieben wurden. Zusätzlich wurde die Retrospektive visuell stärker aufbereitet und Sprint Goals wurden präziser formuliert.

Ausserdem wurde deutlich, dass Deploy Automatisierung sehr fehleranfällig ist, wenn Variablen und Image Tags nicht deterministisch gesetzt werden. Mehrere Fehlerquellen entstanden durch falsche Repo und SHA Übernahme und durch unstimmige Workflow Logik. Daraus ergibt sich als wichtiger Lernpunkt, dass CI CD Schritte nicht nur gebaut, sondern auch konsequent mit Rollout Status und externem Health Check verifiziert werden müssen. Im selben Zuge wurde das Thema Schätzung verbessert. Tasks wurden mit Story Points dokumentiert und die Priorisierung im Board wurde sichtbar gemacht, um Abhängigkeiten und kritische Aufgaben zuerst umzusetzen.

Für die kommenden Sprints wurde festgehalten, dass die Kombination aus stabiler Technik und laufender Evidenz der Schlüssel ist. Dozentenfeedback muss früh erfasst, im Backlog sichtbar priorisiert und durch konkrete Anpassungen nachweisbar umgesetzt werden. Der Schwerpunkt liegt in Sprint 3 darauf, Deploy und Betrieb weiter zu stabilisieren, die Dokumentation als zentrale Quelle konsequent weiterzuführen und den Projektstatus für Dozenten dauerhaft transparent zu halten.

---

### Sprint 3 Planung

#### Sprint Zeitraum

15.12.2025 bis 21.01.2026 (Terminorientiert wegen Gespräch mit Corrado am 13.01.2026)

#### Sprint Ziel

CI und CD für den Cloud Native Betrieb stabil und nachvollziehbar umsetzen. Fokus liegt auf einem reproduzierbaren Build und Push nach GHCR, einem automatischen Deployment nach K3s auf AWS EC2, klarer Tagging Strategie sowie einer vollständigen technischen Dokumentation als Basis für das Gespräch mit Corrado.

![Sprint 3 Milestone und Issues](./screenshots/Sprint_3_Milestone_Issues.png)

**Reviewgespräch Hinweis**  
Für Sprint 3 ist ein Gespräch mit Corrado am 13.01.2026 geplant. Ziel ist es, bis dahin einen stabilen Stand inklusive Nachweisen und Dokumentation vorzeigen zu können.

#### Sprint 3 Scope

Die folgenden Umsetzungspakete gehören zu Sprint 3:

| Bereich | Inhalt |
|---|---|
| CI Build | GitHub Actions Build robust machen und nur bei relevanten Änderungen ausführen |
| Registry | Push nach GHCR mit konsistenten Tags wie latest und Commit SHA sowie lowercase Repository |
| Secrets | Zugriff für GHCR und EC2 sauber über GitHub Secrets abbilden und testen |
| CD Deployment | Automatisches Deployment nach K3s via Workflow, inkl. apply, set image, rollout status |
| Tagging | Tagging Strategie definieren und konsistent in Build und Deploy anwenden |
| Tests und Checks | Pipeline Testlauf als Nachweis dokumentieren, inklusive Logs und Outputs |
| Dokumentation | Technische Dokumentation zu CI, CD und Betrieb aktualisieren und prüfbar machen |

---

#### Sprint 3 User Stories

Die folgenden User Stories gehören zu Sprint 3:

[Link zu Issues auf GitHub Projects](https://github.com/Cancani/geraeteausleihe-sem4/milestone/3)

| US | Titel | Bereich | Story Points |
|---|---|---|---|
| US18 | GitHub Actions Build und Push nach GHCR | CI | 5 |
| US19 | Secrets für GHCR und Cluster Zugriff einrichten | Security | 3 |
| US20 | CD Workflow deployt nach K3s | Kubernetes | 5 |
| US21 | Tagging Strategie dokumentieren und anwenden | Repo | 3 |
| US22 | Pipeline Testlauf dokumentieren | Testing | 3 |
| US23 | Sprint 3 Review und Retro dokumentieren | PM | 2 |

**Geplanter Aufwand Sprint 3:** **21 Story Points**

#### WIP Regel

In Progress sind maximal zwei parallel laufende Issues erlaubt.

#### Evidence Standard für Sprint 3

Für Sprint 3 werden mindestens folgende Nachweise geplant und laufend in die technische Dokumentation ergänzt:

* Screenshot oder Link zu GitHub Actions Run für Build und Push nach GHCR  
* Screenshot GHCR Package mit latest und Commit SHA Tag  
* Screenshot oder Link zu Deploy Workflow Run inklusive Logs  
* Output von kubectl get pods und kubectl rollout status als Rollout Nachweis  
* Screenshot oder Output der gesetzten Image Version im Deployment  
* Externer Health Check Nachweis über den Ingress Host  
  * http://geraeteausleihe.13.223.28.53.nip.io/healthz  
* Dokumentierte Tagging Strategie mit Begründung  
* Dokumentierter Pipeline Testlauf als End to End Nachweis  

---


## Sprint 3 Review

**Reviewgespräch Hinweis**  
Für Sprint 3 ist ein Gespräch mit Corrado am 13.01.2026 geplant. Aktuell ist Sprint 3 in Umsetzung. Dieses Review basiert auf dem aktuellen Arbeitsstand und den bereits nachweisbaren Ergebnissen.


### Aktueller Stand

Sprint 3 fokussiert auf stabile und nachvollziehbare CI und CD. Der Container Build und Push nach GHCR funktioniert. Deploy nach K3s wurde umgesetzt und läuft, inklusive Apply der Manifeste, Setzen des Images und Rollout Kontrolle. Externe Verifikation über den Ingress Host ist möglich und die Endpoints sind erreichbar.

### Review Ergebnis

Sprint 3 ist technisch weit fortgeschritten. Der Betrieb ist erreichbar und die Pipeline läuft. Einzelne Punkte sind noch in Arbeit und müssen dokumentiert werden, vor allem die Stabilisierung der Workflow Logik und die laufende Evidence Ablage pro Change.

| User Story | Titel | Status | Nachweis |
|---|---|---|---|
| US18 | GitHub Actions Build und Push nach GHCR | Erledigt | GitHub Actions Run, GHCR Package Tags |
| US19 | Secrets für GHCR und Cluster Zugriff | Erledigt | Secrets gesetzt, Deploy Run mit SSH und SCP |
| US20 | CD Workflow deployt nach K3s | In Arbeit | Deploy läuft, Stabilisierung der Variablen und Pfade |
| US21 | Tagging Strategie dokumentieren und anwenden | Erledigt | Tags latest und Commit SHA, lowercase Repo |
| US22 | Pipeline Testlauf dokumentieren | In Arbeit | Screenshot Logs, kubectl Outputs, externe Checks |
| US23 | Sprint 3 Review und Retro dokumentieren | In Arbeit | Dieser Abschnitt, Retro folgt |

### Was ist aktuell noch in Arbeit

* Deploy Workflow Robustheit  
  Variablen müssen deterministisch sein, besonders DEPLOY SHA und Image Referenz, damit nicht wieder ein leeres Repository wie ghcr.io/:sha gesetzt wird

* Trigger Logik für Container Build  
  Build soll nur bei Service relevanten Änderungen laufen und nicht bei reinen Doku Änderungen wie README

* Evidence und Nachweise pro Änderung  
  Pro Deployment Run sollen Logs, kubectl Status und externer Health Check als Screenshots oder Text Output abgelegt werden, damit Stakeholder laufend den Stand sehen

  

---

#### Sprint 3 Retrospektive



---


## Verwaltung der Aufgaben

Die Aufgaben wurden vollständig in [GitHub Projects](https://github.com/users/Cancani/projects/3/views/1) organisiert.  
Das Board ist nach Sprints gegliedert und orientiert sich an der Kanban-Struktur mit den Spalten  
**Backlog**, **Ready**, **In Progress**, **Review** und **Done**.  

Jede Aufgabe ist als **GitHub Issue** (US01 – US27) angelegt und enthält:
- eine klare **User Story**,
- **Akzeptanzkriterien** und **Definition of Done** als Checkboxen,
- eine **Priorität** (Must / Should / Could),
- die Zuordnung zum **Sprint** als Milestone


![Project Board](./screenshots/Projectboard_Sprint_1.png)

Der Fortschritt ist über das Board jederzeit nachvollziehbar:  
Geschlossene Issues wandern automatisch nach „Done“, offene bleiben in „Review“, bis alle DoD-Kriterien erfüllt und Nachweise in der Dokumentation ergänzt sind.  
Diese Struktur sorgt für durchgängige Transparenz im gesamten Projektmanagementprozess.

---

## Wechsel von GitLab zu GitHub Projects und Issues

### Hintergrund

Zu Beginn der Semesterarbeit 4 wurde die Projektplanung zunächst provisorisch in GitLab vorbereitet, da das Tool visuell bekannt war und bereits in früheren Arbeiten genutzt wurde.  
Mit dem Start der technischen Umsetzung erfolgte jedoch der Umstieg auf **GitHub Projects**, um Code, Doku und Aufgabenverwaltung auf einer Plattform zu bündeln.  

Durch diesen Wechsel konnten alle User Stories direkt mit Commits, Pull Requests und Actions-Runs verknüpft werden.  
Damit war es erstmals möglich, Planung, Automatisierung und Deployment vollständig integriert zu führen.

---

### Gründe für den Wechsel

- **Zentrale Plattform:** Code, Doku und Tasks an einem Ort  
- **Nachvollziehbarkeit:** Verknüpfung von Issues, Commits und Deployments  
- **Automatisierung:** Actions können Status oder Nachweise direkt aktualisieren  
- **Klarer Prozess:** Backlog → Sprint → Review → Done (identisch mit Planner, aber nachvollziehbar versioniert)  
- **GitHub Labels und Milestones:** Ersetzen Buckets und Fälligkeitsdaten aus Planner  
- **Synchronität mit CI/CD:** Automatische Workflows binden den Projektfortschritt direkt an den technischen Build Prozess  


---

### Fazit

Der Wechsel zu GitHub Projects und Issues hat sich als entscheidender Schritt erwiesen.  
Er ermöglicht einen durchgängigen Arbeitsfluss zwischen Code, Automation und Projektmanagement, ohne Tool-Brüche.  
Zudem ist die Nachweisführung durch Screenshots, Actions-Runs und verlinkte Dokumentation klar prüfbar und Versionen lassen sich über Commit-SHAs direkt nachvollziehen.

---

## SWOT-Analyse

Die SWOT-Analyse fasst die internen und externen Faktoren des Projekts zusammen und dient zur Bewertung der technologischen Tragfähigkeit und prozessualen Stabilität. Die SWOT-Analyse bietet einen strukturierten Überblick über die internen Stärken und Schwächen sowie die externen Chancen und Risiken des Projekts. Ziel ist es, das Projekt im Hinblick auf seine technologische, organisatorische und strategische Tragfähigkeit zu reflektieren.

![SWOT-Analyse](./screenshots/SWOT.png)

### Stärken

- **Cloud Native Architektur**
  - Kubernetes ermöglicht skalierbaren und stabilen Betrieb
  - Self Healing durch automatische Pod Neustarts

- **Automatisierte CI/CD Pipeline**
  - Build, Push und Deployment laufen vollautomatisch
  - Reduktion von manuellen Fehlern bei Deployments

- **Moderne DevOps Praktiken**
  - Infrastructure as Code Denkweise
  - Versionierte Deployments über GitHub Container Registry

- **Technologie Unabhängigkeit**
  - Kein Vendor Lock In wie bei proprietären Plattformen
  - Offene Standards (Docker, Kubernetes, GitHub Actions)

- **Saubere Dokumentation**
  - Projektmanagement und Technik transparent dokumentiert
  - GitHub Pages ermöglicht jederzeitigen Zugriff


### Schwächen

- **Erhöhte Komplexität**
  - Kubernetes und CI/CD erfordern tiefere Einarbeitung
  - Höherer initialer Setup Aufwand

- **Single Node Setup**
  - K3s läuft auf einer einzelnen EC2 Instanz
  - Keine echte Hochverfügbarkeit

- **Betriebsverantwortung**
  - Wartung und Updates liegen vollständig beim Betreiber
  - Monitoring und Alerting nur rudimentär umgesetzt

- **Kein Managed Service**
  - Im Vergleich zu EKS mehr manueller Aufwand
  - Sicherheitsupdates müssen selbst geplant werden

### Chancen

- **Skalierbarkeit für Zukunft**
  - Erweiterung auf Multi Node Cluster möglich
  - Einfache Integration weiterer Microservices

- **Übertragbarkeit auf reale Projekte**
  - Architektur entspricht modernen Unternehmensstandards
  - Direkter Praxisbezug für DevOps und Cloud Rollen

- **Automatisierungspotenzial**
  - Erweiterbar um Monitoring, Logging und Alerts
  - GitOps Ansatz später möglich

- **Weiterentwicklung der Anwendung**
  - Anbindung weiterer Systeme oder Services
  - Trennung von Frontend und Backend möglich

- **Wiederverwendbarkeit**
  - Pipeline und Kubernetes Manifeste können für andere Projekte genutzt werden


### Risiken

- **Fehlkonfigurationen**
  - Fehler in Kubernetes Manifests können Service Ausfall verursachen
  - Sicherheitsrelevante Fehlkonfigurationen möglich

- **Kostenrisiken**
  - AWS EC2 Kosten bei längerem Betrieb
  - Speicher und Traffic Kosten bei Skalierung

- **Know how Abhängigkeit**
  - Betrieb erfordert Kubernetes und Linux Wissen
  - Fehlende Erfahrung kann zu Ausfällen führen

- **Zeitliche Überforderung**
  - Parallel laufende Module können Zeitdruck erzeugen
  - Debugging von CI/CD kann zeitintensiv sein


### Fazit der SWOT Analyse

Die Cloud Native Umsetzung bietet klare Vorteile in Bezug auf Automatisierung, Skalierbarkeit und Wartbarkeit.  
Die erhöhte technische Komplexität und der manuelle Betriebsaufwand stellen jedoch Herausforderungen dar.  
Insgesamt überwiegen die Stärken und Chancen, insbesondere im Hinblick auf Lerngewinn und Praxisnähe für moderne IT Betriebsmodelle.




---

## Use-Case Diagramm

Das Use-Case Diagramm zeigt die Akteure und Interaktionen mit dem Geräteausleihe-System aus technischer Sicht.  
Die Zielgruppe sind vor allem Stakeholder, die den Betrieb oder die Integration bewerten möchten.

![Use-Case](./screenshots/use_case_diagramm.png)

### Akteure

| Akteur | Rolle | Berechtigung | Hauptfunktionen |
|--------|-------|---------------|-----------------|
| **Developer / Student** | Projektverantwortlicher | Vollzugriff auf Repo und Cluster | Code, Deploy, Doku |
| **Fachdozent** | Reviewer | Leserechte auf Board und Repo | Sprint Reviews, Feedback |
| **AWS System** | Infrastruktur | Cluster Hosting und Networking | CI/CD Zielsystem |
| **GitHub Actions** | Automatisierung | Build, Push, Deploy | Workflows, Status, Rollbacks |
| **Nutzer (PowerApps)** | Externer Konsument | Zugriff auf /healthz und /pdf | Nutzung der API |

---

### Use-Cases im Detail

| Use-Case | Beschreibung | Akteur | Priorität |
|-----------|--------------|---------|-----------|
| **UC1** | Codeänderung pushen | Developer | Hoch |
| **UC2** | Workflow ausführen | GitHub Actions | Hoch |
| **UC3** | Container bauen und pushen | GitHub Actions / GHCR | Hoch |
| **UC4** | Deployment auf K3s durchführen | GitHub Actions | Hoch |
| **UC5** | Service testen über /healthz | Nutzer / Dozent | Hoch |
| **UC6** | PDF-Endpoint überprüfen | Nutzer / Dozent | Mittel |
| **UC7** | Rollback auf älteres Image durchführen | Developer | Mittel |
| **UC8** | Dokumentation aktualisieren und deployen | GitHub Actions | Mittel |

---

### Externe System-Integrationen

| System | Beschreibung | Use-Cases | Schnittstelle |
|---------|---------------|------------|----------------|
| **GitHub Actions** | CI/CD-Automatisierung | UC1 – UC4, UC8 | Workflow-YAML |
| **GHCR** | Container Registry für Images | UC3 – UC4 | Docker API |
| **AWS EC2** | Hostet den K3s Cluster | UC4 – UC7 | SSH / kubectl |
| **K3s Cluster** | Kubernetes Runtime | UC4 – UC7 | API Server |
| **PowerApps** | Client Frontend für Nutzer | UC5 – UC6 | HTTP GET |
| **GitHub Pages** | Dokumentationshosting | UC8 | Static Site Deploy |

---

### Geschäftsregeln und technische Constraints

**Berechtigungen:**
- Nur der Developer darf Deployments ausführen.
- Dozenten haben Leserechte auf Board, Repo und Doku.
- GitHub Actions arbeitet mit SSH-Key und Secret Authentication.

**Regeln für Deployments:**
- Nur Änderungen im Ordner `/service` lösen einen Container Build aus.
- Deployments erfolgen nur auf dem Branch `main`.  
- Erfolgreiche Deployments werden in der Doku unter Evidence pro Sprint nachgewiesen.

**Technische Constraints:**
- Cluster: Einzelinstanz K3s auf AWS EC2 t3.medium  
- Registry: GHCR öffentlich lesbar, privat schreibgeschützt  
- Keine Persistenz im Cluster, da State nicht Teil des Projekts  
- Keine TLS Zertifikate, da nip.io Host für interne Demo

---

## Risikomatrix

Die Risikomatrix dient zur strukturierten Bewertung potenzieller Risiken im Projekt.

Bewertet werden Risiken aus den Bereichen **Infrastruktur, Kubernetes, CI/CD, Sicherheit und Betrieb**.  
Die Kombination aus Eintrittswahrscheinlichkeit und Auswirkung zeigt die Dringlichkeit notwendiger Gegenmassnahmen.

**(Stand 07.01.2025)**

![Risikomatrix](./screenshots/Risikomatrix_Sem4.png)



### Achsenbeschreibung

- **Y-Achse:** Eintrittswahrscheinlichkeit  
  (Unwahrscheinlich → Sehr wahrscheinlich)

- **X-Achse:** Auswirkung  
  (Niedrig → Kritisch)

### Farbbedeutung

- 🟩 Grün: Geringes Risiko  
- 🟨 Gelb: Akzeptables Risiko  
- 🟧 Orange: Erhöhtes Risiko  
- 🔴 Rot: Kritisches Risiko

---

### Risiken im Detail

| Nr. | Risiko                                                                 | Eintritt        | Auswirkung | Bewertung | Massnahme / Lösung |
|----:|------------------------------------------------------------------------|-----------------|------------|-----------|--------------------|
| 1 | Fehlkonfiguration von Kubernetes Manifests (Pods starten nicht) | Gelegentlich | Hoch | Orange | Manifeste schrittweise testen, `kubectl apply --dry-run`, Logs prüfen |
| 2 | CI Pipeline schlägt fehl durch falsche Secrets oder Tokens | Wahrscheinlich | Mittel | Orange | Secrets früh testen, klare Namenskonventionen, Test Runs |
| 3 | Kein Zugriff auf EC2 Instanz (SSH Key verloren oder Security Group Fehler) | Unwahrscheinlich | Kritisch | Gelb | SSH Keys sichern, Dokumentation der Zugänge, Fallback Zugriff |
| 4 | Container Image wird nicht korrekt nach GHCR gepusht | Gelegentlich | Mittel | Gelb | Image Tags prüfen, lowercase Repo Namen erzwingen |
| 5 | Ingress ist falsch konfiguriert, Service nicht erreichbar | Gelegentlich | Hoch | Orange | Ingress separat testen, Logs des Ingress Controllers prüfen |
| 6 | K3s Dienst oder Node fällt aus (Single Node Setup) | Selten | Hoch | Gelb | Neustart Strategien dokumentieren, Risiko bewusst akzeptieren |
| 7 | Fehlende Health Checks führen zu instabilem Betrieb | Wahrscheinlich | Mittel | Orange | Readiness und Liveness Probes definieren |
| 8 | Fehlerhafte CI/CD Änderung deployed fehlerhafte Version | Gelegentlich | Hoch | Orange | Deployment nur über main, saubere Reviews, Rollback via Image Tag |
| 9 | Dokumentation nicht aktuell zum Projektstand | Gelegentlich | Niedrig | Grün | Doku als Teil der Definition of Done |
| 10 | Zeitmangel durch parallele Module und Aufgaben | Sehr Wahrscheinlich | Hoch | Rot | Priorisierung auf Kernanforderungen, Sprint Planung strikt einhalten |

---

### Einordnung in die Risikomatrix

Die Risiken wurden in der Risikomatrix wie folgt positioniert:

- **Orange (erhöhtes Risiko):** 1, 2, 5, 7, 8  
- **Gelb (akzeptables Risiko):** 3, 4, 6  
- **Grün (geringes Risiko):** 9  
- **Rot (kritisch):** 10


---

### Fazit

- Insgesamt wurden 10 projektrelevante Risiken identifiziert und bewertet.
- Mehrere Risiken befinden sich im orangefarbenen Bereich, was die erhöhte technische Komplexität von Kubernetes und CI/CD widerspiegelt.
- Ein Risiko (Nr. 10: Zeitmangel durch parallele Module und Aufgaben) wurde bewusst als **kritisch (rot)** eingestuft, da die zeitlichen Rahmenbedingungen während des Semesters eine reale und hohe Gefahr darstellen.
- Dieses Risiko wird durch klare Priorisierung der Kernanforderungen, Sprint-Planung sowie konsequente Fokussierung auf Mindestanforderungen aktiv adressiert.
- Insgesamt bleibt das Risikoprofil trotz des identifizierten kritischen Risikos kontrollierbar und angemessen für ein praxisorientiertes Lernprojekt.

# Architektur

Die folgenden Abschnitte erklären die drei Diagramme inhaltlich und bezogen auf dein aktuelles Setup mit GitHub, GHCR, AWS EC2, K3s und Traefik Ingress. Externe Erreichbarkeit erfolgt über den Host `geraeteausleihe.<EC2_IP>.nip.io`, die wichtigsten Endpoints sind `/healthz` und `/pdf`.

## Deployment Ablauf

Dieses Diagramm zeigt den Ablauf einer Änderung vom Commit bis zum erfolgreichen Rollout im K3s Cluster.

1. Entwickler pusht Änderungen auf den Branch `main` im GitHub Repository.  
2. GitHub triggert den GitHub Actions Workflow aufgrund des Push Events.  
3. GitHub Actions baut ein neues Docker Image aus dem aktuellen Repository Stand. Dabei wird der Service reproduzierbar erstellt, inklusive Abhängigkeiten.  
4. Das erzeugte Image wird in die GitHub Container Registry GHCR gepusht. Als Tag wird ein eindeutiger Wert genutzt, typischerweise die Commit SHA, damit jede Version klar nachvollziehbar ist.  
5. Danach startet der Deploy Schritt. GitHub Actions authentifiziert sich auf die AWS EC2 Instanz, auf der K3s läuft. In deinem Setup passiert das üblicherweise über SSH zur EC2 Instanz und anschliessend über `kubectl` Befehle im richtigen Cluster Kontext.  
6. Mit `kubectl apply` werden die Kubernetes Manifeste angewendet oder aktualisiert. Damit sind Namespace, Deployment, Service und Ingress definiert.  
7. K3s führt ein Rolling Update durch. Neue Pods werden gestartet, Readiness greift, danach werden alte Pods beendet. Der Service bleibt während des Updates erreichbar.  
8. Der Workflow prüft den Rollout Status. Bei Erfolg gilt das Deployment als abgeschlossen. Optional kann danach zusätzlich ein externer Smoke Test erfolgen, zum Beispiel ein Request auf `https://geraeteausleihe.<EC2_IP>.nip.io/healthz`.

Kernaussage: Jeder Push auf `main` erzeugt eine neue deployte Version. Der Commit SHA Tag in GHCR dient als Nachweis, welche Version gerade produktiv läuft und ermöglicht ein sauberes Rollback auf eine frühere Version.

**Sequenzdiagramm**


```mermaid
sequenceDiagram
  autonumber
  participant Dev as Developer
  participant GH as GitHub
  participant GA as GitHub Actions
  participant Reg as GHCR
  participant K as K3s on EC2

  Dev->>GH: Push auf main
  GH->>GA: Trigger Workflow
  GA->>GA: Build Docker Image
  GA->>Reg: Push Image Tag commit sha
  GA->>K: Auth und kubectl apply
  K->>K: Rollout Deployment
  K-->>GA: Rollout Status ok
```
___

#### Flowchart LR Komponenten und Datenfluss von Entwicklung bis Nutzerzugriff

Dieses Diagramm zeigt die Systemlandschaft und den Datenfluss von links nach rechts, also vom lokalen Arbeiten bis zum Aufruf durch Nutzer.

1. Der Entwickler arbeitet lokal am Service, an den Kubernetes Manifesten und an den Workflows.  
2. Der Code wird ins GitHub Repository gepusht. Das Repository ist die zentrale Quelle für Source Code, `k8s` Manifeste und Workflows unter `.github/workflows`.  
3. Bei einem Push auf `main` startet GitHub Actions.  
4. GitHub Actions baut das Docker Image und pusht es nach GHCR. Dadurch ist das Artefakt zentral verfügbar und eindeutig versioniert.  
5. Anschliessend führt GitHub Actions den Deploy Job aus und verbindet sich mit der AWS EC2 Instanz, auf der K3s läuft.  
6. In K3s existiert ein Namespace `geraeteausleihe`. Dort laufen Deployment, Pods, Service und Ingress.  
7. Der Ingress wird über Traefik bereitgestellt. Er nimmt externe HTTP Requests an, matched Host und Pfade und leitet den Traffic intern an den Service weiter.  
8. Der Service verteilt den Traffic auf die laufenden Pods. Die Pods beantworten die Requests, zum Beispiel `/healthz` für den Health Check und `/pdf` für die PDF Ausgabe.  
9. Der Nutzer greift extern über `geraeteausleihe.<EC2_IP>.nip.io` zu. nip.io löst den Host automatisch auf die EC2 IP auf und ersetzt damit eine klassische DNS Konfiguration.

Kernaussage: Das Diagramm zeigt die saubere Trennung zwischen Artefakt Ebene und Laufzeit Ebene. Das Image entsteht und lebt in GHCR, die Ausführung erfolgt in K3s als Pods, gesteuert durch deklarative Manifeste.


```mermaid
flowchart LR
  Dev[Developer Laptop] --> Repo[GitHub Repository]
  Repo -->|push auf main| Actions[GitHub Actions Workflow]

  Actions --> Build[Build Docker Image]
  Build --> GHCR[GitHub Container Registry]

  Actions --> Deploy[Deploy Job]
  Deploy -->|kubectl apply| EC2[AWS EC2 Instance]
  EC2 --> K3s[K3s Cluster]

  K3s --> NS[Namespace]
  NS --> DEP[Deployment]
  DEP --> PODS[Pods]
  NS --> SVC[Service]
  NS --> ING[Ingress]

  Users[User Browser] --> ING
  ING --> SVC
  SVC --> PODS

```

---

#### Flowchart TB interne Kubernetes Struktur im Cluster

Dieses Diagramm zoomt in den K3s Cluster hinein und zeigt die internen Kubernetes Objekte und deren Rollen.

1. K3s ist die Kubernetes Laufzeitplattform auf deiner AWS EC2 Instanz. Sie übernimmt Scheduling, Rollouts, Self Healing und Cluster Networking.  
2. Im Cluster existiert der Namespace `geraeteausleihe`. Er dient der logischen Trennung, verbessert die Übersicht und erleichtert die Wartung.  
3. Das Deployment beschreibt, welches Container Image laufen soll, wie viele Replikate gewünscht sind und welche Ports und Einstellungen der Service braucht.  
4. Aus dem Deployment entsteht ein ReplicaSet. Das ReplicaSet stellt sicher, dass die gewünschte Anzahl Pods wirklich läuft. Fällt ein Pod aus, wird automatisch ein neuer erstellt.  
5. Die Pods sind die eigentlichen Instanzen deines Flask Microservice. Dort laufen die Endpoints `/healthz` und `/pdf`.  
6. Der Service vom Typ ClusterIP stellt eine interne stabile Adresse bereit und verteilt Requests an die Pods anhand von Labels.  
7. Der Ingress Controller Traefik nimmt externe Requests entgegen. Er leitet sie anhand von Regeln im Ingress Objekt an den Service weiter.  
8. Der Nutzer spricht nur den Ingress an. Alles danach passiert intern über Service und Pod Networking.

Kernaussage: Extern sichtbar ist der Ingress, intern bleibt die Applikation über Service und Deployment abstrahiert. Das entspricht der erwarteten Kubernetes Struktur für stabile Deployments und Rolling Updates.


```mermaid
flowchart TB
  subgraph K3s[K3s Cluster]
    subgraph NS[Namespace geraeteausleihe]
      DEP[Deployment]
      DEP --> RS[ReplicaSet]
      RS --> P1[Pod 1]
      RS --> P2[Pod 2]
      SVC[Service ClusterIP]
    end

    INGCTRL[Ingress Controller]
  end

  Users[User Browser] --> INGCTRL
  INGCTRL --> SVC
  SVC --> P1
  SVC --> P2
```

---

### Zielbild

FlowChart Zielbild <add Text>


```mermaid
flowchart TD
  subgraph Clients
    PA[PowerApps Client]
    BR[Browser]
  end

  subgraph GitHub
    REPO[Repository]
    ACT[GitHub Actions]
    GHCR[GitHub Container Registry]
    PAGES[GitHub Pages]
  end

  subgraph AWS
    EC2[AWS EC2 Instanz]
    K3S[K3s Cluster]
    TRF[Traefik Ingress]
    SVC[Flask Microservice geraeteausleihe]
  end

  PA -->|HTTP| TRF
  BR -->|HTTP| TRF
  TRF -->|Service Routing| SVC

  REPO --> ACT
  ACT -->|Build und Push| GHCR
  ACT -->|kubectl apply set image| K3S
  GHCR -->|pull image| SVC

  REPO -->|MkDocs Build| PAGES
```

---

## Komponenten

| Komponente | Aufgabe | Hinweis |
| --- | --- | --- |
| PowerApps | Konsument des Microservice | Ruft den PDF Endpoint auf |
| Flask Microservice | REST API und PDF Ausgabe | Läuft containerisiert |
| GitHub Actions | Build, Push, Deploy und Docs | CI CD und GitHub Pages |
| GHCR | Container Images | Versionierung über Tags |
| AWS EC2 | Compute Basis | K3s läuft auf der Instanz |
| K3s | Kubernetes Distribution | Single Node Betrieb für das Projekt |
| Traefik Ingress | HTTP Ingress Controller | Routing auf Service |
| nip io | DNS Convenience | Hostname ohne eigene DNS Zone |

---

## Schnittstellen und Endpunkte

| Endpoint | Methode | Zweck | Erwartung |
| --- | --- | --- | --- |
| `/healthz` | GET | Health Check | 200 OK |
| `/pdf` | GET | PDF Ausgabe für PowerApps | PDF Response |

---

## Kubernetes Ressourcen

| Manifest | Ressource | Zweck | Wichtige Punkte |
| --- | --- | --- | --- |
| `k8s/namespace.yaml` | Namespace | Trennung der App Ressourcen | eigener Namespace |
| `k8s/deployment.yaml` | Deployment | Pods und Rolling Update | Image Tag, Probes |
| `k8s/service.yaml` | Service | Interner Zugriff | ClusterIP |
| `k8s/ingress.yaml` | Ingress | Externer Zugriff | Host und Path Routing |

---

## Ingress Host Handling

Für die Erreichbarkeit ohne eigene DNS Zone wird nip io verwendet.

| Element | Beispiel |
| --- | --- |
| Muster | `geraeteausleihe.<EC2_IP>.nip.io` |
| Vorteil | Keine DNS Konfiguration, sofort testbar |
| Nachteil | Nicht geeignet für produktive Umgebungen |

---

## Security und Betrieb

| Bereich | Umsetzung | Offener Ausbau |
| --- | --- | --- |
| Secrets | GitHub Secrets, EC2 SSH, Registry Zugriff | Rotation und Least Privilege |
| Probes | Readiness und Liveness geplant | Grenzwerte und Fehlerfälle testen |
| Logs | Container Logs über kubectl abrufbar | Zentrales Logging optional |
| Rollback | Über Image Tags möglich | Strategie dokumentieren und üben |

---

# Branching Strategie und Regeln

## Ziel
Die Branching Strategie stellt sicher, dass der **main Branch jederzeit stabil** ist und den Stand für Demo und Abgabe abbildet. Entwicklung und laufende Arbeiten erfolgen auf **develop** oder auf **feature branches**. Die Dokumentation wird über GitHub Pages aus dem Repository veröffentlicht.

## Branches

- **main**
  - Stabiler Stand für Sprint Reviews, Demo und Abgabe
  - Änderungen erfolgen nur über Pull Requests
  - Keine direkten Pushes, sofern Branch Regeln aktiv sind

- **develop**
  - Integrationsbranch für laufende Entwicklung
  - Feature branches werden zuerst nach develop gemerged
  - develop dient als Sammelpunkt bis zum stabilen Merge nach main

- **feature branches**
  - Kurzlebige branches für einzelne Themen oder Issues
  - Namensschema Empfehlung:
    - `feature/us08-ec2-setup`
    - `feature/us09-k3s-install`
    - `feature/us20-ci-cd-deploy`
  - Nach Abschluss wird per Pull Request nach develop gemerged

- **gh-pages**
  - Enthält die generierte GitHub Pages Ausgabe
  - Wird ausschliesslich durch den GitHub Actions Workflow aktualisiert
  - Keine manuelle Bearbeitung



## Merge Flow

- **Feature Umsetzung**
  - feature branch wird von develop erstellt
  - Pull Request von feature nach develop
  - Review und Checks, dann Merge

- **Sprint Stand oder Release**
  - Pull Request von develop nach main
  - main wird nur gemerged, wenn der Stand stabil ist

## Regeln und Schutz

- **main**
  - Force Push blockiert
  - Direkte Pushes blockiert, Merge nur über Pull Request
  - Status Checks müssen bestehen, falls Workflows definiert sind

- **develop**
  - Direkte Pushes erlaubt, aber bevorzugt über Pull Requests
  - Force Push blockiert, falls Regeln aktiv sind

- **gh-pages**
  - Branch ist geschützt
  - Updates erfolgen nur über den GitHub Actions Workflow
  - Keine manuellen Pushes

## Dokumentation und GitHub Pages
Die GitHub Pages Dokumentation wird aus dem Repository gebaut. Der Workflow wird nur ausgeführt, wenn relevante Dateien geändert wurden, zum Beispiel `docs` oder `mkdocs.yml`. Dadurch bleibt die Pages Ausgabe konsistent mit dem Stand auf main.

## Commit Konvention
Konvention: `type(scope): message`

Beispiele:
- **docs(pm):** add sprint 1 review and retrospective
- **docs(arch):** add target architecture overview
- **ci(pages):** enable docs deployment workflow
- **ci(cd):** deploy to k3s on push to main
- **feat(k8s):** add deployment and service manifests
- **fix(ci):** correct ghcr image tag
- **chore:** update dependencies

## Definition of Done für Branching Doku
- **Dokumentation ist committed und gepusht**
- **Merge Flow ist nachvollziehbar beschrieben**
- **Branch Regeln sind dokumentiert**
- **Issue US05 ist im Board auf Done**


# Technische Dokumentation (fortlaufend)

Repository: https://github.com/Cancani/geraeteausleihe-sem4  
GitHub Pages: https://cancani.com/geraeteausleihe-sem4/  

AWS Region: us east 1  
EC2 Public IP: 13.223.28.53  
Externer Endpoint: http://geraeteausleihe.13.223.28.53.nip.io  

---

## Ziel dieser technischen Dokumentation
Diese technische Dokumentation beschreibt den vollständigen Stand bis Ende Sprint 2. Die Dokumentation wird sich im Laufe des Projekts ständig verändern.
Fokus ist ein lauffähiger End to End Betrieb inklusive Service Code, Tests, Containerisierung, GHCR, AWS EC2, K3s, Kubernetes Ressourcen, GitHub Actions CI und CD sowie nachvollziehbaren Nachweisen.

Alle Aussagen sind so strukturiert, dass sie mit Commands, Outputs oder Screenshots belegt werden können.

---

# Systemübersicht

## Zielbild
```mermaid
flowchart TD
  subgraph Clients
    PA[PowerApps Client]
    BR[Browser]
  end

  subgraph GitHub
    REPO[Repository]
    ACT[GitHub Actions]
    GHCR[GitHub Container Registry]
    PAGES[GitHub Pages]
  end

  subgraph AWS
    EC2[AWS EC2 Instanz]
    K3S[K3s Cluster]
    TRF[Traefik Ingress]
    SVC[Flask Microservice geraeteausleihe]
  end

  PA -->|HTTP| TRF
  BR -->|HTTP| TRF
  TRF -->|Service Routing| SVC

  REPO --> ACT
  ACT -->|Build und Push| GHCR
  ACT -->|kubectl apply, set image| K3S
  GHCR -->|pull image| SVC

  REPO -->|MkDocs Build| PAGES
```

## Komponenten
| Komponente | Aufgabe | Hinweis |
| --- | --- | --- |
| PowerApps | Konsument des Microservice | Ruft den PDF Endpoint auf |
| Flask Microservice | REST API und PDF Ausgabe | Läuft containerisiert |
| GitHub Actions | Build, Push, Deploy und Docs | CI CD und GitHub Pages |
| GHCR | Container Images | Versionierung über Tags |
| AWS EC2 | Compute Basis | K3s läuft auf der Instanz |
| K3s | Kubernetes Distribution | Single Node Betrieb |
| Traefik Ingress | HTTP Ingress Controller | Routing auf Service |
| nip.io | DNS Convenience | Hostname ohne eigene DNS Zone |

## Schnittstellen und Endpunkte
| Endpoint | Methode | Zweck | Erwartung |
| --- | --- | --- | --- |
| `/` | GET | Basis Response | Text Response |
| `/healthz` | GET | Health Check | 200 OK mit JSON |
| `/pdf` | GET | PDF Ausgabe für PowerApps | PDF Response mit Content Disposition Attachment |

Externe Verifikation:
```bash
curl -i http://geraeteausleihe.13.223.28.53.nip.io/
curl -i http://geraeteausleihe.13.223.28.53.nip.io/healthz
curl -I "http://geraeteausleihe.13.223.28.53.nip.io/pdf?borrower=Test&device=Notebook&staff=TBZ"
```


![Curl Commands Endpoints](./screenshots/curl_commands.png)

---

# Repository Struktur

## Struktur
Wichtige Bereiche im Repository:

- `service/` Python Flask App
- `service/test_api.py` Pytest Tests
- `Dockerfile` Container Image Build
- `.github/workflows/` Workflows für CI, CD, PR Checks, Docs
- `k3s/` Kubernetes Manifeste (Namespace, Deployment, Service, Ingress)
- `docs/` MkDocs Seiten
- `mkdocs.yml` MkDocs Konfiguration

---

# Python Flask Service

## Zweck
Der Service stellt eine REST API bereit und erzeugt PDFs für die Geräteausleihe. Nutzung erfolgt durch PowerApps oder Browser. Der Service läuft lokal und produktionsnah im Container mit gunicorn.

## Konfiguration
Umgebungsvariable:
- `PORT` wird im Kubernetes Deployment auf `8080` gesetzt.

## Ausführung Lokal

```bash
cd service
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```


## Endpoints

### GET /
Erwartung:
- HTTP 200
- Text Response


```bash
curl -i http://localhost:8080/
```

![GET / Lokal](./screenshots/GET_Lokal.png)

### GET /healthz
Erwartung:
- HTTP 200
- JSON mit status und timestamp


```bash
curl -i http://localhost:8080/healthz
```

![GET Healthz](./screenshots/get_healthz.png)

### GET /pdf
Erwartung:
- HTTP 200
- PDF Response
- Content Disposition Attachment


```bash
curl -I "http://localhost:8080/pdf?borrower=Test&device=Notebook&staff=IT"
```

![GET /PDF](./screenshots/get_pdf.png)

---

# Tests

## Ziel
Automatisierte Tests prüfen die wichtigsten API Endpoints. Fokus liegt auf Response Codes, Content Type und Basis Inhalt.

## Besonderheiten und Lösung
WeasyPrint benötigt System Libraries. Lokale Tests auf Windows waren dadurch aufwendig. Lösung war, die Tests im Docker Container auszuführen.

Weitere Besonderheit:
- Bytes Assertions mit Umlauten führten zu Syntax Problemen
- Lösung: `response.get_data(as_text=True)`

## Testausführung im Container
```bash
docker build -t geraeteausleihe:test .
docker run --rm geraeteausleihe:test sh -c "pip install pytest && cd /srv && pytest -q -p no:cacheprovider test_api.py"
```

Erwartung:
- Alle Tests erfolgreich,  `5 passed`

![Pytest](./screenshots/Pytest.png)

---

# Containerisierung

## Dockerfile Ziel
Das Dockerfile baut ein Image auf Basis `python:3.11-slim`. Es installiert WeasyPrint Abhängigkeiten (pango, cairo, gdk pixbuf und weitere) und startet den Service mit gunicorn.

## Lokaler Build und Run
Build:
```bash
docker build -t geraeteausleihe:local .
```

Test im Container:
```bash
docker run --rm -p 8080:8080 geraeteausleihe:local
```

![Docker Container Run](./screenshots/Container_Run.png)

Verifikation:
```bash
curl -i http://localhost:8080/healthz
```

![Verifikation Container](./screenshots/Lokale_Endpoints.png)

---

# GitHub Container Registry GHCR

## Naming und Tagging
Tags:
- `latest`
- Commit SHA, zum Beispiel `115b431876813ef6867c26de7e7cf6df0c533809`


![GHCR Tags](./screenshots/ghcr_package_latest.png)

---

# AWS Setup

## EC2 Instanz
Konfiguration:
- Region: us east 1
- OS: Ubuntu 22.04
- Public IP: 13.223.28.53
- Elastic IP verwendet

![EC2 Instanz](./screenshots/EC2_Instanz.png
)

## Security Group
Inbound Rules:
- 22 SSH
- 80 HTTP
- optional 443 später

---

# K3s Installation und Cluster Zugriff

## K3s Installation
K3s wurde manuell installiert. Traefik ist standardmässig aktiv.

Nachweise:
```bash
sudo systemctl status k3s
kubectl get nodes
kubectl get pods -A
```

![k3s_status](./screenshots/k3s_status.png)
![kubectl get nodes](./screenshots/get_nodes.png)

---

# Kubernetes Ressourcen

## Übersicht
Die App wird über deklarative YAML Manifeste betrieben.

| Manifest | Ressource | Zweck |
| --- | --- | --- |
| `namespace.yaml` | Namespace | Logische Trennung |
| `deployment.yaml` | Deployment | Pods, Rolling Update, Probes |
| `service.yaml` | Service ClusterIP | Interner Zugriff |
| `ingress.yaml` | Ingress | Externer Zugriff über Traefik |

## Namespace
Anwendung:
```bash
kubectl apply -f namespace.yaml
```
![Namescpace](./screenshots/Namespace.png)

## Deployment
Deployment enthält:
- 1 Replica
- containerPort 8080
- env PORT 8080
- readinessProbe auf /healthz
- livenessProbe auf /healthz
- imagePullPolicy Always

![Deployment K3S](./screenshots/deployment_k3s.png)

## Service

![k3s Service](./screenshots/k3s_service.png)

## Ingress
Ingress Host:
- `geraeteausleihe.13.223.28.53.nip.io`

![k3s Ingress](./screenshots/k3s_ingress.png)

---

# GitHub Actions

## Workflow Übersicht
Bis Ende Sprint 2 sind folgende Workflows im Einsatz:

- container-build.yml: Build und Push nach GHCR
- deploy-k3s.yml: Deployment auf EC2 und Rollout Check
- pr-checks.yml: Build, Lint, Tests für PR nach main
- docs-pages.yml: MkDocs Build und Deploy nach gh-pages bei Docs Änderungen auf main

![Workflows](./screenshots/GH_Actions.png)

## Benötigte Secrets
Erforderlich:
- EC2_HOST
- EC2_USER
- EC2_SSH_KEY

![Github Actions Secrets](./screenshots/GH_Secrets.png)

---

# Deployment Verifikation

## Kubernetes Status
```bash
kubectl -n geraeteausleihe get all
kubectl -n geraeteausleihe get ingress
```
![Kubernetes Status](./screenshots/Kubernetes_Status.png)


## Externe Requests
```bash
curl -f http://geraeteausleihe.13.223.28.53.nip.io/healthz
curl -I "http://geraeteausleihe.13.223.28.53.nip.io/pdf?borrower=Test&device=Notebook&staff=IT"
```


![Externe Requests](./screenshots/Externe_Requests.png)

---

# PowerApps Integration

## Launch auf PDF Endpoint
PowerApps ruft `/pdf` über Launch auf und nutzt EncodeUrl für borrower, device und staff.

![Heruntergeladene PDF](./screenshots/PowerApps.png)

**Ausgegebene Quittung**

![Screenshot PDF](./screenshots/ScreenshotQuittung.png)

---

# Status bisher
Ende Sprint 2 ist der Service in K3s auf AWS EC2 produktionsnah lauffähig und extern erreichbar.

Checkliste:
- Namespace `geraeteausleihe` existiert
- Deployment läuft und Pods sind Ready
- Service und Ingress sind vorhanden
- Endpoint `http://geraeteausleihe.13.223.28.53.nip.io` liefert /healthz und /pdf
- GHCR enthält Tags latest und Commit SHA
- CI Build und CD Deploy sind als Workflows dokumentiert
- Tests laufen reproduzierbar im Container

Start Umsetzung Sprint 3

---
