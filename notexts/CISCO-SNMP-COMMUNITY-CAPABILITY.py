#
# PySNMP MIB module CISCO-SNMP-COMMUNITY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SNMP-COMMUNITY-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:22 2026
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
mibBuilder.exportSymbols("CISCO-SNMP-COMMUNITY-CAPABILITY", ciscoSnmpCommunityCapability=ciscoSnmpCommunityCapability, cSnmpCommunityCapCatOSV06R0301=cSnmpCommunityCapCatOSV06R0301, cSnmpCommunityCapACSWV03R000=cSnmpCommunityCapACSWV03R000, cSnmpCommunityCapc4710aceVA1R700=cSnmpCommunityCapc4710aceVA1R700, PYSNMP_MODULE_ID=ciscoSnmpCommunityCapability)
