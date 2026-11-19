#
# PySNMP MIB module CISCO-UDP-STD-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-UDP-STD-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:23 2026
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
ciscoUdpStdCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 482))
ciscoUdpStdCapability.setRevisions(('2008-06-30 00:00', '2006-11-08 00:00', '2006-05-26 00:00', '2006-02-07 00:00',))
if mibBuilder.loadTexts: ciscoUdpStdCapability.setLastUpdated('200806300000Z')
if mibBuilder.loadTexts: ciscoUdpStdCapability.setOrganization('Cisco Systems, Inc.')
ciscoUdpStdCapIOSXRV3R2CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 482, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdpStdCapIOSXRV3R2CRS1 = ciscoUdpStdCapIOSXRV3R2CRS1.setProductRelease('Cisco IOS XR 3.2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdpStdCapIOSXRV3R2CRS1 = ciscoUdpStdCapIOSXRV3R2CRS1.setStatus('current')
ciscoUdpStdCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 482, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdpStdCapACSWV03R000 = ciscoUdpStdCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0\n                     for Application Control Engine(ACE) \n                     Service Module.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdpStdCapACSWV03R000 = ciscoUdpStdCapACSWV03R000.setStatus('current')
ciscoUdpStdCapIOSXRV3R4CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 482, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdpStdCapIOSXRV3R4CRS1 = ciscoUdpStdCapIOSXRV3R4CRS1.setProductRelease('Cisco IOS XR 3.4 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdpStdCapIOSXRV3R4CRS1 = ciscoUdpStdCapIOSXRV3R4CRS1.setStatus('current')
ciscoUdpStdCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 482, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdpStdCapc4710aceVA1R700 = ciscoUdpStdCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                    for ACE 4710 Application Control Engine \n                    Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdpStdCapc4710aceVA1R700 = ciscoUdpStdCapc4710aceVA1R700.setStatus('current')
mibBuilder.exportSymbols("CISCO-UDP-STD-CAPABILITY", ciscoUdpStdCapIOSXRV3R4CRS1=ciscoUdpStdCapIOSXRV3R4CRS1, ciscoUdpStdCapability=ciscoUdpStdCapability, PYSNMP_MODULE_ID=ciscoUdpStdCapability, ciscoUdpStdCapACSWV03R000=ciscoUdpStdCapACSWV03R000, ciscoUdpStdCapc4710aceVA1R700=ciscoUdpStdCapc4710aceVA1R700, ciscoUdpStdCapIOSXRV3R2CRS1=ciscoUdpStdCapIOSXRV3R2CRS1)
