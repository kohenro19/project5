import os
import sys
import eel
import datetime
import pathlib
import pandas as pd


class PosSystem():
    def __init__(self, item_master_csv) -> None:
        self.item_master = []
        self.item_master_csv = item_master_csv

    def add_item_master(self):
        print("------- マスタ登録開始 ---------")
        count=0
        try:
            item_master_df=pd.read_csv(self.item_master_csv,dtype={"item_code":object}) # CSVでは先頭の0が削除されるためこれを保持するための設定
            for item_code,item_name,price in zip(list(item_master_df["item_code"]),list(item_master_df["item_name"]),list(item_master_df["price"])):
                self.item_master.append(Item(item_code,item_name,price))
                print("{}({})".format(item_name,item_code))
                count+=1
            print("{}品の登録を完了しました。".format(count))
            print("------- マスタ登録完了 ---------")
            return self.item_master
        except:
            print("マスタ登録が失敗しました")
            print("------- マスタ登録完了 ---------")
            sys.exit()
        
class Item():
    def __init__(self, item_code, item_name, price) -> None:
        self.item_code = item_code
        self.item_name = item_name
        self.item_price = price
    pass
if __name__ == "__main__":
    main()