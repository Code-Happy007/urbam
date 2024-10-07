def test_function():        # 1
    def inner_function():   # 2
        print("Я в области видимости функции test_function")

    inner_function()        # 3 - здесь ничего не возвращает

#inner_function()   (ошибка)

test_function()     