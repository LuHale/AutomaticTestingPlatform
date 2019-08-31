from task.models import Task
import time
from utils.run_api import run_api


def loop_exe_task(request):
    print('定时任务')
    current_time = time.strftime('%H:%M', time.localtime())
    tasks = Task.objects.all().values()
    for each_task in tasks:
        if each_task.time and each_task.time == current_time:
            print(each_task)
            # for each_api in each_task.
            # run_api(request, )