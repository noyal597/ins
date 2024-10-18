class Policy:
    def __init__(self, local_subnet, remote_subnet, mode, pfs, esp):
        self.local_subnet = local_subnet
        self.remote_subnet = remote_subnet
        self.mode = mode
        self.pfs = pfs
        self.esp = esp


class Connection:
    def __init__(self, local_ip, remote_ip, shared_key=None):
        self.local_ip = local_ip
        self.remote_ip = remote_ip
        self.shared_key = shared_key
        self.policies = []

    def add_policy(self, policy):
        self.policies.append(policy)

    def set_shared_key(self, shared_key):
        self.shared_key = shared_key

    def up(self):
        print("Starting IPsec connection...")
        print("Local IP:", self.local_ip)
        print("Remote IP:", self.remote_ip)
        for policy in self.policies:
            print("\nLocal Subnet:", policy.local_subnet)
            print("Remote Subnet:", policy.remote_subnet)
            print("Mode:", policy.mode)
            print("esp:", policy.esp)
            print("pfs:", policy.pfs)
        print("\nShared Key:", self.shared_key)
        print("IPsec connection is up")


if __name__ == '__main__':
    local_ip = "192.168.0.1"
    remote_ip = "192.168.1.1"
    local_subnet = "10.0.0.0/24"
    remote_subnet = "10.0.1.0/24"
    shared_secret = "My shared secret."

    conn = Connection(local_ip, remote_ip)
    inbound_policy = Policy(local_subnet, remote_subnet, mode="tunnel",
                            pfs="group14", esp="aes128-sha256")
    outbound_policy = Policy(local_subnet, remote_subnet, mode="tunnel",
                            pfs="group14", esp="aes128-sha256")
    conn.add_policy(outbound_policy)
    conn.add_policy(inbound_policy)
    conn.set_shared_key(shared_secret)
    conn.up()
