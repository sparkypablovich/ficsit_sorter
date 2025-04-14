import struct
import os

# Соединитель отсортированных блоков в выходной конвеер

class FicsitBlockMerger:

	result_filename = 'new_left.bin'

	def Merge(self, leftfile, rightfile):
		with open(leftfile) as lfile, open(rightfile) as rfile, open('result.txt', 'w') as res:
			left = lfile.read(4)
			right = rfile.read(4)
			while True:
				
				if left == '':
					self.writer(right)
					right = rfile.read()
					self.writer(right)
					break
				if right == '':
					self.writer(left)
					left = lfile.read()
					self.writer(left)
					break
				
				if int(left) <= int(right):
					self.writer(left)
					left = lfile.read(1)
				else:
					self.writer(right)
					right = rfile.read(1)
		return self.result_filename

	def writer(self, number):
		with open(self.result_filename, 'w+') as output:
			output.write(number)

	
    

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
	
	def __init__(self, filename, block_size=4096): # block_size=32000
		self.__filename = filename
		self.__block_size = block_size

	def ReadBlock(self):
		with open(self.__filename, 'rb') as file:
			while True:
				block = file.read(self.__block_size)
				if not block:
					break  # End of file
				# Process the block here
				yield block  # or do something else with the block



	__leftmergefile = ''
	__rightmergefile = ''

	def WriteBlock(self, block):
		if self.__leftmergefile == '':
			filename = 'left.bin'
			self.__leftmergefile = filename
		else:
			filename = 'right.bin'
			self.__rightmergefile = filename

		with open(filename, 'wb') as file:
			file.write(block)


	def ReadyMerge(self):
		return self.LeftMergeFile() != '' and self.RightMergeFile() != ''
		
	def SetMergedFile(self, filename):
		self.__leftmergefile = filename
		os.rename(filename, 'left.bin')
		self.__rightmergefile = ''

	def LeftMergeFile(self):
		return self.__leftmergefile

	def RightMergeFile(self):
		return self.__rightmergefile