#
# PySNMP MIB module CISCO-GGSN-QOS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-GGSN-QOS-CAPABILITY
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
ciscoGgsnQosCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 295))
ciscoGgsnQosCapability.setRevisions(('2003-04-08 16:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoGgsnQosCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoGgsnQosCapability.setLastUpdated('200304081600Z')
if mibBuilder.loadTexts: ciscoGgsnQosCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoGgsnQosCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                        Postal: 170 West Tasman Drive\n                                San Jose, CA  95134\n                                USA\n                                Tel: +1 800 553-NETS\n\n                        E-mail: cs-gprs@cisco.com')
if mibBuilder.loadTexts: ciscoGgsnQosCapability.setDescription('Agent capabilities for CISCO-GGSN-QOS-MIB.')
ciscoGgsnQosCapabilityV12R2M4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 295, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGgsnQosCapabilityV12R2M4 = ciscoGgsnQosCapabilityV12R2M4.setProductRelease('Cisco IOS 12.2(4)MX, 12.2(8)YY')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGgsnQosCapabilityV12R2M4 = ciscoGgsnQosCapabilityV12R2M4.setStatus('current')
if mibBuilder.loadTexts: ciscoGgsnQosCapabilityV12R2M4.setDescription('Cisco GGSN QOS MIB capabilities.')
ciscoGgsnQosCapabilityV12R2M8 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 295, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGgsnQosCapabilityV12R2M8 = ciscoGgsnQosCapabilityV12R2M8.setProductRelease('Cisco IOS 12.2(8)YW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGgsnQosCapabilityV12R2M8 = ciscoGgsnQosCapabilityV12R2M8.setStatus('current')
if mibBuilder.loadTexts: ciscoGgsnQosCapabilityV12R2M8.setDescription('Cisco GGSN QOS MIB capabilities.')
mibBuilder.exportSymbols("CISCO-GGSN-QOS-CAPABILITY", PYSNMP_MODULE_ID=ciscoGgsnQosCapability, ciscoGgsnQosCapabilityV12R2M8=ciscoGgsnQosCapabilityV12R2M8, ciscoGgsnQosCapability=ciscoGgsnQosCapability, ciscoGgsnQosCapabilityV12R2M4=ciscoGgsnQosCapabilityV12R2M4)
