#
# PySNMP MIB module CISCO-SNMP-USM-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SNMP-USM-CAPABILITY
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
ciscoSnmpUsmCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 323))
ciscoSnmpUsmCapability.setRevisions(('2008-08-01 00:00', '2006-05-22 00:00', '2003-08-26 00:00',))
if mibBuilder.loadTexts: ciscoSnmpUsmCapability.setLastUpdated('200808010000Z')
if mibBuilder.loadTexts: ciscoSnmpUsmCapability.setOrganization('Cisco Systems, Inc.')
ciscoSnmpUsmCapCatOSV05R0501 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 323, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpUsmCapCatOSV05R0501 = ciscoSnmpUsmCapCatOSV05R0501.setProductRelease('Cisco CatOS 5.5(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpUsmCapCatOSV05R0501 = ciscoSnmpUsmCapCatOSV05R0501.setStatus('current')
ciscoSnmpUsmCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 323, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpUsmCapACSWV03R000 = ciscoSnmpUsmCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpUsmCapACSWV03R000 = ciscoSnmpUsmCapACSWV03R000.setStatus('current')
ciscoSnmpUsmCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 323, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpUsmCapc4710aceVA1R700 = ciscoSnmpUsmCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                    for ACE 4710 Application Control Engine \n                    Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpUsmCapc4710aceVA1R700 = ciscoSnmpUsmCapc4710aceVA1R700.setStatus('current')
mibBuilder.exportSymbols("CISCO-SNMP-USM-CAPABILITY", ciscoSnmpUsmCapACSWV03R000=ciscoSnmpUsmCapACSWV03R000, ciscoSnmpUsmCapCatOSV05R0501=ciscoSnmpUsmCapCatOSV05R0501, ciscoSnmpUsmCapability=ciscoSnmpUsmCapability, ciscoSnmpUsmCapc4710aceVA1R700=ciscoSnmpUsmCapc4710aceVA1R700, PYSNMP_MODULE_ID=ciscoSnmpUsmCapability)
