## Project Setup

Option1: With docker

    1) Clone the repo 
        git clone git@github.com:Rupesh2056/reportcard-management-backend.git

    2) Change directory to the project directory
        cd report-card-management-backend/

    3) build the docker image
        docker build .

    4) Run the docker compose file
        docker compose up

Option2: Without Docker
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

    6) Migrate database:
        python manage.py migrate

    7) Run the server
        python manage.py runserver 0.0.0.0:8000



 For API docs go to:
    http://127.0.0.1:8000/api/swagger/
    http://127.0.0.1:8000/api/docs/


For Dummy data, use the management command:
    python manage.py create_data




## Deliveries:
    a) CRUD API for Subject. Search feature with name and code.
    b) CRUD API for Student. Search feature with name and email.
    c) Create,Read & Update API for Term. Search by title.
    d) Create , Read (list and detail) and Update Feature for ReportCard.Filter by term,year,student(name and email).
        Validation for unique student,term and year.
        Index (Student,Year) added.
    e) Create and Update API for Mark. (Update api is limited to updating score only.)
    f) Student`s Yearly report Card API with aggregation summary.
    g) Management command (inside report app) to create dummy data (Student,Course,Term,ReportCArd & Marks)
    h) Custom data validation for fields like score and Year.
    i) Postman Collection for APIs.
    j) API docs (swagger).
    k) Docker setup.



### About the Project

1) App Structure:
    Apps are segregated for student, report and course, while root is the project app (containing setting.py).

2) APIs:
    All apis are written in seperate directory api/ 

3) About "Term" Model:
    I have decided to create a seperate model for Term, instead of Using CharField. This is alot Safer while creating
        ReportCard.

4) Query Optimization:
    - For StudentReportCardAPIView, I used a minimal Serializer excluding Student from each Report. This is because, we are 
      looking for reports of a particular student. So, it not worth mentioning the student for every reports. Rather, i have 
      used a single key "student" for the overall response.
    - Beside that, prefetch_related and select_related are used to make the join query , ultimately retrieving term, marks and 
      subject priorly.
    - Use of database index with fields (Student,year).


