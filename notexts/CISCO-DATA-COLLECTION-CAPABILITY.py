#
# PySNMP MIB module CISCO-DATA-COLLECTION-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-DATA-COLLECTION-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:00 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, MibIdentifier, Counter32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "MibIdentifier", "Counter32", "Unsigned32", "ObjectIdentity")
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
mibBuilder.exportSymbols("CISCO-DATA-COLLECTION-CAPABILITY", cDataCollectionCapabilityV12R1S=cDataCollectionCapabilityV12R1S, cDataCollectionCapability=cDataCollectionCapability, cDataCollectionCapabilityV12R0S=cDataCollectionCapabilityV12R0S, PYSNMP_MODULE_ID=cDataCollectionCapability)
