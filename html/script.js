add_order_btn.addEventListener("click", () => {
    if (item_code.value != "" && amount.value != "") {
        eel.add_order_item(item_code.value, amount.value);
    } else {
        alert("商品コードおよび個数の入力は必須です")
    }
})