from huffman import HuffmanCoding
import sys

#Nombre del archivo a comprimir dentro de las comillas, ejemplo "0.csv"
path = ""

h = HuffmanCoding(path)

output_path = h.compress()
print("Compressed file path: " + output_path)

decom_path = h.decompress(output_path)
print("Decompressed file path: " + decom_path)
