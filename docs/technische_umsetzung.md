# Technische Umsetzung

## Kontext und Ziel
Ausgangslage war ein bestehender Python Flask Microservice aus Semesterarbeit 3. Ziel war, den Service so vorzubereiten, dass er spaeter Cloud Native betrieben werden kann, inklusive Containerisierung, reproduzierbaren Tests, Kubernetes Manifeste und GitHub Actions Checks.

## Repository Struktur
Die bestehende MkDocs Dokumentation unter `docs/` blieb bestehen. Fuer die technische Umsetzung kamen drei Bereiche dazu:

1. `service/` fuer den Microservice Code
2. `k8s/` fuer Kubernetes Manifeste
3. `.github/workflows/` fuer GitHub Actions

Beispiel Struktur:

```text
.github/workflows/
docs/
k8s/
service/
Dockerfile
.dockerignore
mkdocs.yml
README.md
```

## Branching Vorgehen
Es wurde mit drei Branches gearbeitet:

1. `develop` fuer die laufende Umsetzung
2. `main` als stabiler Stand
3. `gh-pages` ausschliesslich fuer den generierten GitHub Pages Output

Die Umsetzung erfolgte auf `develop`. Wenn alles funktioniert, wird ein Pull Request von `develop` nach `main` erstellt.

## Lokale Vorbereitung
### Virtuelle Umgebung
Fuer lokale Tests wurde eine virtuelle Umgebung eingerichtet:

```bash
python -m venv .venv
source .venv/Scripts/activate
python -m pip install --upgrade pip
pip install -r service/requirements.txt
```

### Typischer Fehler und Loesung
Beim Start trat ein Import Fehler auf, weil `pytz` fehlte. Loesung war das Installieren der Dependencies aus `service/requirements.txt`.

## Microservice Start und Funktionstest
Der Service wurde lokal gestartet und mit Curl getestet.

### Service starten
```bash
cd service
python run.py
```

### Root Endpoint testen
```bash
curl http://localhost:8080/
```

Erwartet war eine Text Antwort.

### PDF Endpoint testen
```bash
curl -I "http://localhost:8080/pdf?borrower=Test&device=Notebook"
```

Erwartet war HTTP 200 und `Content-Type: application/pdf` sowie ein Attachment Header.

### Health Endpoints testen
```bash
curl -i http://localhost:8080/healthz
curl -i http://localhost:8080/health
```

Erwartet war HTTP 200 und ein JSON Payload mit `status` gleich `healthy`.

## Tests mit Pytest
### Problem 1 Syntax Fehler durch Bytes Literal
Beim ersten Test Lauf trat ein Syntax Fehler auf, weil ein Bytes Literal nicht ASCII Zeichen enthielt. Ursache war ein Assert mit `b"..."` und Sonderzeichen.

Loesung war, den Response Body als Text zu lesen und als String zu vergleichen:

```python
body = response.get_data(as_text=True)
assert "Geraeteausleihe Microservice is running" in body
```

### Problem 2 WeasyPrint unter Windows
Beim Import von WeasyPrint trat unter Windows ein Fehler auf, weil externe Libraries wie gobject, pango und cairo fehlten. Das ist ein bekanntes Verhalten bei nativer Windows Ausfuehrung.

Loesung war, Tests in der Container Umgebung auszufuehren. Diese Umgebung entspricht spaeter dem Betrieb auf Linux.

## Container Build und Tests im Container
### Image bauen
```bash
docker build -t geraeteausleihe:test .
```

### Problem pytest nicht vorhanden
Beim ersten Versuch fehlte `pytest` im Container. Loesung war, pytest beim Test Run zu installieren.

### Tests im Container ausfuehren
Da der Dockerfile den Ordner `service/` nach `/srv/` kopiert, liegt die Test Datei im Container unter `/srv/test_api.py`.

```bash
docker run --rm geraeteausleihe:test sh -c "pip install pytest && cd /srv && pytest -q test_api.py"
```

Ergebnis war erfolgreich, alle Tests liefen durch.

### Hinweis zu Pytest Cache Warnungen
Es gab Warnungen, weil Pytest Cache Dateien im Container nicht geschrieben werden konnten. Das ist funktional unkritisch. Optional kann der Cache Provider deaktiviert werden:

```bash
docker run --rm geraeteausleihe:test sh -c "cd /srv && pytest -q -p no:cacheprovider test_api.py"
```

## Git Ignore bereinigen
Damit lokale Artefakte nicht committed werden, wurde eine `.gitignore` erstellt. Ziel war insbesondere, dass `.venv` nicht committet wird.

Optionaler Fix falls `.venv` bereits getrackt war:

```bash
git rm -r --cached .venv
```

## Commits
Es wurde empfohlen, Commits nach Themen zu splitten, zum Beispiel:

1. Git Ignore
2. Dockerfile und dockerignore
3. Requirements und Tests

Damit bleibt die Historie nachvollziehbar.

## Pull Request und Merge Konflikt
Beim Pull Request von `develop` nach `main` gab es einen Konflikt in `README.md`. Da die Version auf `main` erhalten bleiben sollte, wurde im GitHub Conflict Editor die eingehende Version von `main` uebernommen.

In GitHub entspricht das der Auswahl:

Accept incoming change

Danach wurde der Konflikt als geloest markiert und der Merge Commit erstellt.

## GitHub Actions Required Checks
### Problem
Im Pull Request wurden Required Checks erwartet, aber es wurden keine Status Reports geliefert. Das passiert typischerweise, wenn Workflows nicht auf Pull Requests triggern oder die Job Namen nicht zu den erwarteten Checks passen.

### Loesung
Es wurde ein zusaetzlicher Workflow erstellt, der bei `pull_request` auf `main` laeuft und die exakt erwarteten Job Namen bereitstellt:

1. build
2. lint
3. test
4. pages-build

Wichtig ist, dass die Job Namen genau so heissen wie die Required Checks. Danach liefen die Checks im Pull Request und wurden erfolgreich abgeschlossen.

## Ergebnis
Der Microservice ist lokal erreichbar, Health Endpoints liefern OK, PDF Endpoint liefert ein PDF, und die Tests sind reproduzierbar in der Container Umgebung ausfuehrbar. Pull Request Checks liefen erfolgreich, der Merge nach `main` war moeglich.

## Naechste Schritte
1. GHCR Build Push auf `main` verifizieren
2. AWS EC2 vorbereiten
3. K3s installieren
4. Kubernetes Manifeste aus `k8s/` anwenden
5. Ingress testen und dokumentieren
6. Optional Deployment Automatisierung nach K3s ergaenzen
