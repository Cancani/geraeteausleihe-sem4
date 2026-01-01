# Projektmanagement

Diese Seite beschreibt das Vorgehen, die Regeln und die Artefakte der Semesterarbeit.

| Bereich | Link |
| --- | --- |
| Repository | https://github.com/Cancani/geraeteausleihe-sem4 |
| GitHub Projects Board | https://github.com/users/Cancani/projects/3/views/1 |
| GitHub Pages | https://cancani.com/geraeteausleihe-sem4 |

---

## Zweck und Umfang

| Punkt | Beschreibung |
| --- | --- |
| Ziel | Transparente, nachvollziehbare Umsetzung der Semesterarbeit mit klaren Nachweisen |
| Scope | Projektmanagement, Sprint Planung, Reviews, Risiko Management, Doku Struktur |
| Tracking | GitHub Issues und GitHub Projects (Kanban) |
| Nachweise | Markdown Dokumentation, Screenshots, Workflow Runs, Logs, Kubernetes Status |

---

## Vorgehensmodell

Die Arbeit folgt einer sprintbasierten Arbeitsweise mit Kanban Elementen.

| Element | Umsetzung |
| --- | --- |
| Backlog | GitHub Issues (User Stories und Tasks) |
| Planung | Milestones pro Sprint, Priorisierung über Must Should Could |
| Umsetzung | Kanban Board mit klaren Status Spalten und WIP Limit |
| Review | Sprint Review als Dokumentation in `docs/sprints.md` mit Nachweisen |
| Retrospektive | Kurze Reflexion pro Sprint mit konkreten Verbesserungen |
| Dokumentation | MkDocs Material, Publikation über GitHub Pages |

---

## Rollen und Verantwortlichkeiten

| Rolle | Verantwortlich | Aufgaben |
| --- | --- | --- |
| Studierender | Efekan Demirci | Umsetzung, Dokumentation, Nachweise, Abgabe |
| Experte Projektmanagement | Dozent PRJ | Feedback zu Planung, Vorgehen, Risiko Management, Struktur |
| Experte Fachliches Modul | Dozent CNC | Feedback zu Technik, Architektur, Umsetzung, Betriebsaspekten |

---

## Tools und Artefakte

| Tool oder Artefakt | Zweck | Beispiele |
| --- | --- | --- |
| GitHub Repository | Versionierung, Code, Manifeste, Docs | Branches, Pull Requests, Releases |
| GitHub Projects | Kanban Board und Sprint Übersicht | Backlog, Ready, In Progress, Review, Done |
| GitHub Actions | CI CD und Dokumentations Deployment | Build, Push, Deploy, Pages |
| GHCR | Container Registry | Image Tags, Commit SHA |
| AWS EC2 | Laufzeit Umgebung | K3s Node, Traefik Ingress |
| MkDocs Material | Dokumentation | `docs/*.md`, Screenshots, Mermaid Diagramme |

---

## Kanban Setup und Regeln

| Spalte | Zweck | Eintrittskriterium | Austrittskriterium |
| --- | --- | --- | --- |
| Backlog | Sammlung aller Themen | Ticket ist erfasst | Ticket ist priorisiert |
| Ready | Bereit für Umsetzung | Definition of Ready erfüllt | Umsetzung gestartet |
| In Progress | Aktive Bearbeitung | Ticket ist zugewiesen | Umsetzung fertig, Self Check |
| Review | Review und Nachweise | Nachweise vorhanden | Definition of Done erfüllt |
| Done | Abschluss | Review abgeschlossen | Ticket ist abgeschlossen |

Empfohlene Regel
- WIP Limit für In Progress: Zielwert 2

---

## Ticket Standard und Vorlagen

### Ticket Struktur

| Feld | Inhalt |
| --- | --- |
| Titel | Kurzer präziser Titel, z. B. `US12: GHCR Push verifizieren` |
| Kontext | Warum ist das nötig |
| User Story | Als Rolle möchte ich Ziel, damit Nutzen |
| Akzeptanzkriterien | Messbar und abhakbar |
| Nachweis | Link, Screenshot, Logauszug, Workflow Run |
| Labels | Priorität, Bereich, Typ |

