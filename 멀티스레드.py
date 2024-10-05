#하나의 Application 내에서 여러개의 일을 동시에 수행하는 것
from simple_colors import * # 터미널 출력 시 컬러를 지원하기 위해서
import threading # 멀티 쓰레드를 지원하기 위해서
import time # sleep() 사용하기 이해, 주어진 시간만 해당 쓰레드 동작을 일시 정지
import random # 난수 발생

class Unit:
    def __init__(self, pp, mp, ph, mh, hp):
        self.pPower = pp  # Physical power
        self.mPower = mp  # Magical power
        self.pHit = ph  # 물리 적중률
        self.mHit = mh  # 마법 적중률
        self.hp = hp  # 체력
        self.isAlive = True  # 생사 여부

    