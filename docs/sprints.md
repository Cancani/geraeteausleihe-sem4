# Sprint 1 Review und Retro

## Meta
Sprint: 1  
Ort: GitHub Repository und GitHub Project Board  
Teilnehmende: Efekan Demirci  
Review Empfänger: Dozenten

## Sprint Ziel
Projektstart und Projektmanagement Setup in GitHub.
Dazu gehören Board Struktur, Labels, Milestones, initiale User Stories sowie eine Basis Dokumentation auf GitHub Pages.

## Was wurde umgesetzt
1. Labels wurden im Repository angelegt
2. Milestones fuer Sprint 1 bis Sprint 3 sowie Abschluss wurden angelegt
3. User Stories US01 bis US27 wurden als Issues erfasst und den Milestones zugeordnet
4. GitHub Pages Dokumentation ist aktiv und wird per Workflow bei Aenderungen an docs gebaut
5. Dokumentation Projektmanagement wurde erstellt

## Nachweise
1. [Link zu GitHub Issues Liste mit US01 bis US27 und Miulestones](https://github.com/Cancani/geraeteausleihe-sem4/issues)
2. [Project Board mit Spalten Backlog, Ready, In Progress, Review, Done](https://github.com/users/Cancani/projects/3)
3. [Beispiel GitHub Actions Lauf für Docs Deployment](https://github.com/Cancani/geraeteausleihe-sem4/actions/runs/20572615824)
4. [Link zur GitHub Pages Seite](https://cancani.com/geraeteausleihe-sem4/)


Ablageort der Nachweise:
docs assets oder docs images Ordner, Dateinamen mit sprint1 prefix

## Offene Punkte aus Sprint 1
1. Board WIP Regel im Project sichtbar dokumentieren
2. Sprint Review und Retro als wiederholbares Template festlegen
3. Architektur Zielbild finalisieren und in Doku verlinken

## Sprint Retro

### Was lief gut
1. GitHub CLI hat die initiale Projektstruktur sehr schnell aufgebaut
2. Issues sind einheitlich mit Akzeptanzkriterien und Definition of Done aufgebaut
3. GitHub Pages Build funktioniert stabil bei Dokumentations Aenderungen

### Was war schwierig
1. Unterschiedliche CLI Flags zwischen gh api und anderen gh Befehlen
2. Milestone Zuordnung musste nachgebessert werden
3. Klarer Startpunkt im Board musste erst definiert werden

### Verbesserungen für Sprint 2
1. Vor jedem groesseren Schritt kurze Checkliste pflegen
2. K3s Setup in kleine Schritte teilen und je Schritt einen Nachweis sichern
3. Secrets und Zugriffe frueh testen, bevor CI CD fertig gebaut wird

## Beschluss für Sprint 2
Priorit$t ist ein lauff$higer K3s Cluster auf EC2 mit erstem Deploy des Services.
