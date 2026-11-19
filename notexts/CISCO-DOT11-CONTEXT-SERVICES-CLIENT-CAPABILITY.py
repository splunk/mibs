#
# PySNMP MIB module CISCO-DOT11-CONTEXT-SERVICES-CLIENT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-DOT11-CONTEXT-SERVICES-CLIENT-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:43 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Unsigned32, Gauge32, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, iso, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Unsigned32", "Gauge32", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "iso", "Counter64", "Counter32")
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
mibBuilder.exportSymbols("CISCO-DOT11-CONTEXT-SERVICES-CLIENT-CAPABILITY", ciscoDot11CscCapabilityV2=ciscoDot11CscCapabilityV2, ciscoDot11CscCapability=ciscoDot11CscCapability, ciscoDot11CscCapabilityV1=ciscoDot11CscCapabilityV1, PYSNMP_MODULE_ID=ciscoDot11CscCapability)
