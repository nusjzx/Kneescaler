import gzip
import shutil

def gzip_compression(input_file, output_file, num_iterations):
    for i in range(10):
        with open(input_file, 'rb') as f_in, gzip.open(output_file, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

# Example usage:
# Compress 'input.txt' multiple times and overwrite 'output.txt.gz' each time (10 iterations).
# gzip_compression('input.txt', 'output.txt.gz')
