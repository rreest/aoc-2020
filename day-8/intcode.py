from enum import Enum

# Code from last year's challenge
class OpStatus(Enum):
	DONE = 0
	NEED_INPUT = 1


class IntCode:
	def __init__(self, mem, uinput=[]):
		self.mem = mem.copy()
		self.mem.extend([0]*100000)
		self.original_mem = self.mem.copy()
		self.outputs = []
		self.uinput = uinput
		self.uinput_seq = 0
		self.position = 0
		self.relative_base = 0

	def get_mode(self, inst, pos):
		# 0 = position mode, 1 = immediate mode
		if pos + 1 < len(inst):
			return inst.copy()[::-1][pos + 1]
		return 0

	def get_param(self, inst, rpos, cpos):
		mode = self.get_mode(inst, cpos)
		if mode == 1:
			return self.mem[rpos + cpos]
		elif mode == 2:
			return self.mem[self.relative_base + self.mem[rpos + cpos]]
		else:
			return self.mem[self.mem[rpos + cpos]]

	def set_param(self, inst, rpos, cpos, val):
		mode = self.get_mode(inst, cpos)
		if mode == 0:
			self.mem[self.mem[rpos + cpos]] = val
		elif mode == 2:
			self.mem[self.relative_base + self.mem[rpos + cpos]] = val

	def compute(self, uinput=None, quiet=True):
		status = OpStatus.DONE
		while self.position < len(self.mem):
			inst = [int(n) for n in str(self.mem[self.position])]
			inst.insert(0, 0)
			opcode = int(str(inst[len(inst) - 2]) + str(inst[len(inst) - 1]))
			if opcode == 99:
				if not quiet:
					print("Halt!")
				break
			elif opcode == 1:
				# Addition
				a1 = self.get_param(inst, self.position, 1)
				a2 = self.get_param(inst, self.position, 2)
				# print("a1: {}".format(a1))
				# print("a2: {}".format(a2))
				self.set_param(inst, self.position, 3, a1 + a2)
			elif opcode == 2:
				a1 = self.get_param(inst, self.position, 1)
				a2 = self.get_param(inst, self.position, 2)
				self.set_param(inst, self.position, 3, a1 * a2)
			elif opcode == 3:
				if uinput is not None:
					self.set_param(inst, self.position, 1, uinput)
					uinput = None
				else:
					return OpStatus.NEED_INPUT
			elif opcode == 4:
				self.outputs.append(self.get_param(inst, self.position, 1))
			elif opcode == 5:
				if self.get_param(inst, self.position, 1):
					self.position = self.get_param(inst, self.position, 2)
				else:
					self.position += 3
			elif opcode == 6:
				if not self.get_param(inst, self.position, 1):
					self.position = self.get_param(inst, self.position, 2)
				else:
					self.position += 3
			elif opcode == 7:
				a1 = self.get_param(inst, self.position, 1) < self.get_param(
						inst, self.position, 2)
				self.set_param(inst, self.position, 3, a1)

			elif opcode == 8:
				a1 = self.get_param(inst, self.position, 1) == self.get_param(
						inst, self.position, 2)
				self.set_param(inst, self.position, 3, a1)
			elif opcode == 9:
				self.relative_base += self.get_param(inst, self.position, 1)
			else:
				print("Unknown opcode {}!".format(opcode))
				break

			if opcode in [1, 2, 7, 8]:
				self.position += 4
			elif opcode in [3, 4, 9]:
				self.position += 2

		return status

	def reset(self):
		self.mem = self.original_mem.copy()
		self.outputs = []
		self.position = 0

# Intcode 2020
def run(data):
    pos_hist, pos, accum, status = [], 0, 0, 0
    while pos < len(data):
        if pos in pos_hist:
            status = 2
            break

        pos_hist.append(pos)
        i, p = data[pos]
        if i == 'nop':
            pos += 1
        elif i == 'jmp':
            pos += int(p)
        elif i == 'acc':
            accum += int(p)
            pos += 1
   
        if pos == len(data):
            status = 1
            break

    return status, accum
