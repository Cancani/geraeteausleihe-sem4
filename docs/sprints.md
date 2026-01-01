# Sprints

!!! abstract "Kurzüberblick"
    - Sprint 1: Projektmanagement Grundlagen und Artefakte
    - Sprint 2: Technische Umsetzung von CI und CD bis Deployment
    - Nachweise: Screenshots und Links sind in den Sprint Abschnitten enthalten

## Sprint 1 - Review und Retrospektive

### 1. Ziel des Sprints
Ziel von Sprint 1 war der **Projektstart sowie der Aufbau der Projektmanagement-Grundlagen**.  
Der Fokus lag nicht auf technischer Umsetzung, sondern auf Struktur, Planung und Nachvollziehbarkeit gemäss agiler Methodik mit Kanban.

Der Sprint bildet die Basis für alle folgenden technischen Arbeiten.

---

### 2. Geplante Inhalte (Sprint Backlog)
Für Sprint 1 wurden folgende Themen definiert:

- **Aufsetzen eines Kanban Boards** mit klaren Spalten
- **Definition von Labels** zur Klassifizierung der Issues
- **Erstellung von Milestones** für Sprints und Abgabe
- **Erfassung aller User Stories** für das Gesamtprojekt
- **Dokumentation der Projektmanagement-Vorgehensweise**
- **Architektur Zielbild als konzeptionelle Grundlage**

---

### 3. Umsetzung im Sprint
Im Verlauf des Sprints wurden die geplanten Inhalte vollständig umgesetzt.

#### 3.1 Kanban Board
Das Kanban Board wurde in GitHub Projects erstellt und umfasst folgende Spalten:

- **Backlog**
- **Ready**
- **In Progress**
- **Review**
- **Done**

Zusätzlich wurde eine WIP-Regel definiert, um parallele Arbeit zu begrenzen.

![Kanban Board](./screenshots/prj/sprint1_kanban_board.png)

<small>Bild 1: Kanban Board</small>

---

#### 3.2 Issues und User Stories
Alle relevanten Aufgaben wurden als **User Stories (US01 bis US27)** in GitHub Issues erfasst.  
Jede User Story enthält:

- Beschreibung
- Akzeptanzkriterien als Checkboxen
- Definition of Done

Die Issues sind eindeutig benannt und den entsprechenden Milestones zugeordnet.

![alt text](./screenshots/prj/Sprint1_Issues.png)

<small>Bild 2: Issues</small>

---

#### 3.3 Labels
Zur besseren Strukturierung wurden Labels für folgende Bereiche angelegt:

- Projektmanagement
- Dokumentation
- AWS
- K3s
- Kubernetes
- CI/CD
- Security
- Testing
- Story und Task
- Must, Should, Could

Diese Labels werden in allen folgenden Sprints konseqünt verwendet.

![Labels](./screenshots/prj/sprint1_labels.png)

<small>Bild 3: Labels</small>

---

#### 3.4 Milestones
Es wurden Milestones für die einzelnen Projektphasen erstellt:

- Sprint 1 Projektstart und Planung
- Sprint 2 K3s Cluster und erster Deploy
- Sprint 3 CI/CD Build Push Deploy
- Abgabe und Dokumentation

Dadurch ist der Projektfortschritt jederzeit nachvollziehbar.

![Milestones](./screenshots/prj/Sprint1_Milestones.png)

<small>Bild 4: Milestones</small>

---

#### 3.5 Dokumentation
Die Projektdokumentation wurde strukturiert aufgebaut und über **GitHub Pages** veröffentlicht.  
Die Dokumentation umfasst unter anderem:

- Projektdefinition
- Projektmanagement
- Sprint Reviews
- Architektur Zielbild

https://cancani.com/geraeteausleihe-sem4/

---

### 4. Sprint Review (Ergebnisbewertung)

**Sprintziel erreicht:** Ja  

Alle geplanten Inhalte für Sprint 1 wurden umgesetzt.  
Die Projektorganisation ist nun sauber strukturiert, nachvollziehbar dokumentiert und bereit für die technische Umsetzung.

