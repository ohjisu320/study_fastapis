from fastapi import FastAPI

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware
# No 'Access-Control-Allow-Origin'
# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 실제 운영 환경에서는 접근 가능한 도메인만 허용하는 것이 좋습니다.
    allow_methods=["*"],
    allow_headers=["*"],
)
from routes.homes import router as event_router
from routes.gadgets import gadgets as gadgets
from routes.positionings import positionings as positionings
from routes.users import router as users_router
app.include_router(event_router, prefix="/home")
app.include_router(gadgets, prefix="/gadgets")
app.include_router(positionings, prefix="/positionings")
app.include_router(users_router, prefix="/users")


from fastapi import Request
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory ="templates/") # html 틀이 있는 폴더 위치

@app.get("/index")
async def root(request:Request):
    # html 틀로 호출
    return templates.TemplateResponse("index.html",
                                      {"request":request})

@app.get("/")
async def main(request:Request):
    # html 틀로 호출
    return templates.TemplateResponse("main.html",
                                      {"request":request})


