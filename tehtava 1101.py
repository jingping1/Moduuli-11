# 1. 父类：出版物
class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

# 2. 子类：书
class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)  # 调用父类构造函数设置名字
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        print(f"Kirjan nimi: {self.nimi}")
        print(f"Kirjailija: {self.kirjoittaja}")
        print(f"Sivumäärä: {self.sivumaara}")
        print("-" * 20)

# 3. 子类：杂志
class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        print(f"Lehden nimi: {self.nimi}")
        print(f"Päätoimittaja: {self.paatoimittaja}")
        print("-" * 20)

# --- 主程序 ---
if __name__ == "__main__":
    # 创建杂志：Aku Ankka
    lehti1 = Lehti("Aku Ankka", "Aki Hyyppä")
    # 创建书籍：Hytti n:o 6
    kirja1 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

    # 打印信息
    lehti1.tulosta_tiedot()
    kirja1.tulosta_tiedot()te