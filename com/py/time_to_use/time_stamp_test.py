from datetime import datetime

# 将utc时间转换为本地时间
def utc_2_local(utc_time):
    local_tm = datetime.fromtimestamp(0)
    utc_tm = datetime.utcfromtimestamp(0)
    offset = local_tm - utc_tm
    return utc_time + offset

utc_time = datetime.utcnow()
print(utc_time)
utc_2_loc = utc_2_local(utc_time)
utc_2_loc = utc_2_loc.strftime("%Y-%m-%d %H:%M:%S")
print(utc_2_loc)