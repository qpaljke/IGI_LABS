import re
import zipfile
import numpy as np


class TextAnalyzer:
    def __init__(self, filename):
        self.filename = filename
        self.text = self.read_text_from_file()

    def read_text_from_file(self):
        with open(self.filename, 'r') as file:
            return file.read()

    def sentences_count(self):
        return self.narrative_sentences_count() + self.interrogative_sentences_count() + self.imperative_sentences_count()

    def narrative_sentences_count(self):
        dots = re.findall(r'\.', self.text)
        return len(dots)

    def interrogative_sentences_count(self):
        question_marks = re.findall(r'\?', self.text)
        return len(question_marks)

    def imperative_sentences_count(self):
        exclamation_marks = re.findall(r'\!', self.text)
        return len(exclamation_marks)

    def avg_word_len(self):
        words = re.findall(r'\b\w+\b', self.text)
        return np.round(sum(len(word) for word in words) / len(words), 2)

    def avg_sentence_len(self):
        return len(self.text) / self.sentences_count()

    def smileys_count(self):
        smileys = re.findall(r'[;:]-*[(\])\[]+', self.text)
        return len(smileys)

    @staticmethod
    def is_ip_address(string):
        return re.match(r'^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', string) is not None

    def lower_and_digits(self):
        sp_str = self.text.split()
        res_str = ''
        for word in sp_str:
            if re.match(r'\b[a-z0-9]+\b', word):
                res_str += word
                res_str += ' '
        return res_str.rstrip()

    def lowercase_count(self):
        return sum(1 for char in self.text if char.islower())

    def find_first_v(self):
        sp_str = self.text.split()
        for word in sp_str:
            if re.match(r'\b\w*v\w*\b', word):
                return sp_str.index(word)
        return -1

    @staticmethod
    def exclude_s_words(string: str):
        sp_str = string.split()
        res_str = ''
        for word in sp_str:
            if not re.match(r'\bS\w*', string, re.IGNORECASE):
                res_str += word
                res_str += ' '
        return res_str.rstrip()

    def archive(self):
        with zipfile.ZipFile('task2/archive.zip', 'w') as z:
            z.write(self.filename)
        with zipfile.ZipFile('task2/archive.zip', 'r') as z:
            return z.getinfo(self.filename)


def run_task():
    a = TextAnalyzer('task2/file.txt')
    info = a.archive()
    print(f'Sentences count: {a.sentences_count()}\n'
          f'Narrative sentences count: {a.narrative_sentences_count()}\n'
          f'Interrogative sentences count: {a.interrogative_sentences_count()}\n'
          f'Imperative sentences count: {a.imperative_sentences_count()}\n'
          f'Average word length: {a.avg_word_len()}\n'
          f'Average sentence length: {a.avg_sentence_len()}\n'
          f'Smileys count: {a.smileys_count()}\n'
          f'Index first word with "v" in it: {a.find_first_v()}\n'
          f'Lowercase letters count: {a.lowercase_count()}\n'
          f'Words that contain digits and lowercase letters: {a.lower_and_digits()}\n'
          f'Is IP-address 255.255.255.255: {a.is_ip_address("255.255.255.255")}\n'
          f'              198.1sd.23a.110: {a.is_ip_address("198.1.a.0")}\n'
          f'              300.300.300.030: {a.is_ip_address("300.300.300.030")}\n'
          f'String without words that starts with "s": {a.exclude_s_words("ipsum nisi est amet sint ut alias magni.")}\n'
          f'Archive info: {info.filename}, {info.compress_size}, {info.compress_type}')
