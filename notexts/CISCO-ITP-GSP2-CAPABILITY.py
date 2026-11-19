#
# PySNMP MIB module CISCO-ITP-GSP2-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ITP-GSP2-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:22 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoGsp2Capability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 307))
ciscoGsp2Capability.setRevisions(('2004-08-25 00:00', '2003-11-24 00:00', '2003-07-17 00:00',))
if mibBuilder.loadTexts: ciscoGsp2Capability.setLastUpdated('200408250000Z')
if mibBuilder.loadTexts: ciscoGsp2Capability.setOrganization('Cisco Systems, Inc.')
ciscoGsp2CapabilityV12R0204MB4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 307, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsp2CapabilityV12R0204MB4 = ciscoGsp2CapabilityV12R0204MB4.setProductRelease('Cisco IOS 12.2(4)MB10')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsp2CapabilityV12R0204MB4 = ciscoGsp2CapabilityV12R0204MB4.setStatus('current')
ciscoGsp2CapabilityV12R022004SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 307, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsp2CapabilityV12R022004SW = ciscoGsp2CapabilityV12R022004SW.setProductRelease('Cisco IOS 12.2(20.4)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsp2CapabilityV12R022004SW = ciscoGsp2CapabilityV12R022004SW.setStatus('current')
ciscoGsp2CapabilityV12R022300SW1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 307, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsp2CapabilityV12R022300SW1 = ciscoGsp2CapabilityV12R022300SW1.setProductRelease('Cisco IOS 12.2(23)SW1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsp2CapabilityV12R022300SW1 = ciscoGsp2CapabilityV12R022300SW1.setStatus('current')
mibBuilder.exportSymbols("CISCO-ITP-GSP2-CAPABILITY", ciscoGsp2CapabilityV12R022004SW=ciscoGsp2CapabilityV12R022004SW, PYSNMP_MODULE_ID=ciscoGsp2Capability, ciscoGsp2CapabilityV12R0204MB4=ciscoGsp2CapabilityV12R0204MB4, ciscoGsp2CapabilityV12R022300SW1=ciscoGsp2CapabilityV12R022300SW1, ciscoGsp2Capability=ciscoGsp2Capability)
