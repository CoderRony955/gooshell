from rich.console import Console
import psutil

console = Console()


def heatlh() -> None:
    MemUsage = psutil.virtual_memory()
    Processes = psutil.pids()

    MemSit = ''
    ProcessesSit = ''

    # Suggestion as per Memory Usage
    if MemUsage.percent > 10.0 and MemUsage.percent <= 40.0:
        MemSit += f'{MemUsage.percent} % of memory is under use. (All are good)'
    elif MemUsage.percent > 40.0 and MemUsage.percent <= 50.0:
        MemSit += f'{MemUsage.percent} % of memory is under use. (Half of memory is under use)'
    elif MemUsage.percent > 50.0 and MemUsage.percent <= 70.0:
        MemSit += f'{MemUsage.percent} % of memory is under use. (terminate the process of unused programs)'
    elif MemUsage.percent > 70.0:
        MemSit += f'{MemUsage.percent} % of memory is under use. (terminal the process of unused programs immediately to prevent system heat, lags and freezes)'

    # Suggestion as per live running No. of Processes
    if len(Processes) > 0 and len(Processes) <= 150:
        ProcessesSit += f'No. of Processes: {len(Processes)}.(This is not too much!)'
    elif len(Processes) >= 150 and len(Processes) <= 200:
        ProcessesSit += f'No. of Processes: {len(Processes)}. (A little bit too much Processes are running now, if your system causing heat then you can terminate unused programs)'
    elif len(Processes) >= 200:
        ProcessesSit += f'No. of Processes: {len(Processes)}. (There are too much Processes are running, please terminate the processes of unused programs, close unused background apps to prevent system heat, lags and freezes)'

    console.print(MemSit)
    console.print(ProcessesSit)

heatlh()