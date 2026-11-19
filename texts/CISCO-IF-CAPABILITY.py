#
# PySNMP MIB module CISCO-IF-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IF-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:13 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, Gauge32, MibIdentifier, NotificationType, Unsigned32, Counter64, ObjectIdentity, IpAddress, iso, Counter32, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "Gauge32", "MibIdentifier", "NotificationType", "Unsigned32", "Counter64", "ObjectIdentity", "IpAddress", "iso", "Counter32", "ModuleIdentity", "TimeTicks")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
ciscoIfCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 125))
ciscoIfCapability.setRevisions(('2008-03-17 00:00', '2006-11-03 00:00', '2006-10-30 00:00', '2006-07-17 00:00', '2006-02-02 00:00', '2004-08-09 00:00', '2004-02-21 00:00', '2004-02-20 00:00', '2003-03-14 00:00', '2002-06-12 00:00', '2000-02-09 00:00', '1998-11-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIfCapability.setRevisionsDescriptions(('Added ciscoIfCapabilityc4710aceVA1R700\n        agent capabilities for ACE 4710 Application \n        Control Engine(ACE) Appliance.', 'Added ciscoIfCapabilityIOSXRV3R4CRS1 agent\n        capability for IOS XR 3.4', 'Added capability for Cisco TelePresence System (CTS) and\n        Cisco TelePresence Manager (CTM) platforms.', 'Added ciscoIfCapabilityACSWV03R000 agent capabilities\n        for Cisco Application Control Software (ACSW) 3.0.', 'Added  ciscoIfCapabilityIOSXRV2R0CRS1 agent capabilities\n        for IOS XR release 2.0.', 'Added ciscoIfCapabilityV5R015 agent capabilities for MGX\n        product series: MPSM Service Module and VXSM (Voice Switch \n        Service Module).', 'Added following Agent capabilities for Catalyst\n        6000/6500 and Cisco 7600 series devices:\n\n        ciscoIfCapabilityCatOSV08R0101 and\n        ciscoIfCapabilityCatOSV08R0301.', 'Added ciscoIfCapabilityV5R00 agent capabilities for MGX\n        product series: MPSM Service Module and VXSM (Voice Switch\n        Service Module.', 'Added following Agent capabilities for MGX product series:\n\n        - ciscoIfCapabilityV4R00 for\n          AXSM 10 Gig. Module (AXSM-XG) and \n          AXSM Enhanced Module (AXSM-E).', 'Added following Agent capabilities for MGX product series:\n\n        - ciscoIfCapabilityPxmVR200 for \n          PXM(Processor Switch Module) Module\n\n        - ciscoIfCapabilityAxsmVR200 for \n          AXSM(ATM Switch Service Module)\n\n        - ciscoIfCapabilityAxsmeV21R60 for \n          AXSM Enhanced Module.\n\n        - ciscoIfCapabilityFrsm12V3R00 for\n          Frame Relay Service Module(FRSM-12).', 'Modification of ifCounterDiscontinuityTime,\n        ifTableLastChange object and LinkUp/Down trap\n        objects.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoIfCapability.setLastUpdated('200803170000Z')
if mibBuilder.loadTexts: ciscoIfCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIfCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-snmp@cisco.com\n                   cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoIfCapability.setDescription('Agent capabilities for IF-MIB')
ciscoIfCapabilityV11R03 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 125, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityV11R03 = ciscoIfCapabilityV11R03.setProductRelease('Cisco IOS 11.3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityV11R03 = ciscoIfCapabilityV11R03.setStatus('current')
if mibBuilder.loadTexts: ciscoIfCapabilityV11R03.setDescription('IF MIB capabilities')
ciscoIfCapabilityV12R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 125, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityV12R00 = ciscoIfCapabilityV12R00.setProductRelease('Cisco IOS 12.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityV12R00 = ciscoIfCapabilityV12R00.setStatus('current')
if mibBuilder.loadTexts: ciscoIfCapabilityV12R00.setDescription('IF MIB capabilities')
ciscoIfCapabilityV12R01T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 125, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityV12R01T = ciscoIfCapabilityV12R01T.setProductRelease('Cisco IOS 12.1T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityV12R01T = ciscoIfCapabilityV12R01T.setStatus('current')
if mibBuilder.loadTexts: ciscoIfCapabilityV12R01T.setDescription('IF MIB capabilities')
ciscoIfCapabilityPxmVR200 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 125, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityPxmVR200 = ciscoIfCapabilityPxmVR200.setProductRelease('MGX8850 Release 2.00,BPX SES Release 1.00.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityPxmVR200 = ciscoIfCapabilityPxmVR200.setStatus('current')
if mibBuilder.loadTexts: ciscoIfCapabilityPxmVR200.setDescription('IF MIB capabilities for PXM45, PXM1 Modules.')
ciscoIfCapabilityAxsmVR200 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 125, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityAxsmVR200 = ciscoIfCapabilityAxsmVR200.setProductRelease('MGX8850 Release 2.00.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityAxsmVR200 = ciscoIfCapabilityAxsmVR200.setStatus('current')
if mibBuilder.loadTexts: ciscoIfCapabilityAxsmVR200.setDescription('IF MIB capabilities for ATM Switch Service\n        Module(AXSM).')
ciscoIfCapabilityAxsmeV21R60 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 125, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityAxsmeV21R60 = ciscoIfCapabilityAxsmeV21R60.setProductRelease('MGX8850 Release 2.1.60')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityAxsmeV21R60 = ciscoIfCapabilityAxsmeV21R60.setStatus('current')
if mibBuilder.loadTexts: ciscoIfCapabilityAxsmeV21R60.setDescription('IF MIB capabilities for Enhanced ATM\n        Switch Service Module (AXSM-E).')
ciscoIfCapabilityFrsm12V3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 125, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityFrsm12V3R00 = ciscoIfCapabilityFrsm12V3R00.setProductRelease('MGX8850 Release 3.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityFrsm12V3R00 = ciscoIfCapabilityFrsm12V3R00.setStatus('current')
if mibBuilder.loadTexts: ciscoIfCapabilityFrsm12V3R00.setDescription('IF MIB capabilities for\n        Frame Relay Service Module(FRSM-12).')
ciscoIfCapabilityV4R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 125, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityV4R00 = ciscoIfCapabilityV4R00.setProductRelease('MGX8950, MGX8850 Release 4.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityV4R00 = ciscoIfCapabilityV4R00.setStatus('current')
if mibBuilder.loadTexts: ciscoIfCapabilityV4R00.setDescription('IF MIB capabilities for 10 Gig. ATM\n        Switch Service Module (AXSM-XG) and \n        Enhanced ATM Switch Service Module \n        (AXSM-E).')
ciscoIfCapabilityV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 125, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityV5R00 = ciscoIfCapabilityV5R00.setProductRelease('MGX8850 Release 5.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityV5R00 = ciscoIfCapabilityV5R00.setStatus('current')
if mibBuilder.loadTexts: ciscoIfCapabilityV5R00.setDescription('IF MIB capabilities for Voice Switch\n        Service Module (VXSM) and MPSM in \n        release 5.0.0')
ciscoIfCapabilityCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 125, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityCatOSV08R0101 = ciscoIfCapabilityCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityCatOSV08R0101 = ciscoIfCapabilityCatOSV08R0101.setStatus('current')
if mibBuilder.loadTexts: ciscoIfCapabilityCatOSV08R0101.setDescription('IF MIB agent capabilities.')
ciscoIfCapabilityCatOSV08R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 125, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityCatOSV08R0301 = ciscoIfCapabilityCatOSV08R0301.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityCatOSV08R0301 = ciscoIfCapabilityCatOSV08R0301.setStatus('current')
if mibBuilder.loadTexts: ciscoIfCapabilityCatOSV08R0301.setDescription('IF MIB agent capabilities.')
ciscoIfCapabilityV5R015 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 125, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityV5R015 = ciscoIfCapabilityV5R015.setProductRelease('MGX8850 Release 5.0.15')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityV5R015 = ciscoIfCapabilityV5R015.setStatus('current')
if mibBuilder.loadTexts: ciscoIfCapabilityV5R015.setDescription('IF MIB capabilities for Voice Switch\n        Service Module (VXSM) 5.0.15')
ciscoIfCapabilityIOSXRV2R0CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 125, 13))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityIOSXRV2R0CRS1 = ciscoIfCapabilityIOSXRV2R0CRS1.setProductRelease('Cisco IOS XR 2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityIOSXRV2R0CRS1 = ciscoIfCapabilityIOSXRV2R0CRS1.setStatus('current')
if mibBuilder.loadTexts: ciscoIfCapabilityIOSXRV2R0CRS1.setDescription('IF-MIB capabilities for Cisco IOS\n        XR in releases 2.0')
ciscoIfCapabilityACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 125, 14))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityACSWV03R000 = ciscoIfCapabilityACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0\n                    for Application Control Engine (ACE) \n                    Service Module.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityACSWV03R000 = ciscoIfCapabilityACSWV03R000.setStatus('current')
if mibBuilder.loadTexts: ciscoIfCapabilityACSWV03R000.setDescription('IF-MIB capabilities for Cisco ACSW 3.0.')
ciscoIfCapabilityCTSV100 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 125, 15))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityCTSV100 = ciscoIfCapabilityCTSV100.setProductRelease('Cisco TelePresence System (CTS) 1.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityCTSV100 = ciscoIfCapabilityCTSV100.setStatus('current')
if mibBuilder.loadTexts: ciscoIfCapabilityCTSV100.setDescription('IF-MIB capabilities for CTS 1.0.0')
ciscoIfCapabilityCTMV1000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 125, 16))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityCTMV1000 = ciscoIfCapabilityCTMV1000.setProductRelease('Cisco TelePresence Manager (CTM) 1.0.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityCTMV1000 = ciscoIfCapabilityCTMV1000.setStatus('current')
if mibBuilder.loadTexts: ciscoIfCapabilityCTMV1000.setDescription('IF-MIB capabilities for CTM 1.0.0.0')
ciscoIfCapabilityIOSXRV3R4CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 125, 17))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityIOSXRV3R4CRS1 = ciscoIfCapabilityIOSXRV3R4CRS1.setProductRelease('Cisco IOS XR 3.4 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityIOSXRV3R4CRS1 = ciscoIfCapabilityIOSXRV3R4CRS1.setStatus('current')
if mibBuilder.loadTexts: ciscoIfCapabilityIOSXRV3R4CRS1.setDescription('IF-MIB capabilities for Cisco IOS\n        XR in releases 3.4')
ciscoIfCapabilityc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 125, 18))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityc4710aceVA1R700 = ciscoIfCapabilityc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                     for ACE 4710 Application Control Engine \n                     Appliance')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityc4710aceVA1R700 = ciscoIfCapabilityc4710aceVA1R700.setStatus('current')
if mibBuilder.loadTexts: ciscoIfCapabilityc4710aceVA1R700.setDescription('IF-MIB capabilities for Cisco ACSW A1(7)')
mibBuilder.exportSymbols("CISCO-IF-CAPABILITY", ciscoIfCapabilityAxsmeV21R60=ciscoIfCapabilityAxsmeV21R60, ciscoIfCapabilityPxmVR200=ciscoIfCapabilityPxmVR200, ciscoIfCapabilityFrsm12V3R00=ciscoIfCapabilityFrsm12V3R00, ciscoIfCapabilityc4710aceVA1R700=ciscoIfCapabilityc4710aceVA1R700, ciscoIfCapabilityV5R00=ciscoIfCapabilityV5R00, ciscoIfCapabilityCTSV100=ciscoIfCapabilityCTSV100, ciscoIfCapabilityV11R03=ciscoIfCapabilityV11R03, ciscoIfCapabilityCatOSV08R0301=ciscoIfCapabilityCatOSV08R0301, ciscoIfCapabilityIOSXRV3R4CRS1=ciscoIfCapabilityIOSXRV3R4CRS1, ciscoIfCapabilityV12R01T=ciscoIfCapabilityV12R01T, ciscoIfCapabilityV5R015=ciscoIfCapabilityV5R015, ciscoIfCapabilityV12R00=ciscoIfCapabilityV12R00, ciscoIfCapabilityV4R00=ciscoIfCapabilityV4R00, ciscoIfCapability=ciscoIfCapability, ciscoIfCapabilityAxsmVR200=ciscoIfCapabilityAxsmVR200, ciscoIfCapabilityCTMV1000=ciscoIfCapabilityCTMV1000, ciscoIfCapabilityACSWV03R000=ciscoIfCapabilityACSWV03R000, ciscoIfCapabilityCatOSV08R0101=ciscoIfCapabilityCatOSV08R0101, ciscoIfCapabilityIOSXRV2R0CRS1=ciscoIfCapabilityIOSXRV2R0CRS1, PYSNMP_MODULE_ID=ciscoIfCapability)
