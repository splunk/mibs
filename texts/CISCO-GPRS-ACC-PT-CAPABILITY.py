#
# PySNMP MIB module CISCO-GPRS-ACC-PT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-GPRS-ACC-PT-CAPABILITY
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
cgprsAccPtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 298))
cgprsAccPtCapability.setRevisions(('2003-04-08 17:50',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cgprsAccPtCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: cgprsAccPtCapability.setLastUpdated('200304081750Z')
if mibBuilder.loadTexts: cgprsAccPtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cgprsAccPtCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                        Postal: 170 West Tasman Drive\n                                San Jose, CA  95134\n                                USA\n                                Tel: +1 800 553-NETS\n\n                        E-mail: cs-gprs@cisco.com')
if mibBuilder.loadTexts: cgprsAccPtCapability.setDescription('Agent capabilities for CISCO-GPRS-ACC-PT-MIB.')
cgprsAccPtCapabilityV12R2M4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 298, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cgprsAccPtCapabilityV12R2M4 = cgprsAccPtCapabilityV12R2M4.setProductRelease('Cisco IOS 12.2(4)MX & 12.2(8)YY')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cgprsAccPtCapabilityV12R2M4 = cgprsAccPtCapabilityV12R2M4.setStatus('current')
if mibBuilder.loadTexts: cgprsAccPtCapabilityV12R2M4.setDescription('Cisco GPRS ACCESS POINT MIB capabilities.')
cgprsAccPtCapabilityV12R2M8 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 298, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cgprsAccPtCapabilityV12R2M8 = cgprsAccPtCapabilityV12R2M8.setProductRelease('Cisco IOS 12.2(8)YW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cgprsAccPtCapabilityV12R2M8 = cgprsAccPtCapabilityV12R2M8.setStatus('current')
if mibBuilder.loadTexts: cgprsAccPtCapabilityV12R2M8.setDescription('Cisco GPRS ACCESS POINT MIB capabilities.')
mibBuilder.exportSymbols("CISCO-GPRS-ACC-PT-CAPABILITY", PYSNMP_MODULE_ID=cgprsAccPtCapability, cgprsAccPtCapabilityV12R2M4=cgprsAccPtCapabilityV12R2M4, cgprsAccPtCapabilityV12R2M8=cgprsAccPtCapabilityV12R2M8, cgprsAccPtCapability=cgprsAccPtCapability)
