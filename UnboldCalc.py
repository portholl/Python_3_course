def UnlodCalc():
    variables = {}
    variables['__builtins__'] = {}
    while True:
        try:
            line = input().strip()
            if line == "":
                break
            if line.startswith('#'):
                continue  

            if '=' in line:
                id, expression = map(str.strip, line.split('=', 1))
                
                if not id.isidentifier():
                    print("Assignment error")
                    continue
                if expression == "":
                    continue
                
                try:
                    value = eval(expression, {'__builtins__' : {} }, variables)
                    variables[id] = value  
                except NameError:
                    print("Name error")
                except SyntaxError:
                    print("Syntax error")
                except Exception:
                    print("Runtime error")
            else:
                try:
                    result = eval(line, {'__builtins__' : {} }, variables)
                    print(result)
                except NameError:
                    print("Name error")
                except SyntaxError:
                    print("Syntax error")
                except Exception:
                    print("Runtime error")
        except Exception as e:
            print("Runtime error") 
UnlodCalc()
