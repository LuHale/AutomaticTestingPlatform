from django.conf import settings
import time
import os
import shutil


def save_result(result_page):
    pattern = r'/static/'
    replace_str = r'./static/'
    result = ''
    # 拼接执行结果保存路径
    path = '\\'.join((settings.SAVE_DIRS, time.strftime('%Y\%m\%d', time.localtime())))
    # 判断路径是否存在
    if not os.path.exists(path):
        # 如果路径不存在，则拷贝静态文件到新建的目录下
        shutil.copytree('\\'.join((settings.BASE_DIR, 'static')), '\\'.join((path, 'static')))

    filename = 'result_' + time.strftime('%H%M%S', time.localtime()) + '.html'
    with open('\\'.join((path, filename)), 'w', encoding='utf-8') as f:
        for eachline in result_page:
            result += (eachline.decode('utf-8'))
        result = result.replace(pattern, replace_str)
        f.writelines(result)
        f.close()
