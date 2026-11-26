#
# PySNMP MIB module CISCO-PORT-QOS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-PORT-QOS-CAPABILITY
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
ciscoPortQosCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 209))
ciscoPortQosCapability.setRevisions(('2008-09-25 00:00', '2001-02-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoPortQosCapability.setRevisionsDescriptions(('Added ciscoPortQosCapabilityV12R0250SE\n                        capabilities.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoPortQosCapability.setLastUpdated('200809250000Z')
if mibBuilder.loadTexts: ciscoPortQosCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoPortQosCapability.setContactInfo('       Cisco Systems\n                                Customer Service\n\n                        Postal: 170 West Tasman Drive\n                                San Jose, CA  95134\n                                USA\n\n                           Tel: +1 800 553-NETS\n\n                        E-mail: cs-port-qos@cisco.com')
if mibBuilder.loadTexts: ciscoPortQosCapability.setDescription('Agent capabilities for the CISCO-PORT-QOS-MIB')
ciscoPortQosCapabilityCat2948gL3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 209, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPortQosCapabilityCat2948gL3 = ciscoPortQosCapabilityCat2948gL3.setProductRelease('Cisco IOS 12.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPortQosCapabilityCat2948gL3 = ciscoPortQosCapabilityCat2948gL3.setStatus('current')
if mibBuilder.loadTexts: ciscoPortQosCapabilityCat2948gL3.setDescription('IOS 12.0 Cisco PORT QOS MIB capabilities')
ciscoPortQosCapabilityV12R0250SE = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 209, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPortQosCapabilityV12R0250SE = ciscoPortQosCapabilityV12R0250SE.setProductRelease('Cisco IOS 12.2(50)SE')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPortQosCapabilityV12R0250SE = ciscoPortQosCapabilityV12R0250SE.setStatus('current')
if mibBuilder.loadTexts: ciscoPortQosCapabilityV12R0250SE.setDescription('MIB Capability from IOS release 12.2(50)SE.')
mibBuilder.exportSymbols("CISCO-PORT-QOS-CAPABILITY", ciscoPortQosCapabilityCat2948gL3=ciscoPortQosCapabilityCat2948gL3, ciscoPortQosCapability=ciscoPortQosCapability, PYSNMP_MODULE_ID=ciscoPortQosCapability, ciscoPortQosCapabilityV12R0250SE=ciscoPortQosCapabilityV12R0250SE)
