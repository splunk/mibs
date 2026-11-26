#
# PySNMP MIB module CISCO-SNMP-COMMUNITY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SNMP-COMMUNITY-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
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
ciscoSnmpCommunityCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 318))
ciscoSnmpCommunityCapability.setRevisions(('2008-08-04 00:00', '2006-03-29 00:00', '2004-01-30 00:00',))
if mibBuilder.loadTexts: ciscoSnmpCommunityCapability.setLastUpdated('200808040000Z')
if mibBuilder.loadTexts: ciscoSnmpCommunityCapability.setOrganization('Cisco Systems, Inc.')
cSnmpCommunityCapCatOSV06R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 318, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpCommunityCapCatOSV06R0301 = cSnmpCommunityCapCatOSV06R0301.setProductRelease('Cisco CatOS 6.3(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpCommunityCapCatOSV06R0301 = cSnmpCommunityCapCatOSV06R0301.setStatus('current')
cSnmpCommunityCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 318, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpCommunityCapACSWV03R000 = cSnmpCommunityCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpCommunityCapACSWV03R000 = cSnmpCommunityCapACSWV03R000.setStatus('current')
cSnmpCommunityCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 318, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpCommunityCapc4710aceVA1R700 = cSnmpCommunityCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                    for ACE 4710 Application Control Engine \n                    Appliance')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpCommunityCapc4710aceVA1R700 = cSnmpCommunityCapc4710aceVA1R700.setStatus('current')
mibBuilder.exportSymbols("CISCO-SNMP-COMMUNITY-CAPABILITY", cSnmpCommunityCapCatOSV06R0301=cSnmpCommunityCapCatOSV06R0301, ciscoSnmpCommunityCapability=ciscoSnmpCommunityCapability, PYSNMP_MODULE_ID=ciscoSnmpCommunityCapability, cSnmpCommunityCapc4710aceVA1R700=cSnmpCommunityCapc4710aceVA1R700, cSnmpCommunityCapACSWV03R000=cSnmpCommunityCapACSWV03R000)
