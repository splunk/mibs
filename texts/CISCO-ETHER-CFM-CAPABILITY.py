#
# PySNMP MIB module CISCO-ETHER-CFM-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ETHER-CFM-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:45 2026
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
ciscoEtherCfmMibCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 431))
ciscoEtherCfmMibCapability.setRevisions(('2005-02-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoEtherCfmMibCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoEtherCfmMibCapability.setLastUpdated('200502110000Z')
if mibBuilder.loadTexts: ciscoEtherCfmMibCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoEtherCfmMibCapability.setContactInfo('            Cisco Systems\n                     Customer Service\n             Postal: 170 W Tasman Drive\n                     San Jose, CA 95134\n                     USA\n                Tel: +1 800 553-NETS\n             E-mail: cs-ethermibs@cisco.com')
if mibBuilder.loadTexts: ciscoEtherCfmMibCapability.setDescription('Agent capabilities for the CISCO-ETHER-CFM-MIB.')
ciscoEtherCfmMibCapabilityV122 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 431, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEtherCfmMibCapabilityV122 = ciscoEtherCfmMibCapabilityV122.setProductRelease('Cisco IOS 12.2X (exact rev TBD)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEtherCfmMibCapabilityV122 = ciscoEtherCfmMibCapabilityV122.setStatus('current')
if mibBuilder.loadTexts: ciscoEtherCfmMibCapabilityV122.setDescription('CISCO-ETHER-CFM-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-ETHER-CFM-CAPABILITY", PYSNMP_MODULE_ID=ciscoEtherCfmMibCapability, ciscoEtherCfmMibCapabilityV122=ciscoEtherCfmMibCapabilityV122, ciscoEtherCfmMibCapability=ciscoEtherCfmMibCapability)
