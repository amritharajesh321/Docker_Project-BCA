from flask import Flask, render_template
import psycopg2
import os

app = Flask(__name__)

def connect_db():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "host.docker.internal"),
        database=os.getenv("DB_NAME", "docker_project_db"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD"),
        port="5432"
    )

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/db-status')
def db_status():
    try:
        conn = connect_db()
        conn.close()
        return "PostgreSQL Connected Successfully!"
    except Exception as e:
        return f"Database Connection Failed: {e}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
