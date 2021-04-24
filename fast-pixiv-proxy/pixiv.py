from aiohttp import ClientSession
from typing import Optional, Dict
from config import PROXY

base_url = "https://i.pximg.net/"
p_headers = {
    "Referer": 'https://www.pixiv.net',
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
}


async def get_pixiv(query: str) -> Optional[bytes]:
    split_query = query.split("/")
    if query.startswith("img-original/img/"):
        return await reverse_pixiv(base_url + query)
    else:
        if split_query[0].isdigit():
            img_urls = await ajax_pixiv(split_query[0])
            img_url = img_urls["original"]
            if len(split_query) == 2:
                if split_query[1].isdigit():
                    page = split_query[1]
                    img_url = img_urls["original"].replace("_p0", f"_p{page}")
            return await reverse_pixiv(img_url)


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


async def reverse_pixiv(path: str) -> Optional[bytes]:
    async with ClientSession() as cs:
        async with cs.get(path,
                          headers=p_headers,
                          proxy=PROXY) as rep:
            content = await rep.read()
            if rep.status == 200:
                return content
            else:
                return None
