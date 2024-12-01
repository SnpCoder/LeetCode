import numpy as np
import time


def memory_stress_test(target_gb, duration=60):
    """
    内存压力测试，占用指定大小的内存并执行读写操作。

    :param target_gb: 目标内存占用大小（GB）。
    :param duration: 测试持续时间（秒）。
    """
    print(f"开始内存压力测试，占用目标大小约 {target_gb} GB...")
    memory_blocks = []
    block_size = 256 * 1024 * 1024  # 每个块 256 MB
    total_blocks = (target_gb * 1024) // 256  # 计算所需块的数量

    # 分配内存
    print(f"分配内存块（每块 256MB，总共 {total_blocks} 块）...")
    for i in range(int(total_blocks)):
        try:
            block = np.ones(block_size // 8, dtype=np.float64)  # 每块 256 MB
            memory_blocks.append(block)
            print(f"已分配内存块 {i + 1}/{total_blocks}")
        except MemoryError:
            print("内存不足，无法继续分配！")
            break

    allocated_gb = len(memory_blocks) * (block_size / 1024 / 1024 / 1024)
    print(f"成功分配约 {allocated_gb:.2f} GB 的内存。")

    # 开始读写测试
    print(f"开始读写测试，持续 {duration} 秒...")
    start_time = time.time()
    while time.time() - start_time < duration:
        for i, block in enumerate(memory_blocks):
            block += 1  # 模拟写入操作
            block -= 1  # 模拟恢复操作
        print(f"读写循环完成，当前时间：{time.time() - start_time:.2f}s")

    print("内存压力测试完成，释放内存。")

    # 清空内存
    del memory_blocks
    print("内存已释放。")


if __name__ == "__main__":
    target_memory_gb = 32  # 设置目标内存大小（GB）
    test_duration = 60  # 设置测试持续时间（秒）
    memory_stress_test(target_memory_gb, test_duration)
