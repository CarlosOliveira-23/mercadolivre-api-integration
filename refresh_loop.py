import asyncio
import httpx


async def refresh_token_loop():
    while True:
        async with httpx.AsyncClient() as client:
            await client.get("http://localhost:8000/refresh_token")
            await asyncio.sleep(60 * 60 * 6)


async def main():
    await asyncio.gather(refresh_token_loop())


if __name__ == "__main__":
    asyncio.run(main())
