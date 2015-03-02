__author__ = 'agallo'

from jnpr.junos import Device
from jnpr.junos.op import routes
import yaml

dev = Device('10.40.40.100', user='netconf', ssh_private_key_file='/home/agallo/.ssh/netconf-id_rsa')

dev.open()

# get as-path-regex from router


ASNprefixes = dev.rpc.get_route_information(aspath-regex=".* 16509 .*")
# othercmd = dev.rpc.get_route_information(destination="30.30.30.4")
#othercmd = dev.rpc.get_interface_information(descriptions)
# othercmd = dev.rpc.get_interface_information(media=True, interface_name='fxp0')


# print ASNprefixes
print othercmd

dev.rpc.get_route_information()
dev.rpc.get_interface-information()
