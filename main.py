from src.memory_bus import MemoryBus
from src.cpu import CPU
from src.utils import parse_instruction

def main():
    memory_bus = MemoryBus()
    try:
        with open('data/data_input.txt', 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    address, value = line.split(',')
                    memory_bus.write(int(address), int(value))
        print("Memory initialized successfully.")
    except FileNotFoundError:
        print("data_input.txt not found. Proceeding with empty memory.")

    instructions = []
    try:
        with open('data/instruction_input.txt', 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    parsed = parse_instruction(line)
                    instructions.append(parsed)
        print("Instructions loaded successfully.")
    except FileNotFoundError:
        print("instruction_input.txt not found. Exiting.")
        return

    print(f"Loaded {len(instructions)} instructions.")
    for i, instr in enumerate(instructions):
        print(f"Instruction {i}: {instr}")

    cpu = CPU(memory_bus, instructions)
    cpu.execute()

    print("\nFinal registers:")
    for i in range(32):
        if cpu.registers[i] != 0:
            print(f"R{i}: {cpu.registers[i]}")

    print("\nMemory contents:")
    for addr in sorted(memory_bus.data.keys()):
        print(f"Address {addr}: {memory_bus.data[addr]}")

if __name__ == "__main__":
    main()