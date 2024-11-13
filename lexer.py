#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

KEYWORD_LIST = [
    "if",
    "else",
    "while",
    "break",
    "continue",
    "for",
    "double",
    "int",
    "float",
    "long",
    "short",
    "switch",
    "case",
    "return",
    "void",
]

SEPARATOR_LIST = ["{", "}", "[", "]", "(", ")", "~", ",", ";", ".", "?", ":"]

OPERATOR_LIST = [
    "+",
    "++",
    "-",
    "--",
    "+=",
    "-=",
    "*",
    "*=",
    "%",
    "%=",
    "->",
    "|",
    "||",
    "|=",
    "/",
    "/=",
    ">",
    "<",
    ">=",
    "<=",
    "=",
    "==",
    "!=",
    "!",
]

CATEGORY_DICT = {
    "double": 265,
    "int": 266,
    "break": 268,
    "else": 269,
    "switch": 271,
    "case": 272,
    "char": 276,
    "return": 278,
    "float": 281,
    "continue": 284,
    "for": 285,
    "void": 287,
    "do": 292,
    "if": 293,
    "while": 294,
    "static": 295,
    "{": 299,
    "}": 300,
    "[": 301,
    "]": 302,
    "(": 303,
    ")": 304,
    "~": 305,
    ",": 306,
    ";": 307,
    "?": 310,
    ":": 311,
    "<": 314,
    "<=": 315,
    ">": 316,
    ">=": 317,
    "=": 318,
    "==": 319,
    "|": 320,
    "||": 321,
    "|=": 322,
    "^": 323,
    "^=": 324,
    "&": 325,
    "&&": 326,
    "&=": 327,
    "%": 328,
    "%=": 329,
    "+": 330,
    "++": 331,
    "+=": 332,
    "-": 333,
    "--": 334,
    "-=": 335,
    "->": 336,
    "/": 337,
    "/=": 338,
    "*": 339,
    "*=": 340,
    "!": 341,
    "!=": 342,
    "ID": 256,
    "INT10": 346,
    "FLOAT": 347,
    "STRING": 351,
    "//": 360,
}

current_row = -1
current_line = 0
input_str = []


def is_keyword(s):
    return s in KEYWORD_LIST


def is_separator(s):
    return s in SEPARATOR_LIST


def is_operator(s):
    return s in OPERATOR_LIST


def get_cate_id(s):
    return CATEGORY_DICT[s]


def getchar():
    global current_row
    global current_line
    current_row += 1

    if current_row == len(input_str[current_line]):
        current_line += 1
        current_row = 0

    if current_line == len(input_str):
        return "SCANEOF"

    return input_str[current_line][current_row]


def ungetc():
    global current_row
    global current_line
    current_row = current_row - 1
    if current_row < 0:
        current_line = current_line - 1
        current_row = len(input_str[current_row]) - 1
    return input_str[current_line][current_row]


def read_source_file(file):
    global input_str
    with open(file, "r") as f:
        input_str = f.readlines()


def lexical_error(msg, line=None, row=None):
    if line is None:
        line = current_line + 1
    if row is None:
        row = current_row + 1
    print(f"{line}:{row} Lexical error: {msg}")


