from .cache import Cache

class CPU:
    """Simulates a simple CPU that processes MIPS instructions."""
    
    def __init__(self, memory_bus, instructions):
        """
        Initialize the CPU.
        
        Args:
            memory_bus (MemoryBus): The memory bus connected to the CPU.
            instructions (list): List of instructions to execute.
        """
        
        
        self.registers = [0] * 32 # 32 general-purpose registers
        self.pc = 0 # Program Counter
        self.memory_bus = memory_bus
        self.cache = Cache()
        self.running = True
        self.instructions = instructions

    def execute(self):
        """Execute the loaded instructions."""
        while self.running:
            if self.pc // 4 >= len(self.instructions):
                print("PC out of instruction bounds. HALTING.")
                break
            current_instr = self.instructions[self.pc // 4]
            print(f"\nFetch: PC={self.pc}, Instruction={current_instr}")
            self.process_instruction(current_instr)

    def process_instruction(self, instr):
        op = instr['op']
        operands = instr['operands']
        if op == 'ADD':
            self.add(*operands)
        elif op == 'ADDI':
            self.addi(*operands)
        elif op == 'SUB':
            self.sub(*operands)
        elif op == 'SLT':
            self.slt(*operands)
        elif op == 'BNE':
            self.bne(*operands)
        elif op == 'J':
            self.j(*operands)
        elif op == 'JAL':
            self.jal(*operands)
        elif op == 'LW':
            self.lw(*operands)
        elif op == 'SW':
            self.sw(*operands)
        elif op == 'CACHE':
            self.cache_instruction(*operands)
        elif op == 'HALT':
            self.halt()
        else:
            print(f"Unknown instruction: {op}")
            self.pc += 4

    # Instruction implementations
    def add(self, rd, rs, rt):
        if rd == 0:
            print("ADD: Ignoring write to R0")
            self.pc += 4
            return
        rs_val = self.registers[rs]
        rt_val = self.registers[rt]
        result = rs_val + rt_val
        self.registers[rd] = result
        print(f"ADD: R{rd} = {rs_val} + {rt_val} = {result}")
        self.pc += 4

    def addi(self, rt, rs, immd):
        if rt == 0:
            print("ADDI: Ignoring write to R0")
            self.pc += 4
            return
        rs_val = self.registers[rs]
        result = rs_val + immd
        self.registers[rt] = result
        print(f"ADDI: R{rt} = {rs_val} + {immd} = {result}")
        self.pc += 4

    def sub(self, rd, rs, rt):
        if rd == 0:
            print("SUB: Ignoring write to R0")
            self.pc += 4
            return
        rs_val = self.registers[rs]
        rt_val = self.registers[rt]
        result = rs_val - rt_val
        self.registers[rd] = result
        print(f"SUB: R{rd} = {rs_val} - {rt_val} = {result}")
        self.pc += 4

    def slt(self, rd, rs, rt):
        if rd == 0:
            print("SLT: Ignoring write to R0")
            self.pc += 4
            return
        rs_val = self.registers[rs]
        rt_val = self.registers[rt]
        result = 1 if rs_val < rt_val else 0
        self.registers[rd] = result
        print(f"SLT: R{rd} = 1 if R{rs}({rs_val}) < R{rt}({rt_val}) else 0 → {result}")
        self.pc += 4

    def bne(self, rs, rt, offset):
        rs_val = self.registers[rs]
        rt_val = self.registers[rt]
        if rs_val != rt_val:
            new_pc = self.pc + 4 + (offset * 4)
            print(f"BNE: R{rs}({rs_val}) != R{rt}({rt_val}), PC → {new_pc}")
            self.pc = new_pc
        else:
            print(f"BNE: R{rs}({rs_val}) == R{rt}({rt_val}), PC → {self.pc + 4}")
            self.pc += 4

    def j(self, target):
        new_pc = target * 4
        print(f"J: PC ← {new_pc}")
        self.pc = new_pc

    def jal(self, target):
        # Convert target from instruction index to byte address
        new_pc = target * 4
        if 7 < 32:  # Ensure R7 is a valid register
            self.registers[7] = self.pc + 4  # Save return address
            print(f"JAL: R7 ← {self.pc + 4}, PC ← {target * 4}")
        self.pc = new_pc

    def lw(self, rt, rs, offset):
        address = self.registers[rs] + offset
        value = self.cache.read(address, self.memory_bus)
        if rt != 0:
            self.registers[rt] = value
            print(f"LW: R{rt} ← MEM[{address}] = {value}")
        else:
            print("LW: Ignoring write to R0")
        self.pc += 4

    def sw(self, rt, rs, offset):
        address = self.registers[rs] + offset
        value = self.registers[rt]
        self.cache.write(address, value, self.memory_bus)
        print(f"SW: MEM[{address}] ← R{rt}({value})")
        self.pc += 4
        
        
    def beq(self, rs, rt, offset):
        rs_val = self.registers[rs]
        rt_val = self.registers[rt]
        if rs_val == rt_val:
            new_pc = self.pc + 4 + (offset * 4)
            print(f"BEQ: R{rs}({rs_val}) == R{rt}({rt_val}), PC → {new_pc}")
            self.pc = new_pc
        else:
            print(f"BEQ: R{rs}({rs_val}) != R{rt}({rt_val}), PC → {self.pc + 4}")
            self.pc += 4

    def or_(self, rd, rs, rt):
        if rd == 0:
            print("OR: Ignoring write to R0")
            self.pc += 4
            return
        rs_val = self.registers[rs]
        rt_val = self.registers[rt]
        result = rs_val | rt_val
        self.registers[rd] = result
        print(f"OR: R{rd} = {rs_val} | {rt_val} = {result}")
        self.pc += 4

    def and_(self, rd, rs, rt):
        if rd == 0:
            print("AND: Ignoring write to R0")
            self.pc += 4
            return
        rs_val = self.registers[rs]
        rt_val = self.registers[rt]
        result = rs_val & rt_val
        self.registers[rd] = result
        print(f"AND: R{rd} = {rs_val} & {rt_val} = {result}")
        self.pc += 4

    def sll(self, rd, rt, shamt):
        if rd == 0:
            print("SLL: Ignoring write to R0")
            self.pc += 4
            return
        rt_val = self.registers[rt]
        result = rt_val << shamt
        self.registers[rd] = result
        print(f"SLL: R{rd} = R{rt}({rt_val}) << {shamt} = {result}")
        self.pc += 4

    def srl(self, rd, rt, shamt):
        if rd == 0:
            print("SRL: Ignoring write to R0")
            self.pc += 4
            return
        rt_val = self.registers[rt]
        result = rt_val >> shamt
        self.registers[rd] = result
        print(f"SRL: R{rd} = R{rt}({rt_val}) >> {shamt} = {result}")
        self.pc += 4

    def cache_instruction(self, code):
        if code == 0:
            self.cache.turn_off()
            print("CACHE: Cache turned off")
        elif code == 1:
            self.cache.turn_on()
            print("CACHE: Cache turned on")
        elif code == 2:
            self.cache.flush()
            print("CACHE: Cache flushed")
        self.pc += 4

    def halt(self):
        print("HALT: Execution terminated")
        self.running = False
        self.pc += 4