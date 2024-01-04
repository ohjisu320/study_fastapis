from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
templates = Jinja2Templates(directory ="templates/")
router = APIRouter()

# @router.get("/", response_class=HTMLResponse) # 펑션 호출 방식
# async def home():
#     html = "<body> <h2> It's Home. </h2> </body>"
#     return html
@router.get("/")
async def root(request:Request) :
    pass
    return templates.TemplateResponse(name="homes/standards.html",
                                      context={"request":request})


# @ = Annotation  / 체질을 바꿔주는 역할 / 웹에서 펑션 호출 
@router.get("/list", response_class=HTMLResponse) # 주로 2단계까지만 연결
async def home_list() :
    html = "<body> <h2> It's Home List. </h2> </body>"
    return html

# /homes/params_query -> parametes_query.html 호출
@router.get("/params_query")
async def home_param(request:Request) :
    pass
    return templates.TemplateResponse(name="homes/parameters_query.html",
                                      context={"request":request})