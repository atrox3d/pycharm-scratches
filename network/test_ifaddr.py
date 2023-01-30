import ifaddr

for adapter in ifaddr.get_adapters():
    print(f"{adapter.name=}")
    print(f"{adapter.nice_name=}")
    ip: ifaddr.IP
    for ip in adapter.ips:
        # if ip.network_prefix != 24:
        #     continue
        if not ip.is_IPv4:
            continue
        print(f"\t{ip.nice_name=}")
        print(f"\t{ip.network_prefix=}")
        print(f"\t{ip.ip=}")