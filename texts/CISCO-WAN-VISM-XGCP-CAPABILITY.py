#
# PySNMP MIB module CISCO-WAN-VISM-XGCP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-WAN-VISM-XGCP-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:46 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoWanAgentCapability, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWanAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoWanVismXgcpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 160, 322))
ciscoWanVismXgcpCapability.setRevisions(('2002-02-27 00:00', '2002-01-21 00:00', '2001-08-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoWanVismXgcpCapability.setRevisionsDescriptions(('Fix bug CSCdw32263 where xgcpRestartDelay returns illegal value', 'Changed INCLUDES fields in order to pass SMIC compiler', 'Added ciscoWanVismXgcpCapabilityV2R01 AGENT-CAPABILITIES.',))
if mibBuilder.loadTexts: ciscoWanVismXgcpCapability.setLastUpdated('200202270000Z')
if mibBuilder.loadTexts: ciscoWanVismXgcpCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoWanVismXgcpCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                        Tel: +1 800 553-NETS\n\n                E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoWanVismXgcpCapability.setDescription('The Agent Capabilities for XGCP-MIB.')
ciscoWanVismXgcpCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 322, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismXgcpCapabilityV2R00 = ciscoWanVismXgcpCapabilityV2R00.setProductRelease('VISM Release1.5,VISM Release2.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismXgcpCapabilityV2R00 = ciscoWanVismXgcpCapabilityV2R00.setStatus('current')
if mibBuilder.loadTexts: ciscoWanVismXgcpCapabilityV2R00.setDescription('XGCP MIB Capabilities')
ciscoWanVismXgcpCapabilityV2R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 322, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismXgcpCapabilityV2R01 = ciscoWanVismXgcpCapabilityV2R01.setProductRelease('VISM Release2.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismXgcpCapabilityV2R01 = ciscoWanVismXgcpCapabilityV2R01.setStatus('current')
if mibBuilder.loadTexts: ciscoWanVismXgcpCapabilityV2R01.setDescription('XGCP MIB Capabilities')
ciscoWanVismXgcpCapabilityV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 322, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismXgcpCapabilityV3R00 = ciscoWanVismXgcpCapabilityV3R00.setProductRelease('VISM Release3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismXgcpCapabilityV3R00 = ciscoWanVismXgcpCapabilityV3R00.setStatus('current')
if mibBuilder.loadTexts: ciscoWanVismXgcpCapabilityV3R00.setDescription('XGCP MIB Capabilities')
mibBuilder.exportSymbols("CISCO-WAN-VISM-XGCP-CAPABILITY", ciscoWanVismXgcpCapabilityV3R00=ciscoWanVismXgcpCapabilityV3R00, PYSNMP_MODULE_ID=ciscoWanVismXgcpCapability, ciscoWanVismXgcpCapabilityV2R01=ciscoWanVismXgcpCapabilityV2R01, ciscoWanVismXgcpCapabilityV2R00=ciscoWanVismXgcpCapabilityV2R00, ciscoWanVismXgcpCapability=ciscoWanVismXgcpCapability)
