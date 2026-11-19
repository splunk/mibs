#
# PySNMP MIB module CISCO-PROCESS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-PROCESS-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:44 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Unsigned32, Gauge32, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, iso, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Unsigned32", "Gauge32", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "iso", "Counter64", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoProcessCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 256))
ciscoProcessCapability.setRevisions(('2013-08-29 00:00', '2009-03-18 00:00', '2008-09-15 00:00', '2007-11-27 00:00', '2007-11-22 00:00', '2006-03-22 00:00', '2006-02-21 00:00', '2005-12-12 00:00', '2004-11-05 00:00', '2003-08-06 00:00', '2001-11-20 00:00',))
if mibBuilder.loadTexts: ciscoProcessCapability.setLastUpdated('201308290000Z')
if mibBuilder.loadTexts: ciscoProcessCapability.setOrganization('Cisco Systems, Inc.')
ciscoProcessCapabilityV12R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 256, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityV12R00 = ciscoProcessCapabilityV12R00.setProductRelease('Cisco IOS 12.0S')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityV12R00 = ciscoProcessCapabilityV12R00.setStatus('current')
ciscoProcessCapabilityV12R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 256, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityV12R01 = ciscoProcessCapabilityV12R01.setProductRelease('Cisco IOS 12.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityV12R01 = ciscoProcessCapabilityV12R01.setStatus('current')
ciscoProcessCapabilityV12R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 256, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityV12R02 = ciscoProcessCapabilityV12R02.setProductRelease('Cisco IOS 12.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityV12R02 = ciscoProcessCapabilityV12R02.setStatus('current')
ciscoProcessCapCatOSV07R0201 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 256, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapCatOSV07R0201 = ciscoProcessCapCatOSV07R0201.setProductRelease('Cisco CatOS 7.2(1)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapCatOSV07R0201 = ciscoProcessCapCatOSV07R0201.setStatus('current')
ciscoProcessCapabilityV12R02S = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 256, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityV12R02S = ciscoProcessCapabilityV12R02S.setProductRelease('Cisco IOS 12.2S')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityV12R02S = ciscoProcessCapabilityV12R02S.setStatus('current')
ciscoProcessCapabilityV12R03 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 256, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityV12R03 = ciscoProcessCapabilityV12R03.setProductRelease('Cisco IOS 12.3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityV12R03 = ciscoProcessCapabilityV12R03.setStatus('current')
ciscoProcessCapabilityV12R03T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 256, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityV12R03T = ciscoProcessCapabilityV12R03T.setProductRelease('Cisco IOS 12.3T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityV12R03T = ciscoProcessCapabilityV12R03T.setStatus('current')
ciscoProcessCapabilitySAN3R0001 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 256, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilitySAN3R0001 = ciscoProcessCapabilitySAN3R0001.setProductRelease('SAN-OS 3.0(1)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilitySAN3R0001 = ciscoProcessCapabilitySAN3R0001.setStatus('current')
ciscoProcessCapabilityACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 256, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityACSWV03R000 = ciscoProcessCapabilityACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityACSWV03R000 = ciscoProcessCapabilityACSWV03R000.setStatus('current')
ciscoProcessCapIOSXRV2R0CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 256, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapIOSXRV2R0CRS1 = ciscoProcessCapIOSXRV2R0CRS1.setProductRelease('Cisco IOS XR 2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapIOSXRV2R0CRS1 = ciscoProcessCapIOSXRV2R0CRS1.setStatus('current')
ciscoProcessCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 256, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapc4710aceVA1R700 = ciscoProcessCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                for ACE 4710 Application Control Engine \n                Appliance')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapc4710aceVA1R700 = ciscoProcessCapc4710aceVA1R700.setStatus('current')
ciscoProcessCapabilityIONV12R02SXH33 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 256, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityIONV12R02SXH33 = ciscoProcessCapabilityIONV12R02SXH33.setProductRelease('Modular IOS(ION) 12.2SXH33')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityIONV12R02SXH33 = ciscoProcessCapabilityIONV12R02SXH33.setStatus('current')
ciscoProcessCapabilityIOSV12R02SXH33 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 256, 13))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityIOSV12R02SXH33 = ciscoProcessCapabilityIOSV12R02SXH33.setProductRelease('Cisco IOS 12.2SXH33')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityIOSV12R02SXH33 = ciscoProcessCapabilityIOSV12R02SXH33.setStatus('current')
ciscoProcessCapabilityGssV03R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 256, 14))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityGssV03R00 = ciscoProcessCapabilityGssV03R00.setProductRelease('Global Site Selector(GSS) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityGssV03R00 = ciscoProcessCapabilityGssV03R00.setStatus('current')
ciscoProcessCapabilityGssV03R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 256, 15))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityGssV03R01 = ciscoProcessCapabilityGssV03R01.setProductRelease('Global Site Selector(GSS) 3.1(0)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityGssV03R01 = ciscoProcessCapabilityGssV03R01.setStatus('current')
ciscoProcessCapabilityWAASV05R03 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 256, 16))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityWAASV05R03 = ciscoProcessCapabilityWAASV05R03.setProductRelease('OS=WAAS\n                     OSVERSION=5.3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityWAASV05R03 = ciscoProcessCapabilityWAASV05R03.setStatus('current')
mibBuilder.exportSymbols("CISCO-PROCESS-CAPABILITY", ciscoProcessCapabilityACSWV03R000=ciscoProcessCapabilityACSWV03R000, ciscoProcessCapabilityV12R03T=ciscoProcessCapabilityV12R03T, ciscoProcessCapabilityV12R01=ciscoProcessCapabilityV12R01, ciscoProcessCapabilityV12R02=ciscoProcessCapabilityV12R02, ciscoProcessCapCatOSV07R0201=ciscoProcessCapCatOSV07R0201, ciscoProcessCapc4710aceVA1R700=ciscoProcessCapc4710aceVA1R700, ciscoProcessCapabilityIONV12R02SXH33=ciscoProcessCapabilityIONV12R02SXH33, PYSNMP_MODULE_ID=ciscoProcessCapability, ciscoProcessCapabilityIOSV12R02SXH33=ciscoProcessCapabilityIOSV12R02SXH33, ciscoProcessCapabilityGssV03R00=ciscoProcessCapabilityGssV03R00, ciscoProcessCapabilityV12R03=ciscoProcessCapabilityV12R03, ciscoProcessCapabilityGssV03R01=ciscoProcessCapabilityGssV03R01, ciscoProcessCapabilityV12R00=ciscoProcessCapabilityV12R00, ciscoProcessCapabilitySAN3R0001=ciscoProcessCapabilitySAN3R0001, ciscoProcessCapabilityWAASV05R03=ciscoProcessCapabilityWAASV05R03, ciscoProcessCapabilityV12R02S=ciscoProcessCapabilityV12R02S, ciscoProcessCapability=ciscoProcessCapability, ciscoProcessCapIOSXRV2R0CRS1=ciscoProcessCapIOSXRV2R0CRS1)
