import time

from kneed import KneeLocator

from metrics_collector import get_throughput, get_latency

class Kneescaler:
    def __init__(self, CPU_threshold, thr_threshold, e_threshold, r_cur, CPU_cur, max_instances):
        self.CPU_threshold = CPU_threshold
        self.thr_threshold = thr_threshold
        self.e_threshold = e_threshold

        self.r_cur = r_cur
        self.t_cur = 0
        self.e_cur = 0
        self.CPU_pre = 0
        self.CPU_cur = CPU_cur
        self.K = {}
        self.f_min = float("inf")
        self.max_instances = max_instances

    def find_closest_throughput(self):
        t_closest = float("inf")
        for t in self.K:
            if abs(self.t_cur - t) < self.f_min:
                self.f_min = abs(self.t_cur - t)
                t_closest = self.t_cur

        return t_closest

    def scale_up(self):
        t_closest = self.find_closest_throughput()
        if abs(self.t_cur - t_closest) < self.thr_threshold:
            self.update_r_cur(self.K[t_closest])
        else:
            if self.e_cur < self.e_threshold:
                k = self.find_knee(self.r_cur + 1, min(self.r_cur + self.max_instances / 2, self.max_instances))
            else:
                k = self.find_knee(self.r_cur + 1, self.max_instances)
            self.K[self.t_cur] = k
            self.update_r_cur(k)

    def scale_down(self):
        t_closest = self.find_closest_throughput()
        self.update_r_cur(self.K[t_closest])

    def update_cur_data(self, t_cur, e_cur, CPU_cur):
        self.t_cur = t_cur
        self.e_cur = e_cur
        self.CPU_pre = self.CPU_cur
        self.CPU_cur = CPU_cur

        if e_cur > 0:
            self.scale_up()
        if (self.CPU_pre - self.CPU_cur) / self.CPU_pre > self.CPU_threshold:
            self.scale_down()

    def find_knee(self, bl, br):
        direction = 'L'
        replica_nums = [bl, br, (bl + br) // 2]
        scores = [self.run_trials(replica_num) for replica_num in replica_nums]
        knee = KneeLocator(replica_nums, scores, curve="concave", direction="increasing").knee

        while bl < br and (br - bl) > 2:
            last_replica_num = replica_nums[len(replica_nums) - 1]
            if direction == 'L':
                if knee is None or knee == last_replica_num:
                    new_replica = (last_replica_num + bl) // 2
                else:
                    direction = 'R'
                    bl = last_replica_num
                    new_replica = (bl + br) // 2
            else:
                if knee is None or knee == last_replica_num:
                    new_replica = (last_replica_num + br) // 2
                else:
                    direction = 'L'
                    br = last_replica_num
                    new_replica = (bl + br) // 2

            replica_nums.append(new_replica)
            if new_replica in replica_nums:
                score = scores[replica_nums.index(new_replica)]
            else:
                score = self.run_trials(new_replica)
            scores.append(score)
            knee = KneeLocator(replica_nums, scores, curve="concave", direction="increasing").knee

        return knee


    def run_trials(self, c):
        self.update_r_cur(c)
        time.sleep(5)
        t_trial = get_throughput()
        latency_trial = get_latency()
        # run trials and return
        return t_trial/latency_trial

    def update_r_cur(self, r_cur):
        self.r_cur = r_cur
        #update in k8s as well