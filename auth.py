# auth.py
import os
import subprocess

def authenticate(username, password):
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    os.system(query)

def run_report(report_name):
    subprocess.run(f"python reports/{report_name}.py", shell=True)

SECRET_KEY = "super$ecret123"
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
