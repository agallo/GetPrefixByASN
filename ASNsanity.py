__author__ = 'agallo'

'''
scratch pad to test ASN sanity checking and characterization
function
'''

ianareserved2byte = (0, range(64198, 64495))
ianapriv2byte = range(64512, 65534)
ianadoc2byte = range(64496, 64511)

ianadoc4byte = range(65536, 65551)

# range command may not be the best for the 4-byte special ranges
# because they're so large and it takes so long to populate the list
# probably just use numeric evaluation in if statement
ianareserved4byte = range(65552, 131071)
# need to figure out how to have a list var of multiple ranges
# ianaunalloc4byte = range(135581-196607, 202240-262143)
#  , 265629-327679, 328704-393215, 394240-4199999999)
# maybe use extend??

# ianapriv4byte = range(4200000000, 4294967294)


# maybe use dictionary for var in function?
# ASNtype & ASNnotes would be the dictionary keys?


def ASNsanity(ASN):
    if not isinstance(ASN, int):
        print "ASN is not an integer"
    ASNnotes="Normal ASN"
    if ASN > 65535:
        ASNtype="Four byte ASN"
        if ASN in ianadoc4byte:
            ASNnotes="Reserved for documentation"
        if ASN in ianapriv4byte:
            ASNnotes="Private ASN range"
        if ASN in ianaunalloc4byte:
            ASNnotes="Unallocated range"
        return {'ASNtype':ASNtype, 'ASNnotes':ASNnotes}
    ASNtype="Two byte ASN"
    if ASN in ianareserved2byte:
        ASNnotes="IANA reservered"
    elif ASN in ianapriv2byte:
        ASNnotes="Private ASN range"
    elif ASN in ianadoc2byte:
        ASNnotes="Reserved for documentation"
    return ASNtype, ASNnotes


ASN = 42
