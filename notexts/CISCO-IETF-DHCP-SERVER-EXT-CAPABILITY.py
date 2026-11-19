#
# PySNMP MIB module CISCO-IETF-DHCP-SERVER-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IETF-DHCP-SERVER-EXT-CAPABILITY
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
ciscoIetfDhcpSrvExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 438))
ciscoIetfDhcpSrvExtCapability.setRevisions(('2007-02-14 12:00', '2005-05-24 00:00',))
if mibBuilder.loadTexts: ciscoIetfDhcpSrvExtCapability.setLastUpdated('200702141200Z')
if mibBuilder.loadTexts: ciscoIetfDhcpSrvExtCapability.setOrganization('Cisco Systems, Inc.')
ciscoIetfDhcpServerExtCapabilityV62R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 438, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfDhcpServerExtCapabilityV62R00 = ciscoIetfDhcpServerExtCapabilityV62R00.setProductRelease('Cisco CNS Network Registrar 6.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfDhcpServerExtCapabilityV62R00 = ciscoIetfDhcpServerExtCapabilityV62R00.setStatus('current')
ciscoIetfDhcpServerExtCapabilityV12R02SRC = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 438, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfDhcpServerExtCapabilityV12R02SRC = ciscoIetfDhcpServerExtCapabilityV12R02SRC.setProductRelease('Cisco IOS 12.2SRC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfDhcpServerExtCapabilityV12R02SRC = ciscoIetfDhcpServerExtCapabilityV12R02SRC.setStatus('current')
mibBuilder.exportSymbols("CISCO-IETF-DHCP-SERVER-EXT-CAPABILITY", ciscoIetfDhcpServerExtCapabilityV62R00=ciscoIetfDhcpServerExtCapabilityV62R00, ciscoIetfDhcpServerExtCapabilityV12R02SRC=ciscoIetfDhcpServerExtCapabilityV12R02SRC, PYSNMP_MODULE_ID=ciscoIetfDhcpSrvExtCapability, ciscoIetfDhcpSrvExtCapability=ciscoIetfDhcpSrvExtCapability)
