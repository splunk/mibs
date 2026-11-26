#
# PySNMP MIB module CISCO-ENTITY-SENSOR-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ENTITY-SENSOR-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:59 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoEntitySensorCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 350))
ciscoEntitySensorCapability.setRevisions(('2011-02-03 00:00', '2008-10-06 00:00', '2007-07-09 00:00', '2007-06-29 00:00', '2006-06-29 00:00', '2005-09-15 00:00', '2005-04-22 00:00', '2004-09-09 00:00', '2003-08-12 00:00', '2003-03-13 00:00',))
if mibBuilder.loadTexts: ciscoEntitySensorCapability.setLastUpdated('201102030000Z')
if mibBuilder.loadTexts: ciscoEntitySensorCapability.setOrganization('Cisco Systems, Inc.')
ciscoEntitySensorCapabilityV5R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 350, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntitySensorCapabilityV5R000 = ciscoEntitySensorCapabilityV5R000.setProductRelease('MGX8850 Release 5.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntitySensorCapabilityV5R000 = ciscoEntitySensorCapabilityV5R000.setStatus('current')
cEntitySensorCapV12R0119ECat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 350, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntitySensorCapV12R0119ECat6K = cEntitySensorCapV12R0119ECat6K.setProductRelease('Cisco IOS 12.1(19)E on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntitySensorCapV12R0119ECat6K = cEntitySensorCapV12R0119ECat6K.setStatus('current')
cEntitySensorCapV12R0214SXCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 350, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntitySensorCapV12R0214SXCat6K = cEntitySensorCapV12R0214SXCat6K.setProductRelease('Cisco IOS 12.2(14)SX on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntitySensorCapV12R0214SXCat6K = cEntitySensorCapV12R0214SXCat6K.setStatus('current')
cEntitySensorCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 350, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntitySensorCapCatOSV08R0101 = cEntitySensorCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntitySensorCapCatOSV08R0101 = cEntitySensorCapCatOSV08R0101.setStatus('current')
cEntitySensorCapabilityV5R015 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 350, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntitySensorCapabilityV5R015 = cEntitySensorCapabilityV5R015.setProductRelease('MGX8850 Release 5.0.15')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntitySensorCapabilityV5R015 = cEntitySensorCapabilityV5R015.setStatus('current')
cEntitySensorCapMDS3R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 350, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntitySensorCapMDS3R0 = cEntitySensorCapMDS3R0.setProductRelease('Cisco MDS 3.0(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntitySensorCapMDS3R0 = cEntitySensorCapMDS3R0.setStatus('current')
cEntitySensorCapCatOSV08R0601 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 350, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntitySensorCapCatOSV08R0601 = cEntitySensorCapCatOSV08R0601.setProductRelease('Cisco CatOS 8.6(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntitySensorCapCatOSV08R0601 = cEntitySensorCapCatOSV08R0601.setStatus('current')
cEntitySensorCapIOSXRV3R06CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 350, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntitySensorCapIOSXRV3R06CRS1 = cEntitySensorCapIOSXRV3R06CRS1.setProductRelease('Cisco IOS-XR Release 3.6 for CRS-1.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntitySensorCapIOSXRV3R06CRS1 = cEntitySensorCapIOSXRV3R06CRS1.setStatus('current')
cEntitySensorCapMDS3R1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 350, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntitySensorCapMDS3R1 = cEntitySensorCapMDS3R1.setProductRelease('Cisco MDS Series Storage switches\n                         Release 3.1 onwards.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntitySensorCapMDS3R1 = cEntitySensorCapMDS3R1.setStatus('current')
cEntitySensorCapDCOSNEXUS = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 350, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntitySensorCapDCOSNEXUS = cEntitySensorCapDCOSNEXUS.setProductRelease('Cisco Nexus7000 Series Storage switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntitySensorCapDCOSNEXUS = cEntitySensorCapDCOSNEXUS.setStatus('current')
cEntitySensorCapV12R0250SE = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 350, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntitySensorCapV12R0250SE = cEntitySensorCapV12R0250SE.setProductRelease('Cisco IOS 12.2(50)SE')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntitySensorCapV12R0250SE = cEntitySensorCapV12R0250SE.setStatus('current')
cEntitySensorCapV12R0250SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 350, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntitySensorCapV12R0250SYPCat6K = cEntitySensorCapV12R0250SYPCat6K.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntitySensorCapV12R0250SYPCat6K = cEntitySensorCapV12R0250SYPCat6K.setStatus('current')
mibBuilder.exportSymbols("CISCO-ENTITY-SENSOR-CAPABILITY", ciscoEntitySensorCapability=ciscoEntitySensorCapability, cEntitySensorCapV12R0119ECat6K=cEntitySensorCapV12R0119ECat6K, cEntitySensorCapCatOSV08R0101=cEntitySensorCapCatOSV08R0101, cEntitySensorCapV12R0250SYPCat6K=cEntitySensorCapV12R0250SYPCat6K, cEntitySensorCapDCOSNEXUS=cEntitySensorCapDCOSNEXUS, cEntitySensorCapV12R0214SXCat6K=cEntitySensorCapV12R0214SXCat6K, cEntitySensorCapCatOSV08R0601=cEntitySensorCapCatOSV08R0601, cEntitySensorCapMDS3R1=cEntitySensorCapMDS3R1, cEntitySensorCapMDS3R0=cEntitySensorCapMDS3R0, cEntitySensorCapV12R0250SE=cEntitySensorCapV12R0250SE, cEntitySensorCapabilityV5R015=cEntitySensorCapabilityV5R015, cEntitySensorCapIOSXRV3R06CRS1=cEntitySensorCapIOSXRV3R06CRS1, ciscoEntitySensorCapabilityV5R000=ciscoEntitySensorCapabilityV5R000, PYSNMP_MODULE_ID=ciscoEntitySensorCapability)
