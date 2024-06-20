import csv
from ipwhois import IPWhois

def get_whois_info(ip):
    try:
        w = IPWhois(ip)
        result = w.lookup_rdap()
        return result
    except Exception as e:
        return str(e)

def read_ips_from_csv(file_path):
    try:
        with open(file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            ips = [row[0] for row in reader]
        return ips
    except Exception as e:
        print(f"Error while reading the CSV:{e}")
        return []

def main(csv_file):
    ips = read_ips_from_csv(csv_file)
    for ip in ips:
        print(f"IP: {ip}")
        whois_info = get_whois_info(ip)
        print(whois_info)
        print("-" * 80)

if '__name__' == "_main_":
    csv_file_path = 'IP.csv'
    main(csv_file_path)