Besonders positiv ist die vollständige Erfassung aller User Stories bereits zu Projektbeginn.

---

### 5. Sprint Retrospektive

#### 5.1 Was lief gut
- Klare Strukturierung des Projekts von Anfang an
- Einheitliche User Stories mit Akzeptanzkriterien
- Kanban Board ermöglicht transparente Arbeitsweise
- Dokumentation ist früh vorhanden und versioniert

#### 5.2 Was war schwierig
- Einstieg in GitHub CLI und Automatisierung der Projektanlage
- Feinabstimmung von Milestones und deren Zuordnung
- Entscheidung für die geeignete Kubernetes Variante

#### 5.3 Verbesserungen für Sprint 2
- Technische Tasks noch granularer aufteilen
- Nachweise direkt während der Umsetzung sichern
- K3s Installation schrittweise dokumentieren

---

### 6. Ausblick auf Sprint 2
In Sprint 2 liegt der Fokus auf der **technischen Basis**:

- Bereitstellung einer AWS EC2 Instanz
- Installation und Konfiguration von K3s
- Erstes Deployment des Microservices
- Verifikation der Container Registry Anbindung

Damit wird der Übergang von Planung zu technischer Umsetzung vollzogen.

## Sprint 2 Review und Retrospektive

## 1 Ziel des Sprints
Ziel von Sprint 2 war der Aufbau der technischen Basis für den produktionsnahen Betrieb des Microservice auf AWS. Der Fokus lag auf einer lauffähigen Kubernetes Umgebung mit K3s, einem funktionierenden Container Build und Push nach GHCR sowie einem automatisierten Deployment per GitHub Actions.

## 2 Geplante Inhalte
Geplant waren folgende Themen gemäss Milestone Sprint 2 K3s Cluster und erster Deploy

- AWS EC2 Instanz bereitstellen und Netzwerkregeln konfigurieren
- K3s auf der EC2 Instanz installieren und verifizieren
- Kubernetes Namespace und Basis Ressourcen erstellen
- Kubernetes Manifeste für Deployment, Service und Ingress erstellen
- GitHub Actions Workflow für Build und Push nach GHCR erstellen
- GitHub Actions Workflow für Deploy nach K3s erstellen
- Smoke Tests durchführen und Endpunkte testen

## 3 Umsetzung im Sprint

### 3.1 AWS Setup
- EC2 Instanz wurde erstellt und als Deployment Ziel definiert
- Security Group wurde so konfiguriert, dass SSH und HTTP Zugriff möglich ist
- Der Microservice wird über Ingress via Port 80 bereitgestellt

Hinweis
Der aktülle Zugriff erfolgt über eine temporäre Domain via nip.io. Diese kann später durch eine echte Domain ersetzt werden.

### 3.2 K3s Installation
Die Installation von K3s wurde bewusst manüll durchgeführt, um die Umgebung zürst stabil zu testen. Eine Automatisierung mit Terraform oder Ansible ist möglich, wurde in diesem Sprint aber bewusst nicht umgesetzt.

Ergebnis
- K3s läuft auf der EC2 Instanz
- kubectl Zugriff ist eingerichtet
- Träfik ist als Ingress Controller verfügbar

### 3.3 Kubernetes Ressourcen
Es wurde ein eigener Namespace für die Applikation erstellt und die Basis Ressourcen wurden umgesetzt

- Namespace geräteausleihe
- Deployment für den Microservice
- Service als ClusterIP
- Ingress via Träfik

Der Ingress stellt den Service unter folgender Struktur bereit
- Host geräteausleihe.<Public IP>.nip.io
- Pfade für Health und PDF Generierung

### 3.4 Container Image Build und Push nach GHCR
Für das Container Build wurde ein GitHub Actions Workflow erstellt, der ein Docker Image baut und nach GHCR pusht.

Tagging Strategie
- latest für den aktüllen Stand
- Commit SHA Tag für reproduzierbare Releases

