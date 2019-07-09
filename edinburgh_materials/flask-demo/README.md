# Flask / Hug webapp demo

Simple proof-of-concept webapp.  Hug provides API endpoint onto SOBI database,
Flask renders HTML from templates and results of website calls.

Example result: [example_999.html](example_999.html)

#### Setup

```bash
pip install -r requirements.txt
```

#### Database endpoint

Start database API (on port 8000)

```bash
ORACLE_PASSWORD=somesecretpassword hug -f endpoint.py
```

Example query:

```bash
curl localhost:8000/borehole/1234
```

#### Web app

Start webapp (on port 5000)

```bash
FLASK_APP=app.py flask run
```

Navigate to [http://localhost:5000/borehole/1234](http://localhost:5000/borehole/1234).
