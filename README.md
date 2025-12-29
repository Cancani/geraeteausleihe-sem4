# Geräteausleihe Microservice Sem4

Diese Dokumentation beschreibt die Semesterarbeit 4.  
Fokus ist Cloud Native Deployment auf AWS mit Kubernetes und GitHub Actions.

## Inhalte
- Projektmanagement
- Sprint Planung und Umsetzung
- Architektur und technische Entscheide


#
# geraeteausleihe-sem4


## Branching Strategie

Das Projekt verwendet eine einfache, aber klare Branching Strategie zur Trennung von Entwicklung, Stabilisierung und Dokumentationsauslieferung.

### Verwendete Branches

**main**  
Stabiler Hauptbranch. Enthält ausschliesslich geprüften Code und freigegebene Dokumentation.

**develop**  
Integrationsbranch für laufende Entwicklung während der Sprints.

**feature/**  
Kurzlebige Branches zur Umsetzung einzelner User Stories.

**gh-pages**  
Branch zur automatischen Auslieferung der Projektdokumentation via GitHub Pages.  
Dieser Branch wird ausschliesslich durch GitHub Actions befüllt und nicht manuell bearbeitet.

### Merge Flow

- feature → develop  
- develop → main  
- GitHub Actions → gh-pages

### Commit Konvention

Commits folgen dem Format  
`type(scope): kurze beschreibung`
