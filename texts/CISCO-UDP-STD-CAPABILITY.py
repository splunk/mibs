#
# PySNMP MIB module CISCO-UDP-STD-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-UDP-STD-CAPABILITY
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
ciscoUdpStdCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 482))
ciscoUdpStdCapability.setRevisions(('2008-06-30 00:00', '2006-11-08 00:00', '2006-05-26 00:00', '2006-02-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoUdpStdCapability.setRevisionsDescriptions(('Added ciscoUdpStdCapc4710aceVA1R700 agent capability\n        for ACE 4710 Application Control Engine Appliance.', 'Added agent capability for IOS XR 3.4', 'Added capability statement\n        ciscoUdpStdCapACSWV03R000.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoUdpStdCapability.setLastUpdated('200806300000Z')
if mibBuilder.loadTexts: ciscoUdpStdCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoUdpStdCapability.setContactInfo('Cisco Systems\n            Customer Service\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoUdpStdCapability.setDescription('Agent capabilities for UDP-MIB')
ciscoUdpStdCapIOSXRV3R2CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 482, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdpStdCapIOSXRV3R2CRS1 = ciscoUdpStdCapIOSXRV3R2CRS1.setProductRelease('Cisco IOS XR 3.2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdpStdCapIOSXRV3R2CRS1 = ciscoUdpStdCapIOSXRV3R2CRS1.setStatus('current')
if mibBuilder.loadTexts: ciscoUdpStdCapIOSXRV3R2CRS1.setDescription('UDP-MIB capabilities\n        for IOS XR release 3.2.0')
ciscoUdpStdCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 482, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdpStdCapACSWV03R000 = ciscoUdpStdCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0\n                     for Application Control Engine(ACE) \n                     Service Module.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdpStdCapACSWV03R000 = ciscoUdpStdCapACSWV03R000.setStatus('current')
if mibBuilder.loadTexts: ciscoUdpStdCapACSWV03R000.setDescription('UDP-MIB capabilities for ACSW 3.0')
ciscoUdpStdCapIOSXRV3R4CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 482, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdpStdCapIOSXRV3R4CRS1 = ciscoUdpStdCapIOSXRV3R4CRS1.setProductRelease('Cisco IOS XR 3.4 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdpStdCapIOSXRV3R4CRS1 = ciscoUdpStdCapIOSXRV3R4CRS1.setStatus('current')
if mibBuilder.loadTexts: ciscoUdpStdCapIOSXRV3R4CRS1.setDescription('UDP-MIB capabilities\n        for IOS XR release 3.4')
ciscoUdpStdCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 482, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdpStdCapc4710aceVA1R700 = ciscoUdpStdCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                    for ACE 4710 Application Control Engine \n                    Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdpStdCapc4710aceVA1R700 = ciscoUdpStdCapc4710aceVA1R700.setStatus('current')
if mibBuilder.loadTexts: ciscoUdpStdCapc4710aceVA1R700.setDescription('UDP-MIB capabilities for ACSW A1(7).')
mibBuilder.exportSymbols("CISCO-UDP-STD-CAPABILITY", ciscoUdpStdCapc4710aceVA1R700=ciscoUdpStdCapc4710aceVA1R700, ciscoUdpStdCapACSWV03R000=ciscoUdpStdCapACSWV03R000, ciscoUdpStdCapIOSXRV3R4CRS1=ciscoUdpStdCapIOSXRV3R4CRS1, ciscoUdpStdCapIOSXRV3R2CRS1=ciscoUdpStdCapIOSXRV3R2CRS1, PYSNMP_MODULE_ID=ciscoUdpStdCapability, ciscoUdpStdCapability=ciscoUdpStdCapability)
