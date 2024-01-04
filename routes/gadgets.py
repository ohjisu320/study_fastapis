from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
gadgets = APIRouter()
from fastapi import Request
templates = Jinja2Templates(directory ="templates/")


@gadgets.get("/buttons")
async def buttons(request: Request):
    return templates.TemplateResponse(name="gadgets/buttons.html",
                                      context={"request": request})

@gadgets.get("/cards") # 'query : 질의' 라는 의미
# "request = Request(query_parameters)" == async def cards_get("request:Request")
async def cards_get(request:Request): # request - client가 날린 모든 정보를 담아서 변수로 전환한 것.
    request._query_params
    # QueryParams('name=jisu&email=ohjisu320%40gmail.com')
    request._query_params._dict
    # {'name': 'jisu', 'email': 'ohjisu320@gmail.com'}
    dict(request._query_params)
    # {'name': 'jisu', 'email': 'ohjisu320@gmail.com'}
    return templates.TemplateResponse(name="gadgets/cards.html",
                                      context={"request": request})

@gadgets.post("/cards")
async def cards_post(request:Request):
    # form_datas = await request.form()
    request._query_params
    # QueryParams('')
    await request.form()
    # FormData([('name', 'jisu'), ('email', 'ohjisu320@gmail.com')])
    dict(await request.form())
    # {'name': 'jisu', 'email': 'ohjisu320@gmail.com'}
    return templates.TemplateResponse(name="gadgets/cards.html",
                                      context={"request": request})

@gadgets.get("/colors")
async def colors(request:Request):
    return templates.TemplateResponse(name="gadgets/colors.html",
                                      context={"request": request})


@gadgets.get("/containers")
async def containers(request:Request):
    return templates.TemplateResponse(name="gadgets/containers.html",
                                      context={"request": request})

