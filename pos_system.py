import os
import sys
import eel
import datetime
import pathlib
import pandas as pd

class Item():
    def __init__(self, item_code, item_name, price) -> None:
        self.item_code = item_code
        self.item_name = item_name
        self.item_price = price

class Order():
    def __init__(self, item_master) -> None:
        self.item_order_list=[]
        self.item_count_list=[]
        self.item_master=item_master

    def add_item_order(self, item_code, item_count):
        if self.get_item_data(item_code):
            self.item_order_list.append(item_code)
            self.item_count_list.append(item_count)            
            return True
        else:
            return False

    def get_item_data(self, item_code):
        for master in self.item_master:
            if item_code == master.item_code:
                return master.item_name, master.item_price

    def get_order_items(self):
        res = ""
        num = 1
        total_price = 0
        total_count = 0
        for item_code,count in zip(self.item_order_list,self.item_count_list):
            for item in self.item_master:
                if item.item_code == item_code:
                    res += f"{num} | {item_code} {item.item_name} | ￥{item.item_price}円 × {count} 個\n"
                    num += 1
                    total_price += item.item_price * count
                    total_count += count
                    break   
        res += "---------------------------------------------\n"
        res += f"合計: ￥{total_price}円 | {total_count}個\n"

        return res

    def calc_total_price(self):
        total_price = []
        for item_code, count in zip(self.item_order_list, self.item_count_list):
            for item in self.item_master:
                if item.item_code == item_code:
                    total_price.append(item.item_price * count)    
        return sum(total_price)

    def checkout(self, deposit_money):
        return deposit_money - self.calc_total_price()  


class PosSystem():
    def __init__(self, item_master_csv) -> None:
        self.item_master = []
        self.item_master_csv = item_master_csv
        self.order = None

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

    def init_order(self):
        self.order = Order(self.item_master) 

  
# if __name__ == "__main__":
#     main()