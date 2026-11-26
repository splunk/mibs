#
# PySNMP MIB module CISCO-SNMP-USM-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SNMP-USM-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:46 2026
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
ciscoSnmpUsmCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 323))
ciscoSnmpUsmCapability.setRevisions(('2008-08-01 00:00', '2006-05-22 00:00', '2003-08-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSnmpUsmCapability.setRevisionsDescriptions(('Added the correct mib name under the\n        SUPPORTS clause for ciscoSnmpUsmCapCatOSV05R0501\n        and ciscoSnmpUsmCapACSWV03R000.\n        Added terminating quotes for \n        ciscoSnmpUsmCapACSWV03R000 PRODUCT-RELEASE clause.\n        Added capability statement \n        ciscoSnmpUsmCapc4710aceVA1R700 for ACE 4710 Application\n        Control Engine Appliance.', 'Added capability statement\n        ciscoSnmpUsmCapACSWV03R000 for \n        Application Control Engine (ACE).', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSnmpUsmCapability.setLastUpdated('200808010000Z')
if mibBuilder.loadTexts: ciscoSnmpUsmCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSnmpUsmCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com, cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSnmpUsmCapability.setDescription('The capabilities description of SNMP-USER-BASED-SM-MIB.')
ciscoSnmpUsmCapCatOSV05R0501 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 323, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpUsmCapCatOSV05R0501 = ciscoSnmpUsmCapCatOSV05R0501.setProductRelease('Cisco CatOS 5.5(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpUsmCapCatOSV05R0501 = ciscoSnmpUsmCapCatOSV05R0501.setStatus('current')
if mibBuilder.loadTexts: ciscoSnmpUsmCapCatOSV05R0501.setDescription('SNMP-USER-BASED-SM-MIB capabilities.')
ciscoSnmpUsmCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 323, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpUsmCapACSWV03R000 = ciscoSnmpUsmCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpUsmCapACSWV03R000 = ciscoSnmpUsmCapACSWV03R000.setStatus('current')
if mibBuilder.loadTexts: ciscoSnmpUsmCapACSWV03R000.setDescription('SNMP-USER-BASED-SM-MIB capabilities.')
ciscoSnmpUsmCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 323, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpUsmCapc4710aceVA1R700 = ciscoSnmpUsmCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                    for ACE 4710 Application Control Engine \n                    Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpUsmCapc4710aceVA1R700 = ciscoSnmpUsmCapc4710aceVA1R700.setStatus('current')
if mibBuilder.loadTexts: ciscoSnmpUsmCapc4710aceVA1R700.setDescription('SNMP-USER-BASED-SM-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-SNMP-USM-CAPABILITY", ciscoSnmpUsmCapACSWV03R000=ciscoSnmpUsmCapACSWV03R000, ciscoSnmpUsmCapc4710aceVA1R700=ciscoSnmpUsmCapc4710aceVA1R700, ciscoSnmpUsmCapCatOSV05R0501=ciscoSnmpUsmCapCatOSV05R0501, ciscoSnmpUsmCapability=ciscoSnmpUsmCapability, PYSNMP_MODULE_ID=ciscoSnmpUsmCapability)
