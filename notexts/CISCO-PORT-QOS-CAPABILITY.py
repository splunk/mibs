#
# PySNMP MIB module CISCO-PORT-QOS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-PORT-QOS-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:22 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
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
mibBuilder.exportSymbols("CISCO-PORT-QOS-CAPABILITY", PYSNMP_MODULE_ID=ciscoPortQosCapability, ciscoPortQosCapabilityCat2948gL3=ciscoPortQosCapabilityCat2948gL3, ciscoPortQosCapability=ciscoPortQosCapability, ciscoPortQosCapabilityV12R0250SE=ciscoPortQosCapabilityV12R0250SE)
