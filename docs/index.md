# Geräteausleihe Microservice Semesterarbeit 4

!!! abstract "Kurzüberblick"
    - Ziel: Cloud Native Betrieb des Microservice aus Semesterarbeit 3
    - Plattform: AWS EC2 mit K3s, Deployment via Kubernetes Manifeste
    - Automation: CI und CD via GitHub Actions, Container Images via GHCR
    - Dokumentation: MkDocs Material auf GitHub Pages

<div class="grid cards" markdown>

-   ## Schnellzugriff
    [Repository öffnen](https://github.com/Cancani/geraeteausleihe-sem4){ .md-button .md-button--primary }

    [Kanban Board](https://github.com/users/Cancani/projects/3/views/1){ .md-button }

    [Dokumentation](https://cancani.com/geraeteausleihe-sem4/){ .md-button }

-   ## Technischer Stack
    - Python und Flask
    - Docker und GHCR
    - GitHub Actions für CI und CD
    - AWS EC2 mit K3s
    - Kubernetes: Namespace, Deployment, Service, Ingress
    - Traefik Ingress, Host via `nip.io`

</div>

## Inhalt dieser Dokumentation

- Projektmanagement (Vorgehen, Rollen, Board Regeln)
- Sprints (Review und Retrospektiven, Nachweise)
- Architektur (Zielbild, Komponenten, Datenfluss)
- Technische Umsetzung (CI und CD, Kubernetes Ressourcen, Lessons Learned)

## Ergebnis in einem Satz

Der Microservice wird als Container Image gebaut, in GHCR publiziert und automatisch auf ein K3s Cluster in AWS ausgerollt, inklusive Ingress Endpoint und begleitender Dokumentation.
