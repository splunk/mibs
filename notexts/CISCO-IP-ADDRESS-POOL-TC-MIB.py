#
# PySNMP MIB module CISCO-IP-ADDRESS-POOL-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IP-ADDRESS-POOL-TC-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:01 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, MibIdentifier, Counter32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "MibIdentifier", "Counter32", "Unsigned32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIpAddressPoolTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 742))
ciscoIpAddressPoolTcMIB.setRevisions(('2010-02-02 00:00',))
if mibBuilder.loadTexts: ciscoIpAddressPoolTcMIB.setLastUpdated('201005030000Z')
if mibBuilder.loadTexts: ciscoIpAddressPoolTcMIB.setOrganization('Cisco Systems, Inc.')
class IpAddrPoolInstanceIdentifier(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class IpAddrPoolInstanceIdentifierOrZero(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class IpAddressPoolName(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for Describing Simple Network Management Protocol (SNMP) Management Frameworks', RFC-3411, December 2002."
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

class IpAddressPoolNameOrNull(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class IpAddressPoolGroupName(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for Describing Simple Network Management Protocol (SNMP) Management Frameworks', RFC-3411, December 2002."
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

class IpAddressPoolGroupNameOrNull(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class IpAddressPoolThresholdUnits(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("other", 1), ("absolute", 2), ("percent", 3))

mibBuilder.exportSymbols("CISCO-IP-ADDRESS-POOL-TC-MIB", IpAddrPoolInstanceIdentifier=IpAddrPoolInstanceIdentifier, ciscoIpAddressPoolTcMIB=ciscoIpAddressPoolTcMIB, IpAddressPoolName=IpAddressPoolName, IpAddressPoolGroupNameOrNull=IpAddressPoolGroupNameOrNull, PYSNMP_MODULE_ID=ciscoIpAddressPoolTcMIB, IpAddrPoolInstanceIdentifierOrZero=IpAddrPoolInstanceIdentifierOrZero, IpAddressPoolNameOrNull=IpAddressPoolNameOrNull, IpAddressPoolThresholdUnits=IpAddressPoolThresholdUnits, IpAddressPoolGroupName=IpAddressPoolGroupName)
