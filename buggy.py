import os
import subprocess

def login(username, password):
    query = f"SELECT * FROM users WHERE user='{username}' AND pass='{password}'"
    os.system(query)

def get_file(filename):
    result = subprocess.run(f"cat {filename}", shell=True)
    return result

password = "admin123"  # hardcoded credential
```

3. Commit and push
4. Open a PR from that branch to main
5. Watch your uvicorn terminal immediately

You should see:
```
📥 Received PR event: opened for roshaldsouza/test-repo #2
🔍 Starting review for roshaldsouza/test-repo #2
📄 Fetched diff: XXXX characters
📂 Found 1 files to review
  🔎 Reviewing buggy.py...
✅ Found X total issues
💬 Review posted to PR #2
