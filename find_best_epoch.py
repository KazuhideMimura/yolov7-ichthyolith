import os
import numpy as np
import argparse
from utils.general import fitness

def main(name):
    results_file = f"runs/train/{name}/results.txt"
    assert os.path.exists(results_file), f"path not exists: {results_file}"
    
    best_epoch, best_fitness = -1, -1.0
    results = np.loadtxt(results_file, usecols = [8, 9, 10, 11], ndmin = 2)
    for x in range(results.shape[0]):
        y = results[x:x+1, :]
        fi = fitness(y)
        if fi >= best_fitness:
            best_epoch, best_fitness = x, round(float(fi), 5)
    log = f"best epoch: epoch_{best_epoch:0=3}.pt, best fitness: {best_fitness}"
    print(log)
    with open(f"runs/train/{name}/best_epoch_{best_epoch}.txt", 'w') as f1:
        f1.write(log)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', type=str, help='train dir name')
    opt = parser.parse_args()
    main(opt.name)