### Definition of Ready

| Check | Beschreibung |
| --- | --- |
| Ziel ist klar | Ticket beschreibt Ergebnis und Nutzen |
| Akzeptanzkriterien vorhanden | Kriterien sind messbar und abhakbar |
| Aufwand grob einschätzbar | Ticket ist nicht zu gross oder unklar |
| Nachweis definiert | Es ist klar, wie das Ergebnis belegt wird |

### Definition of Done

| Check | Beschreibung |
| --- | --- |
| 1 | Code oder Doku ist committed und gepusht |
| 2 | Akzeptanzkriterien sind abgehakt |
| 3 | Nachweis ist in docs abgelegt, Screenshot oder Logauszug |
| 4 | Issue ist im Board korrekt verschoben |

---

## Schätzung und Planung

| Grösse | Beschreibung | Beispiel |
| --- | --- | --- |
| S | Kurze Aufgabe, unter 1 Stunde | Doku Abschnitt ergänzen |
| M | Mittlere Aufgabe, 1 bis 3 Stunden | Workflow Trigger anpassen |
| L | Grössere Aufgabe, über 3 Stunden | K3s Setup und Ingress testen |

---

## Labels

| Kategorie | Labels (Beispiele) |
| --- | --- |
| Priorität | Must, Should, Could |
| Typ | Story, Task, Bug |
| Bereich | PM, Docs, Repo, Pages, AWS, K3s, Docker, Kubernetes, CI, Security, Testing |

---

## Milestones und Sprints

| Milestone | Fällig (geplant) | Inhalt |
| --- | --- | --- |
| Sprint 1 Projektstart und Planung | 05.01.2026 | Board, Labels, Milestones, Doku Struktur, Backlog, erste Reviews |
| Sprint 2 K3s Cluster und erster Deploy | 12.01.2026 | EC2, K3s Installation, Kubernetes Manifeste, Ingress, Probes |
| Sprint 3 CI CD Build Push Deploy | 19.01.2026 | GitHub Actions, GHCR, automatisches Deployment nach K3s |
| Abgabe und Doku fertig | 28.01.2026 | Dokumentation final, Demo Ablauf, Endkontrolle, Abgabe Links |


---

## Branching und Merge Flow

| Branch | Zweck | Regel |
| --- | --- | --- |
| develop | Arbeitsbranch | Feature Arbeit, regelmässige Commits |
| main | Stabile Version | Nur geprüfte Änderungen via Pull Request |
| gh pages | GitHub Pages Deployment | Wird durch Workflow befüllt |

Ablauf
- Entwicklung erfolgt auf `develop`
- Pull Request von `develop` nach `main`
- Merge nur, wenn Build und Checks erfolgreich sind
- Deploy Pipeline läuft bei Push auf `main`

---

## Wechsel auf GitHub, GitHub Pages und GitHub Projects

| Aspekt | Entscheidung | Nutzen |
| --- | --- | --- |
| Versionsverwaltung | GitHub Repository als zentrale Quelle | Einheitlicher Workflow, Pull Requests, Actions |
| Dokumentation | GitHub Pages via MkDocs Material | Saubere Doku Struktur und öffentliche Nachweise |
| Projektmanagement | GitHub Projects als Kanban | Backlog, Sprints, Status und Nachvollziehbarkeit |

---

## Backlog und User Stories

Die User Stories und Tasks wurden als Issues definiert und automatisiert erstellt. Grundlage sind die Skripte in `create_issues.ps1` und `create_issues_rest.ps1`.

### Sprint 1 Projektstart und Planung

