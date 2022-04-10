import socket
import ssl
from typing import Any, Dict, List

import aiohttp
from aiohttp.abc import AbstractResolver


class ByPassResolver(AbstractResolver):

    async def resolve(self, host: str, port, family) -> List[Dict[str, Any]]:
        if host in ["app-api.pixiv.net", "public-api.secure.pixiv.net", "www.pixiv.net", "oauth.secure.pixiv.net"]:
            host = "www.pixivision.net"

        ips = ["210.140.92.145", "210.140.92.142", "210.140.92.141", "210.140.92.146",
               "210.140.92.148", "210.140.92.149", "210.140.92.147", "210.140.92.143", "210.140.92.144"]
        result = [
            {
                "hostname": "",
                "host": i,
                "port": port,
                "family": family,
                "proto": 0,
                "flags": socket.AI_NUMERICHOST,
            } for i in ips]
        return result

    async def close(self) -> None:
        pass


class BypassClient:
    def __init__(self):
        ssl_ctx = ssl.SSLContext()
        ssl_ctx.check_hostname = False
        ssl_ctx.verify_mode = ssl.CERT_NONE
        connector = aiohttp.TCPConnector(
            ssl=ssl_ctx, resolver=ByPassResolver())
        self.client = aiohttp.ClientSession(connector=connector)

    async def __aenter__(self) -> aiohttp.ClientSession:
        return self.client

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.client.close()
