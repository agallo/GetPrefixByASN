__author__ = 'agallo'

# script to get all the prefixes for a given ASN
# should allow user to suppress v4 or v6
# should generate summary report:
# normalize v4 space to num of /24 equiv
# total IP space represented by all v4 prefixes
# normalize v6 to /64 equiv

from jnpr.junos import Device

dev = Device('ip', user = 'username', ssh_private_key_file = 'path to keyfile')

dev.open()

# the autonomous system we're looking for
# eventually, this should be a command line argument
# need to do ASN sanity check:
# see IANA http://www.iana.org/assignments/as-numbers/as-numbers.xhtml
# 1. make sure it is a number
# 2. test and classify:
# a. 0 and 65535 are reserved (error)
# 2-byte Public ASNs are between 1 - 64197 (inclusive)
# 2-byte reserved ASNs are between 64198 and 64495 (inclusive) (generate warning)
# 2-byte private ASNs are between 64512 and 65534 (inclusive) (generate warning)
# 2-byte reserved ASNs for documentation are between 64496 and 64511 (generate warning)
# need to enumerate 4-byte ASNs
ASN = 2906

# need to check syntax of this command
# cli command is show route aspath-regex ".* 2906 .*"
ASNprefixes = dev.rpc.get_route_information(aspath-regex=".* " ASN " .*")
# othercmd1 = dev.rpc.get_route_information(destination="30.30.30.4")

# should return an XML object
# search for an put in a list (dictionary?) all entries with this XML tag
# <rt-destination>

