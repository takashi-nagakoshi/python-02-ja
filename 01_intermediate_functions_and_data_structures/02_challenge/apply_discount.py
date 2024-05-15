def apply_discount(products, minimum_price, discount_rate):
    # リスト内包表記を使用して、最低価格のしきい値以上の商品をフィルタリングします。
    # リスト内包表記の中でラムダ関数を使用し、フィルタリングされた商品に割引を適用します。
    # タプルのリストとして結果を出力し、各タプルには商品名とその割引価格を含みます。
    # [<式> for <要素> in <イテラブル> if <条件>]
    discounted_products = [
        (product["name"], round(product["price"] * (1 - discount_rate / 100), 2))
        for product in products
        if product["price"] >= threshold
    ]
    # (product["name"], ...): 商品名と割引価格をタプルにします。
    # round(..., 2): 割引価格を小数点以下2桁に丸めます。
    # product["price"] * (1 - discount_rate / 100): 割引を適用した価格を計算します。
    # product["price"] >= threshold: 商品の価格がしきい値以上であるかをチェックします。
    return discounted_products

# 商品リスト
products = [
    {"name": "Laptop", "category": "Electronics", "price": 1200},
    {"name": "Bread", "category": "Food", "price": 2},
    {"name": "Jacket", "category": "Apparel", "price": 100}
]

# 最低価格のしきい値と割引率
threshold = 50
discount_rate = 10

# 関数の呼び出し
result = apply_discount(products, threshold, discount_rate)

# 結果の表示
print(result)

# 商品リスト
products2 = [
    {"name": "Smartphone", "category": "Electronics", "price": 800},
    {"name": "Sneakers", "category": "Footwear", "price": 120},
    {"name": "Coffee", "category": "Beverage", "price": 5}
]

# 最低価格のしきい値と割引率
threshold = 100
discount_rate = 15

# 関数の呼び出し
result2 = apply_discount(products2, threshold, discount_rate)

# 結果の表示
print(result2)