import os
import datetime
import pathlib
import pandas as pd


ITEM_MASTER_CSV_PATH="./item_master.csv"
RECEIPT_FOLDER= "receipt"

### 商品クラス
class Item:
    def __init__(self,item_code,item_name,price):
        self.item_code=item_code
        self.item_name=item_name
        self.price=price

    def get_price(self):
        return self.price

### オーダークラス
class Order:
    # 初期化
    def __init__(self,item_master,reciept_folder):
        self.item_order_list=[]
        self.item_master=item_master
        self.reciept_folder=reciept_folder
        
        now = datetime.datetime.now()
        self.reciept_file = '{0:%Y%m%d%H%M%S}.txt'.format(now)
        try:
            os.makedirs(self.reciept_folder, exist_ok=True)
            reciept = pathlib.Path(self.reciept_folder + "/" + self.reciept_file)
            with reciept.open(mode='w') as f:
                f.write('')

        except FileExistsError as e:
            print(e.strerror)  # エラーメッセージ ('Cannot create a file when that file already exists')
            print(e.errno)     # エラー番号 (17)
            print(e.filename)  # 作成できなかったディレクトリ名 ('foo')
    
    def add_item_order(self):

        with open(self.reciept_folder + "/" + self.reciept_file, mode='a', encoding="utf8") as f1:     
            f1.write("#### 購入商品 ###\n")
            while True:
                self.input_item_code = input("商品コードを入力して下さい：")
                self.item_num = input("何個買いますか：")
                f1.write("商品コード："+"{}\n".format(self.input_item_code))
                self.item_order_list.append(self.input_item_code)
                checkStop = input("買い物を続けますか。続ける場合：Y、中止する場合：Qと入力してください：")
                if checkStop in ["Q", "q", "quit", "end", "終了"]:
                    break
            f1.write("################\n")

    # 課題1
    def view_item_list(self):
        total_price = []
        for order_item_code in self.item_order_list:
            for master in self.item_master:
                if order_item_code == master.item_code:
                    total_price.append(int(master.price*int(self.item_num))) 

        # 課題5
        with open(self.reciept_folder + "/" + self.reciept_file, 'a', encoding="utf8") as f2:
            print("すべての合計金額："+"{}".format(sum(total_price)))
            f2.write("すべての合計金額："+"{}".format(sum(total_price))+"\n")

            payment = input("お預かり金額を入力してください：")
            f2.write("お預かり金額："+"{}".format(payment)+"\n")

            change = int(payment) - sum(total_price)

            while int(change) < 0:
                print("お預かりの金額では足りません")
                payment = input("もう一度お預かりの金額を入力してください：")
                change = int(payment) - sum(total_price)
            print("お返しの金額は、"+"{}".format(change)+"です。")
            f2.write("お返しの金額："+"{}".format(change))

def add_item_master_by_csv(csv_path):
        print("------- マスタ登録開始 ---------")
        item_master=[]
        count=0
        try:
            item_master_df=pd.read_csv(csv_path,dtype={"item_code":object}) # CSVでは先頭の0が削除されるためこれを保持するための設定
            for item_code,item_name,price in zip(list(item_master_df["item_code"]),list(item_master_df["item_name"]),list(item_master_df["price"])):
                item_master.append(Item(item_code,item_name,price))
                print("{}({})".format(item_name,item_code))
                count+=1
            print("{}品の登録を完了しました。".format(count))
            print("------- マスタ登録完了 ---------")
            return item_master
        except:
            print("マスタ登録が失敗しました")
            print("------- マスタ登録完了 ---------")
            sys.exit()
        
### メイン処理
def main():
    # マスタ登録
    item_master=add_item_master_by_csv(ITEM_MASTER_CSV_PATH) # CSVからマスタへ登録
    order=Order(item_master,RECEIPT_FOLDER) 
    # item_master=[]
    # path = "./item_master.csv"
    # df = pd.read_csv(path)
    # item_master.append(Item(df["item_code"], df["item_name"], df["price"]))

    # オーダー登録
    # order=Order(item_master)
    order.add_item_order()
    
    # オーダー表示
    order.view_item_list()
 

if __name__ == "__main__":
    main()