| US | Titel | Typ | Priorität | Labels | Akzeptanzkriterien |
| --- | --- | --- | --- | --- | --- |
| US01 | Kanban Board finalisieren | Story | Must | PM | - Spalten Backlog, Ready, In Progress, Review, Done sind vorhanden<br>- WIP Limit für In Progress ist dokumentiert, Zielwert 2<br>- Mindestens 10 Issues sind dem Board hinzugefügt |
| US02 | Labels anlegen | Task | Must | PM, Repo | - Must, Should, Could sind vorhanden<br>- PM, Docs, Repo, Pages, AWS, K3s, Docker, Kubernetes, CI, Security, Testing sind vorhanden<br>- Story, Task, Bug sind vorhanden |
| US03 | Milestones anlegen | Task | Must | PM, Repo | - Sprint 1, Sprint 2, Sprint 3, Abgabe sind angelegt<br>- Due Dates sind gesetzt<br>- Beschreibungen sind gesetzt |
| US04 | Issue Template einrichten | Task | Should | PM, Repo | - Template existiert in .github/ISSUE_TEMPLATE<br>- Akzeptanzkriterien sind als Checkboxen im Template vorhanden<br>- DoD ist als Checkboxen im Template vorhanden |
| US05 | Branching Strategie dokumentieren | Story | Should | Docs, Repo | - Branches main, develop, feature, gh pages sind beschrieben<br>- Merge Flow ist beschrieben<br>- Branch Rulesets sind kurz dokumentiert |
| US06 | Sprint 1 Review und Retro dokumentieren | Story | Must | Docs, PM | - Sprint Goal ist dokumentiert<br>- Ergebnis ist dokumentiert, Repo, Board, Pages als Nachweis<br>- Retro enthält gut, schlecht, verbessern |
| US07 | Architektur Zielbild skizzieren | Story | Should | Docs, Kubernetes | - Komponenten sind beschrieben, GitHub Actions, GHCR, EC2, K3s, Ingress<br>- Datenfluss Push bis Deploy ist beschrieben<br>- Entscheide sind dokumentiert, kein Monitoring |


### Sprint 2 K3s Cluster und erster Deploy

| US | Titel | Typ | Priorität | Labels | Akzeptanzkriterien |
| --- | --- | --- | --- | --- | --- |
| US08 | EC2 Instanz vorbereiten | Story | Must | AWS, K3s | - EC2 Instanz läuft<br>- SSH Zugriff von meiner IP funktioniert<br>- HTTP und HTTPS sind offen für Ingress Tests |
| US09 | K3s auf EC2 installieren | Story | Must | K3s, Kubernetes | - K3s läuft als Service<br>- kubectl get nodes zeigt Node Ready<br>- kubeconfig Zugriff von meinem Client funktioniert |
| US10 | Namespace und Basis Ressourcen erstellen | Task | Should | Kubernetes | - Namespace manifest existiert<br>- Ressourcen sind applied und sichtbar |
| US11 | Dockerfile finalisieren | Story | Must | Docker | - docker build ist erfolgreich<br>- Container startet lokal<br>- Service Endpoint ist erreichbar |
| US12 | GHCR Push verifizieren | Task | Must | Docker, Repo | - Image ist in GHCR sichtbar<br>- Tagging Konzept ist definiert, latest plus commit sha<br>- Pull von GHCR ist getestet |
| US13 | Kubernetes Deployment manifest erstellen | Story | Must | Kubernetes | - deployment yaml existiert<br>- Pod startet im Cluster<br>- Replica Count ist definiert |
| US14 | Kubernetes Service manifest erstellen | Story | Must | Kubernetes | - service yaml existiert<br>- Service zeigt korrekt auf Pods<br>- Ports sind korrekt |
| US15 | Ingress konfigurieren | Story | Should | Kubernetes, K3s | - ingress yaml existiert<br>- Zugriff über Public IP oder Domain funktioniert<br>- Routing auf Service funktioniert |
| US16 | Readiness und Liveness Probes definieren | Story | Should | Kubernetes, Testing | - Probes sind im Deployment gesetzt<br>- Pod reagiert korrekt bei Fehler<br>- Probe Endpunkte sind dokumentiert |
| US17 | Sprint 2 Review und Retro dokumentieren | Story | Must | Docs, PM | - Screenshots kubectl get pods svc ingress vorhanden<br>- Review Text mit Ergebnis<br>- Retro mit Verbesserungen für Sprint 3 |


