#
# PySNMP MIB module CISCO-WAN-VISM-XGCP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-WAN-VISM-XGCP-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:00 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoWanAgentCapability, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWanAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoWanVismXgcpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 160, 322))
ciscoWanVismXgcpCapability.setRevisions(('2002-02-27 00:00', '2002-01-21 00:00', '2001-08-09 00:00',))
if mibBuilder.loadTexts: ciscoWanVismXgcpCapability.setLastUpdated('200202270000Z')
if mibBuilder.loadTexts: ciscoWanVismXgcpCapability.setOrganization('Cisco Systems, Inc.')
ciscoWanVismXgcpCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 322, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismXgcpCapabilityV2R00 = ciscoWanVismXgcpCapabilityV2R00.setProductRelease('VISM Release1.5,VISM Release2.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismXgcpCapabilityV2R00 = ciscoWanVismXgcpCapabilityV2R00.setStatus('current')
ciscoWanVismXgcpCapabilityV2R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 322, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismXgcpCapabilityV2R01 = ciscoWanVismXgcpCapabilityV2R01.setProductRelease('VISM Release2.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismXgcpCapabilityV2R01 = ciscoWanVismXgcpCapabilityV2R01.setStatus('current')
ciscoWanVismXgcpCapabilityV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 322, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismXgcpCapabilityV3R00 = ciscoWanVismXgcpCapabilityV3R00.setProductRelease('VISM Release3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismXgcpCapabilityV3R00 = ciscoWanVismXgcpCapabilityV3R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-WAN-VISM-XGCP-CAPABILITY", ciscoWanVismXgcpCapabilityV2R00=ciscoWanVismXgcpCapabilityV2R00, ciscoWanVismXgcpCapabilityV3R00=ciscoWanVismXgcpCapabilityV3R00, PYSNMP_MODULE_ID=ciscoWanVismXgcpCapability, ciscoWanVismXgcpCapability=ciscoWanVismXgcpCapability, ciscoWanVismXgcpCapabilityV2R01=ciscoWanVismXgcpCapabilityV2R01)
