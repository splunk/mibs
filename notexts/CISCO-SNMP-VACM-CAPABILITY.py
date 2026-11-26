#
# PySNMP MIB module CISCO-SNMP-VACM-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SNMP-VACM-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
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
ciscoSnmpVacmCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 333))
ciscoSnmpVacmCapability.setRevisions(('2008-08-04 00:00', '2007-06-22 00:00', '2006-05-22 00:00', '2003-09-05 00:00',))
if mibBuilder.loadTexts: ciscoSnmpVacmCapability.setLastUpdated('200808040000Z')
if mibBuilder.loadTexts: ciscoSnmpVacmCapability.setOrganization('Cisco Systems, Inc.')
ciscoSnmpVacmCapCatOSV05R0501 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 333, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpVacmCapCatOSV05R0501 = ciscoSnmpVacmCapCatOSV05R0501.setProductRelease('Cisco CatOS 5.5(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpVacmCapCatOSV05R0501 = ciscoSnmpVacmCapCatOSV05R0501.setStatus('current')
ciscoSnmpVacmCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 333, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpVacmCapACSWV03R000 = ciscoSnmpVacmCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpVacmCapACSWV03R000 = ciscoSnmpVacmCapACSWV03R000.setStatus('current')
ciscoSnmpVacmCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 333, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpVacmCapc4710aceVA1R700 = ciscoSnmpVacmCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                         for ACE 4710 Application Control Engine \n                         Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpVacmCapc4710aceVA1R700 = ciscoSnmpVacmCapc4710aceVA1R700.setStatus('current')
mibBuilder.exportSymbols("CISCO-SNMP-VACM-CAPABILITY", ciscoSnmpVacmCapACSWV03R000=ciscoSnmpVacmCapACSWV03R000, PYSNMP_MODULE_ID=ciscoSnmpVacmCapability, ciscoSnmpVacmCapc4710aceVA1R700=ciscoSnmpVacmCapc4710aceVA1R700, ciscoSnmpVacmCapability=ciscoSnmpVacmCapability, ciscoSnmpVacmCapCatOSV05R0501=ciscoSnmpVacmCapCatOSV05R0501)
