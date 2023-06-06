# pdfファイルを読み込みcsvファイルとして出力する

import glob
import tabula
import re

# glob を使用して、pdf_filesの中にあるpdfを取得する
# files = glob.glob("./data/pdf_files/*.pdf")

def pdf_to_csv(files):
          # tryを利用してpdfファイル以外を読み込んだ場合の例外処理を記述
          # 正規表現を利用してpdfファイルのみを取得するようにする
          for file_path in files:
                    try:
                              # lattice: excelのような格子区切りの内容を強制抽出, pages: 抽出するページを指定
                              pdf = tabula.read_pdf(file_path, lattice=True , pages = "all")
                    except:
                              print("PDFファイルを読み取れませんでした。")
                              # pdfファイルを読み取れない場合は、次のファイルへスキップする
                              continue
                    
                    # 必要な情報だけ取得する
                    detail = pdf[1:-3]
                              
                    # pathを生成する
                    csv_path = re.sub("\.pdf", "", file_path)
                    csv_path = re.sub("pdf_files", "csv_files", csv_path)
                    
                    # write csv
                    for i in range(len(detail)):
                              detail[i].to_csv(csv_path + "-" + str(i) + ".csv", index=None)
