from datetime import datetime, timedelta
import time

# 将utc时间转换为本地时间
def utc_2_local(utc_time):
    local_tm = datetime.fromtimestamp(0)
    utc_tm = datetime.utcfromtimestamp(0)
    offset = local_tm - utc_tm
    return utc_time + offset

utc_time = datetime.utcnow()
print(type(utc_time))
print(utc_time)
utc_2_loc = utc_2_local(utc_time)
print(type(utc_2_loc))

utc_2_loc = utc_2_loc.strftime("%Y-%m-%d %H:%M:%S")
print(utc_2_loc)


# print(time.strftime("%Y-%m-%d %H:%M:%S", utc_2_loc))
print(type(time.localtime()))

modified_date = datetime.now().now()
# print(type(modified_date))
# print(time.strftime("%Y-%m-%d %H:%M:%S", modified_date))

# print((datetime.now() - timedelta(hours=1)).strftime("%Y%m%d%H"))
def get_timestamp_str_yyyyMMddHH(hours):
    return (datetime.now() + timedelta(hours=hours)).strftime("%Y%m%d%H")
print(get_timestamp_str_yyyyMMddHH(0))

def get_timestamp_str_yyyyMMdd(days):
    return (datetime.now() + timedelta(days=days)).strftime("%Y%m%d")
print(get_timestamp_str_yyyyMMdd(-1))