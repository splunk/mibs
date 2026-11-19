#
# PySNMP MIB module CISCO-SYSTEM-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SYSTEM-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:24 2026
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
ciscoSystemCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 276))
ciscoSystemCapability.setRevisions(('2008-07-02 00:00', '2007-07-31 00:00', '2003-09-15 00:00', '2002-03-06 00:00',))
if mibBuilder.loadTexts: ciscoSystemCapability.setLastUpdated('200807020000Z')
if mibBuilder.loadTexts: ciscoSystemCapability.setOrganization('Cisco Systems, Inc.')
ciscoSystemCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 276, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemCapabilityV2R00 = ciscoSystemCapabilityV2R00.setProductRelease('MGX8850 Release 2.00,\n                         BPX SES Release 1.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemCapabilityV2R00 = ciscoSystemCapabilityV2R00.setStatus('current')
ciscoSystemCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 276, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemCapCatOSV08R0101 = ciscoSystemCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemCapCatOSV08R0101 = ciscoSystemCapCatOSV08R0101.setStatus('current')
ciscoSystemCapabilityMGXV5R0500 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 276, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemCapabilityMGXV5R0500 = ciscoSystemCapabilityMGXV5R0500.setProductRelease('MGX8850 5.5 Release')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemCapabilityMGXV5R0500 = ciscoSystemCapabilityMGXV5R0500.setStatus('current')
ciscoSystemCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 276, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemCapACSWV03R000 = ciscoSystemCapACSWV03R000.setProductRelease('ACSW (Application Control Software)\n                    version 3.0(0)A1(2).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemCapACSWV03R000 = ciscoSystemCapACSWV03R000.setStatus('current')
ciscoSystemCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 276, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemCapc4710aceVA1R700 = ciscoSystemCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                    for ACE 4710 Application Control Engine Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemCapc4710aceVA1R700 = ciscoSystemCapc4710aceVA1R700.setStatus('current')
mibBuilder.exportSymbols("CISCO-SYSTEM-CAPABILITY", PYSNMP_MODULE_ID=ciscoSystemCapability, ciscoSystemCapACSWV03R000=ciscoSystemCapACSWV03R000, ciscoSystemCapc4710aceVA1R700=ciscoSystemCapc4710aceVA1R700, ciscoSystemCapabilityMGXV5R0500=ciscoSystemCapabilityMGXV5R0500, ciscoSystemCapCatOSV08R0101=ciscoSystemCapCatOSV08R0101, ciscoSystemCapability=ciscoSystemCapability, ciscoSystemCapabilityV2R00=ciscoSystemCapabilityV2R00)
