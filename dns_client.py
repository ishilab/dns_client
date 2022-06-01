# dns_client.py
#
#  Starter code for the assignment
#

import sys


class DNSClient:
    def __init__(self):
        pass

    def do_query(self, name_server: str, domain_str: str) -> None:
        pass


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(
            f'Usage python3 {sys.argv[0]} server domain_in_question', file=sys.stderr)
        sys.exit(1)

    name_server = sys.argv[1]
    domain_str = sys.argv[2]
    dns_client = DNSClient()
    dns_client.do_query(name_server, domain_str)
