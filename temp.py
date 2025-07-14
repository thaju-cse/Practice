#quick sort algorithm
#hello world program
class quicksort:
	def __init__(self, array):
		self.array = array

	def sort(self):
		self._quicksort(0, len(self.array) - 1)

	def _quicksort(self, low, high):
		if low < high:
			pivot_index = self._partition(low, high)
			self._quicksort(low, pivot_index - 1)
			self._quicksort(pivot_index + 1, high)

	def _partition(self, low, high):
		pivot = self.array[high]
		i = low - 1
		for j in range(low, high):
			if self.array[j] <= pivot:
				i += 1
				self.array[i], self.array[j] = self.array[j], self.array[i]
		self.array[i + 1], self.array[high] = self.array[high], self.array[i + 1]
		return i + 1
class insertion_sort:
	def __init__(self, array):
		self.array = array

	def sort(self):
		for i in range(1, len(self.array)):
			key = self.array[i]
			j = i - 1
			while j >= 0 and self.array[j] > key:
				self.array[j + 1] = self.array[j]
				j -= 1
			self.array[j + 1] = key
class bubble_sort:
	def __init__(self, array):
		self.array = array

	def sort(self):
		n = len(self.array)
		for i in range(n):
			for j in range(0, n-i-1):
				if self.array[j] > self.array[j+1]:
					self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
	
class binary_sort:
    def __init__(self, array):
        self.array = array

    def sort(self):
        self._binary_sort(0, len(self.array) - 1)

    def _binary_sort(self, low, high):
        if low < high:
            mid = (low + high) // 2
            self._binary_sort(low, mid)
            self._binary_sort(mid + 1, high)
            self._merge(low, mid, high)

    def _merge(self, low, mid, high):
        left = self.array[low:mid+1]
        right = self.array[mid+1:high+1]
        i = j = 0
        k = low

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                self.array[k] = left[i]
                i += 1
            else:
                self.array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            self.array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            self.array[k] = right[j]
            j += 1
            k += 1