def scanner():
    current_char = getchar()

    # 文件结束标记
    if current_char == "SCANEOF":
        return ("SCANEOF", "", "")

    # 跳过空白字符
    if current_char.strip() == "":
        return

    # 处理数字
    if current_char.isdigit():
        int_value = 0
        while current_char.isdigit():
            int_value = int_value * 10 + int(current_char)
            current_char = getchar()

        # 检查是否有非法标识符，例如“10abc”
        if current_char.isalpha() or current_char == "_":
            lexical_error("非法标识符：标识符不能以数字开头")
            while (
                current_char.isalpha() or current_char.isdigit() or current_char == "_"
            ):
                current_char = getchar()
            return None

        if current_char.isalpha() or current_char == "_":
            # 发现以数字开头，后面跟着字母或下划线，这是非法标识符
            invalid_token = str(int_value) + current_char
            while current_char.isalnum() or current_char == "_":
                current_char = getchar()
                invalid_token += current_char
                # current_char = getchar()
            if current_char == ".":
                # invalid_token += current_char
                # 继续读取小数点后面的部分
                current_char = getchar()  # 先读取小数点后的第一个字符
                while current_char.isdigit() or current_char.isalnum():
                    invalid_token += current_char
                    current_char = getchar()  # 继续读取下一个字符
                # 退出循环后，将最后一个非数字字符放回去
                ungetc()
                # 抛出“非法浮点类型”的错误
                lexical_error("invalid float type: " + invalid_token)
            else:
                ungetc()
                lexical_error("invalid identifier: " + invalid_token)
            return None

        if current_char != ".":
            ungetc()
            return ("INT", int_value, get_cate_id("INT10"))

        # 处理浮点数
        float_value = str(int_value) + "."
        current_char = getchar()
        while current_char.isdigit():
            float_value += current_char
            current_char = getchar()
        ungetc()
        return ("FLOAT", float_value, get_cate_id("FLOAT"))

    # 处理标识符和关键字
    if current_char.isalpha() or current_char == "_":
        string = ""
        while current_char.isalpha() or current_char.isdigit() or current_char == "_":
            string += current_char
            current_char = getchar()

        # 检测非法字符，例如“abc$”
        if not (
            current_char.isalpha()
            or current_char.isdigit()
            or current_char == "_"
            or current_char == "SCANEOF"
        ):
            lexical_error(f"非法标识符：包含非法字符 '{current_char}'")
            # 跳过非法字符，避免干扰后续扫描
            while (
                current_char.isalpha()
                or current_char.isdigit()
                or current_char == "_"
                or not current_char.strip()
            ):
                current_char = getchar()
            return None

        # 检查是否为关键字
        ungetc()
        if is_keyword(string):
            return (string, "", get_cate_id(string))
        else:
            return ("ID", string, get_cate_id("ID"))

    # 处理字符串字面量
    if current_char == '"':
        str_literal = ""
        line = current_line + 1
        row = current_row + 1

        current_char = getchar()
        while current_char != '"':
            str_literal += current_char
            current_char = getchar()
            if current_char == "SCANEOF":
                lexical_error('missing terminating "', line, row)
                current_line = line
                current_row = row
                return ("SCANEOF", "", "")
        return ("STRING_LITERAL", str_literal, get_cate_id("STRING"))

    # 新增字符字面量逻辑
    if current_char == "'":
        char_literal = ""
        current_char = getchar()

        # 检查字符字面量是否格式正确
        if current_char == "SCANEOF" or current_char == "'":
            lexical_error("empty character literal")
            return None

        char_literal = current_char  # 保存字符内容
        next_char = getchar()  # 检查字符后的内容

        # 如果后面是第二个字符，继续读取，检查是否只有一个字符
        if next_char != "'":
            # 如果下一个字符不是单引号，继续读取并报错
            char_literal += next_char
            while True:
                next_char = getchar()
                if next_char == "'":
                    lexical_error(
                        "invalid character literal (multiple characters): "
                        + char_literal
                    )
                    return None
                elif next_char == "SCANEOF":
                    lexical_error("unterminated character literal")
                    return None
                char_literal += next_char  # 继续累积非法字符

        # 如果字符字面量格式正确（只有一个字符并以单引号结束）
        return ("CHAR_LITERAL", char_literal, get_cate_id("char"))

    if current_char == "/":
        next_char = getchar()
        line = current_line + 1
        row = current_row + 1
        if next_char == "*":
            # 处理多行注释 /* ... */
            comment = ""
            next_char = getchar()
            while True:
                if next_char == "SCANEOF":
                    lexical_error("unterminated /* comment", line, row)
                    return ("SCANEOF", "", "")
                if next_char == "*":
                    end_char = getchar()
                    if end_char == "/":
                        return None  # 忽略注释内容
                    if end_char == "SCANEOF":
                        lexical_error("unterminated /* comment", line, row)
                        return ("SCANEOF", "", "")
                comment += next_char
                next_char = getchar()
        else:
            # 处理单字符操作符 "/"
            ungetc()
            op = current_char
            current_char = getchar()
            if is_operator(current_char):
                op += current_char
                next_char = getchar()
                while next_char != "\n" and next_char != "SCANEOF":
                    next_char = getchar()
                if next_char == "\n":
                    return None
                elif next_char == "SCANEOF":  # the end
                    return ("SCANEOF", "", "")
                return None
            else:
                ungetc()
            return ("OP", op, get_cate_id(op))

    # 处理分隔符
    if is_separator(current_char):
        return ("SEP", current_char, get_cate_id(current_char))

    # 处理操作符
    if is_operator(current_char):
        op = current_char
        current_char = getchar()
        if is_operator(current_char):
            op += current_char
        else:
            ungetc()
        return ("OP", op, get_cate_id(op))

    # 处理未知字符
    lexical_error(f"unknown character: {current_char}")
    return None


def main():
    # file_name = sys.argv[1]
    file_name = "lexical_analyzer_testcase3.txt"
    read_source_file(file_name)

    # 打开 out.txt 文件，并将标准输出重定向到该文件
    with open("out.txt", "w") as f:
        sys.stdout = f  # 重定向输出

        while True:
            r = scanner()
            if r is not None:
                if r[0] == "SCANEOF":
                    break
                print(r)

        sys.stdout = sys.__stdout__  # 恢复标准输出


if __name__ == "__main__":
    main()


# python lexer.py lexical_analyzer_testcase3.txt
