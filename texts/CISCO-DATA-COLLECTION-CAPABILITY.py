#
# PySNMP MIB module CISCO-DATA-COLLECTION-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-DATA-COLLECTION-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:46 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cDataCollectionCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 425))
cDataCollectionCapability.setRevisions(('2007-08-07 00:00', '2005-01-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cDataCollectionCapability.setRevisionsDescriptions(('Added Agent-Capability support for IOS 12.2SR.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: cDataCollectionCapability.setLastUpdated('200708070000Z')
if mibBuilder.loadTexts: cDataCollectionCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cDataCollectionCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n                   San Jose, CA  95134\n                    USA\n\n                Tel:+1 800 553-NETS\n\n                    E-mail:        cs-snmp@cisco.com')
if mibBuilder.loadTexts: cDataCollectionCapability.setDescription('Agent capabilities for CISCO-DATA-COLLECTION-MIB')
cDataCollectionCapabilityV12R0S = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 425, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDataCollectionCapabilityV12R0S = cDataCollectionCapabilityV12R0S.setProductRelease('Cisco IOS 12.0S')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDataCollectionCapabilityV12R0S = cDataCollectionCapabilityV12R0S.setStatus('current')
if mibBuilder.loadTexts: cDataCollectionCapabilityV12R0S.setDescription('cisco-data-collection mib capabilities')
cDataCollectionCapabilityV12R1S = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 425, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDataCollectionCapabilityV12R1S = cDataCollectionCapabilityV12R1S.setProductRelease('Cisco IOS 12.2SR')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDataCollectionCapabilityV12R1S = cDataCollectionCapabilityV12R1S.setStatus('current')
if mibBuilder.loadTexts: cDataCollectionCapabilityV12R1S.setDescription('cisco-data-collection mib capabilities')
mibBuilder.exportSymbols("CISCO-DATA-COLLECTION-CAPABILITY", cDataCollectionCapabilityV12R1S=cDataCollectionCapabilityV12R1S, cDataCollectionCapability=cDataCollectionCapability, PYSNMP_MODULE_ID=cDataCollectionCapability, cDataCollectionCapabilityV12R0S=cDataCollectionCapabilityV12R0S)
