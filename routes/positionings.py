from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
positionings = APIRouter()
from fastapi import Request
templates = Jinja2Templates(directory = "templates/")

@positionings.get("/forms")
async def forms(request: Request):
    return templates.TemplateResponse(name="positionings/forms.html",
                                      context={"request": request})

@positionings.get("/grids")
async def grids(request: Request):
    return templates.TemplateResponse(name="positionings/grids.html",
                                      context={"request": request})

@positionings.get("/standards")
async def standards(request: Request):
    return templates.TemplateResponse(name="positionings/standards.html",
                                      context={"request": request})

@positionings.get("/tables")
async def tables(request: Request):
    return templates.TemplateResponse(name="positionings/tables.html",
                                      context={"request": request})