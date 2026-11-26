#
# PySNMP MIB module CISCO-PORT-QOS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-PORT-QOS-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:00 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoPortQosCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 209))
ciscoPortQosCapability.setRevisions(('2008-09-25 00:00', '2001-02-05 00:00',))
if mibBuilder.loadTexts: ciscoPortQosCapability.setLastUpdated('200809250000Z')
if mibBuilder.loadTexts: ciscoPortQosCapability.setOrganization('Cisco Systems, Inc.')
ciscoPortQosCapabilityCat2948gL3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 209, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPortQosCapabilityCat2948gL3 = ciscoPortQosCapabilityCat2948gL3.setProductRelease('Cisco IOS 12.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPortQosCapabilityCat2948gL3 = ciscoPortQosCapabilityCat2948gL3.setStatus('current')
ciscoPortQosCapabilityV12R0250SE = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 209, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPortQosCapabilityV12R0250SE = ciscoPortQosCapabilityV12R0250SE.setProductRelease('Cisco IOS 12.2(50)SE')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPortQosCapabilityV12R0250SE = ciscoPortQosCapabilityV12R0250SE.setStatus('current')
mibBuilder.exportSymbols("CISCO-PORT-QOS-CAPABILITY", PYSNMP_MODULE_ID=ciscoPortQosCapability, ciscoPortQosCapabilityCat2948gL3=ciscoPortQosCapabilityCat2948gL3, ciscoPortQosCapabilityV12R0250SE=ciscoPortQosCapabilityV12R0250SE, ciscoPortQosCapability=ciscoPortQosCapability)
