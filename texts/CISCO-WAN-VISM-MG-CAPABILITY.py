#
# PySNMP MIB module CISCO-WAN-VISM-MG-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-WAN-VISM-MG-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:14 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ciscoWanAgentCapability, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWanAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Bits, Gauge32, MibIdentifier, NotificationType, Unsigned32, Counter64, ObjectIdentity, IpAddress, iso, Counter32, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Bits", "Gauge32", "MibIdentifier", "NotificationType", "Unsigned32", "Counter64", "ObjectIdentity", "IpAddress", "iso", "Counter32", "ModuleIdentity", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoWanVismMgCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 160, 320))
ciscoWanVismMgCapability.setRevisions(('2000-07-17 00:00', '2000-03-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoWanVismMgCapability.setRevisionsDescriptions(('Added AGENT-CAPABILITIES macro for\n                ', 'Initial version of this MIB module',))
if mibBuilder.loadTexts: ciscoWanVismMgCapability.setLastUpdated('200003170000Z')
if mibBuilder.loadTexts: ciscoWanVismMgCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoWanVismMgCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                        Tel: +1 800 553-NETS\n\n                E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoWanVismMgCapability.setDescription('The Agent Capabilities for CISCO-WAN-MG-MIB.')
ciscoWanVismMgCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 320, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismMgCapabilityV2R00 = ciscoWanVismMgCapabilityV2R00.setProductRelease('VISM Release1.5,VISM Release2.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismMgCapabilityV2R00 = ciscoWanVismMgCapabilityV2R00.setStatus('current')
if mibBuilder.loadTexts: ciscoWanVismMgCapabilityV2R00.setDescription('CISCO-WAN-MG-MIB Capabilities')
ciscoWanVismMgCapabilityV2R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 320, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismMgCapabilityV2R02 = ciscoWanVismMgCapabilityV2R02.setProductRelease('VISM Release2.02')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismMgCapabilityV2R02 = ciscoWanVismMgCapabilityV2R02.setStatus('current')
if mibBuilder.loadTexts: ciscoWanVismMgCapabilityV2R02.setDescription('CISCO-WAN-MG-MIB Capabilities')
mibBuilder.exportSymbols("CISCO-WAN-VISM-MG-CAPABILITY", ciscoWanVismMgCapability=ciscoWanVismMgCapability, PYSNMP_MODULE_ID=ciscoWanVismMgCapability, ciscoWanVismMgCapabilityV2R00=ciscoWanVismMgCapabilityV2R00, ciscoWanVismMgCapabilityV2R02=ciscoWanVismMgCapabilityV2R02)
