# тест для проверки одинаковости input.bin и output.bin

import ficsit

def main():

	io = ficsit.FicsitPipelineIO('input.bin')

	sorter = ficsit.FicsitBlockSorter()
	merger = ficsit.FicsitBlockMerger()

	while io.HasBlock():
		block = io.ReadBlock()
		sorter.Sort(block)
		io.WriteBlock(block)
		if io.ReadyMerge():
			merged_file = merger.Merge(io.LeftMergeFile(), io.RightMergeFile())
			io.SetMergedFile(merged_fle)

main()