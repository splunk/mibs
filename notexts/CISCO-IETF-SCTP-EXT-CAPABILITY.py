#
# PySNMP MIB module CISCO-IETF-SCTP-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IETF-SCTP-EXT-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:00 2026
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
mibBuilder.exportSymbols("CISCO-IETF-SCTP-EXT-CAPABILITY", ciscoSctpExtCapabilityV12R0204MB3=ciscoSctpExtCapabilityV12R0204MB3, ciscoSctpExtCapability=ciscoSctpExtCapability, PYSNMP_MODULE_ID=ciscoSctpExtCapability, ciscoSctpExtCapabilityV12R024MB1=ciscoSctpExtCapabilityV12R024MB1)
