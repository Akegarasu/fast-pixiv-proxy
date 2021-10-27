# fast-pixiv-proxy
A proxy for pixiv images using fastapi&amp;aiohttp: 一个简单便捷的 pixiv 图片反代服务

### 部署：
   - aiohttp
   - fastapi
   - uvicorn

### 使用方法：
Usage:

1. http://{SELF_URL}/$path
   - http://{SELF_URL}/img-original/img/0000/00/00/00/00/00/12345678_p0.png

2. http://{SELF_URL}/$pid[/$p][?img_type=original|regular|small|thumb|mini]
   - http://{SELF_URL}/12345678    (p0)
   - http://{SELF_URL}/12345678/0  (p0)
   - http://{SELF_URL}/12345678/1  (p1)
   - http://{SELF_URL}/12345678?img_type=small (small image)