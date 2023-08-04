import math
import threading


# Leibniz algo should run way faster, but because the Global Interpreter Lock (GIL)
# does not allow parallel execution of Python Code in multiple Threads it won't
# One could use multiprocessing but that is way over my head and would just be me copying code

def partOfLeibniz(start, end):
    sumPart = 0.0
    for k in range(start, end):
        sumPart += ((-1) ** k) / (2 * k + 1)
    return sumPart


if __name__ == "__main__":
    numberOfThreads = 12
    numberOfLeibnizIterations = 100000000
    threads = []
    partialSumOfLeibniz = []

    iterationCountPerThread = numberOfLeibnizIterations // numberOfThreads  # divide and throw away decimals
    print("Starting: ", numberOfThreads, " Threads with each Thread computing: ", iterationCountPerThread,
          " Leibniz iterations")
    # there could be some rest computations to do,
    # we do them on the main thread afterward, not ideal, but it is what it is
    restIterations = numberOfLeibnizIterations % numberOfThreads
    for i in range(numberOfThreads):
        start = i * iterationCountPerThread
        end = start + iterationCountPerThread
        thread = threading.Thread(target=lambda: partialSumOfLeibniz.append(partOfLeibniz(start, end)))
        threads.append(thread)
        thread.start()

    # Blocking main thread until every thread has finished its computation
    for x in threads:
        x.join()

    # Compute rest on main thread
    if restIterations > 0:
        print("Computing rest ...")
        partialSumOfLeibniz.append(partOfLeibniz(numberOfThreads * iterationCountPerThread, numberOfLeibnizIterations))

    res = sum(partialSumOfLeibniz) * 4

    print("Our Pi:  '{:.12f}'".format(res))
    print("Math Pi: '{:.12f}'".format(math.pi))
    print("Diff:    '{:.12f}'".format(math.pi - res))

# ----------------------------------------------------------------------------------
# 10.000.000 Iterations:                                  \/
# Starting:  12  Threads with each Thread computing:  833.333  Leibniz iterations
# Computing rest ...
# Our Pi:  '3.141592553590'
# Math Pi: '3.141592653590'
# Diff:    '0.000000100000'
# ----------------------------------------------------------------------------------
# 1.000.000.000 Iterations:                                \/
# Starting:  12  Threads with each Thread computing:  83.333.333  Leibniz iterations
# Computing rest ...
# Our Pi:  '3.141592652589'
# Math Pi: '3.141592653589'
# Diff:    '0.000000001000'
# ----------------------------------------------------------------------------------
