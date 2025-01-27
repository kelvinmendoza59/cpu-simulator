# CPU Simulator Project

This project simulates a simple CPU that processes MIPS instructions. It includes components like a Memory Bus, Cache, and CPU, and can execute instructions such as `ADD`, `SUB`, `LW`, `SW`, `J`, and more.

---

## Table of Contents
1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Input Files](#input-files)
5. [Output](#output)
6. [Testing](#testing)
7. [Contributing](#contributing)
8. [License](#license)

---

## Features
- Simulates a CPU with registers, memory, and cache.
- Supports MIPS instructions:
  - Arithmetic: `ADD`, `ADDI`, `SUB`, `SLT`
  - Control Flow: `BNE`, `J`, `JAL`
  - Memory Access: `LW`, `SW`
  - Cache Control: `CACHE` (enable/disable/flush)
  - Program Termination: `HALT`
- Detailed logging of CPU execution stages.

---

## Installation

### Prerequisites
- Python 3.8 or higher.
- Git (for version control).

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/@kelvinmendoza59/cpu-simulator.git
   cd cpu-simulator