from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os
from settings import LOG_DIR, PORT, HOST

app = FastAPI()

@app.get("/{app}", response_class=HTMLResponse)
async def read_logs(app):
    logs_html = "<html><body>"
    file_path = os.path.join(LOG_DIR, f'{app}.log')
    if os.path.isfile(file_path):
        logs_html += f"<h2>{app}</h2><pre>"
        with open(file_path, 'r') as f:
            logs_html += f.read()
        logs_html += "</pre><hr>"

    logs_html += "</body></html>"
    return logs_html


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=HOST, port=PORT)

