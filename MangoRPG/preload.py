# Debugger!!!
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from rich.console import Console
from rich.color import Color
from rich.progress import (
    Progress,
    BarColumn,
    TextColumn,
    SpinnerColumn,
    MofNCompleteColumn,
    ProgressColumn,
    TaskProgressColumn,
    TimeElapsedColumn,
    TimeRemainingColumn
    )
import time

console = Console()
#[progress.description]
def preload():
    progress = Progress(
        SpinnerColumn(),
        TextColumn("{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        #MofNCompleteColumn(),
        TimeRemainingColumn(),
        TimeElapsedColumn()
    )

    progress2 = Progress(
        SpinnerColumn(),
        TextColumn("{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        #MofNCompleteColumn(),
        TimeRemainingColumn(),
        TimeElapsedColumn()
    )

    progress3 = Progress(
        SpinnerColumn(),
        TextColumn("{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        #MofNCompleteColumn(),
        TimeRemainingColumn(),
        TimeElapsedColumn()
    )

    with progress:
        preloadTask1 = progress.add_task("[#005fff]加载脚本文件",total=28)
        preloadTask2 = progress.add_task("[#ff0000]加载资源文件",total=1)
    
        while not progress.finished:
            progress.update(preloadTask1,advance=0.75)
            progress.update(preloadTask2,advance=0.75)
            time.sleep(0.12)
    
    # with progress2:
    #     preloadDBTask1 = progress2.add_task("[#005fff]加载数据库中",total=1)
    
    #     while not progress2.finished:
    #         progress2.update(preloadDBTask1,advance=0.25)
    #         time.sleep(0.12)


    console.print("[#ff9f3f]资源加载完成!")
    time.sleep(1.2)    
