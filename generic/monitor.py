import subprocess
import time
import json

def get_docker_stats(container_name):
    """
    Retrieves resource usage statistics for a specified Docker container.

    Args:
    container_name (str): The name or ID of the Docker container.
    """
    try:
        stats = subprocess.check_output(["docker", "stats", "--no-stream", "--format", "{{json .}}", container_name])
        return json.loads(stats)
    except subprocess.CalledProcessError as e:
        print(f"Error retrieving stats for container {container_name}: {e}")
        return None

def monitor_docker_container(container_name, duration=60):
    """
    Monitors the specified Docker container for a given duration.

    Args:
    container_name (str): The name or ID of the Docker container.
    duration (int): The monitoring duration in seconds.
    """
    start_time = time.time()
    while time.time() - start_time < duration:
        stats = get_docker_stats(container_name)
        if stats:
            print(f"Container: {container_name}, CPU: {stats['CPUPerc']}, Memory: {stats['MemPerc']}, Net I/O: {stats['NetIO']}, Block I/O: {stats['BlockIO']}")
        time.sleep(1)

# Example usage
if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python script.py <container_name> <duration_in_seconds>")
        sys.exit(1)

    container_name = sys.argv[1]
    duration = int(sys.argv[2])
    monitor_docker_container(container_name, duration)
