#
# PySNMP MIB module CISCO-IETF-MPLS-VPN-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IETF-MPLS-VPN-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:24 2026
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
ciscoMplsVpnCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 308))
ciscoMplsVpnCapability.setRevisions(('2003-06-25 12:00',))
if mibBuilder.loadTexts: ciscoMplsVpnCapability.setLastUpdated('200306251200Z')
if mibBuilder.loadTexts: ciscoMplsVpnCapability.setOrganization('Cisco Systems, Inc.')
ciscoMplsVpnCapabilityV12 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 308, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMplsVpnCapabilityV12 = ciscoMplsVpnCapabilityV12.setProductRelease('Cisco IOS 12.0(21)ST, Cisco IOS 12.2(21)T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMplsVpnCapabilityV12 = ciscoMplsVpnCapabilityV12.setStatus('current')
mibBuilder.exportSymbols("CISCO-IETF-MPLS-VPN-CAPABILITY", ciscoMplsVpnCapability=ciscoMplsVpnCapability, PYSNMP_MODULE_ID=ciscoMplsVpnCapability, ciscoMplsVpnCapabilityV12=ciscoMplsVpnCapabilityV12)
