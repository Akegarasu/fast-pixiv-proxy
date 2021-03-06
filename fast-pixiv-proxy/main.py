import uvicorn
from fastapi import FastAPI
from fastapi.responses import Response

from config import HOST, PORT, SELF_URL
from pixiv import get_pixiv, PixivImage

app = FastAPI()


@app.get("/")
async def read_root():
    rep = f'''Usage:

1. http://{SELF_URL}/$path
   - http://{SELF_URL}/img-original/img/0000/00/00/00/00/00/12345678_p0.png

2. http://{SELF_URL}/$pid[/$p][?img_type=original|regular|small|thumb|mini]
   - http://{SELF_URL}/12345678    (p0)
   - http://{SELF_URL}/12345678/0  (p0)
   - http://{SELF_URL}/12345678/1  (p1)
   - http://{SELF_URL}/12345678?img_type=small (small image)'''
    return Response(rep)

@app.get("/favicon.ico")
async def _():
    return Response()

@app.get("/{pixiv_path:path}")
async def read_root(pixiv_path: str, img_type: str = "original"):
    resp = await get_pixiv(query=pixiv_path, img_type=img_type)
    if isinstance(resp, Response):
        return resp
    if isinstance(resp, PixivImage):
        headers = {
            "cache-control": "no-cache",
            "Content-Type": resp.ext,
            "Content-Disposition": f'''inline; filename="{resp.pid}"'''
        }
        return Response(resp.content, headers=headers, media_type="stream")
    return Response("Invalid request", status_code=400)

if __name__ == '__main__':
    uvicorn.run(app='main:app', host=HOST, port=PORT, reload=True)