Wichtigste Erkenntnis
Ein falscher Image String führt in Kubernetes zu InvalidImageName. Das wurde behoben, indem der vollständige GHCR Pfad verwendet wird, inklusive Owner und Repository.

### 3.5 Deployment per GitHub Actions
Der Deploy Workflow übernimmt folgende Schritte

- Kubernetes Manifeste werden auf die EC2 Instanz kopiert
- kubectl apply wird im Namespace ausgeführt
- das Deployment Image wird auf den aktüllen Commit SHA Tag gesetzt
- Rollout Status wird überwacht

Damit ist eine Lieferung ohne manülles kubectl Setzen möglich, sobald die Workflows korrekt konfiguriert sind.

### 3.6 Verifikation und Smoke Tests
Erfolgreich verifiziert wurden

- Pod Status Running
- Deployment Ready
- Ingress Host erreichbar
- GET /healthz liefert Status 200 mit JSON
- GET /pdf liefert Status 200 und ein PDF als Download

## 4 Sprint Review

### 4.1 Sprintziel erreicht
Ja. Die Applikation läuft auf K3s innerhalb der EC2 Instanz, ist über Ingress erreichbar und kann PDFs generieren.

### 4.2 Lieferobjekte
- Lauffähige K3s Installation auf EC2
- Kubernetes Manifeste für Namespace, Deployment, Service, Ingress
- Build Workflow für GHCR
- Deploy Workflow für K3s
- Erfolgreiche Smoke Tests mit Health und PDF

### 4.3 Offene Punkte
- Workflow Trigger sauber eingrenzen, damit Docs Changes keinen Container Build auslösen
- Branching Prozess stabilisieren, damit Änderungen über Pull Requests laufen können
- Dokumentation der Pipeline Testläufe ergänzen

## 5 Sprint Retrospektive

### 5.1 Was lief gut
- Der produktionsnahe Betrieb auf K3s konnte erfolgreich hergestellt werden
- Der End to End Ablauf wurde mit echten Requests validiert
- Die Workflows sind grundsätzlich vorhanden und lauffähig

### 5.2 Was war schwierig
- Fehleranalyse bei InvalidImageName war zeitintensiv
- Konflikte zwischen main und develop Branch mussten nachträglich bereinigt werden
- Workflow Trigger und Pfad Filter waren anfangs zu breit definiert

### 5.3 Verbesserungen für den nächsten Sprint
- paths Filter in Workflows verwenden, damit Build Jobs nur bei Service Code laufen
- zusätzliche Checks nach Deploy integrieren, zum Beispiel ein curl Smoke Test gegen den Ingress Host

## 6 User Stories Status

### 6.1 Erledigt im Sprint 2
- US08 EC2 Instanz vorbereiten
- US09 K3s auf EC2 installieren
- US10 Namespace und Basic Ressourcen erstellen

### 6.2 Technische Umsetzung abgeschlossen, Dokumentation oder Feinschliff noch offen
- US11 Dockerfile finalisieren
- US12 GHCR Push verifizieren
- US13 Kubernetes Deployment manifest erstellen
- US14 Kubernetes Service manifest erstellen
- US15 Ingress konfigurieren
- US16 Readiness und Liveness Probes definieren
- US18 GitHub Actions Build und Push nach GHCR
- US19 Secrets für GHCR und Cluster Zugriff einrichten
- US20 CD Workflow deploy nach K3s
- US21 Tagging Strategie dokumentieren und anwenden
- US22 Pipeline Testlauf dokumentieren

Hinweis
Falls einzelne Punkte bereits komplett erledigt sind, kann diese Liste direkt im Review an den aktüllen Stand der Issues angepasst werden.

## 7 Ausblick Sprint 3
In Sprint 3 liegt der Fokus auf Stabilisierung und Vertiefung

  Workflows sauber trennen und Trigger präzise definieren
- Dokumentation finalisieren und strukturieren
- Demo Ablauf definieren und Endkontrolle gegen Anforderungen durchführen
