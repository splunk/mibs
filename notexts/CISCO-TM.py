#
# PySNMP MIB module CISCO-TM (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-TM
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:57 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoDomains, = mibBuilder.importSymbols("CISCO-SMI", "ciscoDomains")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoTransportMappings = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 19, 1))
ciscoTransportMappings.setRevisions(('2001-08-23 16:00', '2000-06-21 16:00',))
if mibBuilder.loadTexts: ciscoTransportMappings.setLastUpdated('200108231600Z')
if mibBuilder.loadTexts: ciscoTransportMappings.setOrganization('Cisco Systems, Inc.')
snmpUDPVPNDomain = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 1, 1))
if mibBuilder.loadTexts: snmpUDPVPNDomain.setStatus('current')
class SnmpUDPVPNAddress(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1d.1d.1d.1d/2d/32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(7, 38)

snmpAAL5Domain = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 1, 2))
if mibBuilder.loadTexts: snmpAAL5Domain.setStatus('current')
class SnmpAAL5VCIdentifier(TextualConvention, OctetString):
    status = 'current'
    displayHint = '4d/4d/4d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(12, 12)
    fixedLength = 12

snmpCNSDomain = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 1, 3))
if mibBuilder.loadTexts: snmpCNSDomain.setStatus('current')
class SnmpCNSIdentifier(TextualConvention, OctetString):
    status = 'current'
    displayHint = '19a.255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(19, 274)

mibBuilder.exportSymbols("CISCO-TM", PYSNMP_MODULE_ID=ciscoTransportMappings, ciscoTransportMappings=ciscoTransportMappings, SnmpUDPVPNAddress=SnmpUDPVPNAddress, snmpCNSDomain=snmpCNSDomain, SnmpCNSIdentifier=SnmpCNSIdentifier, snmpAAL5Domain=snmpAAL5Domain, snmpUDPVPNDomain=snmpUDPVPNDomain, SnmpAAL5VCIdentifier=SnmpAAL5VCIdentifier)
