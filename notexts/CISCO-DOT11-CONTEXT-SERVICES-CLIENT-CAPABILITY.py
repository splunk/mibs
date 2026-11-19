#
# PySNMP MIB module CISCO-DOT11-CONTEXT-SERVICES-CLIENT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-DOT11-CONTEXT-SERVICES-CLIENT-CAPABILITY
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
ciscoDot11CscCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 336))
ciscoDot11CscCapability.setRevisions(('2004-07-24 00:00', '2003-08-25 00:00',))
if mibBuilder.loadTexts: ciscoDot11CscCapability.setLastUpdated('200407240000Z')
if mibBuilder.loadTexts: ciscoDot11CscCapability.setOrganization('Cisco Systems, Inc.')
ciscoDot11CscCapabilityV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 336, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11CscCapabilityV1 = ciscoDot11CscCapabilityV1.setProductRelease('Cisco IOS 12.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11CscCapabilityV1 = ciscoDot11CscCapabilityV1.setStatus('current')
ciscoDot11CscCapabilityV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 336, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11CscCapabilityV2 = ciscoDot11CscCapabilityV2.setProductRelease('Cisco IOS 12.3(2) JA')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11CscCapabilityV2 = ciscoDot11CscCapabilityV2.setStatus('current')
mibBuilder.exportSymbols("CISCO-DOT11-CONTEXT-SERVICES-CLIENT-CAPABILITY", PYSNMP_MODULE_ID=ciscoDot11CscCapability, ciscoDot11CscCapability=ciscoDot11CscCapability, ciscoDot11CscCapabilityV1=ciscoDot11CscCapabilityV1, ciscoDot11CscCapabilityV2=ciscoDot11CscCapabilityV2)
