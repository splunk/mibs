#
# PySNMP MIB module CISCO-WAN-VISM-LAPD-TRUNK-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-WAN-VISM-LAPD-TRUNK-CAPABILITY
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
cwVismLapdTrunkCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 160, 336))
cwVismLapdTrunkCapability.setRevisions(('2001-03-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cwVismLapdTrunkCapability.setRevisionsDescriptions(('Initial version of this MIB module',))
if mibBuilder.loadTexts: cwVismLapdTrunkCapability.setLastUpdated('200108220000Z')
if mibBuilder.loadTexts: cwVismLapdTrunkCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cwVismLapdTrunkCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                        Tel: +1 800 553-NETS\n\n                E-mail: cs-vism@cisco.com')
if mibBuilder.loadTexts: cwVismLapdTrunkCapability.setDescription('The Agent Capabilities for CISCO-WAN-LAPD-TRUNK-MIB.')
cwVismLapdTrunkCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 336, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwVismLapdTrunkCapabilityV2R00 = cwVismLapdTrunkCapabilityV2R00.setProductRelease('VISM Release2.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwVismLapdTrunkCapabilityV2R00 = cwVismLapdTrunkCapabilityV2R00.setStatus('current')
if mibBuilder.loadTexts: cwVismLapdTrunkCapabilityV2R00.setDescription('CISCO-WAN-LAPD-TRUNK-MIB Capabilities')
mibBuilder.exportSymbols("CISCO-WAN-VISM-LAPD-TRUNK-CAPABILITY", PYSNMP_MODULE_ID=cwVismLapdTrunkCapability, cwVismLapdTrunkCapability=cwVismLapdTrunkCapability, cwVismLapdTrunkCapabilityV2R00=cwVismLapdTrunkCapabilityV2R00)
