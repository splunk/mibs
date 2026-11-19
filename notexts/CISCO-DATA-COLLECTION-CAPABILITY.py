#
# PySNMP MIB module CISCO-DATA-COLLECTION-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-DATA-COLLECTION-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:21 2026
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
cDataCollectionCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 425))
cDataCollectionCapability.setRevisions(('2007-08-07 00:00', '2005-01-05 00:00',))
if mibBuilder.loadTexts: cDataCollectionCapability.setLastUpdated('200708070000Z')
if mibBuilder.loadTexts: cDataCollectionCapability.setOrganization('Cisco Systems, Inc.')
cDataCollectionCapabilityV12R0S = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 425, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDataCollectionCapabilityV12R0S = cDataCollectionCapabilityV12R0S.setProductRelease('Cisco IOS 12.0S')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDataCollectionCapabilityV12R0S = cDataCollectionCapabilityV12R0S.setStatus('current')
cDataCollectionCapabilityV12R1S = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 425, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDataCollectionCapabilityV12R1S = cDataCollectionCapabilityV12R1S.setProductRelease('Cisco IOS 12.2SR')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDataCollectionCapabilityV12R1S = cDataCollectionCapabilityV12R1S.setStatus('current')
mibBuilder.exportSymbols("CISCO-DATA-COLLECTION-CAPABILITY", cDataCollectionCapabilityV12R1S=cDataCollectionCapabilityV12R1S, cDataCollectionCapabilityV12R0S=cDataCollectionCapabilityV12R0S, cDataCollectionCapability=cDataCollectionCapability, PYSNMP_MODULE_ID=cDataCollectionCapability)
