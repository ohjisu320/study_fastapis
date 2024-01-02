from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
gadgets = APIRouter()
from fastapi import Request
templates = Jinja2Templates(directory ="templates/")


@gadgets.get("/buttons")
async def home(request: Request):
    return templates.TemplateResponse(name="gadgets/buttons.html",
                                      context={"request": request})

@gadgets.get("/cards")
async def home(request:Request):
    return templates.TemplateResponse(name="gadgets/cards.html",
                                      context={"request": request})

@gadgets.get("/colors")
async def home(request:Request):
    return templates.TemplateResponse(name="gadgets/colors.html",
                                      context={"request": request})

@gadgets.get("/containers")
async def home(request:Request):
    return templates.TemplateResponse(name="gadgets/containers.html",
                                      context={"request": request})