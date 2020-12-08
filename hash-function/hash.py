# coding: UTF-8

# 索引を用意するようなイメージ
# インデックス 番号を付与すれば、ダイレクトで情報にアクセスできる
# 英単語辞書の索引

import hashlib

class HashTable():
    def __init__(self,size=10):
        self.size = size
        # 10個分のhashを作る
        self.table = [[] for _ in range(self.size)]
    
    def hash(self,key):
        # ある文字列を入れたら同じハッシュが出てくる
        return int(hashlib.md5(key.encode()).hexdigest(),base=16) % self.size

    def add(self,key,value):
        # 該当するindex番号を取得
        index = self.hash(key)
        print(self.table[index])
        # 該当するindex番号のkeyとvalueをループ
        for data in self.table[index]:
            # 既存のindexにあるkeyと追加しようとするkeyが一致していたら
            if data[0] == key:
                print(value)
                print(data[1])
                # valueのみ再格納
                data[1] = value
                #ループから抜け出す
                break
        else:
            self.table[index].append([key,value])

    def test(self):
        for index in range(self.size):
            print(index)
            for data in self.table[index]:
                print(data)
    def get(self,key):
        index = self.hash(key)
        for data in self.table[index]:
            if data[0] == key:
                return data[1]


            


if __name__ == '__main__':
    hash_table = HashTable()
    hash_table.add('cars','Tesla')
    hash_table.add('cars','Tesla')
    hash_table.add('pc','mac')
    hash_table.add('sns','YouTube')
    print(hash_table.get('pc'))
    # print(hash_table.table)
    # hash_table.test()

import hashlib


