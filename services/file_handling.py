import os
import sys


BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book = dict()


def _get_part_text(text: str, start: int, page_size: int):
    punctuation = {',', '.', '!', '?', ':', ';'}
    end = min(page_size + start, len(text))

    while end >= start:
        while text[end:][:1] in punctuation:
            end -= 1
        if text[end-1] in punctuation:
            break
        end -= 1
    page = text[start: end]
    return(page, len(page))


def prepare_book(path: str) -> None:
    with open(path, 'r', encoding='utf-8') as raw_book:
        prefix = ''
        page_num = 1
        text = prefix + raw_book.read(PAGE_SIZE)
        while text != '':
            page, len_page = _get_part_text(text, 0, PAGE_SIZE)
            book[page_num] = page.strip()
            page_num += 1

            prefix = text[len_page:]
            text = prefix + raw_book.read(PAGE_SIZE)
            

prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))
