#
# PySNMP MIB module CISCO-TCP-STD-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-TCP-STD-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:01 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoTcpStdCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 481))
ciscoTcpStdCapability.setRevisions(('2008-08-11 00:00', '2008-02-08 00:00', '2006-11-08 00:00', '2006-10-25 00:00', '2006-05-26 00:00', '2006-02-06 00:00',))
if mibBuilder.loadTexts: ciscoTcpStdCapability.setLastUpdated('200808110000Z')
if mibBuilder.loadTexts: ciscoTcpStdCapability.setOrganization('Cisco Systems, Inc.')
ciscoTcpStdCapIOSXRV3R2CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 481, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpStdCapIOSXRV3R2CRS1 = ciscoTcpStdCapIOSXRV3R2CRS1.setProductRelease('Cisco IOS XR 3.2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpStdCapIOSXRV3R2CRS1 = ciscoTcpStdCapIOSXRV3R2CRS1.setStatus('current')
ciscoTcpStdCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 481, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpStdCapACSWV03R000 = ciscoTcpStdCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0\n\n                    for Application Control Engine(ACE)\n\n                    Service Module.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpStdCapACSWV03R000 = ciscoTcpStdCapACSWV03R000.setStatus('current')
ciscoTcpStdCapCTSV100 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 481, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpStdCapCTSV100 = ciscoTcpStdCapCTSV100.setProductRelease('Cisco TelePresence System (CTS) 1.0.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpStdCapCTSV100 = ciscoTcpStdCapCTSV100.setStatus('current')
ciscoTcpStdCapCTMV1000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 481, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpStdCapCTMV1000 = ciscoTcpStdCapCTMV1000.setProductRelease('Cisco TelePresence Manager (CTM) 1.0.0.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpStdCapCTMV1000 = ciscoTcpStdCapCTMV1000.setStatus('current')
ciscoTcpStdCapIOSXRV3R4CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 481, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpStdCapIOSXRV3R4CRS1 = ciscoTcpStdCapIOSXRV3R4CRS1.setProductRelease('Cisco IOS XR 3.4 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpStdCapIOSXRV3R4CRS1 = ciscoTcpStdCapIOSXRV3R4CRS1.setStatus('current')
ciscoTcpStdCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 481, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpStdCapc4710aceVA1R700 = ciscoTcpStdCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                    for ACE 4710 Application Control Engine \n                    Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpStdCapc4710aceVA1R700 = ciscoTcpStdCapc4710aceVA1R700.setStatus('current')
mibBuilder.exportSymbols("CISCO-TCP-STD-CAPABILITY", ciscoTcpStdCapc4710aceVA1R700=ciscoTcpStdCapc4710aceVA1R700, ciscoTcpStdCapCTSV100=ciscoTcpStdCapCTSV100, ciscoTcpStdCapACSWV03R000=ciscoTcpStdCapACSWV03R000, ciscoTcpStdCapIOSXRV3R2CRS1=ciscoTcpStdCapIOSXRV3R2CRS1, ciscoTcpStdCapIOSXRV3R4CRS1=ciscoTcpStdCapIOSXRV3R4CRS1, ciscoTcpStdCapCTMV1000=ciscoTcpStdCapCTMV1000, PYSNMP_MODULE_ID=ciscoTcpStdCapability, ciscoTcpStdCapability=ciscoTcpStdCapability)
