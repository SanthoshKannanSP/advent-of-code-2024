with open("input.txt","r") as f:
    data = [line.strip() for line in f.readlines()]

D = len(data)
values = dict()
index = 0
while data[index]:
    wire,value = data[index].split(": ")
    values[wire] = int(value)
    index+=1

def AND(input1,input2):
    return input1 & input2

def OR(input1,input2):
    return input1 | input2

def XOR(input1,input2):
    return input1 ^ input2

gateMap = {
    "AND":AND,
    "OR":OR,
    "XOR":XOR
}

gates = []

index+=1
while index<D:
    inputWires,outputWire = data[index].split(" -> ")
    input1,gate,input2 = inputWires.split()
    gates.append((input1,input2,gateMap[gate],outputWire))
    index+=1

index = 0
G = len(gates)

while G>0:
    index = 0
    while index<G:
        input1,input2,gate,outputWire = gates[index]
        if input1 in values and input2 in values:
            values[outputWire] = gate(values[input1],values[input2])
            gates.pop(index)
            index-=1
            G-=1
        index+=1

outputWires = [key for key in values.keys() if key[0]=="z"]

ans = ""
for wire in sorted(outputWires,reverse=True):
    ans += str(values[wire])

print(int(ans,2))