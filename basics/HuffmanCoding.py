
import os
from collections import Counter
import heapq


class HeapNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, HeapNode):
            return False
        return self.freq == other.freq


class HuffmanCoding:

    def __init__(self, path):
        self.path = path
        self.heap = []
        self.codes = {}
        self.reverse_codes = {}

    @staticmethod
    def make_freq_dict(text):
        # calc freq and return
        c = Counter(list(text))
        return c

    def make_heap(self, frequency):
        for k, v in frequency.items():
            node = HeapNode(char=k, freq=v)
            heapq.heappush(self.heap, node)

    def merge_codes(self):
        # build huffman tree, save root node in heap
        while len(self.heap) > 1:
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)
            merged = HeapNode(char=None, freq=node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2
            heapq.heappush(self.heap, merged)

    def make_code_helper(self, node, current_code):
        if node is None:
            return

        if node.char is not None:
            self.codes[node.char] = current_code
            self.reverse_codes[current_code] = node.char

        self.make_code_helper(node.left, current_code + "0")
        self.make_code_helper(node.right, current_code + "1")

    def make_codes(self):
        # make codes for characters and save
        root = heapq.heappop(self.heap)
        current_code = ""
        self.make_code_helper(root, current_code)

    def get_encoded_text(self, text):
        # replace chars with code and returns
        encoded = ""
        for char in text:
            encoded += self.codes[char]
        return encoded

    def pad_encoded_text(self, encoded_text):
        # pad encoded text and return
        extra_padding = 8 - (len(encoded_text) % 8)
        for i in range(extra_padding):
            encoded_text += "0"

        padded_info = "{0:08b}".format(extra_padding)
        return padded_info + encoded_text

    def get_byte_array(self, padded_encoded_text):
        # convert bits into bytes. Returns byte array
        b = bytearray()
        for i in range(0, len(padded_encoded_text), 8):
            byte = padded_encoded_text[i:i+8]
            b.append(int(byte, 2))
        return b

    def compress(self):
        fname, ext = os.path.splitext(self.path)
        output_path = fname + ".bin"

        with open(self.path, "r") as f, open(output_path, "wb") as o:
            text = f.read().rstrip()
            freq = self.make_freq_dict(text)
            self.make_heap(freq)
            self.merge_codes()
            self.make_codes()

            encoded_text = self.get_encoded_text(text)
            padded_encoded_text = self.pad_encoded_text(encoded_text)

            b = self.get_byte_array(padded_encoded_text)
            o.write(bytes(b))

    def remove_padding(self, bit_string):
        padded_info = bit_string[:8]
        extra_padding = int(padded_info, 2)

        bit_string = bit_string[8:]
        encoded_text = bit_string[:-extra_padding]

        return encoded_text

    def decode_text(self, encoded_text):
        # decode and return
        current_code = ""
        decoded_text = ""
        for bit in encoded_text:
            current_code += bit
            if current_code in self.reverse_codes:
                char = self.reverse_codes[current_code]
                decoded_text += char
                current_code = ""
        return decoded_text

    def decompress(self, input_path):
        fname, ext = os.path.splitext(input_path)
        output_path = fname + "_decompress" + ".txt"
        with open(input_path, "rb") as i, open(output_path, "w") as out:
            bit_string = ""
            byte = i.read(1)
            while len(byte) > 0:
                _byte = ord(byte)
                bits = bin(_byte)[2:].rjust(8, '0')
                bit_string += bits
                byte = i.read(1)

            encoded_txt = self.remove_padding(bit_string)
            txt = self.decode_text(encoded_txt)
            out.write(txt)

        print("Decompress at {}".format(output_path))


if __name__ == '__main__':
    huff = HuffmanCoding("./Tries.py")
    huff.compress()
    huff.decompress("./Tries.bin")
