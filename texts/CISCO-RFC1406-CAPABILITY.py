#
# PySNMP MIB module CISCO-RFC1406-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-RFC1406-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:07 2026
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
ciscoRFC1406Capability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 102))
ciscoRFC1406Capability.setRevisions(('2002-10-22 00:00', '2001-08-17 00:00', '1994-08-18 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoRFC1406Capability.setRevisionsDescriptions(('Support SET operation for dsx1LineCoding and\n\t\t\tdsx1LineType', 'Support SET operation for dsx1LoopbackConfig object.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoRFC1406Capability.setLastUpdated('200210220000Z')
if mibBuilder.loadTexts: ciscoRFC1406Capability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoRFC1406Capability.setContactInfo('\tCisco Systems\n\t\t\t\tCustomer Service\n\t\t\t\n\t\t\tPostal:\t170 West Tasman Drive\n\t\t\t\tSan Jose, CA  95134\n\t\t\t\tUSA\n\t\t\t\n\t\t\t   Tel:\t+1 800 553-NETS\n\t\t\t\n\t\t\tE-mail:\tcs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoRFC1406Capability.setDescription('Agent capabilities for RFC1406-MIB (DS1 MIB)')
ciscoRFC1406CapabilityV10R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 102, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1406CapabilityV10R02 = ciscoRFC1406CapabilityV10R02.setProductRelease('Cisco IOS 10.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1406CapabilityV10R02 = ciscoRFC1406CapabilityV10R02.setStatus('current')
if mibBuilder.loadTexts: ciscoRFC1406CapabilityV10R02.setDescription('ds1 capabilities')
ciscoRFC1406CapabilityV122R12T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 102, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1406CapabilityV122R12T = ciscoRFC1406CapabilityV122R12T.setProductRelease('Cisco IOS 12.2(12)T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1406CapabilityV122R12T = ciscoRFC1406CapabilityV122R12T.setStatus('obsolete')
if mibBuilder.loadTexts: ciscoRFC1406CapabilityV122R12T.setDescription('ds1 capabilities')
ciscoRFC1406CapabilityV122R12TRev2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 102, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1406CapabilityV122R12TRev2 = ciscoRFC1406CapabilityV122R12TRev2.setProductRelease('Cisco IOS 12.2(12)T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1406CapabilityV122R12TRev2 = ciscoRFC1406CapabilityV122R12TRev2.setStatus('current')
if mibBuilder.loadTexts: ciscoRFC1406CapabilityV122R12TRev2.setDescription('ds1 capabilities')
mibBuilder.exportSymbols("CISCO-RFC1406-CAPABILITY", PYSNMP_MODULE_ID=ciscoRFC1406Capability, ciscoRFC1406CapabilityV122R12T=ciscoRFC1406CapabilityV122R12T, ciscoRFC1406Capability=ciscoRFC1406Capability, ciscoRFC1406CapabilityV122R12TRev2=ciscoRFC1406CapabilityV122R12TRev2, ciscoRFC1406CapabilityV10R02=ciscoRFC1406CapabilityV10R02)
