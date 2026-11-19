#
# PySNMP MIB module CISCO-RS-232-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-RS-232-CAPABILITY
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
ciscoRS232Capability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 115))
ciscoRS232Capability.setRevisions(('2002-05-16 00:00', '1994-08-18 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoRS232Capability.setRevisionsDescriptions(('Added ciscoRS232CapabilityV2R00\n                         capability for MGX8850 and BPX SES\n                         products.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoRS232Capability.setLastUpdated('200205160000Z')
if mibBuilder.loadTexts: ciscoRS232Capability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoRS232Capability.setContactInfo('\tCisco Systems\n\t\t\t\tCustomer Service\n\t\t\t\n\t\t\tPostal:\t170 West Tasman Drive\n\t\t\t\tSan Jose, CA  95134\n\t\t\t\tUSA\n\t\t\t\n\t\t\t   Tel:\t+1 800 553-NETS\n\t\t\t\n\t\t\tE-mail:\tcs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoRS232Capability.setDescription('Agent capabilities for RS-232-MIB')
ciscoRS232CapabilityV10R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 115, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRS232CapabilityV10R02 = ciscoRS232CapabilityV10R02.setProductRelease('Cisco IOS 10.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRS232CapabilityV10R02 = ciscoRS232CapabilityV10R02.setStatus('current')
if mibBuilder.loadTexts: ciscoRS232CapabilityV10R02.setDescription('IOS 10.2 rs232 mib capabilities')
ciscoRS232CapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 115, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRS232CapabilityV2R00 = ciscoRS232CapabilityV2R00.setProductRelease('MGX8850 Release 2.0,\n                BPX SES Release 1.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRS232CapabilityV2R00 = ciscoRS232CapabilityV2R00.setStatus('current')
if mibBuilder.loadTexts: ciscoRS232CapabilityV2R00.setDescription('MGX8850 and BPX SES \n                RS-232-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-RS-232-CAPABILITY", ciscoRS232Capability=ciscoRS232Capability, ciscoRS232CapabilityV10R02=ciscoRS232CapabilityV10R02, ciscoRS232CapabilityV2R00=ciscoRS232CapabilityV2R00, PYSNMP_MODULE_ID=ciscoRS232Capability)
