import time
retry_times = 10
while retry_times > 0:
    try:
        print("")
    except Exception as e:
        # 如果调用http接口失败，在时间间隔后，重试
        retry_times -= 1
        time.sleep(1)
else:
    raise Exception('failed to call SinaWatch ')