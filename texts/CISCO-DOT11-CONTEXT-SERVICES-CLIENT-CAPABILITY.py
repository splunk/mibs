#
# PySNMP MIB module CISCO-DOT11-CONTEXT-SERVICES-CLIENT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-DOT11-CONTEXT-SERVICES-CLIENT-CAPABILITY
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
ciscoDot11CscCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 336))
ciscoDot11CscCapability.setRevisions(('2004-07-24 00:00', '2003-08-25 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDot11CscCapability.setRevisionsDescriptions(('Added ciscoDot11CscCapabilityV2 for IOS \n                 12.3(2).', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoDot11CscCapability.setLastUpdated('200407240000Z')
if mibBuilder.loadTexts: ciscoDot11CscCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDot11CscCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-dot11@cisco.com')
if mibBuilder.loadTexts: ciscoDot11CscCapability.setDescription('Agent capabilities for CISCO-CONTEXT-SERVICES-\n                 CLIENT-MIB')
ciscoDot11CscCapabilityV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 336, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11CscCapabilityV1 = ciscoDot11CscCapabilityV1.setProductRelease('Cisco IOS 12.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11CscCapabilityV1 = ciscoDot11CscCapabilityV1.setStatus('current')
if mibBuilder.loadTexts: ciscoDot11CscCapabilityV1.setDescription('Cisco Dot11 CONTEXT SERVICES CLIENT\n                           MIB capabilities')
ciscoDot11CscCapabilityV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 336, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11CscCapabilityV2 = ciscoDot11CscCapabilityV2.setProductRelease('Cisco IOS 12.3(2) JA')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11CscCapabilityV2 = ciscoDot11CscCapabilityV2.setStatus('current')
if mibBuilder.loadTexts: ciscoDot11CscCapabilityV2.setDescription('Cisco Dot11 CONTEXT SERVICES CLIENT\n                         MIB capabilities for IOS 12.3(2).')
mibBuilder.exportSymbols("CISCO-DOT11-CONTEXT-SERVICES-CLIENT-CAPABILITY", PYSNMP_MODULE_ID=ciscoDot11CscCapability, ciscoDot11CscCapabilityV1=ciscoDot11CscCapabilityV1, ciscoDot11CscCapability=ciscoDot11CscCapability, ciscoDot11CscCapabilityV2=ciscoDot11CscCapabilityV2)
