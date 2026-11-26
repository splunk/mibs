#
# PySNMP MIB module CISCO-MAU-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-MAU-EXT-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:59 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMauExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 404))
ciscoMauExtCapability.setRevisions(('2008-10-28 00:00', '2004-12-31 00:00',))
if mibBuilder.loadTexts: ciscoMauExtCapability.setLastUpdated('200810280000Z')
if mibBuilder.loadTexts: ciscoMauExtCapability.setOrganization('Cisco Systems, Inc.')
ciscoMauExtCapCatOSV08R0401 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 404, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMauExtCapCatOSV08R0401 = ciscoMauExtCapCatOSV08R0401.setProductRelease('Cisco CatOS 8.4(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMauExtCapCatOSV08R0401 = ciscoMauExtCapCatOSV08R0401.setStatus('current')
ciscoMauExtCapV12R0233SXIPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 404, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMauExtCapV12R0233SXIPCat6K = ciscoMauExtCapV12R0233SXIPCat6K.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMauExtCapV12R0233SXIPCat6K = ciscoMauExtCapV12R0233SXIPCat6K.setStatus('current')
mibBuilder.exportSymbols("CISCO-MAU-EXT-CAPABILITY", ciscoMauExtCapV12R0233SXIPCat6K=ciscoMauExtCapV12R0233SXIPCat6K, ciscoMauExtCapability=ciscoMauExtCapability, PYSNMP_MODULE_ID=ciscoMauExtCapability, ciscoMauExtCapCatOSV08R0401=ciscoMauExtCapCatOSV08R0401)
