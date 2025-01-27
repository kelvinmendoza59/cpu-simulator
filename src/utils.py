def parse_instruction(line):
    parts = line.strip().split(',')
    op = parts[0]
    operands = parts[1:]
    parsed = {'op': op, 'operands': []}
    try:
        if op in ('ADD', 'SUB', 'SLT'):
            # Parse registers (e.g., R1, R2, R3)
            parsed['operands'] = [int(opnd.strip()[1:]) for opnd in operands]
        elif op == 'ADDI':
            # Parse Rt, Rs, and immediate value
            rt = int(operands[0].strip()[1:])
            rs = int(operands[1].strip()[1:])
            immd = int(operands[2].strip())
            parsed['operands'] = [rt, rs, immd]
        elif op in ('LW', 'SW'):
            # Parse Rt, offset(Rs)
            rt = int(operands[0].strip()[1:])
            offset_rs = operands[1].strip().split('(')
            offset = int(offset_rs[0])
            rs = int(offset_rs[1].strip(')')[1:])
            parsed['operands'] = [rt, rs, offset]
        elif op == 'BNE':
            # Parse Rs, Rt, and offset
            rs = int(operands[0].strip()[1:])
            rt = int(operands[1].strip()[1:])
            offset = int(operands[2].strip())
            parsed['operands'] = [rs, rt, offset]
        elif op in ('J', 'JAL'):
            # Parse target address
            target = int(operands[0].strip())
            parsed['operands'] = [target]
        elif op == 'CACHE':
            # Parse cache code (0, 1, or 2)
            code = int(operands[0].strip())
            parsed['operands'] = [code]
        elif op == 'HALT':
            # No operands for HALT
            pass
        else:
            print(f"Unknown instruction: {op}")
    except Exception as e:
        print(f"Error parsing line '{line}': {e}")
    return parsed