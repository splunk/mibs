#
# PySNMP MIB module CISCO-IETF-SCTP-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IETF-SCTP-EXT-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:42 2026
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
ciscoSctpExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 220))
ciscoSctpExtCapability.setRevisions(('2002-01-21 00:00', '2001-11-30 00:00',))
if mibBuilder.loadTexts: ciscoSctpExtCapability.setLastUpdated('200201210000Z')
if mibBuilder.loadTexts: ciscoSctpExtCapability.setOrganization('Cisco Systems, Inc.')
ciscoSctpExtCapabilityV12R024MB1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 220, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSctpExtCapabilityV12R024MB1 = ciscoSctpExtCapabilityV12R024MB1.setProductRelease('Cisco IOS 12.2(4)MB1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSctpExtCapabilityV12R024MB1 = ciscoSctpExtCapabilityV12R024MB1.setStatus('current')
ciscoSctpExtCapabilityV12R0204MB3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 220, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSctpExtCapabilityV12R0204MB3 = ciscoSctpExtCapabilityV12R0204MB3.setProductRelease('Cisco IOS 12.2(4)MB3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSctpExtCapabilityV12R0204MB3 = ciscoSctpExtCapabilityV12R0204MB3.setStatus('current')
mibBuilder.exportSymbols("CISCO-IETF-SCTP-EXT-CAPABILITY", ciscoSctpExtCapability=ciscoSctpExtCapability, ciscoSctpExtCapabilityV12R024MB1=ciscoSctpExtCapabilityV12R024MB1, PYSNMP_MODULE_ID=ciscoSctpExtCapability, ciscoSctpExtCapabilityV12R0204MB3=ciscoSctpExtCapabilityV12R0204MB3)
