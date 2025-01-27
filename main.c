#include <stdio.h>

typedef struct {
    int registers[32];
    int pc;
    int running;
} CPU;

void add(CPU *cpu, int rd, int rs, int rt) {
    if (rd != 0) {
        cpu->registers[rd] = cpu->registers[rs] + cpu->registers[rt];
    }
    cpu->pc += 4;
}

int main() {
    CPU cpu = {0};
    cpu.registers[2] = 5;
    cpu.registers[3] = 10;
    add(&cpu, 1, 2, 3);
    printf("R1 = %d\n", cpu.registers[1]);
    return 0;
}