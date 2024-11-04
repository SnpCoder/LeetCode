import re

# 定义小语言的关键字和符号表，关键字和符号 ID 不同
keywords = {
    "if": 1,
    "else": 2,
    "int": 3,
    "char": 4,
    "while": 5,
    "return": 6,
    "void": 7,
    "float": 8,
    "double": 9,
    "for": 10,
    "do": 11,
    "switch": 12,
    "case": 13,
    "break": 14,
    "continue": 15,
    "default": 16,
    "sizeof": 17,
    "struct": 18,
    "typedef": 19,
    "union": 20,
    "enum": 21,
    "const": 22,
    "static": 23,
    "extern": 24,
    "register": 25,
    "volatile": 26,
    "signed": 27,
    "unsigned": 28,
    "short": 29,
    "long": 30,
}
symbols = {
    "=": 100,
    "+": 101,
    "-": 102,
    "*": 103,
    "/": 104,
    "(": 105,
    ")": 106,
    "{": 107,
    "}": 108,
    "<": 109,
    ">": 110,
    ";": 111,
    "<=": 112,
    ">=": 113,
    "==": 114,
    "!=": 115,
    "&&": 116,
    "||": 117,
}
preprocessors = {"#include": 200}  # 为预处理指令分配特殊ID，200表示预处理指令类型

# 定义正则表达式模式，用于标记关键字、标识符、数字、符号、预处理指令和头文件
token_pattern = re.compile(
    r"(#include\b|<[a-zA-Z_][\w.]*>|"  # 预处理指令和头文件
    r"\bif\b|\belse\b|\bint\b|\bchar\b|\bwhile\b|\breturn\b|\bvoid\b|\bfloat\b|\bdouble\b|\bfor\b|\bdo\b|\bswitch\b|\bcase\b|\bbreak\b|\bcontinue\b|\bdefault\b|\bsizeof\b|\bstruct\b|\btypedef\b|\bunion\b|\benum\b|\bconst\b|\bstatic\b|\bextern\b|\bregister\b|\bvolatile\b|\bsigned\b|\bunsigned\b|\bshort\b|\blong\b|"  # 更多关键字
    r"[a-zA-Z_]\w*|"  # 标识符
    r"\d+|"  # 数字
    r"<=|>=|==|!=|&&|\|\||\+|\-|\*|/|=|<|>|;|\(|\)|{|})"  # 运算符和符号，包括多字符符号
)


# 用于分类每个标记的函数
def classify_token(token, output_file):
    if token in preprocessors:
        output_file.write(f"( {token} -> 预处理指令 ID {preprocessors[token]} )\n")
    elif re.match(r"<[a-zA-Z_][\w.]*>", token):  # 匹配头文件
        output_file.write(f"( {token} -> 头文件 )\n")
    elif token in keywords:
        output_file.write(f"( {token} -> 关键字 ID {keywords[token]} )\n")
    elif token in symbols:
        output_file.write(f"( {token} -> 符号 ID {symbols[token]} )\n")
    elif token.isdigit():
        output_file.write(f"( {token} -> 数字 )\n")
    elif re.match(r"^[a-zA-Z_]\w*$", token):
        output_file.write(f"( {token} -> 标识符 )\n")
    else:
        output_file.write(f"( {token} -> 未定义的符号 )\n")


# 主函数，对输入的源代码进行词法分析并输出到文件
def lexical_analyze(input_filename, output_filename):
    with open(input_filename, "r", encoding="utf-8") as file:
        source_code = file.read()
    tokens = token_pattern.findall(source_code)

    with open(output_filename, "w", encoding="utf-8") as output_file:
        for token in tokens:
            classify_token(token, output_file)


# 测试词法分析器
if __name__ == "__main__":
    input_filename = "lexical_analyzer_test.txt"  # 输入文件名
    output_filename = "lexical_analyzer_out.txt"  # 输出文件名
    lexical_analyze(input_filename, output_filename)
