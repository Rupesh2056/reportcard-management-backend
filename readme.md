## Project Setup

1) Clone the repo 
    git clone git@github.com:Rupesh2056/reportcard-management-backend.git

2) Change directory to the project directory
    cd report-card-management-backend/

3) Create and activate virtual environment
    python3 -m venv venv
    source venv/bin/activate

4) Install Dependencies
    pip install -r requirements.txt

5) Create .env
    a) cp .env.sample .env
    b) make necessary changes on the .env file for database (leave unchanged for sqlite3)

6) Run the server
    python manage.py runserver 0.0.0.0:8000
