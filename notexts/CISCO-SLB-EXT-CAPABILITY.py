#
# PySNMP MIB module CISCO-SLB-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SLB-EXT-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:00 2026
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
ciscoSlbExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 496))
ciscoSlbExtCapability.setRevisions(('2008-07-02 00:00', '2008-02-07 00:00', '2006-12-08 00:00', '2006-02-21 00:00',))
if mibBuilder.loadTexts: ciscoSlbExtCapability.setLastUpdated('200807020000Z')
if mibBuilder.loadTexts: ciscoSlbExtCapability.setOrganization('Cisco Systems, Inc.')
ciscoSlbExtCapabilityACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 496, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbExtCapabilityACSWV03R000 = ciscoSlbExtCapabilityACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbExtCapabilityACSWV03R000 = ciscoSlbExtCapabilityACSWV03R000.setStatus('current')
ciscoSlbExtCapabilityACSWV300RA12 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 496, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbExtCapabilityACSWV300RA12 = ciscoSlbExtCapabilityACSWV300RA12.setProductRelease('ACSW (Application Control Software)\n                version 3.0(0)A1(2).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbExtCapabilityACSWV300RA12 = ciscoSlbExtCapabilityACSWV300RA12.setStatus('current')
ciscoSlbExtCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 496, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbExtCapc4710aceVA1R700 = ciscoSlbExtCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                    for ACE 4710 Application Control Engine \n                    Appliance')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbExtCapc4710aceVA1R700 = ciscoSlbExtCapc4710aceVA1R700.setStatus('current')
ciscoSlbExtCapc4710aceVA3R100 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 496, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbExtCapc4710aceVA3R100 = ciscoSlbExtCapc4710aceVA3R100.setProductRelease('ACSW (Application Control Software) A3(1.0)\n                    for ACE 4710 Application Control Engine \n                    Appliance')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbExtCapc4710aceVA3R100 = ciscoSlbExtCapc4710aceVA3R100.setStatus('current')
mibBuilder.exportSymbols("CISCO-SLB-EXT-CAPABILITY", ciscoSlbExtCapability=ciscoSlbExtCapability, ciscoSlbExtCapc4710aceVA3R100=ciscoSlbExtCapc4710aceVA3R100, ciscoSlbExtCapabilityACSWV300RA12=ciscoSlbExtCapabilityACSWV300RA12, PYSNMP_MODULE_ID=ciscoSlbExtCapability, ciscoSlbExtCapc4710aceVA1R700=ciscoSlbExtCapc4710aceVA1R700, ciscoSlbExtCapabilityACSWV03R000=ciscoSlbExtCapabilityACSWV03R000)
