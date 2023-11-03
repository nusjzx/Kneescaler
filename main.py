from knee_scaler import Kneescaler
import time

from metrics_collector import get_throughput, get_err, get_CPU

if __name__ == "__main__":

	CPU_threshold = 0.05
	thr_threshold = 2
	err_threshold = 1
	r_init = 1
	CPU_init = 1
	max_instances = 30
	period = 60
	knee_scaler = Kneescaler(CPU_threshold, thr_threshold, err_threshold, max_instances)

	while True:
		t_cur = get_throughput()
		e_cur = get_err()
		CPU_cur = get_CPU()
		knee_scaler.update_cur_data(t_cur, e_cur, CPU_cur)
		time.sleep(period)