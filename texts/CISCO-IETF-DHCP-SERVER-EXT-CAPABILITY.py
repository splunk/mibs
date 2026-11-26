#
# PySNMP MIB module CISCO-IETF-DHCP-SERVER-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IETF-DHCP-SERVER-EXT-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:46 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoIetfDhcpSrvExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 438))
ciscoIetfDhcpSrvExtCapability.setRevisions(('2007-02-14 12:00', '2005-05-24 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIetfDhcpSrvExtCapability.setRevisionsDescriptions(('Added capability definition ciscoIetfDhcpServerExtCapabilityV12R02SRC\n        for 12.2SRC.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoIetfDhcpSrvExtCapability.setLastUpdated('200702141200Z')
if mibBuilder.loadTexts: ciscoIetfDhcpSrvExtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIetfDhcpSrvExtCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-dhcp-mib@cisco.com')
if mibBuilder.loadTexts: ciscoIetfDhcpSrvExtCapability.setDescription('Agent capabilities for the CISCO-IETF-DHCP-SERVER-EXT-MIB.')
ciscoIetfDhcpServerExtCapabilityV62R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 438, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfDhcpServerExtCapabilityV62R00 = ciscoIetfDhcpServerExtCapabilityV62R00.setProductRelease('Cisco CNS Network Registrar 6.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfDhcpServerExtCapabilityV62R00 = ciscoIetfDhcpServerExtCapabilityV62R00.setStatus('current')
if mibBuilder.loadTexts: ciscoIetfDhcpServerExtCapabilityV62R00.setDescription('CISCO-IETF-DHCP-SERVER-EXT-MIB capabilities for\n        Cisco CNS Network Registrar 6.2')
ciscoIetfDhcpServerExtCapabilityV12R02SRC = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 438, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfDhcpServerExtCapabilityV12R02SRC = ciscoIetfDhcpServerExtCapabilityV12R02SRC.setProductRelease('Cisco IOS 12.2SRC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfDhcpServerExtCapabilityV12R02SRC = ciscoIetfDhcpServerExtCapabilityV12R02SRC.setStatus('current')
if mibBuilder.loadTexts: ciscoIetfDhcpServerExtCapabilityV12R02SRC.setDescription('CISCO-IETF-DHCP-SERVER-EXT-MIB capabilities for\n        Cisco IOS 12.2SRC')
mibBuilder.exportSymbols("CISCO-IETF-DHCP-SERVER-EXT-CAPABILITY", ciscoIetfDhcpServerExtCapabilityV12R02SRC=ciscoIetfDhcpServerExtCapabilityV12R02SRC, ciscoIetfDhcpSrvExtCapability=ciscoIetfDhcpSrvExtCapability, ciscoIetfDhcpServerExtCapabilityV62R00=ciscoIetfDhcpServerExtCapabilityV62R00, PYSNMP_MODULE_ID=ciscoIetfDhcpSrvExtCapability)
