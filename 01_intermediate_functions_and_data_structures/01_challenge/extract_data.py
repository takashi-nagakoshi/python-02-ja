import re

def extract_data(text):
    # 正規表現パターンを定義
    # \b は単語境界を示します。 \w+ は1つ以上の単語文字（アルファベット、数字、アンダースコア）を示します。
    pattern = r'\b\w+:\w+\b'
    # 正規表現を使用してテキストからデータを抽出
    data_list = re.findall(pattern, text)
    return data_list

# 入力テキスト
input_text = "The subject has Age:25 and Height:180cm.Other details are not relevant.Weight:70kg was noted."

# 関数の呼び出し
extracted_data = extract_data(input_text)

# 結果の表示
print(extracted_data)

def better_extract_data(text2):
    # 正規表現パターンを定義
    pattern2 = r'\b(\w+):(\w+)\b'
    # 正規表現を使用してテキストからデータを抽出し、タプルのリストとして返す
    data_list2 = re.findall(pattern2, text2)
    return data_list2
# 入力テキスト
input_text = "The subject has Age:25 and Height:180cm.Other details are not relevant.Weight:70kg was noted."

# 関数の呼び出し
extracted_data2 = better_extract_data(input_text)

# 結果の表示
print(extracted_data2)