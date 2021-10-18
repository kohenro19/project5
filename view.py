import eel 
from pos_system import PosSystem
import common.desktop as desktop

# フォルダ名
app_name = "html"
end_point = "index.html"
size = (700,600)

#ystem:PosSystem

ITEM_MASTER_CSV_PATH="./item_master.csv"

'''
HTML側とのやり取りは全てview.pyファイルに纏めている
これにより、pos.py側はeelに依存する必要がなくなり
再利用性が高まる
'''

@eel.expose
def add_order_item(item_code:str,amount:str):
    '''
    オーダーに商品を追加する
    '''
    global system
    print(item_code, amount)
    # Orderが存在しなければOrderインスタンスを作成
    if system.order == None:
        system.init_order()
    res = system.order.add_item_order(item_code, int(amount))
    if not res:
        eel.alertJs(f"『{item_code}』は商品マスターに登録されていません")
    else:
        res_text = system.order.get_order_items()
        eel.view_order_items(res_text)
    

def init_pos_system():
    global system
    system = PosSystem(ITEM_MASTER_CSV_PATH)
    system.add_item_master()

if __name__ == "__main__":
    init_pos_system()
    desktop.start(app_name,end_point,size)
