# ここにコードを書いてください
class Library:
        def __init__(self):
            self.__books = []

        def add_book(self, title, author):
            #  """新しい本を追加します"""
            self.__books.append({"title":title,"author":author})

        def remove_book(self, title):
            # """タイトルで指定した本を削除します"""  
            for book in self.__books:
                 if book["title"] == title:
                    self.__books.remove(book)
                    break
            else:
                 print(f"Book with title '{title}' not found.")

        def retrieve_books(self):
            # """ライブラリ内の本を表す辞書のリストを返します"""
            return self.__books
        
if __name__ == "__main__":
        my_library = Library()

    # 本の追加
        my_library.add_book("To Kill a Mockingbird", "Harper Lee")
        my_library.add_book("1984", "George Orwell")

    # コレクションの表示
        print("Current books in the library:")
        for book in my_library.retrieve_books():
            print(f"Title: {book['title']}, Author: {book['author']}")

    # 本の削除
        my_library.remove_book("1984")

        # コレクションの再表示
        print("\nBooks in the library after removal:")
        for book in my_library.retrieve_books():
            print(f"Title: {book['title']}, Author: {book['author']}")


