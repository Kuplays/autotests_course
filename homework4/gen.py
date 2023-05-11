def generate_seq(num, limit):
	for i in reversed(range(num, limit)):
		if i % 3 == 0:
			yield i

for num in generate_seq(10, 100):
	print(num)