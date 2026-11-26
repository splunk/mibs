#
# PySNMP MIB module CISCO-RADIUS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-RADIUS-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:45 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoRadiusCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 399))
ciscoRadiusCapability.setRevisions(('2008-05-21 00:00', '2007-01-17 00:00', '2004-06-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoRadiusCapability.setRevisionsDescriptions(('Added capability statement\n        ciscoRadiusCapCatOSV08R0701.', 'Added capability statement\n        ciscoRadiusCapCatOSV08R0601.\n\n        Removed the VARIATION crRadiusServerType from\n        ciscoRadiusCapCatOSV08R0401.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoRadiusCapability.setLastUpdated('200805210000Z')
if mibBuilder.loadTexts: ciscoRadiusCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoRadiusCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoRadiusCapability.setDescription('The capabilities description of CISCO-RADIUS-MIB.')
ciscoRadiusCapCatOSV08R0401 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 399, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRadiusCapCatOSV08R0401 = ciscoRadiusCapCatOSV08R0401.setProductRelease('Cisco CatOS 8.4(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRadiusCapCatOSV08R0401 = ciscoRadiusCapCatOSV08R0401.setStatus('current')
if mibBuilder.loadTexts: ciscoRadiusCapCatOSV08R0401.setDescription('CISCO-RADIUS-MIB capabilities.')
ciscoRadiusCapCatOSV08R0601 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 399, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRadiusCapCatOSV08R0601 = ciscoRadiusCapCatOSV08R0601.setProductRelease('Cisco CatOS 8.6(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRadiusCapCatOSV08R0601 = ciscoRadiusCapCatOSV08R0601.setStatus('current')
if mibBuilder.loadTexts: ciscoRadiusCapCatOSV08R0601.setDescription('CISCO-RADIUS-MIB capabilities.')
ciscoRadiusCapCatOSV08R0701 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 399, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRadiusCapCatOSV08R0701 = ciscoRadiusCapCatOSV08R0701.setProductRelease('Cisco CatOS 8.7(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRadiusCapCatOSV08R0701 = ciscoRadiusCapCatOSV08R0701.setStatus('current')
if mibBuilder.loadTexts: ciscoRadiusCapCatOSV08R0701.setDescription('CISCO-RADIUS-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-RADIUS-CAPABILITY", PYSNMP_MODULE_ID=ciscoRadiusCapability, ciscoRadiusCapCatOSV08R0701=ciscoRadiusCapCatOSV08R0701, ciscoRadiusCapCatOSV08R0601=ciscoRadiusCapCatOSV08R0601, ciscoRadiusCapCatOSV08R0401=ciscoRadiusCapCatOSV08R0401, ciscoRadiusCapability=ciscoRadiusCapability)
