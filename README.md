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
   git clone https://github.com/kelvinmendoza59/cpu-simulator.git
   cd cpu-simulator


Set up the project:

No external dependencies are required.

Verify the project structure:

cpu_simulator/
├── src/
├── data/
├── tests/
├── README.md
├── requirements.txt
└── main.py
Usage
Running the Simulator
Place your instruction and data files in the data/ directory:

instruction_input.txt: Contains MIPS instructions.

data_input.txt: Contains initial memory values.

Run the simulator:

python main.py

Example Input Files

data_input.txt
0, 10
4, 20
8, 30


instruction_input.txt

ADD, R1, R2, R3
ADDI, R4, R5, 100
LW, R6, 0(R1)
SW, R7, 4(R2)
HALT

Example Output

Fetch: PC=0, Instruction={'op': 'ADD', 'operands': [1, 2, 3]}
ADD: R1 = 0 + 0 = 0

Fetch: PC=4, Instruction={'op': 'ADDI', 'operands': [4, 5, 100]}
ADDI: R4 = 0 + 100 = 100

Fetch: PC=8, Instruction={'op': 'LW', 'operands': [6, 1, 0]}
LW: R6 ← MEM[0] = 10

Fetch: PC=12, Instruction={'op': 'SW', 'operands': [7, 2, 4]}
SW: MEM[4] ← R7(0)

Fetch: PC=16, Instruction={'op': 'HALT', 'operands': []}
HALT: Execution terminated

Final registers:
R1: 0
R4: 100
R6: 10

Memory contents:
Address 0: 10
Address 4: 0
Address 8: 30


Input Files

instruction_input.txt

Each line contains a MIPS instruction in the format:

<INSTRUCTION>,<ARG_1>,<ARG_2>,...,<ARG_n>

Example:

ADD, R1, R2, R3
LW, R4, 8(R5)
HALT

data_input.txt

Each line contains a memory address and its initial value:


<ADDRESS>,<VALUE>


Example:

0, 10
4, 20
8, 30

Output

The simulator logs each stage of instruction processing (fetch, decode, execute).

After execution, it prints:

Final register values.

Final memory contents.

Testing
To run unit tests:

python -m unittest discover tests/


Contributing
Fork the repository.

Create a new branch:

git checkout -b feature/your-feature-name
Commit your changes:

git commit -m "Add your feature"
Push to the branch:

git push origin feature/your-feature-name
Open a pull request.

License
This project is the property of Mendozabyte Solutions and is licensed under the MIT License. See LICENSE for details.

Screenshots
Installation

Description: Running git clone and navigating to the project directory.

Execution

Description: Running python main.py and viewing the output in the terminal.



---

### **License File (`LICENSE`)**
Create a `LICENSE` file in the root directory with the following content:

```

Copyright (c) 2024 Mendozabyte Solutions

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

