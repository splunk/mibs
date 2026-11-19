#
# PySNMP MIB module CISCO-SNMP-FRAMEWORK-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SNMP-FRAMEWORK-CAPABILITY
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
ciscoSnmpFrameworkCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 315))
ciscoSnmpFrameworkCapability.setRevisions(('2007-11-12 00:00', '2006-05-27 00:00', '2003-09-03 00:00',))
if mibBuilder.loadTexts: ciscoSnmpFrameworkCapability.setLastUpdated('200711120000Z')
if mibBuilder.loadTexts: ciscoSnmpFrameworkCapability.setOrganization('Cisco Systems, Inc.')
cSnmpFrameworkCapCatOSV05R0401 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 315, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpFrameworkCapCatOSV05R0401 = cSnmpFrameworkCapCatOSV05R0401.setProductRelease('Cisco CatOS 5.4(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpFrameworkCapCatOSV05R0401 = cSnmpFrameworkCapCatOSV05R0401.setStatus('current')
cSnmpFrameworkCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 315, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpFrameworkCapACSWV03R000 = cSnmpFrameworkCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0\n                          for Application Control Engine (ACE) \n                          Service Module.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpFrameworkCapACSWV03R000 = cSnmpFrameworkCapACSWV03R000.setStatus('current')
cSnmpFrameworkCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 315, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpFrameworkCapc4710aceVA1R700 = cSnmpFrameworkCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                         for ACE 4710 Application Control Engine \n                         Appliance')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpFrameworkCapc4710aceVA1R700 = cSnmpFrameworkCapc4710aceVA1R700.setStatus('current')
mibBuilder.exportSymbols("CISCO-SNMP-FRAMEWORK-CAPABILITY", ciscoSnmpFrameworkCapability=ciscoSnmpFrameworkCapability, cSnmpFrameworkCapCatOSV05R0401=cSnmpFrameworkCapCatOSV05R0401, cSnmpFrameworkCapACSWV03R000=cSnmpFrameworkCapACSWV03R000, cSnmpFrameworkCapc4710aceVA1R700=cSnmpFrameworkCapc4710aceVA1R700, PYSNMP_MODULE_ID=ciscoSnmpFrameworkCapability)
