#
# PySNMP MIB module CISCO-DIST-DIRECTOR-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-DIST-DIRECTOR-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:06 2026
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
ciscoDistDirCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 267))
ciscoDistDirCapability.setRevisions(('2002-04-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDistDirCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoDistDirCapability.setLastUpdated('200204230000Z')
if mibBuilder.loadTexts: ciscoDistDirCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDistDirCapability.setContactInfo('\tCisco Systems\n\t\t\tCustomer Service\n\n\t\tPostal:\t170 West Tasman Drive\n\t\t\tSan Jose, CA  95134\n\t\t\tUSA\n\n\t\t   Tel:\t+1 800 553-NETS\n\n\t\tE-mail:\tcs-dd@cisco.com')
if mibBuilder.loadTexts: ciscoDistDirCapability.setDescription('Agent capabilities for CISCO-DIST-DIRECTOR-MIB')
ciscoDistDirCapabilityV12R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 267, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDistDirCapabilityV12R02 = ciscoDistDirCapabilityV12R02.setProductRelease('Cisco IOS 12.2(8)T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDistDirCapabilityV12R02 = ciscoDistDirCapabilityV12R02.setStatus('current')
if mibBuilder.loadTexts: ciscoDistDirCapabilityV12R02.setDescription('Cisco Distributed Director MIB capabilities')
mibBuilder.exportSymbols("CISCO-DIST-DIRECTOR-CAPABILITY", ciscoDistDirCapability=ciscoDistDirCapability, ciscoDistDirCapabilityV12R02=ciscoDistDirCapabilityV12R02, PYSNMP_MODULE_ID=ciscoDistDirCapability)
