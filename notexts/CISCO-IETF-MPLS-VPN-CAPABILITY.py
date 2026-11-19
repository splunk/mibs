#
# PySNMP MIB module CISCO-IETF-MPLS-VPN-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IETF-MPLS-VPN-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:44 2026
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
ciscoMplsVpnCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 308))
ciscoMplsVpnCapability.setRevisions(('2003-06-25 12:00',))
if mibBuilder.loadTexts: ciscoMplsVpnCapability.setLastUpdated('200306251200Z')
if mibBuilder.loadTexts: ciscoMplsVpnCapability.setOrganization('Cisco Systems, Inc.')
ciscoMplsVpnCapabilityV12 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 308, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMplsVpnCapabilityV12 = ciscoMplsVpnCapabilityV12.setProductRelease('Cisco IOS 12.0(21)ST, Cisco IOS 12.2(21)T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMplsVpnCapabilityV12 = ciscoMplsVpnCapabilityV12.setStatus('current')
mibBuilder.exportSymbols("CISCO-IETF-MPLS-VPN-CAPABILITY", ciscoMplsVpnCapabilityV12=ciscoMplsVpnCapabilityV12, ciscoMplsVpnCapability=ciscoMplsVpnCapability, PYSNMP_MODULE_ID=ciscoMplsVpnCapability)
