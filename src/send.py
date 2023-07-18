import os
import numpy as np
import subprocess
from main import gene_gene_adj

cwd = os.getcwd()
dir = os.path.dirname(cwd)


def send_adj_matrix(matrix):
    serialized_matrix = np.array2string(matrix, separator=",")

    cpp_exec_file = './' + os.path.join(dir, os.path.join('graphs', os.path.join('bin', 'exec')))
    process = subprocess.Popen([cpp_exec_file], stdin=subprocess.PIPE, stout=subprocess.PIPE, text=True)

    process.stdin.write(serialized_matrix + '\n')
    process.stdin.flush()

    result = process.stdout.readline().strip()

    process.stdin.close()
    process.stdout.close()
    process.terminate()

    return result

if __name__ == "__main__":
    adjacencyMatrix = []
    result = send_adj_matrix(adjacencyMatrix)