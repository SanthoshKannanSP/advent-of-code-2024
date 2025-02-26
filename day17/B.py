with open("input.txt","r") as f:
    data = [line.strip() for line in f.readlines()]

registerA = int(data[0].lstrip("Register A: "))
registerB = int(data[1].lstrip("Register B: "))
registerC = int(data[2].lstrip("Register C: "))

program = data[4].lstrip("Program: ").split(",")

def comboOperand(operand,registers):
    if int(operand)<4:
        return int(operand)
    if operand == "4":
        return registers[0]
    if operand == "5":
        return registers[1]
    if operand == "6":
        return registers[2]

def adv(operand,registers, ip):
    operand = comboOperand(operand,registers)
    numerator = registers[0]
    denominator = 2**operand
    result = numerator//denominator
    registers[0] = result
    return ip+2,-1

def bxl(operand,registers,ip):
    result = registers[1] ^ int(operand)
    registers[1] = result
    return ip+2,-1

def bst(operand,registers,ip):
    operand = comboOperand(operand,registers)
    registers[1] = operand%8
    return ip+2,-1
    
def jnz(operand,registers,ip):
    if registers[0]==0:
        return ip+2,-1
    return int(operand),-1

def bxc(operand,registers,ip):
    registers[1] = registers[1] ^ registers[2]
    return ip+2,-1

def out(operand,registers,ip):
    operand = comboOperand(operand,registers)
    result = operand%8
    return ip+2,result

def bdv(operand,registers,ip):
    operand = comboOperand(operand,registers)
    numerator = registers[0]
    denominator = 2**operand
    result = numerator//denominator
    registers[1] = result
    return ip+2,-1
    
def cdv(operand,registers,ip):
    operand = comboOperand(operand,registers)
    numerator = registers[0]
    denominator = 2**operand
    result = numerator//denominator
    registers[2] = result
    return ip+2,-1

opcodeMap = {
    "0":adv,
    "1":bxl,
    "2":bst,
    "3":jnz,
    "4":bxc,
    "5":out,
    "6":bdv,
    "7":cdv
}


N = len(program)

def run_program(N,A):
    ip = 0
    output = []
    registers = [A,registerB,registerC]
    while ip+1<N:
        opcode = program[ip]
        operand = program[ip+1]
        excute = opcodeMap[opcode]
        ip,result = excute(operand,registers,ip)
        if result!=-1:
            output.append(str(result))
    return ",".join(output)

A = 0
for i in reversed(range(N)):
    A <<= 3
    expected_output = ",".join(program[i:])
    while run_program(N,A)!=expected_output:
        A+=1

print(A)