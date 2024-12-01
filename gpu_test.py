import pycuda.driver as cuda
import pycuda.autoinit
from pycuda.compiler import SourceModule
import numpy as np
import time


def gpu_stress_test(block_size, grid_size, iterations, memory_size_gb):
    """
    使用 PyCUDA 测试 GPU 的计算性能。
    :param block_size: 每个线程块的大小
    :param grid_size: 每个网格的大小
    :param iterations: 每个线程运行的循环次数
    :param memory_size_gb: 分配的显存大小（GB）
    """
    # CUDA 内核函数，用于执行大量计算
    kernel_code = """
    __global__ void stress_test(float *data, int iterations) {
        int idx = threadIdx.x + blockIdx.x * blockDim.x;
        for (int i = 0; i < iterations; i++) {
            data[idx] = data[idx] * data[idx] - 0.5f;
            data[idx] = sqrtf(fabsf(data[idx]));
        }
    }
    """

    # 编译 CUDA 内核
    module = SourceModule(kernel_code)  # 针对 4070 Super
    stress_test = module.get_function("stress_test")

    # 初始化数据
    n_elements = int(
        memory_size_gb * (1024**3) / 4
    )  # 数据块大小（以 float 占用 4 字节计算）
    data = np.random.rand(n_elements).astype(np.float32)

    # 分配 GPU 内存并传输数据
    data_gpu = cuda.mem_alloc(data.nbytes)
    cuda.memcpy_htod(data_gpu, data)

    print(
        f"Starting GPU stress test: blocks={grid_size}, threads per block={block_size}, iterations={iterations}, memory={memory_size_gb}GB"
    )

    # 开始计时
    start_time = time.time()

    # 执行内核函数
    stress_test(
        data_gpu, np.int32(iterations), block=(block_size, 1, 1), grid=(grid_size, 1)
    )
    cuda.Context.synchronize()

    # 结束计时
    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"GPU stress test completed in {elapsed_time:.2f} seconds.")
    print(f"Data processed: {n_elements * 4 / (1024 ** 3):.2f} GB")

    # 释放 GPU 内存
    data_gpu.free()


if __name__ == "__main__":
    # 配置测试参数
    block_size = 512  # 每个线程块的线程数
    grid_size = 8192  # 网格大小（线程块数）
    iterations = 100000  # 每个线程的计算次数
    memory_size_gb = 10  # 分配显存大小（GB，最大 12GB，但需保留系统显存）

    # 运行 GPU 压力测试
    gpu_stress_test(block_size, grid_size, iterations, memory_size_gb)
