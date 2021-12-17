# ACTIVATE VIRUTAL ENVIRONMENT
venv\Scripts\activate.bat

# start the server and reload every change
uvicorn app.main:app --reload

