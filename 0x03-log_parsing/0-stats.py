def print_statistics(signal, frame):
    global total_file_size, status_code_counts
    print(f"Total file size: {total_file_size}")
    for code, count in sorted(status_code_counts.items()):
        if count > 0:
            print(f"{code}: {count}")
    sys.exit(0)

signal.signal(signal.SIGINT, print_statistics)

try:
    for line in sys.stdin:
        line = line.strip()
        parts = line.split()
        
        if len(parts) != 7:
            continue
        
        ip_address = parts[0]
        date = parts[3][1:]
        request = parts[5]
        status_code = parts[6]
        file_size = int(parts[7])
        
        if not status_code.isdigit():
            continue
        
        status_code = int(status_code)
        
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1
        
        total_file_size += file_size
        line_count += 1
        
        if line_count % 10 == 0:
            print(f"Total file size: {total_file_size}")
            for code, count in sorted(status_code_counts.items()):
                if count > 0:
                    print(f"{code}: {count}")
            print()
        
except KeyboardInterrupt:
    print_statistics(None, None)
