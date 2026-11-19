#
# PySNMP MIB module CISCO-ITP-MONITOR-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ITP-MONITOR-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:23 2026
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
mibBuilder.exportSymbols("CISCO-ITP-MONITOR-CAPABILITY", ciscoItpMonCapabilityV12R0251SW=ciscoItpMonCapabilityV12R0251SW, ciscoItpMonCapability=ciscoItpMonCapability, PYSNMP_MODULE_ID=ciscoItpMonCapability, ciscoItpMonCapabilityV12R0221SW=ciscoItpMonCapabilityV12R0221SW)
