from PyQt5.QtGui import QTextCharFormat, QSyntaxHighlighter
from PyQt5.QtCore import QRegExp, Qt
from PyQt5.QtGui import QColor

namespace = ["\\blist\\b", "\\bappend\\b", "\\bd_clear\\b",
             "\\blen\\b", "\\baddlist\\b", "\\bclear\\b",
             "\\bcount\\b", "\\binsert\\b", "\\breverse\\b",
             "\\bslice\\b", "\\blist_info\\b", "\\bl_swap\\b",
             "\\bdict\\b", "\\bd_set\\b", "\\bd_pop\\b", "\\bpop\\b",
             "\\bdict_info\\b", "\\bd_swap\b", "\\bd_keys\\b",
             "\\bd_get\\b", "\\bs_len\\b", "\\bs_slice\\b",
             "\\bto_str\\b", "\\bs_join\\b", "\\bs_lower\\b",
             "\\bs_title\\b", "\\bs_count\\b", "\\bstr_to_dict\\b",
             "\\bs_find\\b", "\\bs_split\\b", "\\bs_rfind\\b",
             "\\barray\\b", "\\bd_array\\b", "\\bt_array\\b",
             "\\bb_array\\b", "\\bbd_array\\b", "\\bD_array\\b",
             "\\bTD_array\\b", "\\bB_array\\b", "\\bBD_array\\b",
             "\\bin\\b", "\\bif\\b", "\\belse\\b", "\\bwhile\\b",
             "\\bto\\b", "\\bdownto\\b", "\\bfunc\\b", "\\boutput\\b",
             "\\bindex\\b", "\\bset\\b", "\\bsort\\b", "\\bto_list\\b",
             "\\bd_values\\b", "\\bs_concat\\b", "\\bs_upper\\b",
             "\\bs_swapcase\\b", "\\btd_array\\b", "\\bT_array\\b",
             "\\bfor\\b", "\\breturn\\b", "\\binclude\\b",
             "\\binput\\b", "\\bsize\\b", "\\bdet\\b", "badd",
             "\\bradd\\b", "\\brotate\\b", "\\btranspose\\b",
             "\\bmirror\\b", "\\bgauss\\b", "\\binv\\b",
             "\\bto_int\\b", "\\bto_float\\b", "\\bentrywise_mul\\b",
             "\\bsetitem\\b", "\\bgetitem\\b"]


operators = ["\\=", "\\+", "\\/", "\\-",
             "\\^", "\\*", "\\<", "\\>", "\\!", "\\%"]


brekets = ['\\(', "\\)", "\\[", "\\]", "\\{", "\\}", "\\|"]

numbers = ["\\b\\d+[.]?\\d*\\b"]


class Highlighter(QSyntaxHighlighter):
    def __init__(self, parent):
        super().__init__(parent)
        self.keywords = brekets + operators + namespace + numbers
        self.colors = ([QColor(128, 128, 0)] * len(brekets)
                       + [QColor(65, 105, 225)] * len(operators)
                       + [QColor(128, 0, 128)] * len(namespace)
                       + [QColor(128, 128, 0)] * len(numbers))

    def highlightBlock(self, text):
        for keyword, color in zip(self.keywords, self.colors):
            pattern = QRegExp(keyword)
            index = pattern.indexIn(text)
            while index >= 0:
                print("index====", index)
                length = pattern.matchedLength()
                self.setFormat(index, length, color)
                index = pattern.indexIn(text, index + length)
                if index == 0:
                    break
