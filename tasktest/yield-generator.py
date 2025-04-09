
import struct

def read_file_in_blocks(filename, block_size=4096):
    with open(filename, 'rb') as file:
        while True:
            block = file.read(block_size)
            if not block:
                break  # End of file
            # Process the block here
            yield block  # or do something else with the block


def main():

	# Example usage:
	input_file = "input.bin"
	chunk_size = 1024  # You can adjust this value (1024, 4096, 8192, etc.)

	for block_number, block_data in enumerate(read_file_in_blocks(input_file, chunk_size)):
		print(f"Block {block_number}: {len(block_data)} bytes")

		fmt = '<256i'  # < little-endian, 256 nubmers, i - 32-bit integer
		values = list(struct.unpack(fmt, block_data))
		print(values[:10]) 
          
main()