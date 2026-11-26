#
# PySNMP MIB module CISCO-RFC1407-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-RFC1407-CAPABILITY
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
ciscoRFC1407Capability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 102))
ciscoRFC1407Capability.setRevisions(('2001-08-17 00:00', '1996-06-19 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoRFC1407Capability.setRevisionsDescriptions(('Support SET operation for dsx3LoopbackConfig object.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoRFC1407Capability.setLastUpdated('200108170000Z')
if mibBuilder.loadTexts: ciscoRFC1407Capability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoRFC1407Capability.setContactInfo('\tCisco Systems\n\t\t\t\tCustomer Service\n\t\t\t\n\t\t\tPostal:\t170 West Tasman Drive\n\t\t\t\tSan Jose, CA  95134\n\t\t\t\tUSA\n\t\t\t\n\t\t\t   Tel:\t+1 800 553-NETS\n\t\t\t\n\t\t\tE-mail:\tcs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoRFC1407Capability.setDescription('Agent capabilities for RFC1407-MIB (DS3 MIB)')
ciscoRFC1407CapabilityV11R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 102, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1407CapabilityV11R02 = ciscoRFC1407CapabilityV11R02.setProductRelease('Cisco IOS 11.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1407CapabilityV11R02 = ciscoRFC1407CapabilityV11R02.setStatus('current')
if mibBuilder.loadTexts: ciscoRFC1407CapabilityV11R02.setDescription('ds3 capabilities')
ciscoRFC1407CapabilityV122R12 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 102, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1407CapabilityV122R12 = ciscoRFC1407CapabilityV122R12.setProductRelease('Cisco IOS 12.2(12)T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1407CapabilityV122R12 = ciscoRFC1407CapabilityV122R12.setStatus('current')
if mibBuilder.loadTexts: ciscoRFC1407CapabilityV122R12.setDescription('ds3 capabilities')
mibBuilder.exportSymbols("CISCO-RFC1407-CAPABILITY", PYSNMP_MODULE_ID=ciscoRFC1407Capability, ciscoRFC1407CapabilityV11R02=ciscoRFC1407CapabilityV11R02, ciscoRFC1407Capability=ciscoRFC1407Capability, ciscoRFC1407CapabilityV122R12=ciscoRFC1407CapabilityV122R12)
