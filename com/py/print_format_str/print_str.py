import re
from datetime import timedelta
# 将秒数的时间，转换为 dhms 的方式显示（最多显示2位）
origin_time = timedelta(seconds=10080000)
seconds = int(origin_time.total_seconds() / 60)

s = str(seconds % 60) + "s"
minutes = int(seconds / 60)
m = str(minutes % 60) + "m"
hours = int(minutes / 60)
h = str(hours % 24) + "h"
d = str(int(hours / 24)) + "d"
res_str = ""
show_max_count = 2
match_index = 0
for item in (d, h, m, s):
    if re.match("^[^0]", item):
        res_str += item
        match_index += 1
        if match_index == show_max_count:
            break
print(origin_time)
print(seconds)
print(res_str)