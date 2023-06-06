import glob
import csv
import unicodedata

# glob を使用して、csv_filesの中にあるpdfを取得する
files = glob.glob("./data/csv_files/*.csv")

my_use = {}

# num = 0
for file_path in files:
          # print(file_path)
          with open(file_path) as f: # 読み込み
                    reader = csv.reader(f)
                    csv_list = [row for row in reader]
          
          for payment in csv_list:
                    # ['利用日', '利用店名', '利用者', '支払方法', '利用金額', '手数料', '支払総額', '当月請求額', '翌月繰越残高']
                    # 利用店名, 当月請求額のみ取得する
                    
                    if payment[0] == '':
                              break
                    # print(payment)
                    if payment[0] == '利用日':
                              continue
                    name = payment[1].replace("(ヘンサイヘンコウ", "")
                    # 末尾の空白を削除する
                    name = name.rstrip() 
                    # 半角文字列に変更する
                    name = unicodedata.normalize('NFKC', name)
                    # 大文字のーを-に変更する
                    name = name.replace("ー", "-")
                    # 価格の,を削除する
                    price = payment[7].replace(",", "")
                    # num += int(price)
                    
                    # print(name, price)
                    my_use[name] = my_use.get(name, 0) + int(price)
          
# print(num)
print("*********************")
name_list = []
for i in my_use:
          name_list.append(i)
          
name_list.sort()
# 似ている名前のショップをまとめる
for i in range(1, len(name_list)):
          name = name_list[i]
          before_name = name_list[i - 1]
          if before_name in name:
                    my_use[before_name] += my_use[name]
                    my_use.pop(name)
                    name_list[i] = name_list[i - 1]
          

          # print(name, my_use[name])

total = 0
shop_list = [i for i in my_use.keys()]
shop_list.sort()
for name in shop_list:
          price = my_use[name]
          total += price
          print(name, price)
print("------------------------------")
print(f"total: {total}")