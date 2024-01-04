from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
# html 틀이 있는 폴더 위치
templates = Jinja2Templates(directory ="templates/")
router = APIRouter()

# 회원 가입 form --users/form
@router.get("/form") 
async def inserts(request: Request) :
    return templates.TemplateResponse(name="users/inserts.html",
                                      context={"request":request})

@router.get("/insert") 
async def inserts(request: Request) :
    pass # biz
    return templates.TemplateResponse(name="users/logins.html",
                                      context={"request":request})
# @router.get("/lists") 
# async def inserts(request: Request) :
#     return templates.TemplateResponse(name="users/lists.html",
#                                       context={"request":request})

# @router.get("/reads") 
# async def inserts(request: Request) :
#     return templates.TemplateResponse(name="users/reads.html",
#                                       context={"request":request})
# @router.get("/updates") 
# async def inserts(request: Request) :
#     return templates.TemplateResponse(name="users/updates.html",
#                                       context={"request":request})