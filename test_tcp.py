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

def get_ports(ports_string):
    # Partir por | e -
    port_entries = ports_string.split('|')
    ports = []
    for entry in port_entries:
        if '-' in entry:
            start, end = [int(e) for e in entry.split('-')]
            ports.extend(list(range(start, end + 1)))
        else:
            ports.append(int(entry))
    return ports

def read_input(input_file, output_file):
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

            cid, ip, ports_string = parts
            ports = get_ports(ports_string)

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

    read_input(args.file, args.csv)

'''
# syndic.txt
TMM;192.168.29.30;22|80|443|3000-3003|8000-8003|9109
DEV;192.168.29.40;22|80|443|3000-3003|8000-8003|9109
ENV;192.168.29.50;22|80|443|3000-3003|8000-8003|9109

# Run script
python run.py --file syndics.txt --csv result.csv
'''
