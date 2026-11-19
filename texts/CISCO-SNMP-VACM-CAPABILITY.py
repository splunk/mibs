#
# PySNMP MIB module CISCO-SNMP-VACM-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SNMP-VACM-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:06 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
NotificationType, MibIdentifier, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, TimeTicks, IpAddress, Bits, Counter64, Gauge32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "TimeTicks", "IpAddress", "Bits", "Counter64", "Gauge32", "Integer32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSnmpVacmCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 333))
ciscoSnmpVacmCapability.setRevisions(('2008-08-04 00:00', '2007-06-22 00:00', '2006-05-22 00:00', '2003-09-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSnmpVacmCapability.setRevisionsDescriptions(('Added capability statement\n        ciscoSnmpVacmCapc4710aceVA1R700 for ACE 4710 \n        Application Control Engine Appliance.', 'Added the correct mib name under the SUPPORTS\n        clause for ciscoSnmpVacmCapCatOSV05R0501 and \n        ciscoSnmpVacmCapACSWV03R000.', 'Added capability statement\n        ciscoSnmpVacmCapACSWV03R000 for \n        Application Control Engine (ACE).', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSnmpVacmCapability.setLastUpdated('200808040000Z')
if mibBuilder.loadTexts: ciscoSnmpVacmCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSnmpVacmCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com, cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSnmpVacmCapability.setDescription('The capabilities description of\n        SNMP-VIEW-BASED-ACM-MIB.')
ciscoSnmpVacmCapCatOSV05R0501 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 333, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpVacmCapCatOSV05R0501 = ciscoSnmpVacmCapCatOSV05R0501.setProductRelease('Cisco CatOS 5.5(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpVacmCapCatOSV05R0501 = ciscoSnmpVacmCapCatOSV05R0501.setStatus('current')
if mibBuilder.loadTexts: ciscoSnmpVacmCapCatOSV05R0501.setDescription('SNMP-VIEW-BASED-ACM-MIB capabilities.')
ciscoSnmpVacmCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 333, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpVacmCapACSWV03R000 = ciscoSnmpVacmCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpVacmCapACSWV03R000 = ciscoSnmpVacmCapACSWV03R000.setStatus('current')
if mibBuilder.loadTexts: ciscoSnmpVacmCapACSWV03R000.setDescription('SNMP-VIEW-BASED-ACM-MIB capabilities.')
ciscoSnmpVacmCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 333, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpVacmCapc4710aceVA1R700 = ciscoSnmpVacmCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                         for ACE 4710 Application Control Engine \n                         Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpVacmCapc4710aceVA1R700 = ciscoSnmpVacmCapc4710aceVA1R700.setStatus('current')
if mibBuilder.loadTexts: ciscoSnmpVacmCapc4710aceVA1R700.setDescription('SNMP-VIEW-BASED-ACM-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-SNMP-VACM-CAPABILITY", PYSNMP_MODULE_ID=ciscoSnmpVacmCapability, ciscoSnmpVacmCapc4710aceVA1R700=ciscoSnmpVacmCapc4710aceVA1R700, ciscoSnmpVacmCapability=ciscoSnmpVacmCapability, ciscoSnmpVacmCapCatOSV05R0501=ciscoSnmpVacmCapCatOSV05R0501, ciscoSnmpVacmCapACSWV03R000=ciscoSnmpVacmCapACSWV03R000)
