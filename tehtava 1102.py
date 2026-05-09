# 1. 基础类：汽车
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, nopeuden_muutos):
        uusi_nopeus = self.tamanhetkinen_nopeus + nopeuden_muutos
        if uusi_nopeus > self.huippunopeus:
            self.tamanhetkinen_nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.tamanhetkinen_nopeus = 0
        else:
            self.tamanhetkinen_nopeus = uusi_nopeus

    def kulje(self, tunti):
        self.kuljettu_matka += self.tamanhetkinen_nopeus * tunti

# 2. 子类：电动汽车
class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        # 调用父类 alustaja
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

# 3. 子类：燃油汽车
class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        # 调用父类 alustaja
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankin_koko = bensatankin_koko

# --- 主程序 ---
if __name__ == "__main__":
    # 创建一辆电动汽车
    sahko = Sahkoauto("ABC-15", 180, 52.5)
    # 创建一辆燃油汽车
    poltto = Polttomoottoriauto("ACD-123", 165, 32.3)

    # 设置速度
    sahko.kiihdyta(150)
    poltto.kiihdyta(120)

    # 让汽车行驶 3 小时
    sahko.kulje(3)
    poltto.kulje(3)

    # 打印行驶里程 (matkamittarilukemat)
    print(f"Electric car ({sahko.rekisteritunnus}) mileage: {sahko.kuljettu_matka} km")
    print(f"Gasoline car ({poltto.rekisteritunnus}) mileage: {poltto.kuljettu_matka} km")