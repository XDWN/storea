from threading import Thread
import time

cabinet = 0  # 柜子


class Chefs(Thread):
    tart = 0  # 蛋挞
    work = 0  # 工资

    def run(self) -> None:
        global cabinet  # 引用全局变量
        a = time.time()  # 记录开始时间

        while True:
            b = time.time()  # 记录结束时间
            if b - a == 60:
                self.work = self.tart * 1.5
                print(self.work)
                break
            elif cabinet >= 500:
                time.sleep(3)
            elif cabinet <= 500:
                self.tart += 1
                cabinet = cabinet + self.tart
                print(cabinet)  # 卖出

class Clients(Thread):
    money = 5000

    def run(self) -> None:
        global cabinet  # 引用全局变量

        while True:
            if cabinet == 0:
                time.sleep(2)
            elif self.money > 3:
                cabinet = cabinet - 1
                self.money = self.money - 3
                print(cabinet, 2)  # 卖出
            else:
                break


a1 = Chefs()
a2 = Chefs()
a3 = Chefs()
b1 = Clients()
b2 = Clients()
b3 = Clients()
b4 = Clients()
b5 = Clients()
b6 = Clients()
a1.start()
a2.start()
a3.start()
b1.start()
b2.start()
b3.start()
b4.start()
b5.start()
b6.start()