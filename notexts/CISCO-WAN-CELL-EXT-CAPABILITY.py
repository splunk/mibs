#
# PySNMP MIB module CISCO-WAN-CELL-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-WAN-CELL-EXT-CAPABILITY
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
ciscoWanCellExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 625))
ciscoWanCellExtCapability.setRevisions(('2014-03-21 00:00',))
if mibBuilder.loadTexts: ciscoWanCellExtCapability.setLastUpdated('201403210000Z')
if mibBuilder.loadTexts: ciscoWanCellExtCapability.setOrganization('Cisco Systems, Inc.')
cwceCapV15R0501PIsr = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 625, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwceCapV15R0501PIsr = cwceCapV15R0501PIsr.setProductRelease('Cisco IOS 15.5(1) Version on Cisco ISR\n                    3900/2900/1900/3800/2800/1800/800 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwceCapV15R0501PIsr = cwceCapV15R0501PIsr.setStatus('current')
mibBuilder.exportSymbols("CISCO-WAN-CELL-EXT-CAPABILITY", PYSNMP_MODULE_ID=ciscoWanCellExtCapability, cwceCapV15R0501PIsr=cwceCapV15R0501PIsr, ciscoWanCellExtCapability=ciscoWanCellExtCapability)
