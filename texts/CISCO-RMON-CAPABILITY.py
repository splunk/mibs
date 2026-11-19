#
# PySNMP MIB module CISCO-RMON-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-RMON-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:06 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
NotificationType, MibIdentifier, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, TimeTicks, IpAddress, Bits, Counter64, Gauge32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "TimeTicks", "IpAddress", "Bits", "Counter64", "Gauge32", "Integer32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoRmonCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 357))
ciscoRmonCapability.setRevisions(('2008-08-04 00:00', '2006-03-09 00:00', '2004-04-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoRmonCapability.setRevisionsDescriptions(('Added capability statement ciscoRmonCapNXOSV04R0101PMDS9000.', 'Add VARIATIONs for notifications\n        fallingAlarm and risingAlarm in \n        ciscoRmonCapCatOSV08R0101.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoRmonCapability.setLastUpdated('200808040000Z')
if mibBuilder.loadTexts: ciscoRmonCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoRmonCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com\n            cs-rmon@cisco.com')
if mibBuilder.loadTexts: ciscoRmonCapability.setDescription('The capabilities description of\n        RMON-MIB.')
ciscoRmonCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 357, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRmonCapCatOSV08R0101 = ciscoRmonCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRmonCapCatOSV08R0101 = ciscoRmonCapCatOSV08R0101.setStatus('current')
if mibBuilder.loadTexts: ciscoRmonCapCatOSV08R0101.setDescription('RMON-MIB capabilities.')
ciscoRmonCapNXOSV04R0101PMDS9000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 357, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRmonCapNXOSV04R0101PMDS9000 = ciscoRmonCapNXOSV04R0101PMDS9000.setProductRelease('Cisco NX-OS 4.1(1) on MDS9000 Storage Switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRmonCapNXOSV04R0101PMDS9000 = ciscoRmonCapNXOSV04R0101PMDS9000.setStatus('current')
if mibBuilder.loadTexts: ciscoRmonCapNXOSV04R0101PMDS9000.setDescription('RMON-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-RMON-CAPABILITY", PYSNMP_MODULE_ID=ciscoRmonCapability, ciscoRmonCapNXOSV04R0101PMDS9000=ciscoRmonCapNXOSV04R0101PMDS9000, ciscoRmonCapCatOSV08R0101=ciscoRmonCapCatOSV08R0101, ciscoRmonCapability=ciscoRmonCapability)
