# check_process_limits.py
import os
import platform
import resource
import subprocess


def fmt_limit(v):
    if v == resource.RLIM_INFINITY:
        return "infinity"
    return str(v)


def safe_read(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read().strip()
    except Exception:
        return None


def safe_sysctl(key):
    try:
        return subprocess.check_output(["sysctl", "-n", key], text=True).strip()
    except Exception:
        return None


def current_user_proc_count():
    try:
        user = os.environ.get("USER", "")
        out = subprocess.check_output(["ps", "-u", user, "-o", "pid="], text=True)
        return len([x for x in out.splitlines() if x.strip()])
    except Exception:
        return None


def main():
    print("OS:", platform.system(), platform.release())

    # 每用户进程限制（soft/hard）
    if hasattr(resource, "RLIMIT_NPROC"):
        soft, hard = resource.getrlimit(resource.RLIMIT_NPROC)
        print("RLIMIT_NPROC soft:", fmt_limit(soft))
        print("RLIMIT_NPROC hard:", fmt_limit(hard))
    else:
        print("RLIMIT_NPROC: not supported on this platform")

    # 系统级上限
    if platform.system() == "Linux":
        print("kernel.pid_max:", safe_read("/proc/sys/kernel/pid_max"))
    elif platform.system() == "Darwin":
        print("kern.maxproc:", safe_sysctl("kern.maxproc"))
        print("kern.maxprocperuid:", safe_sysctl("kern.maxprocperuid"))
    else:
        print("System-wide process max: no direct unified API")

    # 当前用户已用进程数
    used = current_user_proc_count()
    print("current user process count:", used if used is not None else "unknown")


if __name__ == "__main__":
    main()
