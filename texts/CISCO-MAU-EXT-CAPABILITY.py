#
# PySNMP MIB module CISCO-MAU-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-MAU-EXT-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:07 2026
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
ciscoMauExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 404))
ciscoMauExtCapability.setRevisions(('2008-10-28 00:00', '2004-12-31 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoMauExtCapability.setRevisionsDescriptions(('Added capability statement\n        ciscoMauExtCapV12R0233SXIPCat6K.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoMauExtCapability.setLastUpdated('200810280000Z')
if mibBuilder.loadTexts: ciscoMauExtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoMauExtCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoMauExtCapability.setDescription('The capabilities description of CISCO-MAU-EXT-MIB.')
ciscoMauExtCapCatOSV08R0401 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 404, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMauExtCapCatOSV08R0401 = ciscoMauExtCapCatOSV08R0401.setProductRelease('Cisco CatOS 8.4(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMauExtCapCatOSV08R0401 = ciscoMauExtCapCatOSV08R0401.setStatus('current')
if mibBuilder.loadTexts: ciscoMauExtCapCatOSV08R0401.setDescription('CISCO-MAU-EXT-MIB capabilities.')
ciscoMauExtCapV12R0233SXIPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 404, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMauExtCapV12R0233SXIPCat6K = ciscoMauExtCapV12R0233SXIPCat6K.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMauExtCapV12R0233SXIPCat6K = ciscoMauExtCapV12R0233SXIPCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoMauExtCapV12R0233SXIPCat6K.setDescription('CISCO-MAU-EXT-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-MAU-EXT-CAPABILITY", PYSNMP_MODULE_ID=ciscoMauExtCapability, ciscoMauExtCapV12R0233SXIPCat6K=ciscoMauExtCapV12R0233SXIPCat6K, ciscoMauExtCapCatOSV08R0401=ciscoMauExtCapCatOSV08R0401, ciscoMauExtCapability=ciscoMauExtCapability)
