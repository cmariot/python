class TinyStatistician:

    def mean(self, x) -> float:
        return float(sum(x) / len(x))

    def median(self, x) -> float:
        x.sort()
        list_len = len(x)
        if list_len == 0:
            return None
        elif list_len % 2 == 0:
            return float(x[len(x) // 2 - 1] + x[len(x) // 2]) / 2
        else:
            return float(x[len(x) // 2])

    def quartile(self, x) -> 'list[float]':
        if len(x) == 0:
            return None
        x.sort()
        return [float(x[len(x) // 4]), float(x[len(x) // 4 * 3])]

    def var(self, x) -> float:
        if len(x) == 0:
            return None
        mean = TinyStatistician.mean(self, x)
        return sum([(i - mean) ** 2 for i in x]) / len(x)

    def std(self, x):
        return TinyStatistician.var(self, x) ** 0.5


if __name__ == "__main__":

    tstat = TinyStatistician()
    a = [1, 42, 300, 10, 59]

    print(tstat.mean(a))
    # Expected result: 82.4

    print(tstat.median(a))
    # Expected result: 42.0

    print(tstat.quartile(a))
    # Expected result: [10.0, 59.0]

    print(tstat.var(a))
    # Expected result: 12279.439999999999

    print(tstat.std(a))
    # Expected result: 110.81263465868862
