import trio
# import concurrent.futures
# with open('test.trio','r') as f:
#     text = f.read()
#     text = text.replace('\n','')
#     # if text.strip() == "":
#     result, error = trio.run('<stdin>', text)
#
#     if error:
#         print(error.as_string())
#     elif result:
#         if len(result.elements) == 1:
#             print(repr(result.elements[0]))
#         else:
#             print(repr(result))
while True:
    text = input("Trio:>>")
    if text == 'exit()':
        exit()
    if text.strip() == "": continue
    result, error = trio.run('<stdin>', text)

    if error:
        print(error.as_string())
    elif result:
        if len(result.elements) == 1:
            print(repr(result.elements[0]))
        else:
            print(repr(result))
