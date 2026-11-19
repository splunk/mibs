#
# PySNMP MIB module CISCO-WAN-CELL-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-WAN-CELL-EXT-CAPABILITY
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
ciscoWanCellExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 625))
ciscoWanCellExtCapability.setRevisions(('2014-03-21 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoWanCellExtCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoWanCellExtCapability.setLastUpdated('201403210000Z')
if mibBuilder.loadTexts: ciscoWanCellExtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoWanCellExtCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoWanCellExtCapability.setDescription('The capabilities description of CISCO-WAN-CELL-EXT-MIB.')
cwceCapV15R0501PIsr = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 625, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwceCapV15R0501PIsr = cwceCapV15R0501PIsr.setProductRelease('Cisco IOS 15.5(1) Version on Cisco ISR\n                    3900/2900/1900/3800/2800/1800/800 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwceCapV15R0501PIsr = cwceCapV15R0501PIsr.setStatus('current')
if mibBuilder.loadTexts: cwceCapV15R0501PIsr.setDescription('CISCO-WAN-CELL-EXT-MIB agent capabilities.')
mibBuilder.exportSymbols("CISCO-WAN-CELL-EXT-CAPABILITY", ciscoWanCellExtCapability=ciscoWanCellExtCapability, cwceCapV15R0501PIsr=cwceCapV15R0501PIsr, PYSNMP_MODULE_ID=ciscoWanCellExtCapability)
