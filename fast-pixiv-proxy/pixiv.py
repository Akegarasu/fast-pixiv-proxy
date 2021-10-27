from aiohttp import ClientSession
from typing import Optional, Dict
from config import PROXY

base_url = "https://i.pximg.net/"
p_headers = {
    "Referer": 'https://www.pixiv.net',
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
}


async def get_pixiv(query: str, img_type: str) -> Optional[Dict]:
    split_query = query.split("/")
    if split_query[0] in ("img-original", "img-master", "c"):
        return {
            "result": await reverse_pixiv(base_url + query),
            "pid": query.split("/")[-1]
        }
    if split_query[0].isdigit():
        if img_type not in ("original", "regular", "small", "thumb", "mini"):
            return None
        img_urls = await ajax_pixiv(split_query[0])
        img_url = img_urls[img_type]
        if len(split_query) == 2:
            if split_query[1].isdigit():
                page = split_query[1]
                img_url = img_urls[img_type].replace("_p0", f"_p{page}")
        return {
            "result": await reverse_pixiv(img_url),
            "pid": img_url.split("/")[-1]
        }
    else:
        return None


async def ajax_pixiv(pid: str) -> Optional[Dict]:
    async with ClientSession() as cs:
        async with cs.get(f"https://www.pixiv.net/ajax/illust/{pid}",
                          headers=p_headers,
                          proxy=PROXY) as rep:
            if rep.status == 200:
                json = await rep.json()
                return json["body"]["urls"]
            else:
                return None


async def reverse_pixiv(path: str) -> Optional[tuple]:
    async with ClientSession() as cs:
        async with cs.get(path,
                          headers=p_headers,
                          proxy=PROXY) as rep:
            content = await rep.read()
            if rep.status == 200:
                return content, rep.headers['Content-Type']
            else:
                return None
