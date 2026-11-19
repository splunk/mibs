#
# PySNMP MIB module CISCO-IP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IP-CAPABILITY
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
ciscoIpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 445))
ciscoIpCapability.setRevisions(('2010-09-30 00:00', '2008-08-11 00:00', '2007-11-05 00:00', '2006-11-03 00:00', '2006-05-27 00:00', '2006-02-17 00:00', '2005-07-25 00:00',))
if mibBuilder.loadTexts: ciscoIpCapability.setLastUpdated('201009300000Z')
if mibBuilder.loadTexts: ciscoIpCapability.setOrganization('Cisco Systems, Inc.')
cIpCapV320CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 445, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIpCapV320CRS1 = cIpCapV320CRS1.setProductRelease('Cisco IOS XR 3.2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIpCapV320CRS1 = cIpCapV320CRS1.setStatus('current')
cIpCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 445, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIpCapACSWV03R000 = cIpCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIpCapACSWV03R000 = cIpCapACSWV03R000.setStatus('current')
cIpCapCTSV100 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 445, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIpCapCTSV100 = cIpCapCTSV100.setProductRelease('Cisco TelePresence System (CTS) 1.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIpCapCTSV100 = cIpCapCTSV100.setStatus('current')
cIpCapCTMV1000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 445, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIpCapCTMV1000 = cIpCapCTMV1000.setProductRelease('Cisco TelePresence Manager (CTM) 1.0.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIpCapCTMV1000 = cIpCapCTMV1000.setStatus('current')
cIpCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 445, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIpCapc4710aceVA1R700 = cIpCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                    for ACE 4710 Application Control Engine \n                    Appliance')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIpCapc4710aceVA1R700 = cIpCapc4710aceVA1R700.setStatus('current')
ciscoIpCapabilityV12R2SE = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 445, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpCapabilityV12R2SE = ciscoIpCapabilityV12R2SE.setProductRelease('Cisco IOS 12.2SE Catalyst 2k/3k Series.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpCapabilityV12R2SE = ciscoIpCapabilityV12R2SE.setStatus('current')
mibBuilder.exportSymbols("CISCO-IP-CAPABILITY", PYSNMP_MODULE_ID=ciscoIpCapability, cIpCapV320CRS1=cIpCapV320CRS1, ciscoIpCapabilityV12R2SE=ciscoIpCapabilityV12R2SE, cIpCapCTMV1000=cIpCapCTMV1000, cIpCapCTSV100=cIpCapCTSV100, cIpCapACSWV03R000=cIpCapACSWV03R000, ciscoIpCapability=ciscoIpCapability, cIpCapc4710aceVA1R700=cIpCapc4710aceVA1R700)
