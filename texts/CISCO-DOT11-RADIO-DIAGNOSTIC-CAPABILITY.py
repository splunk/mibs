#
# PySNMP MIB module CISCO-DOT11-RADIO-DIAGNOSTIC-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-DOT11-RADIO-DIAGNOSTIC-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:05 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
NotificationType, MibIdentifier, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, TimeTicks, IpAddress, Bits, Counter64, Gauge32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "TimeTicks", "IpAddress", "Bits", "Counter64", "Gauge32", "Integer32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDot11RadioDiagCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 335))
if mibBuilder.loadTexts: ciscoDot11RadioDiagCapability.setLastUpdated('200309030000Z')
if mibBuilder.loadTexts: ciscoDot11RadioDiagCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDot11RadioDiagCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-dot11@cisco.com')
if mibBuilder.loadTexts: ciscoDot11RadioDiagCapability.setDescription('Agent capabilities for\n                     CISCO-DOT11-RADIO-DIAGNOSTIC-MIB')
ciscoDot11RadioDiagCapabilityV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 335, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11RadioDiagCapabilityV1 = ciscoDot11RadioDiagCapabilityV1.setProductRelease('Cisco IOS 12.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11RadioDiagCapabilityV1 = ciscoDot11RadioDiagCapabilityV1.setStatus('current')
if mibBuilder.loadTexts: ciscoDot11RadioDiagCapabilityV1.setDescription('Cisco Dot11 RADIO DIAGNOSTIC MIB capabilities')
mibBuilder.exportSymbols("CISCO-DOT11-RADIO-DIAGNOSTIC-CAPABILITY", ciscoDot11RadioDiagCapabilityV1=ciscoDot11RadioDiagCapabilityV1, PYSNMP_MODULE_ID=ciscoDot11RadioDiagCapability, ciscoDot11RadioDiagCapability=ciscoDot11RadioDiagCapability)
