from rich.console import Console

console = Console()

def welcome_description() -> None:
    description = """[magenta]
                       _     _          _ _ 
                      | |   | |        | | |
  __ _  ___   ___   __| |___| |__   ___| | |
 / _` |/ _ \\ / _ \\ / _` / __| '_ \\ / _ \\ | |
| (_| | (_) | (_) | (_| \\__ \\ | | |  __/ | |
 \\__, |\\___/ \\___/ \\__,_|___/_| |_|\\___|_|_|
  __/ |                                     
 |___/ [/magenta]   
 
 
 Good to see you! It's your rich terminal experience that is called [bold]goodshell[/bold]. Run Windows terminal commands and goodshell commands with rich experience. Alirght, so before you start here are the some basic commands that you need to know:
 
 [bold]joke[/bold]                                    If you wants to make your Mood Happy
 [bold]roastme[/bold]                                 If you wants to roast yourself (It may contains some offensive words)
 [bold]curhealth[/bold]                               Know your system's current situation
 [bold]q or quit[/bold]                               Exit goodshell
 
 You can also run [bold]Windows Terminal[/bold] commands. So, let's start!
 
                                    
"""
    console.print(description)


welcome_description()
