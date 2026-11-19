#
# PySNMP MIB module CISCO-ITP-MONITOR-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ITP-MONITOR-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:43 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Unsigned32, Gauge32, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, iso, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Unsigned32", "Gauge32", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "iso", "Counter64", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoItpMonCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 422))
ciscoItpMonCapability.setRevisions(('2004-11-23 00:00', '2004-04-22 00:00',))
if mibBuilder.loadTexts: ciscoItpMonCapability.setLastUpdated('200411230000Z')
if mibBuilder.loadTexts: ciscoItpMonCapability.setOrganization('Cisco Systems, Inc.')
ciscoItpMonCapabilityV12R0221SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 422, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpMonCapabilityV12R0221SW = ciscoItpMonCapabilityV12R0221SW.setProductRelease('Cisco IOS 12.2(21)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpMonCapabilityV12R0221SW = ciscoItpMonCapabilityV12R0221SW.setStatus('current')
ciscoItpMonCapabilityV12R0251SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 422, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpMonCapabilityV12R0251SW = ciscoItpMonCapabilityV12R0251SW.setProductRelease('Cisco IOS 12.2(25)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpMonCapabilityV12R0251SW = ciscoItpMonCapabilityV12R0251SW.setStatus('current')
mibBuilder.exportSymbols("CISCO-ITP-MONITOR-CAPABILITY", ciscoItpMonCapabilityV12R0251SW=ciscoItpMonCapabilityV12R0251SW, ciscoItpMonCapabilityV12R0221SW=ciscoItpMonCapabilityV12R0221SW, ciscoItpMonCapability=ciscoItpMonCapability, PYSNMP_MODULE_ID=ciscoItpMonCapability)
