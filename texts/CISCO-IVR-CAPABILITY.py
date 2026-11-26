#
# PySNMP MIB module CISCO-IVR-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IVR-CAPABILITY
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
ciscoIvrCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 491))
ciscoIvrCapability.setRevisions(('2006-02-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIvrCapability.setRevisionsDescriptions(('Initial version of this MIB.',))
if mibBuilder.loadTexts: ciscoIvrCapability.setLastUpdated('200602020000Z')
if mibBuilder.loadTexts: ciscoIvrCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIvrCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-san@cisco.com')
if mibBuilder.loadTexts: ciscoIvrCapability.setDescription('Agent capabilities for\n                 CISCO-IVR-MIB')
ciscoIvrCapSanOSV30R1MDS9000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 491, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIvrCapSanOSV30R1MDS9000 = ciscoIvrCapSanOSV30R1MDS9000.setProductRelease('Cisco SanOS 3.0(1) on Cisco MDS 9000\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIvrCapSanOSV30R1MDS9000 = ciscoIvrCapSanOSV30R1MDS9000.setStatus('current')
if mibBuilder.loadTexts: ciscoIvrCapSanOSV30R1MDS9000.setDescription('Cisco Inter Virutal Storage Area\n                     Network (Inter-VSAN) Routing\n                     MIB capabilities')
mibBuilder.exportSymbols("CISCO-IVR-CAPABILITY", ciscoIvrCapSanOSV30R1MDS9000=ciscoIvrCapSanOSV30R1MDS9000, ciscoIvrCapability=ciscoIvrCapability, PYSNMP_MODULE_ID=ciscoIvrCapability)
