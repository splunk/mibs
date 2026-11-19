#
# PySNMP MIB module CISCO-SNMP-NOTIFICATION-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SNMP-NOTIFICATION-CAPABILITY
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
ciscoSnmpNotificationCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 330))
ciscoSnmpNotificationCapability.setRevisions(('2008-06-25 00:00', '2006-03-29 00:00', '2004-07-28 00:00', '2003-08-28 00:00',))
if mibBuilder.loadTexts: ciscoSnmpNotificationCapability.setLastUpdated('200806250000Z')
if mibBuilder.loadTexts: ciscoSnmpNotificationCapability.setOrganization('Cisco Systems, Inc.')
cSnmpNotifCapCatOSV05R0501 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 330, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpNotifCapCatOSV05R0501 = cSnmpNotifCapCatOSV05R0501.setProductRelease('Cisco CatOS 5.5(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpNotifCapCatOSV05R0501 = cSnmpNotifCapCatOSV05R0501.setStatus('current')
cSnmpNotifCapVISM33 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 330, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpNotifCapVISM33 = cSnmpNotifCapVISM33.setProductRelease('Cisco VISM Release 3.3.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpNotifCapVISM33 = cSnmpNotifCapVISM33.setStatus('current')
cSnmpNotifCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 330, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpNotifCapACSWV03R000 = cSnmpNotifCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpNotifCapACSWV03R000 = cSnmpNotifCapACSWV03R000.setStatus('current')
cSnmpNotifCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 330, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpNotifCapc4710aceVA1R700 = cSnmpNotifCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                         for ACE 4710 Application Control Engine \n                         Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpNotifCapc4710aceVA1R700 = cSnmpNotifCapc4710aceVA1R700.setStatus('current')
mibBuilder.exportSymbols("CISCO-SNMP-NOTIFICATION-CAPABILITY", cSnmpNotifCapCatOSV05R0501=cSnmpNotifCapCatOSV05R0501, PYSNMP_MODULE_ID=ciscoSnmpNotificationCapability, cSnmpNotifCapACSWV03R000=cSnmpNotifCapACSWV03R000, cSnmpNotifCapVISM33=cSnmpNotifCapVISM33, ciscoSnmpNotificationCapability=ciscoSnmpNotificationCapability, cSnmpNotifCapc4710aceVA1R700=cSnmpNotifCapc4710aceVA1R700)
