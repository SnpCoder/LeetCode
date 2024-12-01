import multiprocessing
import time
import math


def cpu_stress_test(duration):
    """
    执行计算密集型任务，最大化使用 CPU 核心。
    :param duration: 测试持续时间（秒）
    """
    start_time = time.time()
    while time.time() - start_time < duration:
        _ = math.sqrt(12345) ** 2  # 模拟复杂计算


def run_stress_test(cpu_cores, duration):
    """
    使用多进程最大化利用 CPU 性能。
    :param cpu_cores: 使用的 CPU 核心数
    :param duration: 每个进程的运行时间（秒）
    """
    print(f"Starting stress test with {cpu_cores} cores for {duration} seconds...")
    processes = []
    for _ in range(cpu_cores):
        process = multiprocessing.Process(target=cpu_stress_test, args=(duration,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()


if __name__ == "__main__":
    # 获取 CPU 核心数，Intel 13600KF 有 14 核心（6 性能核心 + 8 效率核心）
    total_cores = multiprocessing.cpu_count()
    print(f"Detected {total_cores} CPU cores.")

    # 设置运行参数
    stress_duration = 60  # 持续时间（秒）
    cores_to_use = total_cores  # 使用所有核心

    # 运行压力测试
    run_stress_test(cores_to_use, stress_duration)
    print("Stress test completed.")
