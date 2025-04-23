import struct
import os

# Соединитель отсортированных блоков в выходной конвеер
class FicsitBlockMerger:

	__result_filename = 'new_left.bin'

	def Merge(self, leftfile, rightfile):
		with open(leftfile, 'rb') as lfile, open(rightfile, 'rb') as rfile:
			left = lfile.read(4)
			right = rfile.read(4)
			while True:

				left_int = int.from_bytes(left, byteorder='little', signed=True)
				right_int = int.from_bytes(right, byteorder='little', signed=True)
				
				if left == b'':
					self.write(right)
					right = rfile.read()
					self.write(right)
					break
				if right == b'':
					self.write(left)
					left = lfile.read()
					self.write(left)
					break
				
				if left_int <= right_int:
					self.write(left)
					left = lfile.read(4)
				else:
					self.write(right)
					right = rfile.read(4)

		return self.__result_filename

	def write(self, number):
		with open(self.__result_filename, 'ab') as output:
			output.write(number)

# Сортировщик блоков
class FicsitBlockSorter:

	def Sort(self, alist):
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


# Класс для работы с бинарными файлами
class FicsitPipelineIO:
	
	__leftmergefile = ''
	__rightmergefile = ''

	def __init__(self, filename, block_size=4096):
		self.__filename = filename
		self.__block_size = block_size

	def ReadBlock(self):
		with open(self.__filename, 'rb') as file:
			while True:
				block = file.read(self.__block_size * 4)
				if not block:
					break
				unpacked = [int.from_bytes(block[i:i+4], byteorder='little', signed=True) for i in range(0, len(block), 4)]
				yield unpacked

	def WriteBlock(self, block):
		if self.__leftmergefile == '':
			filename = 'left.bin'
			self.__leftmergefile = filename
		else:
			filename = 'right.bin'
			self.__rightmergefile = filename

		packed = []
		for number in block:
			packed.append(int.to_bytes(number, length=4, byteorder='little', signed=True))
					
		packed_bytes = b''.join(packed)

		with open(filename, 'wb') as file:
			file.write(packed_bytes)


	def ReadyMerge(self):
		return self.LeftMergeFile() != '' and self.RightMergeFile() != ''
		
	def SetMergedFile(self, filename):
		os.remove('left.bin')
		os.rename(filename, 'left.bin')
		self.__leftmergefile = 'left.bin'
		self.__rightmergefile = ''

	def LeftMergeFile(self):
		return self.__leftmergefile

	def RightMergeFile(self):
		return self.__rightmergefile
	
	def RenameMergedFile(self):
		file = self.LeftMergeFile()
		os.rename(file, 'sorted_file.bin')
		os.remove('right.bin')