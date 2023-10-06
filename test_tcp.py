import socket
import csv
import argparse

def test_connectivity(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    try:
        sock.connect((ip, port))
    except socket.error as e:
        return False
    finally:
        sock.close()
    return True

def read_file_and_test_connections(input_file, output_file):
    results = {}
    
    with open(input_file, 'r') as file:
        for line in file.readlines():
            if ';' not in line:
                print(f"Invalid line: {line.strip()}")
                continue

            parts = line.strip().split(';')
            if len(parts) != 3:
                print(f"Invalid line: {line.strip()}")
                continue

            cid, ip, ports = parts
            
            try:
                ports = [int(port) for port in ports.split('-')]
            except ValueError:
                print(f"Invalid ports: {ports}")
                continue

            results_key = (cid, ip)
            if results_key not in results:
                results[results_key] = []
            
            for port in ports:
                connection_ok = test_connectivity(ip, port)
                results[results_key].append((port, connection_ok))

    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)

        unique_ports = sorted(set(port for port_results in results.values() for port, _ in port_results))
        header = ['CID', 'IP'] + [f'{port}/TCP' for port in unique_ports]
        writer.writerow(header)

        for (cid, ip), ports in results.items():
            port_results = {port: result for port, result in ports}
            writer.writerow([cid, ip] + [port_results.get(port, '') for port in unique_ports])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Test connectivity and generate report.')
    parser.add_argument('--file', type=str, help='Input file.')
    parser.add_argument('--csv', type=str, help='Output CSV.')

    args = parser.parse_args()

    read_file_and_test_connections(args.file, args.csv)
