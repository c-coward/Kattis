from heapq import heappop as pop, heappush as push
from sys import stdin

def main():
	line = lambda : stdin.readline().split()
	n, k = map(int, line())

	# Patients
	patients = []
	# Accidents
	accidents = {}
	# Times
	times = []
	# Output list for fast printing
	outs = []

	# Read in input
	for _ in range(n):
		inp = line()
		if inp[0] == "1":
			_, t, name, s = inp
			patients.append(tup(int(s), int(t), name))
		elif inp[0] == "2":
			times.append(int(inp[1]))
		else:
			_, t, name = inp
			accidents[name] = int(t)

	# t values given in increasing order
	# Check the last time value to get the severity cost of EVERY patient
	# Because extra time added after the first time they can be served is equal for all patients,
	# Adding them as soon as they are available alleviates the need to update the cost later
	last_time = times[-1]
	for patient in patients:
		patient.s += (last_time - patient.t) * k

	# Use a heap to store all patients who can currently be served
	# Update the heap at each new serve-time	
	q = []
	# Index for the current patient
	i = 0
	for j in range(len(times)):
		curr_time = times[j]

		# Find all patients who can now be served at this time
		while (i < len(patients) and patients[i].t <= curr_time):
			push(q, patients[i])
			i += 1

		# Find the best patient to serve, or take a break if there are none
		while (q and q[0].name in accidents and accidents[q[0].name] <= curr_time):
			# Remove patients who have had accidents and must leave the clinic
			pop(q)

		if q:
			best = pop(q)
			outs.append(best.name)
		else:
			outs.append("doctor takes a break")

	# Print all output at once, helps for large output sizes
	print("\n".join(outs))

# Tuple class with updateable values for the heap
class tup:
	def __init__(self, s, t, name):
		self.s = s
		self.t = t
		self.name = name

	def __lt__(self, other):
		if self.s == other.s:
			return self.name < other.name
		return self.s > other.s

	def __str__(self):
		return f'({self.s}, {self.t}, {self.name})'

if __name__ == "__main__":
	main()