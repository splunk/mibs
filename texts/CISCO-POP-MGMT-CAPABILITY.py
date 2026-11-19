#
# PySNMP MIB module CISCO-POP-MGMT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-POP-MGMT-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:14 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, Gauge32, MibIdentifier, NotificationType, Unsigned32, Counter64, ObjectIdentity, IpAddress, iso, Counter32, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "Gauge32", "MibIdentifier", "NotificationType", "Unsigned32", "Counter64", "ObjectIdentity", "IpAddress", "iso", "Counter32", "ModuleIdentity", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoPopMgmtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 447))
ciscoPopMgmtCapability.setRevisions(('2005-10-12 00:00', '2005-08-25 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoPopMgmtCapability.setRevisionsDescriptions(('Added variations for cpmDS0UsageGroupRev2.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoPopMgmtCapability.setLastUpdated('200510120000Z')
if mibBuilder.loadTexts: ciscoPopMgmtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoPopMgmtCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W. Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                Tel: +1 800 553-NETS\n\n                E-mail: cs-voice@cisco.com')
if mibBuilder.loadTexts: ciscoPopMgmtCapability.setDescription('Agent capabilities for CISCO-POP-MGMT-MIB.')
ciscoPopMgmtCapabilityV12R04 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 447, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPopMgmtCapabilityV12R04 = ciscoPopMgmtCapabilityV12R04.setProductRelease('Cisco IOS 12.4 for C3600 family platforms')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPopMgmtCapabilityV12R04 = ciscoPopMgmtCapabilityV12R04.setStatus('current')
if mibBuilder.loadTexts: ciscoPopMgmtCapabilityV12R04.setDescription('Cisco POP management agent capabilities for \n                 C3600 family platforms')
mibBuilder.exportSymbols("CISCO-POP-MGMT-CAPABILITY", PYSNMP_MODULE_ID=ciscoPopMgmtCapability, ciscoPopMgmtCapabilityV12R04=ciscoPopMgmtCapabilityV12R04, ciscoPopMgmtCapability=ciscoPopMgmtCapability)
