import os
import time


def disk_usage_recur(path):
    total = os.path.getsize(path)
    if os.path.isdir(path):
        # total += sum([disk_usage_recur(os.path.join(path, p))
        #               for p in os.listdir(path)])
        for filename in os.listdir(path):
            child_path = os.path.join(path, filename)
            total += disk_usage_recur(child_path)

    # print('{0:<7}'.format(total), path)
    return total


def disk_usage_stack(pool):
    total = 0
    while pool:
        current = pool.pop()
        size = os.path.getsize(current)
        # print('{0:<7}'.format(size), current)
        total += size
        if os.path.isdir(current):
            paths = [os.path.join(current, p) for p in os.listdir(current)]
            pool.extend(paths)
    return total

if __name__ == "__main__":
    pool = ['/Users/shouzeluo/Desktop/', ]

    t = time.process_time()
    res_recur = disk_usage_recur('/Users/shouzeluo/Desktop/')
    print(time.process_time() - t)
    print('with recur ', res_recur)

    t = time.process_time()
    res_stack = disk_usage_stack(pool)
    print(time.process_time() - t)
    print('with stack ', res_stack)
