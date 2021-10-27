# fast-pixiv-proxy
A proxy for pixiv images using fastapi&amp;aiohttp: 一个简单便捷的 pixiv 图片反向代理服务，简单快捷方便部署哟

### 部署：
   - python >= 3.7
   - 执行 `pip install aiohttp uvicorn fastapi`
   - 修改`config.py`的`PROXY`和`SELF_URL`（如果有代理需要）
   - 启动程序

### 使用方法：

#### Usage:

1. http://{SELF_URL}/$path
   - http://{SELF_URL}/img-original/img/0000/00/00/00/00/00/12345678_p0.png

2. http://{SELF_URL}/$pid[/$p][?img_type=original|regular|small|thumb|mini]
   - http://{SELF_URL}/12345678    (p0)
   - http://{SELF_URL}/12345678/0  (p0)
   - http://{SELF_URL}/12345678/1  (p1)
   - http://{SELF_URL}/12345678?img_type=small (small image)

#### 简单举例

**这里的example.com是你部署该服务的域名**

1. https://example.com/img-original/img/2021/08/26/11/47/39/92269291_p0.jpg (直接将i.pximg.net换成你的域名)

2. https://example.com/92269291 (直接使用pid获得第一张图片)

3. https://example.com/92269291/1 (获得第二张图片 如果存在)

4. https://example.com/92269291?img_type=regular (regular分辨率 1200的图片)