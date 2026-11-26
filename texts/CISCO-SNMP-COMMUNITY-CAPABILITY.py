#
# PySNMP MIB module CISCO-SNMP-COMMUNITY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SNMP-COMMUNITY-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:44 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoSnmpCommunityCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 318))
ciscoSnmpCommunityCapability.setRevisions(('2008-08-04 00:00', '2006-03-29 00:00', '2004-01-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSnmpCommunityCapability.setRevisionsDescriptions(('Added capability statement\n        cSnmpCommunityCapc4710aceVA1R700 for ACE 4710 \n        Application Control Engine Appliance.', 'Added capability statement\n        cSnmpCommunityCapACSWV03R000 \n        for Application Control Engine (ACE).\n\n        Updated the conformance group name for \n        cSnmpCommunityCapCatOSV06R0301 from \n        snmpCommunityGroup to snmpCommunityTableGroup\n        since the new version of SNMP-COMMUNITY-MIB \n        (RFC3584) has changed the name to avoid conflicts \n        with SNMPv2-MIB.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSnmpCommunityCapability.setLastUpdated('200808040000Z')
if mibBuilder.loadTexts: ciscoSnmpCommunityCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSnmpCommunityCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com, cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSnmpCommunityCapability.setDescription('The capabilities description of\n        SNMP-COMMUNITY-MIB.')
cSnmpCommunityCapCatOSV06R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 318, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpCommunityCapCatOSV06R0301 = cSnmpCommunityCapCatOSV06R0301.setProductRelease('Cisco CatOS 6.3(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpCommunityCapCatOSV06R0301 = cSnmpCommunityCapCatOSV06R0301.setStatus('current')
if mibBuilder.loadTexts: cSnmpCommunityCapCatOSV06R0301.setDescription('SNMP-COMMUNITY-MIB capabilities.')
cSnmpCommunityCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 318, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpCommunityCapACSWV03R000 = cSnmpCommunityCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpCommunityCapACSWV03R000 = cSnmpCommunityCapACSWV03R000.setStatus('current')
if mibBuilder.loadTexts: cSnmpCommunityCapACSWV03R000.setDescription('SNMP-COMMUNITY-MIB capabilities.')
cSnmpCommunityCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 318, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpCommunityCapc4710aceVA1R700 = cSnmpCommunityCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                    for ACE 4710 Application Control Engine \n                    Appliance')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpCommunityCapc4710aceVA1R700 = cSnmpCommunityCapc4710aceVA1R700.setStatus('current')
if mibBuilder.loadTexts: cSnmpCommunityCapc4710aceVA1R700.setDescription('SNMP-COMMUNITY-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-SNMP-COMMUNITY-CAPABILITY", ciscoSnmpCommunityCapability=ciscoSnmpCommunityCapability, cSnmpCommunityCapCatOSV06R0301=cSnmpCommunityCapCatOSV06R0301, cSnmpCommunityCapc4710aceVA1R700=cSnmpCommunityCapc4710aceVA1R700, cSnmpCommunityCapACSWV03R000=cSnmpCommunityCapACSWV03R000, PYSNMP_MODULE_ID=ciscoSnmpCommunityCapability)
