from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os
from settings import LOG_DIR, PORT, HOST, TEMPLATE_FILE
import jinja2

templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE = templateEnv.get_template(TEMPLATE_FILE)


app = FastAPI()

@app.get("/{app}", response_class=HTMLResponse)
async def read_logs(app):
    file_path = os.path.join(LOG_DIR, f'{app}.log')
    if os.path.isfile(file_path):
        with open(file_path, 'r') as f:
            return TEMPLATE.render(log_file=app, log_content=f.read())


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=HOST, port=PORT)

