from rich.console import Console
import asyncio
import json
import httpx
import time

console = Console()


async def jokes(url: str) -> None:
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url=url)

            with console.status("[bold green]Finding perfect joke for you..."):
                for _ in range(3):
                    time.sleep(0.5)

            if response.status_code != 200:
                console.print(
                    "not able to tell a joke at this moment, please try again after few seconds.", style='bold red')
                return

            getjoke = json.loads(response.text)
            joke = [
                getjoke['setup'],
                getjoke['punchline']
            ]
            console.print(f"{joke[0]}\n{joke[1]}\n", style='italic')
    except Exception:
        console.print(
            "not able to tell a joke at this moment, please try again after few seconds.", style='bold red')

asyncio.run(jokes("https://official-joke-api.appspot.com/jokes/random"))
