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
    r"(//.*|/\*[\s\S]*?\*/|"  # 单行注释和多行注释
    r"#include\b|<\w+\.h>|"  # 预处理指令和头文件
    r"\b\d+[a-zA-Z_]\w*\b|"  # 无效标识符：数字开头的字母组合
    r"[a-zA-Z_]\w*[^a-zA-Z0-9_\s;]+|"  # 含非法字符的标识符（如包含 $ 的 abc$）
    r"\b[a-zA-Z_]\w*\b|"  # 合法标识符
    r"-?\d+\.\d+|-?\d+|"  # 支持带符号的浮点数和整数
    r"'[a-zA-Z0-9]'|"  # 单个字符常量
    r"\"[^\"]*\"|"  # 字符串常量
    r"(<=|>=|==|!=|&&|\|\||\+|\-|\*|/|=|<|>|;|\(|\)|{|})"  # 运算符和符号，包括多字符符号
)


# 用于分类每个标记的函数
def classify_token(token, output_file):
    # 检查预处理指令
    if token in preprocessors:
        output_file.write(f"( {token} -> 预处理指令 ID {preprocessors[token]} )\n")
    # 检查头文件
    elif re.match(r"<\w+\.h>", token):
        output_file.write(f"( {token} -> 头文件 )\n")
    # 检查关键字
    elif token in keywords:
        output_file.write(f"( {token} -> 关键字 ID {keywords[token]} )\n")
    # 检查符号
    elif token in symbols:
        output_file.write(f"( {token} -> 符号 ID {symbols[token]} )\n")
    # 检查无效标识符（包含非法字符如 $）
    elif re.search(r"[^a-zA-Z0-9_]", token) and not re.match(r"^\d+$", token):
        output_file.write(f"( {token} -> 无效标识符 )\n")
    # 检查合法标识符
    elif re.match(r"^[a-zA-Z_]\w*$", token):
        output_file.write(f"( {token} -> 标识符 )\n")
    # 检查数字
    elif token.isdigit() or re.match(r"^-?\d+(\.\d+)?$", token):
        output_file.write(f"( {token} -> 数字 )\n")
    else:
        output_file.write(f"( {token} -> 未定义的符号 )\n")


# 主函数，对输入的源代码进行词法分析并输出到文件
def lexical_analyze(input_filename, output_filename):
    with open(input_filename, "r", encoding="utf-8") as file:
        source_code = file.read()

    # 使用正则表达式过滤出所有标记
    tokens = token_pattern.findall(source_code)

    with open(output_filename, "w", encoding="utf-8") as output_file:
        for token in tokens:
            # 如果 token 是注释，直接跳过
            if isinstance(token, str) and (
                token.startswith("//") or token.startswith("/*")
            ):
                continue
            classify_token(token, output_file)


# 测试词法分析器
if __name__ == "__main__":
    input_filename = "lexical_analyzer_testcase3.txt"  # 输入文件名
    output_filename = "lexical_analyzer_out.txt"  # 输出文件名
    lexical_analyze(input_filename, output_filename)
