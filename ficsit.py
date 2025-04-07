# Соединитель отсортированных блоков в выходной конвеер

class FicsitBlockMerger:
	def Sort(self):
		pass
	
    

# Сортировщик блоков

class FicsitBlockSorter:

	def Sort(self, alist):
		if len(alist) <= 1:
			return alist
		self.qsort(alist, 0, len(alist) - 1)


	def qsort(self, alist, start, end):
		core = alist[end]
		mid = start
		if start < end:
			for i in range(start, end + 1):
				if alist[i] <= core:
					alist[i], alist[mid] = alist[mid], alist[i]
					if i != end:
						mid += 1
			self.qsort(alist, start, mid - 1)
			self.qsort(alist, mid + 1, end)
		return alist
	


# Класс для работы с бинарными файлами

class FicsitPipelineIO:
	def ReadBlock(self):
		pass
	def WriteBlock(self):
		pass
