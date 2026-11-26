#
# PySNMP MIB module CISCO-WAN-VISM-SRCP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-WAN-VISM-SRCP-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:45 2026
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
ciscoWanVismSrcpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 160, 321))
ciscoWanVismSrcpCapability.setRevisions(('2000-07-21 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoWanVismSrcpCapability.setRevisionsDescriptions(('added ciscoWanVismSrcpCapabilityV2R01 macro\n                ',))
if mibBuilder.loadTexts: ciscoWanVismSrcpCapability.setLastUpdated('200109080000Z')
if mibBuilder.loadTexts: ciscoWanVismSrcpCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoWanVismSrcpCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                        Tel: +1 800 553-NETS\n\n                E-mail: cs-vism@cisco.com')
if mibBuilder.loadTexts: ciscoWanVismSrcpCapability.setDescription('The Agent Capabilities for CISCO-WAN-SRCP-MIB.')
ciscoWanVismSrcpCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 321, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismSrcpCapabilityV2R00 = ciscoWanVismSrcpCapabilityV2R00.setProductRelease('VISM Release1.5,VISM Release2.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismSrcpCapabilityV2R00 = ciscoWanVismSrcpCapabilityV2R00.setStatus('current')
if mibBuilder.loadTexts: ciscoWanVismSrcpCapabilityV2R00.setDescription('SRCP MIB Capabilities')
ciscoWanVismSrcpCapabilityV2R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 321, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismSrcpCapabilityV2R01 = ciscoWanVismSrcpCapabilityV2R01.setProductRelease('VISM release 2.0.3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismSrcpCapabilityV2R01 = ciscoWanVismSrcpCapabilityV2R01.setStatus('current')
if mibBuilder.loadTexts: ciscoWanVismSrcpCapabilityV2R01.setDescription('SRCP MIB Capabilities')
mibBuilder.exportSymbols("CISCO-WAN-VISM-SRCP-CAPABILITY", PYSNMP_MODULE_ID=ciscoWanVismSrcpCapability, ciscoWanVismSrcpCapabilityV2R01=ciscoWanVismSrcpCapabilityV2R01, ciscoWanVismSrcpCapability=ciscoWanVismSrcpCapability, ciscoWanVismSrcpCapabilityV2R00=ciscoWanVismSrcpCapabilityV2R00)
