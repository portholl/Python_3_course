def MroC3(code):
    classes = {}
    for line in code:
        if line.startswith("class "):
            line = line.strip()
            start_name_index = line.find('class ') + len('class ')
            end_name_index = line.find('(') if line.find('(') > 0 else line.find(':')
            name = line[start_name_index : end_name_index]
            parents = []
            if '(' in line:
                line = line[end_name_index + 1:].rstrip(' pass').rstrip('):')
                parents = line.split(', ')
            parent_classes = tuple(classes[parent] for parent in parents if parent in classes)
            try:
                classes[name] = type(name, parent_classes, {})
            except (KeyError, TypeError):
                return 'No'
    return 'Yes'
    

code = []
while s := input():
    code.append(s)
print(MroC3(code))
