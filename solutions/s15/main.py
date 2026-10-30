from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from weather import CITIES, Hour, fetch_today

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/api/today")
def today(min_rain: int = 0) -> list[Hour]:
    return [h for h in fetch_today() if h.rain >= min_rain]


def page(request: Request, city: str) -> HTMLResponse:
    hours = fetch_today(city)
    warmest = max(hours, key=lambda h: h.temp)
    coldest = min(hours, key=lambda h: h.temp)
    return templates.TemplateResponse(
        request,
        "page.html",
        {"city": city, "hours": hours, "warmest": warmest, "coldest": coldest},
    )


@app.get("/", response_class=HTMLResponse)
def home(request: Request) -> HTMLResponse:
    return page(request, "서울")


@app.get("/city/{name}", response_class=HTMLResponse)
def city(request: Request, name: str) -> HTMLResponse:
    if name not in CITIES:
        raise HTTPException(status_code=404, detail="모르는 도시예요")
    return page(request, name)
