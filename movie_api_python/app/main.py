from flask import Flask, jsonify, request
import mysql.connector

# ==== DATABASE SETTING ====
DB_HOST = "103.16.116.159"
DB_PORT = 3306
DB_USER = "devops"
DB_PASSWORD = "ubaya"
DB_NAME = "movie"
# ==========================

app = Flask(__name__)

@app.route("/")
def home():
    return "Server Flask aktif dan siap!"

def get_db_conn():
    return mysql.connector.connect(
        host=DB_HOST, port=DB_PORT, user=DB_USER,
        password=DB_PASSWORD, database=DB_NAME
    )

# === Endpoint 1: Ambil semua movie dengan poster ===
@app.route("/movies/posters", methods=["GET"])
def get_movies_with_posters():
    sql = """
        SELECT m.id, m.title, p.poster AS poster_url
        FROM movies m
        JOIN movie_poster p ON m.id = p.id
        LIMIT 50;
    """
    try:
        conn = get_db_conn()
        cur = conn.cursor()
        cur.execute(sql)
        cols = [d[0] for d in cur.description]
        data = [dict(zip(cols, row)) for row in cur.fetchall()]
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        try:
            cur.close()
            conn.close()
        except:
            pass

# === Endpoint 2: tampilkan semua movie ===
@app.get("/movies")
def get_movies():
    sql = f"SELECT * FROM movies LIMIT 50;"
    try:
        conn = get_db_conn()
        cur = conn.cursor()
        cur.execute(sql)
        cols = [d[0] for d in cur.description]
        data = [dict(zip(col]()
