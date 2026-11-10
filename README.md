# AgroVision – Smart Agriculture Portal

A student-friendly smart agriculture website built with HTML, CSS, JavaScript and Python Flask. It includes a responsive landing page and an educational rule-based crop suggestion demo.

## Features
- Responsive agriculture-themed dashboard and landing page
- Crop finder form using rainfall, soil pH and nitrogen values
- Python Flask API for demo recommendations
- Clear educational disclaimer

## Requirements
- Python 3.9+
- Git
- A web browser

## Run locally (Windows CMD)
```cmd
cd AgroVision
py -m venv venv
venv\Scripts\activate
py -m pip install -r requirements.txt
py app.py
```
Open http://127.0.0.1:5000 in your browser. Stop the server with `Ctrl+C`.

## Git workflow
- `main`: stable release branch
- `dev`: integration branch
- `feature/homepage`: homepage and crop finder work

Create feature branches, commit small changes, push to GitHub, and open pull requests into `dev`. When tested, open a PR from `dev` into `main`.

## Project structure
- `app.py`: Flask application and recommendation endpoint
- `templates/`: HTML templates
- `static/css/`: styles
- `static/js/`: browser interactions
- `docs/`: assignment documentation

## Important note
The crop rules are illustrative and are not validated agricultural guidance. Do not use this demo to make real planting decisions. Consult local soil-test results and qualified agricultural experts.
