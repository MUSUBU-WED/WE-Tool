
#結合プログラム
import glob
import pandas as pd

# 1---フォルダ内のCSVファイルの一覧を取得
files = sorted(glob.glob('/Users/nakagawamasaki/venv10/csv_compile/*.csv'))

# 2---ファイル数を取得
file_number = len(files)

# 3---CSVファイルの中身を読み出して、リスト形式にまとめる
csv_list = []
for file in files:
    csv_list.append(pd.read_csv(file,encoding='cp932'))

# 4---CSVファイルの結合
merge_csv = pd.concat(csv_list, axis=0, ignore_index=True)

merge_file = input("出力ファイル名を指定してください。")
# 5---CSVファイル出力
merge_csv.to_csv(merge_file, encoding='cp932')

# 6---ファイルの規格を表示
file_size = merge_csv.info()
# 7---完了合図
print(file_number,' 個のCSVファイルを結合完了！！')
