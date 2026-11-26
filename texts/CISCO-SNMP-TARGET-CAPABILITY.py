#
# PySNMP MIB module CISCO-SNMP-TARGET-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SNMP-TARGET-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:44 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoSnmpTargetCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 359))
ciscoSnmpTargetCapability.setRevisions(('2008-07-21 00:00', '2007-06-22 00:00', '2006-04-11 00:00', '2004-07-28 00:00', '2003-09-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSnmpTargetCapability.setRevisionsDescriptions(('Added capability statement ciscoSnmpTargetCapc4710aceVA1R700\n        for ACE 4710 Application Control Engine Appliance.\n\n        Added VARIATION clause for snmpTargetSpinLock object in \n        ciscoSnmpTargetCapACSWV03R000 agent capability.', 'Removed SYNTAX for snmpTargetAddrTDomain under\n        ciscoSnmpTargetCapCatOSV05R0501.', 'Added capability statement ciscoSnmpTargetCapACSWV03R000\n        for Application Control Engine (ACE).', 'Added capabilities for VISM release 3.3.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSnmpTargetCapability.setLastUpdated('200807210000Z')
if mibBuilder.loadTexts: ciscoSnmpTargetCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSnmpTargetCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com, cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSnmpTargetCapability.setDescription('The capabilities description of SNMP-TARGET-MIB.')
ciscoSnmpTargetCapCatOSV05R0501 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 359, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpTargetCapCatOSV05R0501 = ciscoSnmpTargetCapCatOSV05R0501.setProductRelease('Cisco CatOS 5.5(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpTargetCapCatOSV05R0501 = ciscoSnmpTargetCapCatOSV05R0501.setStatus('current')
if mibBuilder.loadTexts: ciscoSnmpTargetCapCatOSV05R0501.setDescription('SNMP-TARGET-MIB capabilities.')
ciscoSnmpTargetCapVISM33 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 359, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpTargetCapVISM33 = ciscoSnmpTargetCapVISM33.setProductRelease('Cisco VISM Release 3.3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpTargetCapVISM33 = ciscoSnmpTargetCapVISM33.setStatus('current')
if mibBuilder.loadTexts: ciscoSnmpTargetCapVISM33.setDescription('SNMP-TARGET-MIB capabilities.')
ciscoSnmpTargetCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 359, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpTargetCapACSWV03R000 = ciscoSnmpTargetCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpTargetCapACSWV03R000 = ciscoSnmpTargetCapACSWV03R000.setStatus('current')
if mibBuilder.loadTexts: ciscoSnmpTargetCapACSWV03R000.setDescription('SNMP-TARGET-MIB capabilities.')
ciscoSnmpTargetCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 359, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpTargetCapc4710aceVA1R700 = ciscoSnmpTargetCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                     for ACE 4710 Application Control Engine \n                     Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpTargetCapc4710aceVA1R700 = ciscoSnmpTargetCapc4710aceVA1R700.setStatus('current')
if mibBuilder.loadTexts: ciscoSnmpTargetCapc4710aceVA1R700.setDescription('SNMP-TARGET-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-SNMP-TARGET-CAPABILITY", PYSNMP_MODULE_ID=ciscoSnmpTargetCapability, ciscoSnmpTargetCapc4710aceVA1R700=ciscoSnmpTargetCapc4710aceVA1R700, ciscoSnmpTargetCapability=ciscoSnmpTargetCapability, ciscoSnmpTargetCapCatOSV05R0501=ciscoSnmpTargetCapCatOSV05R0501, ciscoSnmpTargetCapACSWV03R000=ciscoSnmpTargetCapACSWV03R000, ciscoSnmpTargetCapVISM33=ciscoSnmpTargetCapVISM33)
