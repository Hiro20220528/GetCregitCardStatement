# pdfをcsvに書き換える
# pdf_filesにはpdfのみを書く
# csvから利用明細をハッシュ表に取り込む
# 正規表現で似ている明細を一つにまとめる

# (1) pdf_to_csv.pyを呼び出しpdf->csvに変換

import pdf_to_csv as ptoc
import glob
import os
import time
# glob を使用して、pdf_filesの中にあるpdfを取得する
files_path = glob.glob("./data/pdf_files/*.pdf")

# pdf -> csv
ptoc.pdf_to_csv(files_path)






# ./data/csv_files内のファイルを削除する
# delete_files_path = glob.glob("./data/csv_files/*.csv")
# for delete_path in delete_files_path:
#           os.remove(delete_path)



