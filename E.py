import numpy as np
from collections import Counter


class E_math:
    def __init__(self):
        self.p = [0]*20
        self.v1 = None
        self.radar = np.array([[80, 0, 0], [30, 60, 0], [55, 110, 0], [105, 110, 0], [130, 60, 0]])*1000  # 雷达的坐标
        self.falsePoint = np.array([[60600, 69982, 7995],
                                   [61197, 69928, 7980],
                                   [61790, 69838, 7955],
                                   [62377, 69713, 7920],
                                   [62955, 69553, 7875],
                                   [63523, 69359, 7820],
                                   [64078, 69131, 7755],
                                   [64618, 68870, 7680],
                                   [65141, 68577, 7595],
                                   [65646, 68253, 7500],
                                   [66131, 67900, 7395],
                                   [66594, 67518, 7280],
                                   [67026, 67116, 7155],
                                   [67426, 66697, 7020],
                                   [67796, 66263, 6875],
                                   [68134, 65817, 6720],
                                   [68442, 65361, 6555],
                                   [68719, 64897, 6380],
                                   [68966, 64429, 6195],
                                   [69184, 63957, 6000]])  # 虚假航迹数据

    def initPoitionAndSpeed(self, n):
        FalsePoint0 = self.falsePoint[0]
        v = [np.zeros(3) for _ in range(n)]
        p = [np.zeros(3) for _ in range(n)]
        while (not self.nearDistance(v, n, p.copy())) or (not self.onLine([pi+10*19*vi for pi, vi in zip(p, v)], self.falsePoint[-1])) or (not self.judgeEndPoint([pi+10*19*vi for pi, vi in zip(p, v)])):
            #无人机距离不小于100m, 最后时刻满足至少三架无人机符合要求，飞行高度要求，三个条件至少一个不满足就重新初始化
            index = np.random.permutation(self.radar.shape[0])[:3]
            for i, j in enumerate(self.radar[index]):
                a, b, c = j-FalsePoint0
                z = np.random.uniform(2000,2500)
                t = (z-FalsePoint0[2])/c
                x = t*a+FalsePoint0[0]
                y = t*b+FalsePoint0[1]
                p[i] = np.array([x, y, z])
            if n>3:
                for i in range(3,n):#先保证所有的点都在直线上
                    j = self.radar[np.random.permutation(self.radar.shape[1])[0]]
                    a, b, c = j[0] - FalsePoint0[0], j[1] - FalsePoint0[1], j[2] - FalsePoint0[2]
                    z = np.random.uniform(2000,2500)
                    t = (z-FalsePoint0[2])/c
                    x = t*a+FalsePoint0[0]
                    y = t*b+FalsePoint0[1]
                    p[i] = np.array([x, y, z])

                #保证3个点在直线的基础上，对剩下的点施加噪声
                for k in range(3,n):
                    while True:
                        s = p[k].copy()
                        s= s + np.random.normal(0,10,3)
                        if 2000<=s[2]<=2500:
                            p[k] = s
                            break
                        else:
                            continue
            #初始化速度
            v = [0]*n
            for i in range(n):
                while True:
                    t = np.random.uniform(0, 180/3.6, 3)
                    if 120/3.6<=np.sqrt(np.sum(t**2))<=180/3.6:
                        v[i] = t
                        break
                    else:
                        continue
        return p, v

    def judgeEndPoint(self, p):
        for i in p:
            if not (2000<=i[2]<=2500):
                return False
        return True

    def nearDistance(self, v, n, p):
        """
        :param v: 各无人机速度
        :param n: 无人机数量
        :param p: 无人机位置
        :return: 是否满足条件
        """
        for i in range(0,n-1):
            v0, s0 = v.pop(), p.pop()
            for v1, s1 in zip(v, p):
                t0 = s0 + 10*19*v0
                t1 = s1 + 10*19*v1
                d = dist3D_Segment_to_Segment(s0,s1,t0,t1)
                if d<100:
                    return False
        return True

    def onLine(self, p, perFalsePoint):
        #验证一组坐标是否满足至少有三架满足要求
        zs = []
        for i in range(5):
            for pi in p:
                if np.sum(abs((perFalsePoint -  self.radar[i])/np.linalg.norm((perFalsePoint -  self.radar[i])) - (perFalsePoint-pi)/np.linalg.norm((perFalsePoint-pi)))<1e-2)==3:
                    zs.append(i)
        ns = Counter(zs).most_common(3)
        if np.sum([x[1] for x in ns]) >= 3:
            return True
        return False


    def solve(self):
        n_iters = 1e2
        for t in range(3, 10):
            i_iter = 0
            while i_iter < n_iters:
                p, v = self.initPoitionAndSpeed(t)  # 初始化
                self.p[0] = p
                self.v1 = v
                N = 0
                for r, q in enumerate(self.falsePoint[1:], 1):
                    p = [pi + 10 * vi for pi, vi in zip(p, v)]
                    if self.onLine(p, q):
                        self.p[r] = p
                        N += 1
                        continue
                    else:
                        break
                if N==19:
                    return t, (t-3)*n_iters+i_iter
                else:
                    i_iter += 1
        return None

def dist3D_Segment_to_Segment(s0, s1, t0, t1):
    """
    计算空间两条线段的最短距离
    :param s0:
    :param s1:
    :param t0:
    :param t1:
    :return:
    """
    small_num = 1e-7
    u = s1 - s0
    v = t1 - t0
    w = s0 - t0

    a = np.dot(u, u)
    b = np.dot(u, v)
    c = np.dot(v, v)
    d = np.dot(u, w)
    e = np.dot(v, w)

    D = a * c - b * b
    sc = sN = sD = D
    tc = tN = tD = D

    if D < small_num:
        sN = 0.0
        sD = 1.0
        tN = e
        tD = c
    else:
        sN = b * e - c * d
        tN = a * e - b * d
        if sN < 0.0:
            sN = 0.0
            tN = e
            tD = c
        elif sN > sD:
            sN = sD
            tN = e + b
            tD = c
    if tN < 0.0:
        tN = 0.0
        if -d < 0.0:
            sN = 0.0
        elif -d > a:
            sN = sD
        else:
            sN = -d
            sD = a
    elif tN > tD:
        tN = tD
        if (-d + b) < 0.0:
            sN = 0
        elif (-d + b) > a:
            sN = sD
        else:
            sN = -d + b
            sD = a

    sc = 0.0 if abs(sN) < small_num else sN / sD
    tc = 0.0 if abs(tN) < small_num else tN / tD

    dP = w + (sc * u) - (tc * v)
    return np.linalg.norm(dP)

if __name__ == '__main__':
    q1 = E_math()
    print('无人机数目及及迭代次数：',q1.solve())
    print('无人机的坐标：',q1.p)
    print('无人机的速度：',[np.linalg.norm(v)*3.6 for v in q1.v1])

