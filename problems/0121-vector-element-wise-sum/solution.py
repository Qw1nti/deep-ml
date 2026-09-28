def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	sum_of_vectors = []
	# Return the element-wise sum of vectors 'a' and 'b'.
	# If vectors have different lengths, return -1.
	if len(a) != len(b):
		return [-1]
	else:
		for i in range(len(a)):
			sum_of_vectors.append(a[i] + b[i])
	
	return sum_of_vectors