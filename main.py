from fastapi import FastAPI, Request
import models
from database import engine
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from api.api import api_router

app = FastAPI(title="MithilaIT API Server")
models.Base.metadata.create_all(bind=engine)
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(request=request,
                                      name="landing_page.html",
                                      context={
                                          "title": "MithilaIT API Server",
                                          "name": "Serve is Live"
                                      })


# Add Routers
app.include_router(api_router, prefix="/api")