### Sprint 3 CI CD Build Push Deploy

| US | Titel | Typ | Priorität | Labels | Akzeptanzkriterien |
| --- | --- | --- | --- | --- | --- |
| US18 | GitHub Actions Build und Push nach GHCR | Story | Must | CI, Docker | - Workflow startet bei Push auf main<br>- Image wird gebaut<br>- Image wird nach GHCR gepusht mit commit sha Tag |
| US19 | Secrets für GHCR und Cluster Zugriff einrichten | Story | Must | Security, CI | - GHCR Auth funktioniert mit GITHUB_TOKEN oder PAT<br>- kubeconfig oder token ist als Secret vorhanden<br>- Keine Secrets im Repository |
| US20 | CD Workflow deployt nach K3s | Story | Must | CI, Kubernetes | - Workflow wendet Manifeste an<br>- Deployment aktualisiert das Image auf neuen Tag<br>- Rollout Status ist dokumentiert |
| US21 | Tagging Strategie dokumentieren und anwenden | Task | Should | CI, Repo | - Image Tag ist commit sha<br>- Deployment referenziert den Tag<br>- Doku beschreibt das Konzept |
| US22 | Pipeline Testlauf dokumentieren | Story | Must | Docs, Testing | - Screenshot Actions Run vorhanden<br>- Vorher nachher Version dokumentiert<br>- Debug Vorgehen bei Fehler beschrieben |
| US23 | Sprint 3 Review und Retro dokumentieren | Story | Must | Docs, PM | - Review Text mit End to End Ablauf<br>- Retro mit gut, schlecht, verbessern<br>- Offene Punkte für Abgabe sind erfasst |


### Abgabe und Doku fertig

| US | Titel | Typ | Priorität | Labels | Akzeptanzkriterien |
| --- | --- | --- | --- | --- | --- |
| US24 | Dokumentation finalisieren und strukturieren | Story | Must | Docs, Pages | - Projektmanagement Kapitel vollständig<br>- Sprints Kapitel vollständig<br>- Architektur Kapitel vollständig<br>- Links zu Repo, Board, Pages funktionieren |
| US25 | Demo Ablauf definieren | Story | Should | Docs, PM | - Schrittfolge für Demo dokumentiert<br>- Live Nachweise, Actions, GHCR, kubectl, Ingress<br>- Fallback Plan definiert |
| US26 | Endkontrolle gegen Anforderungen | Story | Must | PM, Testing | - Kubernetes läuft, Deploy funktioniert<br>- CI CD läuft, Build Push Deploy erfolgreich<br>- Board ist aktuell, Milestones sind konsistent |
| US27 | Abgabe Links und Paket bereitstellen | Story | Must | Docs, PM | - Repo Link, Board Link, Pages Link gesammelt<br>- Letzte Sprint Reviews sind vorhanden<br>- main enthält den finalen Stand |



---

## Nachweise für Sprint Reviews

| Nachweis | Wo | Beispiel |
| --- | --- | --- |
| Workflow Runs | GitHub Actions | Build und Deploy Logs |
| Container Images | GHCR | Tags `latest` und Commit SHA |
| Kubernetes Status | EC2 Shell | `kubectl get pods -n ...` |
| Ingress Erreichbarkeit | Browser oder curl | Endpoint über nip io |
| Screenshots | `docs/screenshots/` | Pipeline Run, Pods, Ingress |

---

## Risiken und Massnahmen

| Risiko | Auswirkung | Massnahme |
| --- | --- | --- |
| Deployment Fehler durch falsche Image Referenz | Service startet nicht | Image Name und Tag prüfen, Rollout Status kontrollieren |
| Cluster Zugriff aus CI schlägt fehl | Deploy nicht möglich | SSH Keys und Secrets prüfen, kubectl Zugriff verifizieren |
| Zeitdruck | Umfang nicht fertig | Must Tickets priorisieren, Scope begrenzen, Reviews laufend pflegen |
| Kosten AWS | Budgetüberschreitung | Kleine Instanz, Ressourcen Limits, Instanz abschalten wenn nicht benötigt |

