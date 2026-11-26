#
# PySNMP MIB module CISCO-MEDIA-QUALITY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-MEDIA-QUALITY-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:59 2026
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
ciscoMediaQualityCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 604))
ciscoMediaQualityCapability.setRevisions(('2011-09-23 00:00', '2011-04-15 00:00',))
if mibBuilder.loadTexts: ciscoMediaQualityCapability.setLastUpdated('201109230000Z')
if mibBuilder.loadTexts: ciscoMediaQualityCapability.setOrganization('Cisco Systems, Inc.')
ciscoMediaQualityCapabilityV152R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 604, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMediaQualityCapabilityV152R01 = ciscoMediaQualityCapabilityV152R01.setProductRelease('OS=IOS\n                     OSVERSION=15.2(1)T\n                     PLATFORM=c29xx,c3925,c3945,c3925E,c3945E\n                     INTERFACE=None')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMediaQualityCapabilityV152R01 = ciscoMediaQualityCapabilityV152R01.setStatus('current')
ciscoMediaQualityCapabilityV152R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 604, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMediaQualityCapabilityV152R02 = ciscoMediaQualityCapabilityV152R02.setProductRelease('OS=IOS\n                     OSVERSION=15.2(2)T\n                     PLATFORM=c28xx,c3825,c3845,c29xx,c3925,c3945,c3925E,c3945E\n                     INTERFACE=None')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMediaQualityCapabilityV152R02 = ciscoMediaQualityCapabilityV152R02.setStatus('current')
mibBuilder.exportSymbols("CISCO-MEDIA-QUALITY-CAPABILITY", ciscoMediaQualityCapabilityV152R01=ciscoMediaQualityCapabilityV152R01, ciscoMediaQualityCapabilityV152R02=ciscoMediaQualityCapabilityV152R02, PYSNMP_MODULE_ID=ciscoMediaQualityCapability, ciscoMediaQualityCapability=ciscoMediaQualityCapability)
