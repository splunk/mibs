#
# PySNMP MIB module CISCO-GGSN-QOS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-GGSN-QOS-CAPABILITY
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
ciscoGgsnQosCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 295))
ciscoGgsnQosCapability.setRevisions(('2003-04-08 16:00',))
if mibBuilder.loadTexts: ciscoGgsnQosCapability.setLastUpdated('200304081600Z')
if mibBuilder.loadTexts: ciscoGgsnQosCapability.setOrganization('Cisco Systems, Inc.')
ciscoGgsnQosCapabilityV12R2M4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 295, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGgsnQosCapabilityV12R2M4 = ciscoGgsnQosCapabilityV12R2M4.setProductRelease('Cisco IOS 12.2(4)MX, 12.2(8)YY')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGgsnQosCapabilityV12R2M4 = ciscoGgsnQosCapabilityV12R2M4.setStatus('current')
ciscoGgsnQosCapabilityV12R2M8 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 295, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGgsnQosCapabilityV12R2M8 = ciscoGgsnQosCapabilityV12R2M8.setProductRelease('Cisco IOS 12.2(8)YW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGgsnQosCapabilityV12R2M8 = ciscoGgsnQosCapabilityV12R2M8.setStatus('current')
mibBuilder.exportSymbols("CISCO-GGSN-QOS-CAPABILITY", ciscoGgsnQosCapability=ciscoGgsnQosCapability, ciscoGgsnQosCapabilityV12R2M8=ciscoGgsnQosCapabilityV12R2M8, PYSNMP_MODULE_ID=ciscoGgsnQosCapability, ciscoGgsnQosCapabilityV12R2M4=ciscoGgsnQosCapabilityV12R2M4)
