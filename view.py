import eel
from pos_system import Order, Item
import pandas as pd

ITEM_MASTER_CSV_PATH="./item_master.csv"
RECEIPT_FOLDER= "receipt"

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
            # sys.exit()


# マスタ登録
item_master=add_item_master_by_csv(ITEM_MASTER_CSV_PATH) # CSVからマスタへ登録
order=Order(item_master,RECEIPT_FOLDER) 

@eel.expose
def order_function(item_code):
    order.add_item_order(item_code)


eel.init("web")
eel.start("index.html")
