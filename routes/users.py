from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
# html 틀이 있는 폴더 위치
templates = Jinja2Templates(directory ="templates/")
router = APIRouter()

# 회원 가입
@router.get("/inserts") # 주로 2단계까지만 연결
async def inserts(request: Request) :
    return templates.TemplateResponse(name="users/inserts.html",
                                      context={"request":request})
@router.get("/lists") # 주로 2단계까지만 연결
async def inserts(request: Request) :
    return templates.TemplateResponse(name="users/lists.html",
                                      context={"request":request})
@router.get("/logins") # 주로 2단계까지만 연결
async def inserts(request: Request) :
    return templates.TemplateResponse(name="users/logins.html",
                                      context={"request":request})
@router.get("/reads") # 주로 2단계까지만 연결
async def inserts(request: Request) :
    return templates.TemplateResponse(name="users/reads.html",
                                      context={"request":request})
@router.get("/updates") # 주로 2단계까지만 연결
async def inserts(request: Request) :
    return templates.TemplateResponse(name="users/updates.html",
                                      context={"request":request})