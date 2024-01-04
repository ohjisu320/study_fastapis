### installed
```
~$ pip install fastapi uvicorn jinja2
```
### STUDIED FILES
<details>
  <summary>show details</summary>

|구분|소스|설명|
|--|--|--|
|메인파일 생성|[main.py](./main.py)|메인 파일 생성 및 app-router연결|
|라우트파일 생성|[main.py](./home.py)|라우트 파일 생성 및 app-router연결|

</details>

### STUDIED CODES
<details>
  <summary>show details</summary>

### main.py imports - main basic form

```
from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from routes.homes import router as event_router

from fastapi import Request

from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory ="templates/") # html 틀이 있는 폴더 위치

app = FastAPI()

@app.get("/index")
async def root(request:Request):
    pass
    return templates.TemplateResponse("index.html",
                                      {"request":request})

```

### home.py imports - route basic form

```

from fastapi import APIRouter

from starlette.responses import HTMLResponse

from fastapi.templating import Jinja2Templates

from fastapi import Request

templates = Jinja2Templates(directory ="templates/")

router = APIRouter()

@app.get("/index")
async def root(request:Request):
    pass
    return templates.TemplateResponse("index.html",
                                      {"request":request})


```

