import uvicorn
from fastapi import FastAPI
from pixiv import get_pixiv
from fastapi.responses import Response
from config import SELF_URL
app = FastAPI()


@app.get("/")
async def read_root():
    rep = f'''Usage:

1. http://{SELF_URL}/$path
   - http://{SELF_URL}/img-original/img/0000/00/00/00/00/00/12345678_p0.png

2. http://{SELF_URL}/$pid[/$p]
   - http://{SELF_URL}/12345678    (p0)
   - http://{SELF_URL}/12345678/0  (p0)
   - http://{SELF_URL}/12345678/1  (p1)'''
    return Response(rep)


@app.get("/{pixiv_path:path}/")
async def read_root(pixiv_path: str):
    rep = await get_pixiv(pixiv_path)
    headers = {
        "cache-control": "no-cache"
    }
    return Response(rep, headers=headers, media_type="stream")

if __name__ == '__main__':
    uvicorn.run(app='main:app', host="127.0.0.1", port=8000, reload=True, debug=True)