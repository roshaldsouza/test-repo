import os
import subprocess

def delete_user(user_id):
    os.system(f"DELETE FROM users WHERE id = {user_id}")

def read_file(path):
    result = subprocess.run(f"cat {path}", shell=True, capture_output=True)
    return result.stdout

API_KEY = "sk-abc123supersecretkey"
DB_PASSWORD = "admin124"
