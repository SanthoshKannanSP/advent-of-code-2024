with open("input.txt","r") as f:
    data = [line.strip() for line in f.readlines()]

D = len(data)
values = dict()
index = 0
while data[index]:
    wire,value = data[index].split(": ")
    values[wire] = int(value)
    index+=1

gates = []
index+=1
while index<D:
    gates.append(data[index].split())
    index+=1

for gate in gates:
    if gate[0] > gate[2]:
        gate[0], gate[2] = gate[2], gate[0]

level1_gates = sorted([gate for gate in gates if gate[0][0] == 'x'])
level2_xor_gates = [gate for gate in gates if gate[1] == 'XOR' and gate not in level1_gates]
and_gates = [gate for gate in gates if gate[1] == 'AND']
or_gates = [gate for gate in gates if gate[1] == 'OR']
final_gates = sorted([gate for gate in gates if gate[4][0] == 'z'], key=lambda gate: gate[4])

wrong = set()
for i in range(45):
    xor_gate, and_gate = level1_gates[i * 2 + 1], level1_gates[i * 2]
    final_gate, final_wires = final_gates[i], [final_gates[i][0], final_gates[i][2]]

    if i == 0:
        if xor_gate != final_gate:
            wrong |= {xor_gate[4], final_gate[4]}
        carry_in = and_gate[4]
    else:
        xor_ab = xor_gate[4]
        xor2_operands = tuple(sorted((xor_ab, carry_in)))

        if final_gate not in level2_xor_gates:
            for gate in level2_xor_gates:
                if (gate[0], gate[2]) == xor2_operands:
                    wrong |= {final_gate[4], gate[4]}
                    final_gate = gate
                    break

        if carry_in not in final_wires and xor_ab in final_wires:
            wrong |= {carry_in, final_gate[0] if final_gate[0] != xor_ab else final_gate[2]}
        elif xor_ab not in final_wires and carry_in in final_wires:
            xor_ab = final_gate[0] if final_gate[0] != carry_in else final_gate[2]
            wrong |= {xor_gate[4], xor_ab}

        and_operands = tuple(sorted((final_gate[0], final_gate[2])))
        for gate in and_gates:
            if (gate[0], gate[2]) == and_operands:
                or_operand = gate[4]
                break

        or_operands = tuple(sorted((and_gate[4], or_operand)))
        for gate in or_gates:
            if (gate[0], gate[2]) == or_operands:
                break
            if or_operand in gate:
                wrong |= {and_gate[4], gate[0] if gate[0] != or_operand else gate[2]}
                break
            if and_gate[4] in gate:
                wrong |= {or_operand, gate[0] if gate[0] != and_gate[4] else gate[2]}
                break

        carry_in = gate[4]

print(','.join(sorted(wrong)))
