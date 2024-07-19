import re

def actualizar_identificadores(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    new_lines = []
    identifier = 130

    for line in lines:
        match = re.match(r'(\s*google\.protobuf\.StringValue\s+\w+\s*=\s*)\d+(\s*;.*)', line)
        if match:
            new_line = f"{match.group(1)}{identifier}{match.group(2)}\n"
            new_lines.append(new_line)
            identifier += 1
        else:
            new_lines.append(line)

    with open(file_path, 'w') as file:
        file.writelines(new_lines)

# Uso del script
actualizar_identificadores('messages.proto')
actualizar_identificadores('services.proto')
