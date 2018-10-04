search_list = ["a", "b", "c", "d", "e", "f"]
chat_n = "a"

find_num = lambda s_list, n: find_num_fun(s_list, n)

def find_num_fun(s_list, n):
    for item in s_list:
        if n == item:
            print("ok")
            break
    else:
        print("not ok")
    return "fuck"

print(find_num(search_list, chat_n))

# for n in search_list:
#     if n is chat_n:
#         print(id(n))
#         print(id(chat_n))
#         print("ok")
#         break
# else:
#     print("bad")