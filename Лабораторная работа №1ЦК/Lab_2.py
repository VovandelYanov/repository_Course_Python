# TODO Найдите количество книг, которое можно разместить на дискете
volume_disk = 1.44 * 1024 * 1024
volume_one_book = 100 * 50 * 25 * 4
Result = volume_disk/volume_one_book
print("Количество книг, помещающихся на дискету:", int(Result))
