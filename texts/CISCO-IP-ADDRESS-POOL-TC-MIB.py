#
# PySNMP MIB module CISCO-IP-ADDRESS-POOL-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IP-ADDRESS-POOL-TC-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:46 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoIpAddressPoolTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 742))
ciscoIpAddressPoolTcMIB.setRevisions(('2010-02-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIpAddressPoolTcMIB.setRevisionsDescriptions(('The initial version of the MIB module.',))
if mibBuilder.loadTexts: ciscoIpAddressPoolTcMIB.setLastUpdated('201005030000Z')
if mibBuilder.loadTexts: ciscoIpAddressPoolTcMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIpAddressPoolTcMIB.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA 95134\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoIpAddressPoolTcMIB.setDescription('This MIB module defines textual conventions used by MIB\n        modules defining objects describing IP address pools.')
class IpAddrPoolInstanceIdentifier(TextualConvention, Unsigned32):
    description = 'An arbitrary integer-value that uniquely identifies a row in a\n        table defined by a MIB module defining objects describing data\n        relating to IP address pool.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class IpAddrPoolInstanceIdentifierOrZero(TextualConvention, Unsigned32):
    description = "This textual convention serves as an extension of the\n        IpAddressPoolIdentifier textual convention, which permits the\n        value '0'.  The use of the value '0' is specific to an object,\n        thus requiring the descriptive text associated with the object\n        to describe the semantics of its use."
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class IpAddressPoolName(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for\n        Describing Simple Network Management Protocol (SNMP)\n        Management Frameworks', RFC-3411, December 2002."
    description = 'A string-value that denotes the name assigned to an IP address\n        pool.  The semantics of the string-value are the same as those\n        specified by the SnmpAdminString textual convention defined by\n        the SNMP-FRAMEWORK-MIB [RFC3411].'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

class IpAddressPoolNameOrNull(TextualConvention, OctetString):
    description = 'This textual convention serves as an extension of the\n        IpAddressPoolName textual convention, which permits the null\n        string.  The use of the null string is specific to an object,\n        thus requiring the descriptive text associated with the object\n        to describe the semantics of its use.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class IpAddressPoolGroupName(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for\n        Describing Simple Network Management Protocol (SNMP)\n        Management Frameworks', RFC-3411, December 2002."
    description = 'A string-value that denotes the name assigned to an IP address\n        pool group.  The semantics of the string-value are the same as\n        those specified by the SnmpAdminString textual convention\n        defined by the SNMP-FRAMEWORK-MIB [RFC3411].'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

class IpAddressPoolGroupNameOrNull(TextualConvention, OctetString):
    description = 'This textual convention serves as an extension of the\n        IpAddressPoolGroupName textual convention, which permits the\n        null string.  The use of the null string is specific to an\n        object, thus requiring the descriptive text associated with the\n        object to describe the semantics of the its use.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class IpAddressPoolThresholdUnits(TextualConvention, Integer32):
    description = "An enumerated integer-value that denotes the units used when\n        specifying an IP address pool threshold:\n\n            'other'\n                The implementation of the MIB module using this textual\n                convention does not recognize the IP address pool\n                threshold units.\n\n            'absolute'\n                The value of the corresponding IP address pool threshold\n                is an absolute number of IP addresses or IP prefixes,\n                depending on the context.\n\n            'percent'\n                The value of the corresponding IP address pool threshold\n                is a percentage of the total number of free and in-use\n                IP addresses or IP prefixes contained by a pool."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("other", 1), ("absolute", 2), ("percent", 3))

mibBuilder.exportSymbols("CISCO-IP-ADDRESS-POOL-TC-MIB", IpAddrPoolInstanceIdentifier=IpAddrPoolInstanceIdentifier, IpAddressPoolNameOrNull=IpAddressPoolNameOrNull, IpAddressPoolGroupNameOrNull=IpAddressPoolGroupNameOrNull, IpAddressPoolName=IpAddressPoolName, IpAddrPoolInstanceIdentifierOrZero=IpAddrPoolInstanceIdentifierOrZero, ciscoIpAddressPoolTcMIB=ciscoIpAddressPoolTcMIB, PYSNMP_MODULE_ID=ciscoIpAddressPoolTcMIB, IpAddressPoolThresholdUnits=IpAddressPoolThresholdUnits, IpAddressPoolGroupName=IpAddressPoolGroupName)
