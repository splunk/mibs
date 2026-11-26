#
# PySNMP MIB module CISCO-WAN-VISM-MG-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-WAN-VISM-MG-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:00 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoWanAgentCapability, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWanAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoWanVismMgCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 160, 320))
ciscoWanVismMgCapability.setRevisions(('2000-07-17 00:00', '2000-03-17 00:00',))
if mibBuilder.loadTexts: ciscoWanVismMgCapability.setLastUpdated('200003170000Z')
if mibBuilder.loadTexts: ciscoWanVismMgCapability.setOrganization('Cisco Systems, Inc.')
ciscoWanVismMgCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 320, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismMgCapabilityV2R00 = ciscoWanVismMgCapabilityV2R00.setProductRelease('VISM Release1.5,VISM Release2.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismMgCapabilityV2R00 = ciscoWanVismMgCapabilityV2R00.setStatus('current')
ciscoWanVismMgCapabilityV2R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 320, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismMgCapabilityV2R02 = ciscoWanVismMgCapabilityV2R02.setProductRelease('VISM Release2.02')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismMgCapabilityV2R02 = ciscoWanVismMgCapabilityV2R02.setStatus('current')
mibBuilder.exportSymbols("CISCO-WAN-VISM-MG-CAPABILITY", ciscoWanVismMgCapability=ciscoWanVismMgCapability, ciscoWanVismMgCapabilityV2R00=ciscoWanVismMgCapabilityV2R00, ciscoWanVismMgCapabilityV2R02=ciscoWanVismMgCapabilityV2R02, PYSNMP_MODULE_ID=ciscoWanVismMgCapability)
