#
# PySNMP MIB module CISCO-WAN-VISM-MGC-REDUN-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-WAN-VISM-MGC-REDUN-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:07 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoWanAgentCapability, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWanAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
NotificationType, MibIdentifier, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, TimeTicks, IpAddress, Bits, Counter64, Gauge32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "TimeTicks", "IpAddress", "Bits", "Counter64", "Gauge32", "Integer32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoWanVismMgcRedunCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 160, 338))
ciscoWanVismMgcRedunCapability.setRevisions(('1970-01-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoWanVismMgcRedunCapability.setRevisionsDescriptions(('Initial version of this MIB module',))
if mibBuilder.loadTexts: ciscoWanVismMgcRedunCapability.setLastUpdated('200108220000Z')
if mibBuilder.loadTexts: ciscoWanVismMgcRedunCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoWanVismMgcRedunCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                        Tel: +1 800 553-NETS\n\n                E-mail: cs-vism@cisco.com')
if mibBuilder.loadTexts: ciscoWanVismMgcRedunCapability.setDescription('The Agent Capabilities for CISCO-WAN-MGC-REDUN-MIB\n                ')
ciscoWanVismMgcRedunCapV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 338, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismMgcRedunCapV2R00 = ciscoWanVismMgcRedunCapV2R00.setProductRelease('VISM Release2.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismMgcRedunCapV2R00 = ciscoWanVismMgcRedunCapV2R00.setStatus('current')
if mibBuilder.loadTexts: ciscoWanVismMgcRedunCapV2R00.setDescription('CISCO-WAN-VISM-MGC-REDUN-MIB capabilities')
mibBuilder.exportSymbols("CISCO-WAN-VISM-MGC-REDUN-CAPABILITY", ciscoWanVismMgcRedunCapV2R00=ciscoWanVismMgcRedunCapV2R00, PYSNMP_MODULE_ID=ciscoWanVismMgcRedunCapability, ciscoWanVismMgcRedunCapability=ciscoWanVismMgcRedunCapability)
