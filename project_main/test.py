import inspect

def foo(a, f, b, cd):
    # frame = inspect.currentframe()
    # frame = inspect.getouterframes(frame)[1]
    # string = inspect.getframeinfo(frame[0]).code_context[0].strip()
    # args = string[string.find('(') + 1:-1].split(',')
    
    # names = []
    for i in a:
        frame = inspect.currentframe()
        print(frame)
        # frame = inspect.getouterframes(frame)[1]
        # frame = inspect.getinnerframes(frame)[0]
        print(frame.f_locals)
        for iw in frame.f_locals:
            for j in locals().items():
                print(iw + "i")
                print(j)
        # string = inspect.getframeinfo(frame[0]).code_context[0].strip()
        # print(string)
        # args = string[string.find('(') + 1:-1].split(',')
        # print(args)
    # for i in args:
    #     if i.find('=') != -1:
    #         names.append(i.split('=')[1].strip())

    #     else:
    #         names.append(i)
    
    # print(names)

def main():
    e = 1
    c = 2
    list_ = ["a", "b"]
    foo(list_, e, 1000, c)

main()