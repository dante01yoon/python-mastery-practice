from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from weather import Hour, fetch_today

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/api/today")
def today() -> list[Hour]:
    return fetch_today()


@app.get("/", response_class=HTMLResponse)
def home(request: Request) -> HTMLResponse:
    hours = fetch_today()
    warmest = max(hours, key=lambda h: h.temp)
    return templates.TemplateResponse(
        request, "page.html", {"hours": hours, "warmest": warmest}
    )
