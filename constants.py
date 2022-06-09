# System Constants

# In the default IRQ affinity config mode
# ID of the RX queue for each CPU 0-23
#CPU_TO_RX_QUEUE_MAP = [0, 6, 7, 8, 1, 9, 10, 11, 2, 12, 13, 14, 3, 15, 16, 17, 4, 18, 19, 20, 5, 21, 22, 23]
CPU_TO_RX_QUEUE_MAP = [0, 8, 9, 10, 1, 11, 12, 13, 2, 14, 15, 16, 3, 17, 18, 19, 4, 20, 21, 22, 5, 23, 24, 25, 6, 26, 27, 28, 7, 29, 30, 31,32]

# DDIO IO WAYS LLC mm register location
DDIO_REG = 0xc8b

# Port for running the coordination service
COMM_PORT = 50000

# Base port of using iperf and netperf
BASE_PORT = 30000
ADDITIONAL_BASE_PORT = 40000

# Maximum number of ntuple filters
MAX_RULE_LOC = 1023

# Maximum number of CPUs/connections
# NOTE: This should be the same as number of CPUs
MAX_CPUS = 32
CPUS = list(range(MAX_CPUS))
MAX_CONNECTIONS = MAX_CPUS
MAX_RPCS = 32

# Path to executables of profiling tools
PERF_PATH = "/home/qizhe/perf_results/perf"
FLAME_PATH = "/home/qizhe/perf_results/FlameGraph"

