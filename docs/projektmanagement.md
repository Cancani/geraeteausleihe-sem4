# Projektmanagement

!!! abstract "Kurzüberblick"
    - Planung und Nachvollziehbarkeit über GitHub Projects (Kanban)
    - Arbeitspakete als Issues mit Labels und Akzeptanzkriterien
    - Klare Definition of Ready und Definition of Done

## Zweck und Umfang
Dieses Dokument beschreibt die organisatorische Umsetzung der Semesterarbeit 4. Planung, Umsetzung, Nachweise und Dokumentation werden zentral im öffentlichen GitHub Repository geführt.

Repository
https://github.com/Cancani/geraeteausleihe-sem4

Kanban Board
https://github.com/users/Cancani/projects/3/views/1

Dokumentation
https://cancani.com/geraeteausleihe-sem4/

Betrieb
Der Geräteausleihe Microservice läuft auf AWS in einem K3s Cluster auf einer EC2 Instanz. Container Images werden nach GHCR gepusht. Deployments erfolgen über GitHub Actions und kubectl auf die EC2 Instanz.


## Vorgehensmodell
Die Arbeit folgt einer sprintbasierten Arbeitsweise mit Kanban Elementen.

1. Backlog als GitHub Issues
2. Sprint Planung über Milestones
3. Umsetzung und Tracking im GitHub Project Board
4. Sprint Review und Sprint Retro als schriftlicher Nachweis pro Sprint in der Dokumentation


## Rollen und Verantwortlichkeiten
1. Projektleitung und Umsetzung
   1. Efekan Demirci
   2. Planung, Umsetzung, Betrieb, Tests, Dokumentation, Sprint Reviews
2. Dozent PRJ
   1. Corrado Parisi
   2. Feedback zu Projektmanagement, Kanban, Reviews, Nachweisführung
3. Dozent CNC
   1. Philip Stark
   2. Feedback zu Cloud Native Umsetzung, Architektur und Betrieb


## Tools und Artefakte
1. GitHub Repository
   1. Code, Dokumentation, Pull Requests, Issues, Milestones
2. GitHub Project Board
   1. Kanban Spalten, Status Tracking, WIP Regel
3. GitHub Actions
   1. Container Build und Push nach GHCR
   2. Deployment nach K3s auf EC2
   3. Pages Build für Dokumentation
4. GHCR
   1. Container Registry mit Tags latest und git sha
5. AWS EC2 und K3s
   1. Kubernetes Runtime für den Microservice


## Kanban Setup und Regeln
Spalten im Board

1. Backlog
2. Ready
3. In Progress
4. Review
5. Done

Arbeitsregeln

1. WIP Limit
   1. In Progress maximal 2 Tickets gleichzeitig
2. Definition of Ready
   1. Ein Ticket wird erst nach Ready verschoben, wenn Inhalt und Kriterien vollständig sind
3. Review
   1. Technische Kontrolle abgeschlossen
   2. Dokumentation aktualisiert
   3. Nachweise vorhanden
4. Done
   1. Akzeptanzkriterien abgehakt
   2. Definition of Done abgehakt
   3. Ticket im Board final verschoben

Dozentenfeedback, umgesetzt

1. Spalten In Progress und Done sind Pflichtbestandteil
2. Akzeptanzkriterien werden als Checkboxen gepflegt
3. Definition of Done wird als Checkboxen gepflegt und pro Ticket verwendet


## Ticket Standard und Vorlagen

### Ticket Struktur
1. User Story Satz im Format
   1. Als Rolle möchte ich Ziel, damit Nutzen
2. Kontext und Scope
3. Akzeptanzkriterien als Checkboxen
4. Definition of Done als Checkboxen
5. Labels und Milestone gesetzt

### Definition of Ready
Ein Ticket ist Ready, wenn

1. Beschreibung eindeutig ist
2. Akzeptanzkriterien existieren
3. Definition of Done existiert
4. Priorität Label gesetzt ist
5. Milestone gesetzt ist

### Definition of Done
Ein Ticket ist Done, wenn

1. Umsetzung ist committed und gepusht
2. Akzeptanzkriterien sind abgehakt
3. Nachweise sind dokumentiert, zum Beispiel Logs oder Screenshots
4. Ticket ist im Board auf Done verschoben


## Schätzung und Planung
Für die Grobplanung werden Story Points genutzt.

Skala
1, 2, 3, 5, 8

Orientierung
1 entspricht bis 30 Minuten
2 entspricht bis 1 Stunde
3 entspricht bis 2 Stunden
5 entspricht bis 4 Stunden
8 entspricht bis 1 Arbeitstag


## Labels
Ziel ist eine klare Filterung nach Typ, Bereich und Priorität.

1. Typ
   1. Story
   2. Task
   3. Bug
2. Bereich, Beispiele
   1. PM
   2. Docs
   3. CI
   4. CD
   5. Docker
   6. Kubernetes
   7. K3s
   8. AWS
   9. Security
   10. Testing
3. Priorität
   1. Must
   2. Should
   3. Could


## Milestones und Sprints
Pro Sprint existiert ein Milestone. Alle Tickets des Sprints werden dem Milestone zugeordnet.

1. Sprint 1 Projektstart und Planung
2. Sprint 2 K3s Cluster und erster Deploy
3. Sprint 3 CI CD Automatisierung
4. Abschluss Doku, Demo und Abgabe


## Branching und Merge Flow
Ziel ist ein stabiler main Branch für Demo und Abgabe. Entwicklung findet auf develop oder Feature Branches statt.

1. Feature Branch wird von develop erstellt
2. Pull Request von Feature nach develop
3. Pull Request von develop nach main für stabilen Stand
4. Workflows laufen auf Pull Requests und auf main gemäss Trigger Regeln


## Wechsel auf GitHub, GitHub Pages und GitHub Projects

### Entscheidung
Die Arbeit wurde auf GitHub zentralisiert, inklusive Repository, Dokumentation und Kanban Board.

### Gründe
1. Ein zentraler Ort für Code, Tickets, Reviews und Nachweise
2. Direkte Verknüpfung von Commits, Pull Requests, Issues und Workflows
3. Integration von Actions, GHCR und Pages reduziert Tool Wechsel
4. Öffentliche Nachweise sind für Dozenten direkt einsehbar


## Nachweise für Sprint Reviews
Empfohlene Nachweise, die pro Sprint in der Dokumentation verlinkt werden.

1. Screenshot vom Project Board mit Spalten und WIP Regel
2. Screenshot der Milestones Übersicht
3. Screenshot eines erfolgreichen Actions Runs für Build und Deploy
4. kubectl Ausgaben für Pods, Service und Ingress
5. GHCR Übersicht der Image Tags


## Risiken und Massnahmen
1. Deployment Fehler durch falsche Image Referenz
   1. Massnahme: Image Name und Tag im Workflow validieren, Rollout Status prüfen
2. Cluster Zugriff aus CI schlägt fehl
   1. Massnahme: SSH Keys und Secrets prüfen, kubectl Zugriff auf EC2 verifizieren
3. Zeitdruck
   1. Massnahme: Must Tickets priorisieren, Scope begrenzen, Reviews laufend pflegen
4. Kosten AWS
   1. Massnahme: Kleine Instanz, Ressourcen Limits, Abschalten wenn nicht benötigt
