__author__ = 'agallo'

from jnpr.junos import Device

dev = Device('10.40.40.100', user='netconf', ssh_private_key_file='/home/agallo/.ssh/netconf-id_rsa')

dev.open()

# get as-path-regex from router

ASNprefixes = dev.rpc.get_route_information(aspath-regex=".* " ASN " .*")
othercmd = dev.rpc.get_route_information(destination="30.30.30.4")

print ASNprefixes
print othercmd
