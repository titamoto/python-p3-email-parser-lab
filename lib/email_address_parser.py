import re

class EmailAddressParser:

    def __init__(self, addresses):
        self.addresses = addresses

    def parse(self):
        separator = re.compile(r'\s|,(?:\s)|,')
        addresses_list = sorted(list(tuple(separator.split(self.addresses))))
        emails = []
        for address in addresses_list:
            if re.fullmatch(r'^\D[a-zA-Z0-9\.]+@[a-zA-Z]+\.[a-z]+', address):
                emails.append(address)
        return emails