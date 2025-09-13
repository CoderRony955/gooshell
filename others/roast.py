from rich.console import Console
import asyncio
import json
import httpx
import time

console = Console()

async def roastuser(url: str) -> None:
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url=url)
            
            with console.status("[bold green]Thinking..."):
                for _ in range(3):
                    time.sleep(0.5)
                    
            if response.status_code != 200:
                console.print("Shh! I can't Roast you at this moment, please try again after few seconds.", style='bold red')
                return
            
            getroast = json.loads(response.text)
            roast = getroast['insult']
            console.print(roast, style='italic')
    except Exception:
        console.print("Shh! I can't Roast you at this moment, please try again after few seconds.", style='bold red')
        
asyncio.run(roastuser("https://evilinsult.com/generate_insult.php?lang=en&type=json"))