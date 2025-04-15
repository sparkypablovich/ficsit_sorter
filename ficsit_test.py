import ficsit

def main():

	io = ficsit.FicsitPipelineIO('input.bin', 16)

	sorter = ficsit.FicsitBlockSorter()
	merger = ficsit.FicsitBlockMerger()

	for block_number, block in enumerate(io.ReadBlock()):
		print(f'>> Processing Block #{block_number}')
		sorter.Sort(block)
		io.WriteBlock(block)
		if io.ReadyMerge():
			merged_file = merger.Merge(io.LeftMergeFile(), io.RightMergeFile())
			io.SetMergedFile(merged_file)
	
	# TODO
	# io.SaveResultFile() # Сохранит результат в output.bin

main()